# Citadel Delegation Protocol

## Purpose

The Delegation Protocol defines how operational work is transferred between authorities, orchestrators, runtimes, and workers inside The Citadel.

Delegation exists to preserve clarity, accountability, and operational continuity.

---

# Core Principle

Delegation transfers responsibility for execution.

It does not transfer unrestricted authority.

---

# Delegation Requirements

Every meaningful delegation must include:

- objective
- expected artifact
- output contract
- consequence tier
- constraints
- verification requirements
- failure conditions
- reporting expectations
- escalation conditions
- responsible authority
- merge owner when multiple workers contribute

Delegation without operational contract is uncontrolled assignment.

---

# Delegation Packet

A delegation packet should minimally contain:

```yaml
operation:
  id: string
  objective: string

authority:
  delegator: string
  executor: string

contracts:
  execution: reference
  verification: reference

constraints:
  consequence_tier: routine | important | critical
  escalation_policy: reference

artifacts:
  required_outputs: list
  merge_owner: string
  output_contract: reference | inline_schema

reporting:
  required_state_emission: true
  return_conditions: list
```

---

# Delegation Boundaries

Delegated actors may:

- execute assigned work
- request clarification
- emit operational state
- report uncertainty
- escalate when required

Delegated actors may not:

- silently expand scope
- redefine consequence tier
- bypass verification
- suppress failures
- return unmergeable output when mergeable output was required
- mutate trusted governance artifacts
- self-authorize final trust

When multiple workers contribute, ownership boundaries should remain explicit.

Preferred rule:

- disjoint write scopes whenever practical
- one named merge owner
- contradiction surfacing instead of forced synthetic agreement

---

# Subdelegation

Subdelegation is prohibited unless explicitly granted.

If subdelegation is permitted:

- the original consequence tier must persist
- lineage must remain reconstructable
- responsibility chains must remain visible
- escalation semantics must persist

---

# Delegation Failure

Delegation failure occurs when:

- objectives are ambiguous
- authority boundaries are violated
- required reporting is missing
- verification is bypassed
- escalation is suppressed
- artifact lineage is lost

Failure must emit explicit operational state.

Multi-worker delegation also fails when:

- merge ownership is undefined
- outputs cannot be reconciled
- contradiction between outputs is blurred instead of surfaced
- artifact boundaries overlap without coordination

---

# Delegation Completion

Delegation is complete only when:

- required artifacts exist
- operational state is emitted
- verification obligations are satisfied
- final disposition is assigned

If the delegation required a bounded return artifact, "thoughts" or freeform status alone do not satisfy completion.

Execution alone does not complete delegation.

---

# Constitutional Rule

Delegation without accountability becomes operational entropy.
