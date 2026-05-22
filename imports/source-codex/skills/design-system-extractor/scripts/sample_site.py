#!/usr/bin/env python3
"""
Conservatively sample representative pages from a public website and emit a
coverage-oriented JSON summary for the design-system-extractor skill.

This script is intentionally narrow:
- same-origin pages only
- small page cap
- HTML analysis only
- no asset mirroring
- no authenticated flows

Usage:
    python sample_site.py https://example.com --max-pages 8 --output sample.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass, field
from html.parser import HTMLParser
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

try:
    import requests
except ImportError:
    requests = None

REQUEST_EXCEPTIONS: tuple[type[BaseException], ...]
if requests is not None:
    REQUEST_EXCEPTIONS = (requests.exceptions.RequestException,)
else:
    REQUEST_EXCEPTIONS = ()


DEFAULT_PAGE_CLASS_PATTERNS = [
    ("community", r"\b(society|club|membership|member|community)\b"),
    ("menu", r"\b(menu|drinks|cocktails|food)\b"),
    ("faq", r"\b(faq|questions|help)\b"),
    ("team", r"\b(crew|team|about-us|about)\b"),
    ("shop", r"\b(shop|store|cart|checkout|product|products|auctions)\b"),
    ("gallery", r"(gallery|image-gallery|photos)"),
    ("offers", r"(offers|offer|packages|package|special)"),
    ("blog", r"\b(blog|journal|stories|news)\b"),
    ("events", r"\b(events|event|weddings|meetings|conference)\b"),
    ("pricing", r"(pricing|plans|billing|subscribe)"),
    ("auth", r"(login|sign-in|signin|sign-up|signup|register|auth)"),
    ("dashboard", r"(dashboard|overview|workspace|console|app)"),
    ("settings", r"(settings|account|profile|preferences)"),
    ("docs", r"(docs|documentation|guide|api|learn)"),
    ("form", r"(contact|apply|request|checkout|form|survey)"),
    ("data", r"(table|reports|analytics|customers|orders|list)"),
]

DEFAULT_BLOCK_PATTERNS = [
    r"<(script|style|noscript)\b.*?</\1>",
    r"<(header|footer|nav)\b.*?</\1>",
    r"<(?:div|section|aside|form)\b[^>]*(?:id|class)=[\"'][^\"']*(modal-booking|booking|book-now|reservation|reserve|menu|menumobile|cookie|consent|newsletter)[^\"']*[\"'][^>]*>.*?</(?:div|section|aside|form)>",
]

COMPONENT_PATTERNS = {
    "buttons": re.compile(r"<button\b|type=[\"']button[\"']|class=[\"'][^\"']*\b(btn|button|cta)\b", re.I),
    "links": re.compile(r"<a\b", re.I),
    "inputs": re.compile(r"<input\b|<textarea\b", re.I),
    "selects": re.compile(r"<select\b", re.I),
    "checkboxes": re.compile(r"type=[\"']checkbox[\"']", re.I),
    "radios": re.compile(r"type=[\"']radio[\"']", re.I),
    "toggles": re.compile(r"\b(switch|toggle)\b", re.I),
    "tables": re.compile(r"<table\b|\bdatatable\b", re.I),
    "cards": re.compile(r"\b(card|panel|tile)\b", re.I),
    "modals": re.compile(r"\b(modal|dialog|drawer|popover)\b", re.I),
    "tabs": re.compile(r"\b(tabs?|tabpanel|segmented)\b", re.I),
    "alerts": re.compile(r"\b(alert|toast|banner|notice)\b", re.I),
}

STATE_PATTERNS = {
    "hover": re.compile(r":hover\b", re.I),
    "focus": re.compile(r":focus\b|focus-visible", re.I),
    "active": re.compile(r":active\b|aria-pressed", re.I),
    "disabled": re.compile(r":disabled\b|disabled=", re.I),
    "error": re.compile(r"\b(error|invalid|aria-invalid|destructive)\b", re.I),
    "success": re.compile(r"\b(success|complete|confirmed)\b", re.I),
    "empty": re.compile(r"\b(empty state|no results|no data|nothing here)\b", re.I),
    "loading": re.compile(r"\b(loading|spinner|skeleton|progressbar)\b", re.I),
}

COLOR_PATTERN = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)")
FONT_PATTERN = re.compile(r"font-family\s*:\s*([^;]+);", re.I)
CSS_VAR_PATTERN = re.compile(r"(--[\w-]+)\s*:\s*([^;}{]+)")
SITE_FAMILIES_PATH = Path(__file__).resolve().parent.parent / "references" / "site-families.json"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.title: str = ""
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "a":
            href = attrs_dict.get("href")
            if href:
                self.links.append(href)
        elif tag == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data.strip()


@dataclass
class PageSummary:
    url: str
    title: str
    page_class: str
    component_hits: dict[str, int] = field(default_factory=dict)
    state_hits: dict[str, bool] = field(default_factory=dict)
    top_colors: list[str] = field(default_factory=list)
    fonts: list[str] = field(default_factory=list)
    css_vars: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    discrepancy_hints: list[str] = field(default_factory=list)


def compile_page_class_patterns(patterns: list[list[str]] | list[tuple[str, str]]) -> list[tuple[str, re.Pattern[str]]]:
    return [(label, re.compile(pattern, re.I)) for label, pattern in patterns]


def load_site_families() -> dict:
    if not SITE_FAMILIES_PATH.exists():
        return {"families": []}
    with open(SITE_FAMILIES_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def detect_site_family(seed_url: str, html: str, configured_family: str | None = None) -> dict | None:
    config = load_site_families()
    families = config.get("families", [])
    if configured_family:
        for family in families:
            if family.get("name") == configured_family:
                return family
        raise ValueError(f"Unknown site family: {configured_family}")

    hostname = urlparse(seed_url).netloc.lower()
    html_sample = html[:4000].lower()
    for family in families:
        domains = family.get("domains", [])
        domain_match = any(domain.lower() in hostname for domain in domains)
        html_matchers = family.get("html_contains", [])
        html_match = any(token.lower() in html_sample for token in html_matchers)
        if domain_match or html_match:
            return family
    return None


def get_page_class_patterns(family: dict | None) -> list[tuple[str, re.Pattern[str]]]:
    patterns = list(DEFAULT_PAGE_CLASS_PATTERNS)
    if family:
        patterns = family.get("page_classes", []) + patterns
    return compile_page_class_patterns(patterns)


def get_block_patterns(family: dict | None) -> list[str]:
    patterns = list(DEFAULT_BLOCK_PATTERNS)
    if family:
        patterns.extend(family.get("block_patterns", []))
    return patterns


def fetch_html(url: str, timeout: int) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/135.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
    }

    if requests is not None:
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "")
        if "html" not in content_type:
            raise ValueError(f"Non-HTML response for {url}: {content_type}")
        return response.text

    request = Request(url, headers=headers)
    with urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        if "html" not in content_type:
            raise ValueError(f"Non-HTML response for {url}: {content_type}")
        return response.read().decode("utf-8", errors="replace")


def normalize_url(base_url: str, href: str) -> str | None:
    absolute = urljoin(base_url, href)
    parsed = urlparse(absolute)
    if parsed.scheme not in {"http", "https"}:
        return None
    base_scheme = urlparse(base_url).scheme or "https"
    clean = parsed._replace(scheme=base_scheme, fragment="", params="", query="").geturl()
    return clean.rstrip("/") or clean


def same_origin(seed_url: str, candidate_url: str) -> bool:
    return urlparse(seed_url).netloc == urlparse(candidate_url).netloc


def classify_page(url: str, html: str, page_class_patterns: list[tuple[str, re.Pattern[str]]]) -> str:
    parsed = urlparse(url)
    path = parsed.path or "/"
    if path in {"", "/"}:
        return "home"

    for label, pattern in page_class_patterns:
        if pattern.search(path):
            return label

    sample = html[:800]
    for label, pattern in page_class_patterns:
        if pattern.search(sample):
            return label
    return "general"


def top_items(values: Iterable[str], limit: int = 6) -> list[str]:
    counter = Counter(v.strip() for v in values if v and v.strip())
    return [item for item, _count in counter.most_common(limit)]


def summarize_page(url: str, html: str, page_class_patterns: list[tuple[str, re.Pattern[str]]], block_patterns: list[str]) -> PageSummary:
    analysis_html = extract_analysis_html(html, block_patterns)
    parser = LinkParser()
    parser.feed(html)
    page_class = classify_page(url, analysis_html, page_class_patterns)

    component_hits = {
        name: len(pattern.findall(analysis_html)) for name, pattern in COMPONENT_PATTERNS.items()
    }
    state_hits = {name: bool(pattern.search(analysis_html)) for name, pattern in STATE_PATTERNS.items()}
    colors = top_items(COLOR_PATTERN.findall(html))
    fonts = top_items(FONT_PATTERN.findall(html))
    css_vars = top_items(match[0] for match in CSS_VAR_PATTERN.findall(html))

    notes: list[str] = []
    if component_hits["inputs"] or component_hits["selects"]:
        notes.append("Contains form-related controls.")
    if component_hits["tables"]:
        notes.append("Contains data-display hints.")
    if any(state_hits.values()):
        observed = ", ".join(name for name, present in state_hits.items() if present)
        notes.append(f"Observed state cues: {observed}.")
    discrepancy_hints = detect_page_discrepancies(url, parser.title or "", page_class)

    return PageSummary(
        url=url,
        title=parser.title or "",
        page_class=page_class,
        component_hits=component_hits,
        state_hits=state_hits,
        top_colors=colors,
        fonts=fonts,
        css_vars=css_vars,
        notes=notes,
        discrepancy_hints=discrepancy_hints,
    )


def detect_page_discrepancies(url: str, title: str, page_class: str) -> list[str]:
    hints: list[str] = []
    path = (urlparse(url).path or "/").lower()
    title_lc = title.lower()

    expected_classes = [
        ("locations", re.compile(r"\b(locations?|find us|visit us)\b")),
        ("story", re.compile(r"\b(story|our story|about)\b")),
        ("menu", re.compile(r"\b(menu|drinks|cocktails|food)\b")),
        ("faq", re.compile(r"\b(faq|questions|help)\b")),
        ("team", re.compile(r"\b(team|crew|chef)\b")),
    ]

    for expected_class, pattern in expected_classes:
        if pattern.search(path) or pattern.search(title_lc):
            if expected_class != page_class:
                hints.append(
                    f"Expected `{expected_class}` from path/title signals but classified as `{page_class}`."
                )
            break

    if page_class == "menu" and re.search(r"\b(contact|locations?|story|about)\b", path):
        hints.append("`menu` may be too broad for this page type; consider a family-specific class.")

    return hints


def discover_links(seed_url: str, html: str) -> list[str]:
    parser = LinkParser()
    parser.feed(html)
    candidates: list[str] = []
    for href in parser.links:
        normalized = normalize_url(seed_url, href)
        if not normalized:
            continue
        if same_origin(seed_url, normalized):
            candidates.append(normalized)
    # Preserve order while removing duplicates.
    seen: set[str] = set()
    ordered: list[str] = []
    for candidate in candidates:
        if candidate not in seen:
            seen.add(candidate)
            ordered.append(candidate)
    return ordered


def extract_analysis_html(html: str, block_patterns: list[str]) -> str:
    extracted = re.sub(r"<!--.*?-->", " ", html, flags=re.S)

    main_match = re.search(r"<main\b[^>]*>(.*?)</main>", extracted, re.I | re.S)
    if main_match:
        extracted = main_match.group(1)

    for pattern in block_patterns:
        extracted = re.sub(pattern, " ", extracted, flags=re.I | re.S)

    return extracted.strip() or html


def score_candidate(seed_url: str, url: str, page_class_patterns: list[tuple[str, re.Pattern[str]]]) -> tuple[int, str]:
    if url.rstrip("/") == seed_url.rstrip("/"):
        return (-10, url)
    parsed = urlparse(url)
    path = parsed.path or "/"
    score = 100
    depth = len([segment for segment in path.split("/") if segment])
    score -= min(depth, 6) * 3
    for label, pattern in page_class_patterns:
        if pattern.search(path):
            score += 25
            break
    if re.search(r"(privacy|terms|legal|careers|press)", path, re.I):
        score -= 20
    return (-score, url)


def pick_representative_urls(seed_url: str, discovered_urls: list[str], max_pages: int, page_class_patterns: list[tuple[str, re.Pattern[str]]]) -> list[str]:
    sorted_urls = [url for _score, url in sorted(score_candidate(seed_url, url, page_class_patterns) for url in discovered_urls)]
    chosen = [seed_url.rstrip("/")]
    seen_classes: set[str] = set()
    for url in sorted_urls:
        normalized = url.rstrip("/")
        if normalized in chosen:
            continue
        if len(chosen) >= max_pages:
            break
        page_class = classify_page(url, url, page_class_patterns)
        if page_class not in seen_classes or len(chosen) < min(max_pages, 4):
            chosen.append(normalized)
            seen_classes.add(page_class)
    for url in sorted_urls:
        normalized = url.rstrip("/")
        if normalized in chosen:
            continue
        if len(chosen) >= max_pages:
            break
        chosen.append(normalized)
    return chosen[:max_pages]


def build_output(seed_url: str, pages: list[PageSummary], errors: list[dict[str, str]], site_family_name: str | None) -> dict:
    coverage = []
    component_totals: Counter[str] = Counter()
    observed_states: Counter[str] = Counter()
    all_colors: list[str] = []
    all_fonts: list[str] = []
    all_css_vars: list[str] = []
    discrepancy_hints: list[dict[str, str]] = []
    suggested_family_updates: list[str] = []

    for page in pages:
        coverage.append(
            {
                "page_class": page.page_class,
                "url": page.url,
                "title": page.title,
                "key_patterns_found": [name for name, count in page.component_hits.items() if count > 0],
                "confidence": "medium" if page.page_class == "general" else "high",
                "notes": page.notes,
                "discrepancy_hints": page.discrepancy_hints,
            }
        )
        component_totals.update({k: v for k, v in page.component_hits.items() if v})
        observed_states.update({k: int(v) for k, v in page.state_hits.items() if v})
        all_colors.extend(page.top_colors)
        all_fonts.extend(page.fonts)
        all_css_vars.extend(page.css_vars)
        for hint in page.discrepancy_hints:
            discrepancy_hints.append({"url": page.url, "hint": hint})
            if "consider a family-specific class" in hint:
                if "Add or refine page class patterns for this family." not in suggested_family_updates:
                    suggested_family_updates.append("Add or refine page class patterns for this family.")

    if any(page.page_class == "general" for page in pages):
        suggested_family_updates.append("Review `general` pages and add family-specific classes when they repeat.")
    if errors:
        suggested_family_updates.append("Keep skipping broken or non-HTML links; they are normal crawl noise.")

    return {
        "seed_url": seed_url,
        "site_family": site_family_name or "default",
        "sampling_policy": {
            "same_origin_only": True,
            "mirrors_assets": False,
            "requires_public_pages": True,
        },
        "coverage_map": coverage,
        "component_inventory": dict(component_totals),
        "state_coverage": {name: bool(count) for name, count in observed_states.items()},
        "top_signals": {
            "colors": top_items(all_colors, limit=10),
            "fonts": top_items(all_fonts, limit=6),
            "css_vars": top_items(all_css_vars, limit=12),
        },
        "discrepancies": discrepancy_hints,
        "suggested_family_updates": suggested_family_updates,
        "errors": errors,
        "page_summaries": [asdict(page) for page in pages],
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Public seed URL to sample")
    parser.add_argument("--max-pages", type=int, default=6, help="Maximum number of same-origin pages to sample")
    parser.add_argument("--timeout", type=int, default=15, help="Per-request timeout in seconds")
    parser.add_argument("--output", help="Optional output JSON path")
    parser.add_argument("--site-family", help="Optional site family override from references/site-families.json")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    seed_url = args.url.rstrip("/")

    try:
        seed_html = fetch_html(seed_url, timeout=args.timeout)
    except (HTTPError, URLError, TimeoutError, ValueError) + REQUEST_EXCEPTIONS as exc:
        print(json.dumps({"error": str(exc), "seed_url": seed_url}, indent=2))
        return 1

    site_family = detect_site_family(seed_url, seed_html, configured_family=args.site_family)
    page_class_patterns = get_page_class_patterns(site_family)
    block_patterns = get_block_patterns(site_family)

    discovered = discover_links(seed_url, seed_html)
    selected_urls = pick_representative_urls(
        seed_url,
        discovered,
        max_pages=max(1, args.max_pages),
        page_class_patterns=page_class_patterns,
    )

    pages: list[PageSummary] = []
    errors: list[dict[str, str]] = []

    for url in selected_urls:
        try:
            html = seed_html if url == seed_url else fetch_html(url, timeout=args.timeout)
            pages.append(summarize_page(url, html, page_class_patterns, block_patterns))
        except (HTTPError, URLError, TimeoutError, ValueError) + REQUEST_EXCEPTIONS as exc:
            errors.append({"url": url, "error": str(exc)})

    output = build_output(seed_url, pages, errors, site_family.get("name") if site_family else None)
    rendered = json.dumps(output, indent=2)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(rendered)
    else:
        print(rendered)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
