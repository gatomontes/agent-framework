# Coherence Restoration Protocol

**Status:** Adopted  
**Classification:** Core Governance / Operational Recovery  
**Effective:** Immediately

---

# Principle

Detection without restoration is diagnosis without treatment.

Doctrinal coherence can be lost.
Doctrinal coherence must also be recoverable.

Restoration is not punishment.

Restoration is operational reset.

---

# Restoration States

```yaml
restoration_states:
  - MONITORING
  - INVESTIGATING
  - FREEZE
  - RECOVERING
  - VALIDATING
  - RESUME
  - DECOMMISSION
```

---

# Restoration Workflow

## INVESTIGATING

Auditor reconstructs evidence chains.
Blackquill identifies contradictions.

When current state is unclear, investigation should prefer evidence-first reconstruction of the actionable thread before operational resumption.

See:

```txt
/core/protocols/continuity-reconstruction.md
```

Outputs:
- investigation report
- estimated failure origin
- affected scope
- root cause hypothesis

---

## FREEZE

Operations pause.

No new operations begin until restoration progresses.

In-flight operations:
- complete safely
- rollback
- dead-letter

Critical operations cannot proceed under unresolved coherence failure.

---

## RECOVERING

Blackquill and Auditor jointly:
- identify violated doctrine or contract
- determine patch, rollback, override, or exemption review
- apply fixes with verification
- preserve restoration evidence

---

## VALIDATING

Auditor independently validates restoration.

Blackquill reviews validation.

Disagreement triggers escalation.

No single persona may both recover and validate critical operations.

---

## RESUME

Operations resume under enhanced monitoring.

Any repeated failure during monitoring returns system to FREEZE.

---

## DECOMMISSION

If coherence cannot be restored:
- preserve all evidence
- produce final report
- terminate affected runtime or subsystem
- require explicit human intervention before restart

Decommission is preservation of trust boundaries.

---

# Artifact Requirements

```txt
/restoration/
  {timestamp}_investigation_report.md
  {timestamp}_freeze_declaration.md
  {timestamp}_recovery_log.md
  {timestamp}_validation_certificate.md
  {timestamp}_resume_declaration.md
  {timestamp}_decommission_certificate.md
```

Artifacts are immutable.
Artifacts are evidence.
Missing artifacts indicate failed restoration.

---

# Governance Rule

When coherence fails:

```txt
STOP
INVESTIGATE
RESTORE
VALIDATE
RESUME
```

A system that continues operating during unresolved coherence failure is uncontrolled.

---

# Strategic Purpose

The framework is designed for sustained operational endurance.

Everyone in war is tired.
Fatigue is the default state.

Therefore:
- verification shortcuts will emerge
- escalation bypasses will be tempting
- convenience will pressure doctrine
- silent drift will accumulate

The restoration protocol exists to preserve trustworthiness under prolonged operational entropy.
