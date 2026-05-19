# Builder Reference

Use this file when `$persona-builder` needs detailed rules for consuming `$ceo` output and producing persona artifacts.

## Expected CEO Intake

Minimum intake structure:

```text
EXECUTIVE FRAME:
  risk_level: [low | medium | high | critical]
  quality_tier: [ship | standard | excellence]
  confidence: [high | medium | low]

CLASSIFICATION: [STRATEGIC | OPERATIONAL]

SLOT [N] - RESOLVED
...

PROFESSION -> PERSONA MAPPING - SLOT [N]
...

BUILDER HANDOFF:
...
```

Only consume resolved slots.

## Intake Checks

Verify:
- the executive frame is present
- the handoff is operational, or already converted into operational form
- each resolved slot has a matching persona-mapping block
- `persona_goal` aligns with the slot task
- `persona_mode` aligns with the slot mode, unless there is an explicit override reason

If one of these is missing and the omission is material, stop and list the blocking issue.

If `CLASSIFICATION: STRATEGIC` is still present without resolved operational slots, do not build personas. Route the work back to `$ceo` or the strategic operator until operational handoff data exists.

## Persona Spec Template

```text
PERSONA SPEC - SLOT [N]
  persona_name: [Name]
  source_profession: [Title]
  source_soc_code: [Code]
  domain: [Domain]
  mode: [Mode]
  quality_tier: [Inherited tier]
  confidence: [Inherited or slot-specific confidence]

  core_mandate:
    - [What this persona exists to do]

  operating_principles:
    - [Principle 1]
    - [Principle 2]
    - [Principle 3]

  decision_rules:
    - [Rule tied to mode and risk]

  inputs:
    - [Artifacts, signals, or dependencies this persona needs]

  outputs:
    - [Deliverables this persona must produce]

  handoffs:
    - upstream: [What must be true before this persona starts]
    - downstream: [What this persona hands off and to whom]

  escalation_triggers:
    - [When to pause, ask, or route back]

  constraints:
    - [Known constraints and labeled assumptions]
```

## Mode-Specific Guidance

### diagnostic
- emphasize evidence quality, root-cause discipline, and confidence thresholds
- separate observations from interpretations

### generative
- emphasize exploration boundaries, concept quality, and iteration loops
- keep outputs anchored to the declared goal and constraints

### compliance
- emphasize rule sources, exception handling, and auditability
- flag unknown regulations instead of improvising them

### coordination
- emphasize sequencing, ownership clarity, and handoff criteria
- make bottlenecks visible early

### execution
- emphasize procedure fidelity, completion criteria, and output verification
- favor concrete steps over abstract ambition

### negotiation
- emphasize stakeholder interests, tradeoffs, and acceptable outcomes
- distinguish hard constraints from preference conflicts

## Multi-Persona Roster Summary

When multiple personas are built, optionally add:

```text
TEAM ROSTER:
  objective: [shared objective]
  sequence: [how personas interact]
  parallel_work: [which personas can work concurrently]
  critical_handoffs:
    - [handoff 1]
    - [handoff 2]
```

## Guardrails

Do not:
- invent personas for unresolved slots
- silently change the user's risk posture
- erase low confidence from the final artifact
- over-specify a persona beyond what the CEO handoff supports
- rewrite the decomposition unless the intake is clearly inconsistent
