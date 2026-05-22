---
name: soft-ui-design-system-pro-local-elements
description: Build or refactor HTML, Bootstrap, and frontend screens by composing only from the local Soft UI Design System Pro mirror at E:\htdocs\httrack\softuipro\demos.creative-tim.com\soft-ui-design-system-pro. Use when Codex must create landing pages, marketing pages, auth screens, content sections, forms, navigation, or UI fragments that should stay inside this design system and reuse only the elements, classes, assets, and markup patterns already present in that directory tree.
---

# Soft UI Design System Pro Local Elements

## Overview

Use the local Soft UI Design System Pro mirror as a closed component library. Read the existing demo pages and section files, then assemble or adapt markup from that source tree instead of introducing a different design system or outside UI kit.

## Source Of Truth

- Treat `E:\htdocs\httrack\softuipro\demos.creative-tim.com\soft-ui-design-system-pro` as the only allowed design source.
- Reuse the local CSS, JS, icons, images, utility classes, and HTML structures from that tree.
- Prefer copying and adapting whole sections from `sections/` and complete page skeletons from `pages/`.
- Use [references/inventory.md](C:/Users/gatom/.codex/skills/soft-ui-design-system-pro-local-elements/references/inventory.md) to find available templates and [references/composition-rules.md](C:/Users/gatom/.codex/skills/soft-ui-design-system-pro-local-elements/references/composition-rules.md) for guardrails.
- Regenerate the inventory with [scripts/build_inventory.py](C:/Users/gatom/.codex/skills/soft-ui-design-system-pro-local-elements/scripts/build_inventory.py) if the mirrored source tree changes.

## Workflow

1. Identify the target page or fragment type.
2. Search `pages/` for the closest full-page match and `sections/` for reusable fragments.
3. Copy the nearest existing markup pattern, then edit text, imagery, ordering, and small structural details to fit the request.
4. Keep asset paths compatible with the destination file so the local `assets/` and `img/` folders continue to work.
5. Verify every major block in the output can be traced to an existing local template or section.

## Hard Constraints

- Do not introduce Tailwind, React component libraries, new CDN design systems, or custom visual frameworks.
- Do not invent new component families when an existing local section can be adapted.
- Do not reference remote stock assets when an equivalent local asset already exists.
- Do not claim a component exists unless it is present in the mirrored directory.
- Do not widen the scope to files outside the Soft UI mirror unless the user explicitly asks for integration work.

## Allowed Adaptations

- Merge multiple local sections into one page.
- Remove decorative sub-elements from an existing section.
- Swap copy, icons, images, CTA labels, and ordering.
- Adjust Bootstrap grid sizing, spacing, or visibility utilities when the pattern already exists nearby in the source.
- Combine a `pages/` shell with `sections/` fragments to create a new page, as long as the resulting design still reads as native Soft UI.

## Picking Templates

- For complete screens, start in `pages/`.
- For reusable fragments, start in `sections/page-sections`, `sections/navigation`, `sections/input-areas`, `sections/elements`, or `sections/attention-catchers`.
- When multiple candidates fit, choose the one with the fewest structural edits.
- Ignore obvious HTTrack artifact files such as mirrored remote-image `.html` files under nested `assets`, `_https_`, or `https_` paths.

## Implementation Notes

- Keep the original CSS stack centered on `assets/css/soft-design-system-pro.min5438.css`, `nucleo-icons.css`, and `nucleo-svg.css` unless the target file already uses a different local variant.
- Preserve existing class naming and DOM patterns where practical; prefer extension by composition over rewriting.
- Use `rg` or equivalent text search to find specific headings, cards, navbars, forms, or CTA patterns before editing.
- If the user asks for a new page, mention which source templates you are basing it on.

## References

- Read [references/inventory.md](C:/Users/gatom/.codex/skills/soft-ui-design-system-pro-local-elements/references/inventory.md) for the current page and section map.
- Read [references/composition-rules.md](C:/Users/gatom/.codex/skills/soft-ui-design-system-pro-local-elements/references/composition-rules.md) when deciding whether a change stays within the allowed design system.
