---
name: persona-builder
description: Build complete persona specifications from the structured output of $ceo, including EXECUTIVE FRAME, resolved profession slots, and profession-to-persona mappings. Use when Codex receives CEO routing output and needs to turn each resolved slot into a ready-to-use persona definition, prompt packet, or builder artifact without redoing the original decomposition.
---

# Persona Builder

## Overview

Consume structured output from `$ceo` and turn each resolved slot into a complete persona artifact.

Trust the upstream decomposition by default. Do not redo the whole routing pass unless the handoff is clearly inconsistent, incomplete, or unsafe to use as written.

## Required Inputs

Expect these sections from `$ceo`:
- `EXECUTIVE FRAME`
- `CLASSIFICATION`
- resolved `SLOT` blocks
- `PROFESSION -> PERSONA MAPPING` blocks
- `BUILDER HANDOFF`

Do not build personas from unresolved slots.

## Workflow

1. Read the `EXECUTIVE FRAME` and inherit the stated risk level, quality tier, and confidence.
2. Confirm the situation is operational or that a strategic operator already converted it into operational handoff data.
3. Collect only resolved slots that include builder-ready persona mapping fields.
4. Normalize naming, domain language, outputs, and constraints.
5. Build one persona artifact per resolved slot.
6. If useful, add a system-level roster summary that explains how the personas fit together.
7. Surface gaps or inconsistencies instead of inventing critical missing details.

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

Use the executive frame to calibrate tone and rigor:
- `ship`: lean, pragmatic persona with fast iteration bias
- `standard`: balanced persona with normal verification
- `excellence`: highly explicit persona with strong quality controls

If confidence is low, preserve that uncertainty in the persona instructions instead of pretending certainty.

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
- `OPEN ISSUES` only when there are genuine handoff problems

## Quality Bar

Before finalizing:
- Every persona spec is traceable to one resolved slot.
- No unresolved slot is silently converted into a persona.
- Quality level matches the inherited executive tier.
- Handoff responsibilities are explicit.
- Assumptions are labeled.

## Reference

Load [references/builder-reference.md](./references/builder-reference.md) for the expected CEO handoff format, persona-spec template, and consistency checks.
