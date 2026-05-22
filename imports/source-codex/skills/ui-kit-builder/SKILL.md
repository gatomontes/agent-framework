---
name: ui-kit-builder
description: Build or refactor HTML, CSS, Bootstrap, and frontend UI by composing only from elements, assets, classes, and markup patterns found inside a user-specified local directory tree. Use when Codex must create pages, components, forms, dashboards, landing pages, auth screens, or UI fragments that must stay inside an existing local UI kit or template library and should require a source path before any UI work begins.
---

# UI Kit Builder

## Overview

Use the chosen local UI kit directory as a closed design source. Require the path first, generate an inventory of that source tree, identify the nearest existing templates or fragments, and then build only by adapting those local elements instead of introducing a different framework or visual language.

## Workflow

1. Require and verify the source root.
2. Generate and review an inventory for that source tree.
3. Inspect the available templates, sections, assets, and styles.
4. Choose the closest existing local patterns.
5. Assemble or adapt output using only those local ingredients.
6. Refuse unsupported components and verify every major block can be traced back to the chosen directory tree.

## Resolve The Source Root

- If the user already gave a path, use it and do not ask again.
- If the path is missing, ask for the absolute path to the UI kit directory before editing files.
- Do not start UI implementation until the path is known and verified to exist.
- Treat that user-provided directory and its subdirectories as the only allowed source for UI elements unless the user explicitly broadens scope.
- Always run [scripts/build_inventory.py](C:/Users/gatom/.codex/skills/ui-kit-builder/scripts/build_inventory.py) against the chosen source tree before choosing templates.
- Prefer writing the inventory to a markdown file inside the working area, such as `ui-kit-inventory.md`, when that helps later traceability.

## Inspect The Kit

- Search recursively for likely entry points such as `pages`, `sections`, `components`, `templates`, `partials`, `layouts`, `assets`, `css`, `scss`, `js`, and `img`.
- Prefer complete pages when the user wants a full screen and smaller fragments when the user wants a partial UI.
- Look for the closest existing match before writing custom structure.
- Use the generated inventory as the first pass and then open only the most relevant source files.
- Read [references/composition-rules.md](C:/Users/gatom/.codex/skills/ui-kit-builder/references/composition-rules.md) when deciding whether a change stays inside the local kit.

## Build Inside The Kit

- Reuse local HTML structures, CSS classes, JavaScript hooks, icons, imagery, spacing systems, and component patterns from the chosen directory tree.
- Copy and adapt nearby markup instead of inventing a new component family.
- Preserve asset path conventions used by the local kit.
- Keep the resulting UI visually native to the selected source.
- Treat missing source patterns as a constraint, not an invitation to design a new system.

## Hard Constraints

- Do not import a different design system, component library, CSS framework, icon pack, or remote UI dependency unless it already exists inside the chosen directory tree.
- Do not invent components that are absent from the local kit when a nearby existing pattern can be adapted.
- Do not claim an element exists unless it is present in the chosen directory or a subdirectory.
- Do not mix patterns from outside the chosen source root unless the user explicitly asks for integration work.
- Do not silently substitute a made-up component for a missing one.

## Allowed Adaptations

- Merge multiple local sections into one page.
- Remove decorative or optional sub-elements from an existing pattern.
- Replace copy, labels, icons, imagery, and ordering.
- Adjust grid spans, spacing utilities, and visibility classes when those conventions already exist in the kit.
- Combine a full-page shell with local fragments as long as the result still reads as native to the chosen UI kit.

## Refusal Rule

- If a requested component, interaction, or layout pattern is not present in the chosen source tree, say so explicitly.
- Offer the closest supported local pattern only if one genuinely exists.
- If no acceptable local substitute exists, pause and ask whether to broaden scope rather than fabricating the missing UI.

## Delivery Notes

- Mention which local templates, files, or folders the solution is based on when creating or refactoring UI.
- Mention that the inventory was generated before selecting source templates.
- If the kit lacks a requested pattern, say so plainly and either approximate it with the closest local pattern or pause for direction.
- Favor traceability over novelty.
