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


PAGE_CLASS_PATTERNS = [
    ("community", re.compile(r"\b(society|club|membership|member|community)\b", re.I)),
    ("menu", re.compile(r"\b(menu|drinks|cocktails|food)\b", re.I)),
    ("faq", re.compile(r"\b(faq|questions|help)\b", re.I)),
    ("team", re.compile(r"\b(crew|team|about-us|about)\b", re.I)),
    ("shop", re.compile(r"\b(shop|store|cart|checkout|product|products|auctions)\b", re.I)),
    ("gallery", re.compile(r"(gallery|image-gallery|photos)", re.I)),
    ("offers", re.compile(r"(offers|offer|packages|package|special)", re.I)),
    ("blog", re.compile(r"\b(blog|journal|stories|news)\b", re.I)),
    ("events", re.compile(r"\b(events|event|weddings|meetings|conference)\b", re.I)),
    ("pricing", re.compile(r"(pricing|plans|billing|subscribe)", re.I)),
    ("auth", re.compile(r"(login|sign-in|signin|sign-up|signup|register|auth)", re.I)),
    ("dashboard", re.compile(r"(dashboard|overview|workspace|console|app)", re.I)),
    ("settings", re.compile(r"(settings|account|profile|preferences)", re.I)),
    ("docs", re.compile(r"(docs|documentation|guide|api|learn)", re.I)),
    ("form", re.compile(r"(contact|apply|request|checkout|form|survey)", re.I)),
    ("data", re.compile(r"(table|reports|analytics|customers|orders|list)", re.I)),
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


def classify_page(url: str, html: str) -> str:
    parsed = urlparse(url)
    path = parsed.path or "/"
    if path in {"", "/"}:
        return "home"

    for label, pattern in PAGE_CLASS_PATTERNS:
        if pattern.search(path):
            return label

    sample = html[:800]
    for label, pattern in PAGE_CLASS_PATTERNS:
        if pattern.search(sample):
            return label
    return "general"


def top_items(values: Iterable[str], limit: int = 6) -> list[str]:
    counter = Counter(v.strip() for v in values if v and v.strip())
    return [item for item, _count in counter.most_common(limit)]


def summarize_page(url: str, html: str) -> PageSummary:
    analysis_html = extract_analysis_html(html)
    parser = LinkParser()
    parser.feed(html)

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

    return PageSummary(
        url=url,
        title=parser.title or "",
        page_class=classify_page(url, analysis_html),
        component_hits=component_hits,
        state_hits=state_hits,
        top_colors=colors,
        fonts=fonts,
        css_vars=css_vars,
        notes=notes,
    )


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


def extract_analysis_html(html: str) -> str:
    extracted = re.sub(r"<!--.*?-->", " ", html, flags=re.S)

    main_match = re.search(r"<main\b[^>]*>(.*?)</main>", extracted, re.I | re.S)
    if main_match:
        extracted = main_match.group(1)

    block_patterns = [
        r"<(script|style|noscript)\b.*?</\1>",
        r"<(header|footer|nav)\b.*?</\1>",
        r"<(?:div|section|aside|form)\b[^>]*(?:id|class)=[\"'][^\"']*(modal-booking|booking|book-now|reservation|reserve|menu|menumobile|cookie|consent|newsletter)[^\"']*[\"'][^>]*>.*?</(?:div|section|aside|form)>",
    ]
    for pattern in block_patterns:
        extracted = re.sub(pattern, " ", extracted, flags=re.I | re.S)

    return extracted.strip() or html


def score_candidate(seed_url: str, url: str) -> tuple[int, str]:
    if url.rstrip("/") == seed_url.rstrip("/"):
        return (-10, url)
    parsed = urlparse(url)
    path = parsed.path or "/"
    score = 100
    depth = len([segment for segment in path.split("/") if segment])
    score -= min(depth, 6) * 3
    for label, pattern in PAGE_CLASS_PATTERNS:
        if pattern.search(path):
            score += 25
            break
    if re.search(r"(privacy|terms|legal|careers|press)", path, re.I):
        score -= 20
    return (-score, url)


def pick_representative_urls(seed_url: str, discovered_urls: list[str], max_pages: int) -> list[str]:
    sorted_urls = [url for _score, url in sorted(score_candidate(seed_url, url) for url in discovered_urls)]
    chosen = [seed_url.rstrip("/")]
    seen_classes: set[str] = set()
    for url in sorted_urls:
        normalized = url.rstrip("/")
        if normalized in chosen:
            continue
        if len(chosen) >= max_pages:
            break
        page_class = classify_page(url, url)
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


def build_output(seed_url: str, pages: list[PageSummary], errors: list[dict[str, str]]) -> dict:
    coverage = []
    component_totals: Counter[str] = Counter()
    observed_states: Counter[str] = Counter()
    all_colors: list[str] = []
    all_fonts: list[str] = []
    all_css_vars: list[str] = []

    for page in pages:
        coverage.append(
            {
                "page_class": page.page_class,
                "url": page.url,
                "title": page.title,
                "key_patterns_found": [name for name, count in page.component_hits.items() if count > 0],
                "confidence": "medium" if page.page_class == "general" else "high",
                "notes": page.notes,
            }
        )
        component_totals.update({k: v for k, v in page.component_hits.items() if v})
        observed_states.update({k: int(v) for k, v in page.state_hits.items() if v})
        all_colors.extend(page.top_colors)
        all_fonts.extend(page.fonts)
        all_css_vars.extend(page.css_vars)

    return {
        "seed_url": seed_url,
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
        "errors": errors,
        "page_summaries": [asdict(page) for page in pages],
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Public seed URL to sample")
    parser.add_argument("--max-pages", type=int, default=6, help="Maximum number of same-origin pages to sample")
    parser.add_argument("--timeout", type=int, default=15, help="Per-request timeout in seconds")
    parser.add_argument("--output", help="Optional output JSON path")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    seed_url = args.url.rstrip("/")

    try:
        seed_html = fetch_html(seed_url, timeout=args.timeout)
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        print(json.dumps({"error": str(exc), "seed_url": seed_url}, indent=2))
        return 1

    discovered = discover_links(seed_url, seed_html)
    selected_urls = pick_representative_urls(seed_url, discovered, max_pages=max(1, args.max_pages))

    pages: list[PageSummary] = []
    errors: list[dict[str, str]] = []

    for url in selected_urls:
        try:
            html = seed_html if url == seed_url else fetch_html(url, timeout=args.timeout)
            pages.append(summarize_page(url, html))
        except (HTTPError, URLError, TimeoutError, ValueError) as exc:
            errors.append({"url": url, "error": str(exc)})

    output = build_output(seed_url, pages, errors)
    rendered = json.dumps(output, indent=2)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(rendered)
    else:
        print(rendered)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
