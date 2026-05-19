---
name: persona-to-skill
description: Convert published personas or structured persona specs into real installed Codex skills under the local skills directory. Use when Codex already has a stable persona artifact from $persona-builder or $persona-publisher and needs to turn it into a reusable skill folder with valid SKILL.md metadata and optional references for future invocation.
---

# Persona To Skill

## Overview

Turn persona artifacts into real Codex skills that can be reused later.

Use the official skill scaffold, preserve the persona's core behavior, and compress the artifact into a trigger-friendly skill instead of copying the source verbatim.

## Authority And Execution Model

Keep conversion separate from execution:
- the `user` still owns mission scope, final priorities, and approval over material commitments
- the active runtime agent still owns execution in the environment
- upstream persona artifacts define the intended operator behavior
- `$persona-to-skill` owns conversion of those artifacts into reusable installed skills
- an installed skill is an available capability, not an automatically active executor for the current task

Use these terms consistently:
- `installed skill`: a reusable capability placed in the skills directory
- `active agent`: the agent currently operating the session and tools
- `activation`: explicit invocation or adoption of a skill by the active agent

Decision rule:
- do not imply that creating or updating a skill automatically applies it to the current task
- do not imply that installation transfers execution authority away from the active runtime agent
- do not overwrite an existing skill unless the update path is explicit
- if operational status matters, state whether the skill was merely created, updated, validated, or also explicitly invoked elsewhere

## Required Inputs

Accept either:
- one or more `PERSONA SPEC` blocks from `$persona-builder`
- one or more `PUBLISHED PERSONA` blocks from `$persona-publisher`

Optional inputs:
- desired skill name
- desired install path
- whether to create one skill per persona or a bundled skill set

If no install path is provided, default to the local Codex skills directory.

## Workflow

1. Inspect the persona artifact and confirm it is complete enough to become a reusable skill.
2. Decide whether the output should be:
   - one skill per persona
   - one bundled multi-persona skill
3. Derive a short hyphen-case skill name.
4. Use the official skill scaffold to create the folder.
5. Write a lean `SKILL.md` that preserves triggers, core behavior, outputs, and escalation rules.
6. Move detailed templates or examples into `references/` only when needed.
7. Validate the finished skill.

## Conversion Rules

When converting a persona into a skill:
- keep the skill focused on what should trigger it and how it should behave
- preserve uncertainty, assumptions, and escalation triggers from the persona artifact
- convert long prose into concise imperative instructions
- keep frontmatter description trigger-rich so Codex knows when to use the skill
- avoid copying presentation-only sections that do not help execution

Prefer one skill per persona unless the personas are intentionally designed to operate as one inseparable system.

## Escalation Rules

Pause and call out the issue when:
- the persona artifact is missing mandate, outputs, or escalation logic
- the persona is too vague to yield a reliable trigger description
- multiple personas overlap so heavily that separate skill boundaries would be misleading
- the requested conversion would overwrite an existing skill without a clear update path

When the gap is minor, proceed with labeled assumptions.

## Output Contract

Default delivery should include:
- created skill path or paths
- final skill name or names
- notes on what was preserved vs compressed
- validation result
- `AUTHORITY NOTE` whenever installation could be confused with activation or current-task execution

## Quality Bar

Before finalizing:
- the generated skill is narrower and more reusable than the source persona text
- the trigger description is concrete
- important guardrails survive the conversion
- the installed skill validates cleanly

## Reference

Load [references/conversion-reference.md](./references/conversion-reference.md) for naming rules, conversion mapping, and output templates.
