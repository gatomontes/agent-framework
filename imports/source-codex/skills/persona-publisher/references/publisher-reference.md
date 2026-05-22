# Publisher Reference

Use this file when `$persona-publisher` needs detailed rules for turning `$persona-builder` output into polished artifacts.

## Expected Input

Minimum expected structure:

```text
PERSONA SPEC - SLOT [N]
  persona_name: [Name]
  source_profession: [Title]
  source_soc_code: [Code]
  domain: [Domain]
  mode: [Mode]
  quality_tier: [Tier]
  confidence: [Confidence]
  ...
```

Optional supporting structure:
- `BUILDER INTAKE SUMMARY`
- `TEAM ROSTER`
- explicit output target

## Target Selection Rules

Use these defaults:
- no target given -> markdown persona card
- user asks for something to paste into another agent -> prompt packet
- user asks for formal operational documentation -> agent-spec style document

If the requested format would hide important caveats, keep the caveats and note the tradeoff.

## Markdown Persona Card Template

```text
PUBLISHED PERSONA: [persona_name]

Identity
- Role: [source profession]
- Domain: [domain]
- Mode: [mode]
- Quality Tier: [quality_tier]
- Confidence: [confidence]

Mandate
- [core mandate items]

Operating Principles
- [principle 1]
- [principle 2]
- [principle 3]

Decision Rules
- [rule 1]
- [rule 2]

Inputs
- [input 1]
- [input 2]

Outputs
- [output 1]
- [output 2]

Handoffs
- Upstream: [upstream handoff]
- Downstream: [downstream handoff]

Escalation Triggers
- [trigger 1]
- [trigger 2]

Constraints
- [constraint or assumption 1]
- [constraint or assumption 2]
```

## Prompt Packet Template

```text
ROLE: [persona_name]

MISSION:
[compressed mandate]

OPERATING RULES:
- [rule 1]
- [rule 2]
- [rule 3]

INPUTS YOU REQUIRE:
- [input 1]

OUTPUTS YOU MUST PRODUCE:
- [output 1]

ESCALATE WHEN:
- [trigger 1]

CONSTRAINTS:
- [constraint 1]
```

Use the prompt packet when compactness matters more than full documentation.

## Agent-Spec Style Template

```text
AGENT SPEC: [persona_name]

Purpose
- [mandate]

Scope
- Domain: [domain]
- Mode: [mode]
- Quality Tier: [quality_tier]
- Confidence: [confidence]

Behavior
- Operating principles
- Decision rules
- Escalation triggers

Interfaces
- Inputs
- Outputs
- Handoffs

Constraints
- [constraints and assumptions]
```

## Multi-Persona Package Summary

When publishing multiple personas, optionally add:

```text
TEAM PACKAGE SUMMARY
- Objective: [shared objective]
- Persona set: [names]
- Sequence: [interaction order]
- Parallel work: [if any]
- Fragile handoffs: [if any]
```

## Consistency Checks

Verify:
- every published section maps back to a source persona spec
- quality tier and confidence survive the transformation
- escalation triggers remain visible
- formatting changes do not change role meaning

## Guardrails

Do not:
- erase low confidence or assumptions for style reasons
- upgrade a draft persona into a higher-certainty artifact without evidence
- invent capabilities not present in the builder output
- merge distinct personas unless the input explicitly asks for it
