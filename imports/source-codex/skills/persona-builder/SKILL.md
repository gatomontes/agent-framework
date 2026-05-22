---
name: persona-builder
description: Build complete persona specifications from the structured output of $ceo, including EXECUTIVE FRAME, resolved profession slots, and profession-to-persona mappings. Use when Codex receives CEO routing output and needs to turn each resolved slot into a ready-to-use persona definition, prompt packet, or builder artifact without redoing the original decomposition.
---

# Persona Builder

## Overview

Consume structured output from `$ceo` and turn each resolved slot into a complete persona artifact.

Trust the upstream decomposition by default. Do not redo the whole routing pass unless the handoff is clearly inconsistent, incomplete, or unsafe to use as written.

## Authority And Execution Model

Keep the pipeline boundary explicit:
- the `user` still owns mission scope, final priorities, and approval over material commitments
- before chief-of-staff deployment, the active runtime agent still owns execution in the environment
- `$ceo` owns routing and candidate selection upstream
- `$persona-builder` owns artifact construction only: convert resolved routing data into usable persona specs
- once deployed, `$chief-of-staff` owns downstream activation and execution orchestration
- a built persona spec is not automatically the active agent, an installed skill, or an executing operator

Use these terms consistently:
- `active agent`: the agent currently operating the session and tools
- `source slot`: a resolved slot handed off from `$ceo`
- `persona spec`: a constructed artifact that describes how a selected candidate should operate
- `materialize`: create the persona artifact; this does not itself activate or execute the persona

Decision rule:
- do not reinterpret persona-building as approval to execute the underlying task
- do not silently change the selected candidate chosen upstream unless the intake is clearly inconsistent or unsafe
- do not imply that creating a persona spec changes who currently has execution authority
- if execution status matters, state whether the persona is only documented, already available elsewhere, or still requires publishing, conversion, or explicit adoption by the active runtime agent

## Required Inputs

Expect these sections from `$ceo`:
- `EXECUTIVE FRAME`
- `CLASSIFICATION`
- resolved `SLOT` blocks
- `PROFESSION -> PERSONA MAPPING` blocks
- `BUILDER HANDOFF`
- optional `CHIEF OF STAFF HANDOFF`
- optional `TEAM ACTIVATION HANDOFF`

Do not build personas from unresolved slots.

## Workflow

1. Read the `EXECUTIVE FRAME` and inherit the stated risk level, quality tier, and confidence.
2. Confirm the situation is operational or that a strategic operator already converted it into operational handoff data.
3. Collect only resolved slots that include builder-ready persona mapping fields.
4. Read any chief-of-staff or team-activation hints that clarify ownership, outputs, or readiness.
5. Normalize naming, domain language, outputs, and constraints.
6. Build one persona artifact per resolved slot.
7. Add execution-facing activation metadata when the upstream handoff is explicit enough to support it.
8. When publishing from an existing markdown source file, never overwrite the source `.md`; instead create a sibling `*-published.md` copy beside the source file.
9. If useful, add a system-level roster summary that explains how the personas fit together.
10. Surface gaps or inconsistencies instead of inventing critical missing details.

## Build Rules

For each resolved slot, preserve and refine:
- `persona_name`
- `persona_domain`
- `persona_goal`
- `persona_context`
- `persona_mode`
- `persona_outputs`

Then add:
- core mandate
- operating principles
- decision rules tied to the slot's mode
- handoff expectations to upstream and downstream roles
- quality bar for outputs
- limits and escalation triggers

When upstream execution handoff data exists, also add:
- activation posture
- owned workstream scope
- expected inputs
- expected outputs
- dependency gates
- done conditions
- chief-of-staff notes for safe activation

Use the executive frame to calibrate tone and rigor:
- `ship`: lean, pragmatic persona with fast iteration bias
- `standard`: balanced persona with normal verification
- `excellence`: highly explicit persona with strong quality controls

If confidence is low, preserve that uncertainty in the persona instructions instead of pretending certainty.

File-handling rule:
- Never overwrite the source markdown file when generating a published persona artifact.
- Write the published artifact to a sibling file whose name appends `-published` before the `.md` extension.
- Preserve the source file as the editable builder artifact and treat the `*-published.md` file as the presentation-ready copy.

## Escalation Rules

Pause and call out the issue when:
- the intake is still strategic and does not yet include resolved operational slots
- a slot is unresolved
- mapping fields are missing from a resolved slot
- the persona goal conflicts with the task text
- the executive frame implies high risk but the handoff is too vague to build safely

When the gap is minor and reversible, proceed with labeled assumptions.

## Output Contract

Default output shape:
- `BUILDER INTAKE SUMMARY`
- one `PERSONA SPEC` block per resolved slot
- optional `TEAM ROSTER` summary when multiple personas interact
- optional `ACTIVATION PROFILE` block per persona when chief-of-staff-ready execution metadata is available
- `OPEN ISSUES` only when there are genuine handoff problems
- `AUTHORITY NOTE` whenever the reader could confuse a built persona spec with an active executor

## Quality Bar

Before finalizing:
- Every persona spec is traceable to one resolved slot.
- No unresolved slot is silently converted into a persona.
- Quality level matches the inherited executive tier.
- Handoff responsibilities are explicit.
- Chief-of-staff activation metadata is included when upstream data supports it and omitted when it would be guessed.
- Assumptions are labeled.
- Any published markdown artifact is written to a sibling `*-published.md` file rather than overwriting the source `.md`.

## Reference

Load [references/builder-reference.md](./references/builder-reference.md) for the expected CEO handoff format, persona-spec template, and consistency checks.
