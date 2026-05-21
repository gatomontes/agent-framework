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
- consequence tier
- constraints
- verification requirements
- failure conditions
- reporting expectations
- escalation conditions
- responsible authority

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

reporting:
  required_state_emission: true
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
- mutate trusted governance artifacts
- self-authorize final trust

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

---

# Delegation Completion

Delegation is complete only when:

- required artifacts exist
- operational state is emitted
- verification obligations are satisfied
- final disposition is assigned

Execution alone does not complete delegation.

---

# Constitutional Rule

Delegation without accountability becomes operational entropy.
