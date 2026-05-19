# Unified Operational Status Schema

**Status:** Adopted  
**Classification:** Core Contract  
**Effective:** Immediately

---

# Purpose

Define a single operational status schema that binds execution, verification, critique, audit, coherence, restoration, escalation, and final disposition into one inspectable state object.

A task is not complete merely because execution finished.

A task is complete only when final disposition is resolved.

---

# Schema

```yaml
operational_status:
  execution:
    state: "PENDING" | "IN_PROGRESS" | "SUCCESS" | "FAILED"
    artifact: optional reference

  verification:
    state: "NOT_REQUIRED" | "PENDING" | "IN_PROGRESS" | "VERIFIED" | "FAILED"
    confidence: float
    method: "full_independent" | "retrieval_backed" | "sampled" | "none"

  critique:
    blackquill_verdict: "PASS" | "FAIL" | "UNCERTAIN"
    blackquill_notes: string
    auditor_verdict: "PASS" | "FAIL" | "UNCERTAIN"
    auditor_notes: string
    consensus: "AGREED" | "DISAGREED"

  coherence:
    status: "COHERENT" | "DRIFT_DETECTED" | "RESTORING" | "DECOMMISSIONED"
    restoration_state: optional

  final_disposition:
    value: "TRUSTED" | "UNTRUSTED" | "UNCERTAIN" | "BLOCKED" | "DEAD_LETTER"
    human_override: boolean
    override_authority: optional
```

---

# Status Semantics

## Execution

Execution describes whether the assigned work was attempted and whether an artifact was produced.

Execution success does not imply trust.

---

## Verification

Verification describes whether the execution artifact was checked against the applicable verification contract.

If verification is missing when required, the operation cannot become `TRUSTED`.

---

## Critique

Critique records Blackquill and Auditor verdicts.

Consensus is required for critical operations.

Disagreement triggers escalation.

---

## Coherence

Coherence records whether the operation preserved active doctrine and governance constraints.

A successful execution with drift detected is not trusted.

---

## Final Disposition

Final disposition is determined by all previous dimensions.

Allowed final dispositions:

```txt
TRUSTED
UNTRUSTED
UNCERTAIN
BLOCKED
DEAD_LETTER
```

`TRUSTED` requires:
- execution success
- required verification pass
- critique/audit pass or accepted caveat
- coherence intact
- no unresolved escalation

`UNTRUSTED` indicates a failed gate.

`UNCERTAIN` indicates insufficient confidence or unresolved evidence.

`BLOCKED` indicates the operation cannot proceed under current constraints.

`DEAD_LETTER` indicates escalation or restoration could not resolve the operation.

---

# Governance Rule

The status object is the operational truth source.

No agent, wrapper, or runtime may summarize an operation as complete without preserving or reporting final disposition.
