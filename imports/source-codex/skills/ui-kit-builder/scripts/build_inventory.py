#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path

HTML_EXTENSIONS = {".html", ".htm", ".php", ".twig", ".blade.php", ".jsx", ".tsx", ".vue"}
STYLE_EXTENSIONS = {".css", ".scss", ".sass", ".less"}
SCRIPT_EXTENSIONS = {".js", ".mjs", ".cjs", ".ts"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".avif", ".ico"}
COMMON_FOLDERS = [
    "pages",
    "sections",
    "components",
    "templates",
    "partials",
    "layouts",
    "assets",
    "css",
    "scss",
    "js",
    "img",
]
TEMPLATE_HINT_DIRS = {
    "pages",
    "sections",
    "components",
    "templates",
    "partials",
    "layouts",
    "views",
    "fragments",
    "snippets",
}
NOISE_DIRS = {
    "img",
    "image",
    "images",
    "fonts",
    "icons",
    "vendor",
    "vendors",
    "plugins",
    "node_modules",
    ".git",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inventory a local UI kit directory tree for pages, fragments, and assets."
    )
    parser.add_argument("source_root", help="Absolute or relative path to the local UI kit root")
    parser.add_argument(
        "--output",
        help="Optional markdown file to write. If omitted, print to stdout.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Maximum files to list per category",
    )
    return parser.parse_args()


def suffix_key(path: Path) -> str:
    suffixes = path.suffixes
    if len(suffixes) >= 2 and "".join(suffixes[-2:]) == ".blade.php":
        return ".blade.php"
    return path.suffix.lower()


def bucket_for(path: Path) -> str | None:
    ext = suffix_key(path)
    if ext in HTML_EXTENSIONS:
        if not is_template_candidate(path):
            return None
        return "Templates"
    if ext in STYLE_EXTENSIONS:
        return "Styles"
    if ext in SCRIPT_EXTENSIONS:
        return "Scripts"
    if ext in IMAGE_EXTENSIONS:
        return "Images"
    return None


def is_template_candidate(path: Path) -> bool:
    lowered_parts = {part.lower() for part in path.parts}
    if lowered_parts & NOISE_DIRS:
        if not (lowered_parts & TEMPLATE_HINT_DIRS):
            return False
    return bool(lowered_parts & TEMPLATE_HINT_DIRS)


def interesting_dirs(root: Path) -> list[str]:
    found = []
    for name in COMMON_FOLDERS:
        candidate = root / name
        if candidate.exists() and candidate.is_dir():
            found.append(name)
    return found


def collect(root: Path) -> tuple[dict[str, list[str]], Counter]:
    grouped: dict[str, list[str]] = defaultdict(list)
    counts: Counter = Counter()
    seen_template_keys: set[str] = set()
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        bucket = bucket_for(path)
        if bucket is None:
            continue
        rel = path.relative_to(root).as_posix()
        if bucket == "Templates":
            key = canonical_template_key(rel)
            if key in seen_template_keys:
                continue
            seen_template_keys.add(key)
        grouped[bucket].append(rel)
        counts[bucket] += 1
    return dict(grouped), counts


def canonical_template_key(rel: str) -> str:
    parts = rel.split("/")
    collapsed: list[str] = []
    for part in parts:
        if collapsed and part == collapsed[-1]:
            continue
        collapsed.append(part)
    return "/".join(collapsed)


def render(root: Path, grouped: dict[str, list[str]], counts: Counter, limit: int) -> str:
    lines: list[str] = []
    lines.append("# UI Kit Inventory")
    lines.append("")
    lines.append(f"Source root: `{root.resolve()}`")
    lines.append("")
    dirs = interesting_dirs(root)
    if dirs:
        lines.append("## Detected Folders")
        lines.append("")
        for name in dirs:
            lines.append(f"- `{name}/`")
        lines.append("")
    lines.append("## Summary")
    lines.append("")
    for bucket in ("Templates", "Styles", "Scripts", "Images"):
        lines.append(f"- {bucket}: {counts.get(bucket, 0)}")
    lines.append("")
    for bucket in ("Templates", "Styles", "Scripts", "Images"):
        items = grouped.get(bucket, [])
        if not items:
            continue
        lines.append(f"## {bucket}")
        lines.append("")
        for rel in items[:limit]:
            lines.append(f"- `{rel}`")
        remaining = len(items) - limit
        if remaining > 0:
            lines.append(f"- ... plus {remaining} more")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.source_root).expanduser()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Source root does not exist or is not a directory: {root}")

    grouped, counts = collect(root)
    output = render(root, grouped, counts, args.limit)

    if args.output:
        target = Path(args.output).expanduser()
        if target.exists() and target.is_dir():
            target = target / "ui-kit-inventory.md"
        elif target.suffix.lower() != ".md":
            target = target / "ui-kit-inventory.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output, encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
