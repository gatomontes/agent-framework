# Citadel Authority Model

## Purpose

The Authority Model defines who may decide, delegate, halt, restore, verify, and finalize work inside a Citadel-governed operation.

Authority exists to prevent role drift, recursive ambiguity, silent escalation bypass, and uncontrolled agent behavior.

---

# Core Principle

No actor owns more authority than its assigned role, declared capability, and active contract permit.

Authority must be explicit.

Assumed authority is invalid.

---

# Authority Classes

## Human Authority

The human sponsor defines intent, accepts strategic tradeoffs, and may override final direction when the consequence tier permits it.

Human override does not erase failed verification.

If a human chooses to proceed despite failed or uncertain verification, the final disposition must record the override.

## Orchestration Authority

The orchestrator may classify tasks, select workers, issue execution contracts, request verification, and route escalation.

The orchestrator may not mark its own output as trusted without verification.

## Execution Authority

A worker may perform the assigned task and produce the requested artifact.

A worker may not expand mission scope, declare final trust, bypass verification, or suppress uncertainty.

## Verification Authority

A verifier may inspect evidence, test outputs, check claims, and determine whether the artifact satisfies the verification contract.

A verifier may not silently rewrite the objective.

## Critique Authority

A critique authority, such as Blackquill, may pressure-test structure, assumptions, coherence, and strategic quality.

Critique does not replace verification.

## Audit Authority

An auditor verifies the verification and critique chain.

Audit authority exists to detect performative review, evidence gaps, and confidence inflation.

## Restoration Authority

A restoration authority may freeze, recover, validate, resume, decommission, or dead-letter an operation when coherence fails.

Restoration must be recorded as an operational event.

---

# Delegation Rules

1. Delegation must include an execution contract.
2. Delegation must identify the expected artifact.
3. Delegation must define failure conditions.
4. Delegation must preserve the consequence tier.
5. Delegated work must report status using the Citadel status schema.
6. Subdelegation is prohibited unless explicitly granted.
7. A delegate may request clarification but may not invent authority.

---

# Halt Authority

Any verifier, critic, auditor, orchestrator, or human sponsor may halt an operation when one of the following occurs:

- evidence is insufficient for the consequence tier
- verification was skipped
- scope changed without authorization
- authority was exceeded
- a critical contradiction appears
- restoration is required
- the operation enters recursive ambiguity

A halt is not a failure.

A halt is a containment action.

---

# Override Rules

Overrides must record:

- who overrode
- what was overridden
- why the override was permitted
- what risk remains
- whether final disposition is still trusted, uncertain, or human-accepted despite risk

An override may continue work.

An override may not falsify trust.

---

# Final Disposition Authority

Final disposition is assigned only after execution, verification, critique, audit when required, and coherence checks are complete.

Allowed final dispositions:

- TRUSTED
- UNTRUSTED
- UNCERTAIN
- BLOCKED
- DEAD_LETTER

Execution success alone is not final disposition.

---

# Constitutional Rule

Authority is not personality.

Authority is contract-bound operational permission.
