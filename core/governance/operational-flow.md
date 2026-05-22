# Operational Flow

**Status:** Adopted  
**Classification:** Core Governance / Operational Topology  
**Effective:** Immediately

---

# Principle

The framework is not a collection of isolated contracts.

It is a continuous operational chain from:

```txt
Task -> Trust
```

Every operation must traverse the complete operational flow before final disposition can be assigned.

---

# Phase 0: Intake & Triage

Incoming tasks should first pass through:

```txt
/core/contracts/rook-contract.md
```

`Rook` receives inbound intent and emits an intake packet before classification begins.

Incoming tasks are classified using:

```txt
/core/doctrine/tiered-verification.md
```

The system assigns:
- consequence tier
- confidence requirement
- verification depth
- escalation sensitivity

A contract is born.

---

# Phase 1: Execution & Verification

Execution and verification occur in parallel.

## Execution Agent

Performs the assigned task.

## Verification Agent

Independently checks the execution artifact.

Verification must:
- follow verification contracts
- preserve independence requirements
- produce verification artifacts

Execution is not considered successful until verification resolves.

Possible outcomes:

```txt
SUCCESS + VERIFIED
SUCCESS + FAILED_VERIFICATION
EXECUTION_FAILED
```

Silence is treated as:

```txt
FAILURE: UNVERIFIED
```

---

# Phase 2: Critique & Audit Gate

Blackquill receives:

```txt
(Execution, Verification)
```

Blackquill:
- pressure-tests evidence
- exposes contradictions
- identifies uncertainty
- detects doctrinal drift

Auditor verifies:
- verification discipline
- evidence chains
- Blackquill methodology
- critique integrity

If Blackquill and Auditor disagree:

```txt
ESCALATE
```

---

# Phase 3: Governance & Coherence Check

Before finalization:

```txt
/core/doctrine/doctrinal-coherence.md
```

is consulted.

Question:

```txt
Did this operation preserve active doctrine?
```

If coherence failure is detected:

```txt
FREEZE
```

Finalization is aborted.

The operation becomes a recovery artifact.

---

# Phase 4: Restoration or Escalation

If coherence failure exists:

```txt
/core/governance/restoration-protocol.md
```

is invoked.

Possible outcomes:
- restoration
- escalation
- dead-letter
- decommission

If unresolved:

```txt
/core/contracts/escalation-contract.md
```

controls authority routing.

---

# Phase 5: Final Disposition

Final disposition is assigned through:

```txt
/core/contracts/status-schema.md
```

Possible dispositions:

```txt
TRUSTED
UNTRUSTED
UNCERTAIN
BLOCKED
DEAD_LETTER
```

Critical operations marked `UNTRUSTED` require explicit human override.

---

# Operational Invariant

No agent, wrapper, runtime, or orchestration layer may consider an operation complete until it traverses the full operational flow.

---

# Silence Rule

Silence at any stage is:

```txt
FAILURE: UNVERIFIED
```

and may trigger:

```txt
FREEZE
```

---

# Strategic Direction

The framework is evolving toward:

```txt
resilient epistemic operating systems
```

The operational flow exists to preserve trustworthiness under:
- fatigue
- drift
- uncertainty
- governance pressure
- operational entropy
