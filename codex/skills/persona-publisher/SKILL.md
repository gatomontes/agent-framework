---
name: persona-publisher
description: Render polished persona artifacts from the structured output of $persona-builder, such as clean markdown persona cards, reusable prompt packets, or agent-spec style documents. Use when Codex already has persona specs and needs to package them into a presentation-ready or tool-ready format without changing the upstream role logic.
---

# Persona Publisher

## Overview

Consume persona specs from `$persona-builder` and publish them into a polished final artifact.

Preserve the builder's intent. Improve clarity, formatting, and packaging, but do not reassign roles, rewrite upstream decomposition, or erase uncertainty that was intentionally carried forward.

## Authority And Execution Model

Keep publishing separate from activation:
- the `user` still owns mission scope, final priorities, and approval over material commitments
- the active runtime agent still owns execution in the environment
- `$persona-builder` owns the source persona logic upstream
- `$persona-publisher` owns presentation and packaging only
- a published persona is a clearer artifact, not an automatically active agent, installed skill, or running operator

Decision rule:
- do not imply that publishing a persona activates it
- do not add or change execution authority during formatting
- do not smuggle in new role decisions while polishing the artifact
- if the published artifact could be mistaken for an already-running executor, add a brief note clarifying whether it is documented only or already operationalized elsewhere

## Required Inputs

Expect one or more `PERSONA SPEC` blocks from `$persona-builder`.

Useful optional inputs:
- `BUILDER INTAKE SUMMARY`
- `TEAM ROSTER`
- preferred output target such as markdown card, prompt packet, or agent-spec document
- naming or formatting preferences

If no target format is supplied, default to a polished markdown persona document.

## Workflow

1. Read all persona specs and preserve their role boundaries, mode, confidence, constraints, and escalation triggers.
2. Choose the output target:
   - markdown persona card
   - prompt packet
   - agent-spec style document
3. Normalize headings, tone, and field order across personas.
4. Render each persona into the chosen format.
5. If multiple personas are present, optionally add a roster or orchestration summary.
6. Surface unresolved inconsistencies instead of smoothing them away.

## Formatting Rules

For every published persona, keep these fields intact in substance:
- persona name
- source profession and code if present
- domain
- mode
- quality tier
- confidence
- core mandate
- operating principles
- decision rules
- inputs
- outputs
- handoffs
- escalation triggers
- constraints and assumptions

Presentation upgrades are encouraged:
- tighten wording
- remove redundancy
- improve scanability
- standardize section order
- adapt style to the target artifact

Do not introduce new strategic decisions or role assignments during publishing.

## Output Modes

### Markdown persona card

Best default for sharing, review, or reuse in prompts.

### Prompt packet

Use when the user wants a compact artifact that can be pasted into another agent or tool. Keep instructions direct and ready to run.

### Agent-spec style document

Use when the user wants a more formal operational artifact with explicit sections, guardrails, and handoff behavior.

## Escalation Rules

Pause and call out the issue when:
- persona specs disagree with each other materially
- a required persona section is missing
- confidence is low and the requested format would overstate certainty
- the requested target format would discard important constraints or escalation rules

When the gap is cosmetic rather than substantive, fix it during publishing and continue.

## Output Contract

Default markdown output shape:
- `PUBLISHED PERSONA`
- optional `TEAM PACKAGE SUMMARY`
- `OPEN ISSUES` only when something is substantively wrong or incomplete
- `AUTHORITY NOTE` whenever publication could be mistaken for activation or execution

## Quality Bar

Before finalizing:
- Every published artifact is traceable to a source persona spec.
- Confidence and constraints are preserved.
- Formatting is cleaner, not more misleading.
- Multi-persona outputs feel consistent as a set.
- No new role logic is invented during publishing.

## Reference

Load [references/publisher-reference.md](./references/publisher-reference.md) for target format templates, transformation rules, and consistency checks.
