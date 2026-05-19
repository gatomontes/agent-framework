# Conversion Reference

Use this file when `$persona-to-skill` converts persona artifacts into installed Codex skills.

## Accepted Sources

Preferred sources:
- `PERSONA SPEC` blocks from `$persona-builder`
- `PUBLISHED PERSONA` blocks from `$persona-publisher`

Favor `PERSONA SPEC` when both are available because it retains more operational structure.

## Naming Rules

- Normalize names to lowercase hyphen-case.
- Prefer concise action or role-oriented names.
- Keep names under 64 characters.
- If converting several personas, default to one skill per persona unless the user explicitly wants a bundled skill.

Examples:
- `Mobile Payments Developer` -> `mobile-payments-developer`
- `Payments Compliance Lead` -> `payments-compliance-lead`
- `Restaurant GTM Lead` -> `restaurant-gtm-lead`

## Conversion Mapping

Map persona content into skill structure like this:

| Persona artifact | Skill destination |
|---|---|
| persona name | `name` candidate and skill title |
| mandate | overview and core workflow |
| operating principles | behavior rules |
| decision rules | escalation and quality logic |
| inputs and outputs | workflow and output contract |
| handoffs | collaboration notes |
| constraints and assumptions | guardrails or references |

## Skill Writing Rules

### Frontmatter

Use only:

```yaml
---
name: skill-name
description: Trigger-rich description explaining what the skill does and when to use it.
---
```

### Body

Prefer sections like:
- Overview
- Required Inputs
- Workflow
- Rules
- Escalation Rules
- Output Contract
- Quality Bar
- Reference

Keep it imperative and concise.

## Installation Path

Default target:

```text
C:\Users\gatom\.codex\skills
```

Unless the user explicitly requests another install location.

## Validation

After creating or updating a generated skill:
1. run the official skill initializer if creating from scratch
2. write the final `SKILL.md`
3. add references only if they improve reuse
4. run the validator

## Guardrails

Do not:
- copy a long published persona into `SKILL.md` verbatim
- keep decorative publishing prose that does not help execution
- erase uncertainty or escalation rules during conversion
- merge distinct personas into one skill without clear user intent
