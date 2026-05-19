# Verification Contract

**Status:** Adopted  
**Classification:** Core Contract  
**Effective:** Immediately

---

# Principle

Silence is not success.

A task that completes without explicit verification produces an unvalidated artifact, not a confirmed result.

`No errors reported` is not equivalent to `correctly executed`.

---

# Requirement

Every execution contract must be paired with a verification contract unless explicitly exempted.

Exemptions require written justification.

---

# Contract Schema

```yaml
verification_contract:
  name: string
  applies_to: contract_id

  method:
    channel: "independent" | "parallel" | "retrieval" | "human"
    reasoning_path: "different_from_execution" | "same"
    ground_truth_source: optional

  criteria:
    - condition: string
      threshold: float
      failure_handling: "flag" | "escalate" | "retry" | "halt"

  uncertainty_reporting:
    confidence_required: float
    expose_confidence: boolean
    uncertainty_format: "explicit_reasons" | "confidence_interval" | "both"

  independence_requirements:
    no_shared_state_with_execution: boolean
    no_shared_model_call: boolean
    minimum_agent_distance: "different_persona" | "different_runtime" | "same_runtime_different_session"
```

---

# Verification Statuses

Verification status must be tracked separately from execution status.

```txt
VERIFIED
VERIFIED_WITH_CAVEATS
UNVERIFIED
UNVERIFIABLE
FAILED_VERIFICATION
```

Example:

```yaml
execution_status: SUCCESS
verification_status: FAILED_VERIFICATION
```

A successful execution can still fail verification.

---

# Failure Taxonomy

| Failure Mode | Detection Method | Report Signal |
|---|---|---|
| Hallucination | Retrieval-backed verification | `FAILURE: GROUNDING` |
| Divergence | Schema and behavior validation | `FAILURE: CONTRACT_DEVIATION` |
| Improvisation | Boundary audit | `FAILURE: BOUNDARY_VIOLATION` |
| Silence | Absence of verification artifact | `FAILURE: UNVERIFIED` |

---

# Detection Rule

If execution reports `SUCCESS` but verification cannot be completed, is not invoked, or returns confidence below threshold, report:

```txt
FAILURE: UNVERIFIED
```

Execution appearance is irrelevant.

---

# Runtime Wrapper Requirements

All runtime wrappers must implement:

| Requirement | Description |
|---|---|
| Verification hook | Ability to invoke a second agent, channel, or method for cross-checking |
| Uncertainty passthrough | Confidence and uncertainty must survive into final reporting |
| Silence alert | Execution without verification returns `STATUS: INCOMPLETE` or equivalent |
| Divergence log | Boundary or contract deviations must be written to a persistent log |

Wrappers missing any requirement are marked:

```txt
COMPLIANCE: PARTIAL
```

They are prohibited from critical operations unless explicitly exempted.

---

# Immediate Behavioral Rules

1. Always ask: `How would I verify this independently?`
2. Never accept `no errors` as success.
3. Require an explicit verification artifact for success claims.
4. Log silence when verification is skipped.
5. For consequential decisions, use separate verification channels.
6. Expose uncertainty with confidence and justification.

---

# Relationship to Other Contracts

This contract depends on and informs:

- status contracts
- reporting contracts
- critique contracts
- escalation contracts
- runtime wrapper contracts

Verification is not optional decoration.

Verification is part of success semantics.
