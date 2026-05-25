# Citadel Notarial Protocol

## Status

Canonical Citadel protocol.

This protocol defines how Citadel records station findings and proposed actions before a governed scroll is handed to `Rook` for return normalization.

---

# Purpose

The Notarial Protocol exists to preserve substantive institutional memory at the return boundary.

Citadel already preserves:
- movement lineage
- verification artifacts
- critique outputs
- final disposition

The institution also needs a governed summary of:
- what each station concluded
- which actions are proposed or required
- which actions are blocked
- which human decisions remain necessary

without forcing `Rook` or `Scribe` to invent that summary from fragments.

---

# Core Principle

Return without notarial substance is boundary incompleteness.

Movement lineage alone does not explain what the institution learned or what it recommends next.

---

# Position Relative To Flow

Notarial preparation occurs after final disposition and before `Rook` emits a return scroll.

It is not an additional trust gate inside the operational flow.

It is a boundary-preparation requirement for substantive clarity and archival custody.

```text
Final Disposition
  -> Notary Preparation
    -> Archival Copy
      -> Rook Return
```

---

# Notary Duties

Notary must:

- inspect governed station outputs
- record findings for each materially participating station
- record proposed, required, blocked, or deferred actions
- preserve unresolved questions
- prepare the pre-return summary attached to the governed scroll
- ensure an archival copy exists before external return
- escalate when notarial completeness cannot be honestly claimed

Notary may:

- normalize phrasing for clarity
- compress duplicative action recommendations
- group equivalent station findings when lineage remains clear
- annotate evidence references

Notary may not:

- invent findings absent from station outputs
- blur findings into final disposition
- erase contradiction between stations
- suppress blocked actions for presentation comfort
- treat archival copy creation as optional when return is being prepared

---

# Minimum Notarial Record

Every governed return-capable scroll should be able to preserve:

```yaml
notarial_record:
  prepared_by: null
  prepared_at: null
  station_findings:
    - station: null
      finding_summary: null
      evidence_refs: []
      proposed_actions: []
      blocked_actions: []
      unresolved_questions: []

  pre_return_summary:
    disposition_context: null
    required_actions: []
    recommended_actions: []
    blocked_actions: []
    human_decisions_required: []
    follow_up_routes: []
    archival_copy_created: false
    archival_reference: null
```

Serialization may vary.

Semantic completeness may not disappear.

---

# Station Coverage Rule

Materially participating stations should be represented in the notarial record when they affect:

- execution outcome
- verification result
- critique judgment
- audit judgment
- coherence determination
- restoration burden
- escalation necessity
- external next-step safety

Trivial transit-only stations do not require substantive findings merely because they touched the scroll.

---

# Pre-Return Summary Rule

Before `Rook` emits a return scroll, the attached notarial summary must preserve:

- the disposition context
- the actions Citadel recommends
- the actions Citadel requires before safe continuation
- the actions Citadel considers blocked
- the human decisions still required
- the archival custody reference for the copied summary

If any of these remain unknown, the uncertainty must remain explicit.

---

# Archival Requirement

The notarial pre-return summary must be copied into archival custody before the return scroll is emitted externally.

The archival copy should preserve:

- mission reference
- source scroll reference
- prepared summary
- unresolved questions
- required follow-up actions
- preparation timestamp
- preparing authority

Archive custody does not change final disposition.

It preserves substantive return readiness and continuity memory.

---

# Relationship To Other Roles

`Citadel Scribe` preserves movement lineage.

`Notary` preserves station findings and proposed actions.

`Rook` normalizes boundary ingress and egress.

`Auditor` may inspect the notarial record for completeness and honesty when required.

These roles are complementary, not interchangeable.

---

# Failure Conditions

Notarial failure includes:

- return scroll prepared with no station findings summary
- proposed actions omitted despite station recommendations
- archival copy missing before external return
- contradictions flattened into fake consensus
- blocked actions hidden to improve presentation
- notarial completeness claimed without adequate station basis

Failure should produce:

- explicit incompleteness notice
- escalation recommendation
- blocked return readiness when required

---

# Constitutional Rule

No governed return scroll should leave Citadel without:

- preserved movement lineage
- preserved final disposition
- preserved notarial summary
- preserved archival copy reference

Boundary clarity requires both movement memory and substantive memory.
