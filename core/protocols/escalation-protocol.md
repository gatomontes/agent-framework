# Citadel Escalation Protocol

## Purpose

The Escalation Protocol defines how unresolved uncertainty, contradiction, failure, authority conflict, or governance instability is transferred to higher authority inside The Citadel.

Escalation exists to preserve trustworthiness under operational pressure.

---

# Core Principle

Escalation is not failure.

Suppressed escalation is failure.

---

# Escalation Triggers

Escalation should occur when:

- verification fails
- confidence is insufficient
- authority boundaries are unclear
- contradictory evidence exists
- restoration is required
- runtime instability appears
- recursion becomes uncontrolled
- consequence tier exceeds runtime trust
- human decision is required

---

# Escalation Scroll

Escalation must preserve operational continuity.

A valid escalation scroll should include:

```yaml
operation:
  id: string
  current_state: string

reason:
  escalation_trigger: string
  blocking_conditions: list

artifacts:
  relevant_artifacts: list

verification:
  status: VERIFIED | FAILED | UNCERTAIN
  confidence: float

authority:
  current_owner: string
  requested_authority: string
```

---

# Escalation Targets

Escalation may route toward:

- orchestrators
- human sponsors
- critique authorities
- auditors
- restoration authorities
- governance authorities

The escalation target must possess sufficient authority for the unresolved condition.

---

# Escalation Constraints

Escalation may not:

- conceal uncertainty
- suppress contradictory evidence
- erase prior state history
- remove failed verification
- silently downgrade consequence tier

Escalation preserves operational truth.

---

# Escalation Outcomes

Possible escalation outcomes include:

- clarification
- restoration
- reassignment
- verification expansion
- authority override
- operational freeze
- decommission
- dead-letter disposition

---

# Escalation and Trust

An escalated operation is not automatically untrusted.

Escalation indicates:

- operational caution
- governance discipline
- unresolved uncertainty
- authority limitation awareness

Systems that never escalate are usually concealing instability.

---

# Constitutional Rule

Unresolved uncertainty must move upward, not disappear sideways.
