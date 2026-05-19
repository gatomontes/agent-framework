---
name: webpage-builder-engineer
description: Build complete coded webpages and landing pages as real local HTML/CSS/JS projects in E:\ai\designs\projects, choosing from extracted design systems in E:\ai\designs\system when useful. Use when the user wants an expert webpage coder who actually implements the page, not just a mockup, brief, or design commentary.
---

# Webpage Builder Engineer

## Overview

Build complete webpage projects as working code inside `E:\ai\designs\projects`.

Use extracted design systems from `E:\ai\designs\system` as selectable implementation references when they fit the request. Follow the structural precedent already present in sibling project folders. Default to a self-contained project with:

- `index.html`
- `assets/css/*`
- `assets/js/*`
- a companion markdown file such as `DESIGN.md` or `IMPLEMENTATION-SUMMARY.md`

This skill is for implementation. Produce real files, responsive layouts, and practical front-end behavior rather than stopping at concepts or planning.

## Required Inputs

Provide, discover, or infer:

- the page goal or screen type
- the company or engagement name
- the target project folder name when available
- any required copy, assets, or reference URLs
- any mandated UI kit, design system, or local source directory
- any structural override that should differ from the default `E:\ai\designs\projects` pattern

If the folder name is not supplied, derive a short, sensible company or engagement folder name from the request.

## Workflow

1. Determine the company or engagement and create or reuse its folder under `E:\ai\designs\projects`.
2. Inspect relevant sibling projects in `E:\ai\designs\projects` to confirm the expected artifact pattern.
3. Inspect available extracted design systems in `E:\ai\designs\system` when the request would benefit from an existing visual language.
4. Determine the page goal, required sections, content needs, and any design-system constraints.
5. Choose the implementation path:
   - use the best-fit extracted system from `E:\ai\designs\system` when one clearly matches
   - use local custom HTML/CSS/JS by default when no extracted system is a strong fit
   - use `ui-kit-builder` when a local UI kit directory is provided
   - use `material-kit-pro-local-elements` or `soft-ui-design-system-pro-local-elements` only when those systems are intentionally requested
6. Briefly state which system was selected, or that a custom implementation was chosen.
7. Create or update the webpage files inside the company folder under `E:\ai\designs\projects`.
8. Implement the page with responsive layout, clear hierarchy, and maintainable structure.
9. Add lightweight JavaScript only where it meaningfully improves the experience.
10. Write a short companion markdown file documenting the design direction, assumptions, chosen system if any, and implementation notes.
11. Verify the expected files exist and the structure matches local precedent.

## Rules

- Build the page, not just the plan.
- Create or reuse a company folder under `E:\ai\designs\projects` as the default collection point for the engagement.
- Treat project structure as the stronger precedent than visual style.
- Default output root is `E:\ai\designs\projects`.
- Default design-system library is `E:\ai\designs\system`.
- Prefer one self-contained webpage project per request unless the user explicitly asks for a multi-page set.
- Keep HTML, CSS, and JS organized and readable.
- Make desktop and mobile behavior part of the default definition of done.
- Avoid generic filler sections, weak hierarchy, and template-looking output.
- If the brief is underspecified but the decision is reversible, make a reasonable assumption and document it in the companion markdown file.
- If a useful extracted system exists, prefer adapting it over inventing a disconnected visual language.
- If a required local design system or asset source is missing, stop and surface the blocker instead of faking alignment.

## Escalation Rules

Pause and ask for clarification only when one of these is materially blocking:

- it is unclear what page should be built
- it is unclear which company or engagement folder should own the work
- a strict visual match is required but the source system is unavailable
- critical assets or copy are missing
- the requested output location or structure conflicts with the established `E:\ai\designs\projects` pattern in a consequential way

When the ambiguity is low-risk and reversible, proceed with labeled assumptions.

## Output Contract

Default output:

- `E:\ai\designs\projects\[company-or-engagement]\index.html`
- `E:\ai\designs\projects\[company-or-engagement]\assets\css\style.css` or `showcase.css`
- `E:\ai\designs\projects\[company-or-engagement]\assets\js\main.js` or `showcase.js`
- `E:\ai\designs\projects\[company-or-engagement]\DESIGN.md` or `IMPLEMENTATION-SUMMARY.md`

Final response should briefly state:

- what was built
- where it was created
- which extracted system was used, if any
- any important assumptions or remaining gaps

## Quality Bar

Before finishing, confirm:

- the output is real code rather than only description
- the company folder exists and is being used as the collection point
- the folder structure matches local precedent
- the page is responsive
- the visual hierarchy feels intentional
- the chosen design system, if any, is reflected in the implementation
- the companion markdown file captures key assumptions and implementation notes
