---
name: design-system-ui-developer
description: Build or refactor frontend UI so it stays native to a user-selected design system. Use when Codex needs to create pages, screens, components, forms, dashboards, or marketing UI that must follow a named design system, an existing repo system, a local UI kit, or an extracted system instead of inventing a new visual language.
---

# Design System UI Developer

## Overview

Anchor implementation to the design system the user selects, then build inside that system's components, spacing, typography, interaction patterns, and constraints. Preserve the chosen visual language and implementation conventions instead of drifting into generic custom UI.

## Required Inputs

Obtain or infer these before major UI edits:

- the target screen, page, component, or flow
- the selected design system or source of truth
- the implementation surface such as repo files, local UI kit path, extracted system folder, or mirrored template tree
- any hard constraints such as framework, library, device target, accessibility expectations, or no-new-dependencies rules

If the user has not chosen a design system and the work requires one, pause and ask for the source of truth before implementing substantial UI.

## Workflow

1. Confirm the UI task and the chosen design system.
2. Identify the design-system source of truth:
   - existing repository styles, components, and tokens
   - a user-provided local UI kit directory
   - a local mirrored system such as Material Kit Pro or Soft UI Pro
   - an extracted design system package
3. Inspect the available patterns before editing:
   - components
   - layout shells
   - typography
   - spacing rules
   - colors and surfaces
   - states and interaction patterns
4. Choose the closest existing patterns for the requested UI.
5. Implement by adapting those patterns instead of inventing a separate component family.
6. Verify the result still reads as native to the selected system on desktop and mobile.
7. In the final handoff, state which system was used and which source files or patterns informed the build.

## System Selection Rules

Choose the strongest implementation path for the selected system:

- If the user provides a local UI kit directory, use `$ui-kit-builder`.
- If the user explicitly selects the local Material Kit Pro mirror, use `$material-kit-pro-local-elements`.
- If the user explicitly selects the local Soft UI Pro mirror, use `$soft-ui-design-system-pro-local-elements`.
- If the user wants a webpage project built from an extracted system in the design projects area, use `$webpage-builder-engineer`.
- If the system exists only as a website or visual reference and must be distilled first, use `$design-system-extractor` before implementation.
- If the selected design system already lives inside the working repository, inspect and reuse that in-place system directly.

Prefer the most specific existing skill or source over custom reconstruction.

## Build Rules

- Treat the selected design system as the source of truth.
- Reuse existing primitives, class conventions, tokens, variants, and composition patterns whenever they exist.
- Keep new UI structurally consistent with nearby screens from the same system.
- Match the system's density, spacing rhythm, border radii, typography scale, and interaction tone.
- Preserve existing framework conventions in the target codebase.
- Make responsive behavior part of the default definition of done.
- Add only the minimum custom CSS or JS needed when the system does not already cover the requirement.
- When the system has a strong accessibility pattern already in use, continue it.

## Hard Constraints

- Do not mix multiple design systems unless the user explicitly asks for integration work.
- Do not introduce a new component library, icon set, CSS framework, or visual language just because it is convenient.
- Do not claim system alignment without first inspecting the actual source patterns.
- Do not fill gaps by improvising a disconnected aesthetic when a nearby system pattern can be adapted.
- Do not overwrite established repo conventions with trendy defaults.

## Escalation Rules

Pause and surface the issue when:

- no design system has been selected and the request depends on one
- the chosen source cannot be accessed or verified
- the requested UI pattern does not exist in the selected system and no close adaptation is available
- the user asks to blend conflicting systems without clarifying priority
- strict visual fidelity is required but the source artifacts are incomplete

When the ambiguity is low-risk and reversible, proceed with a labeled assumption.

## Output Contract

Deliver:

- implemented UI changes, not just commentary
- a result that is traceable to the selected system
- a brief note naming the design system used and the patterns or files it was based on
- any important assumptions or gaps if the system did not fully cover the request

## Quality Bar

Before finishing, confirm:

- the design system was explicitly selected or safely inferred
- the relevant source patterns were inspected before editing
- the output feels native to the selected system
- responsive behavior was considered
- new code stays consistent with the target stack and local conventions
- any deviation from the system is small, intentional, and explained
