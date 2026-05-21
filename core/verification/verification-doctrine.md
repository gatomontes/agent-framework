# Citadel Verification Doctrine

## Purpose

Verification Doctrine defines how The Citadel evaluates whether an operation, artifact, claim, or execution result deserves operational trust.

Verification exists to separate:

- execution
- confidence
- truth
- trust

---

# Core Principle

Execution is not trust.

Verification is the disciplined attempt to determine whether trust is justified.

---

# Verification Goals

Verification should determine:

- whether requirements were satisfied
- whether evidence supports the result
- whether reasoning remained coherent
- whether constraints were respected
- whether uncertainty was surfaced honestly
- whether operational law remained intact

Verification is not ceremonial approval.

---

# Verification Classes

## Structural Verification

Checks:

- schemas
- formatting
- completeness
- required fields
- operational contract compliance

## Behavioral Verification

Checks:

- runtime behavior
- workflow behavior
- operational state behavior
- escalation compliance

## Evidence Verification

Checks:

- citations
- logs
- proofs
- test results
- reproducibility

## Independent Verification

Uses:

- different reasoning paths
- different runtimes
- separate evaluators
- independent evidence reconstruction

Critical operations should favor independent verification.

## Human Verification

A human authority evaluates the result directly.

Human review may complement verification.

It does not erase unresolved uncertainty.

---

# Verification Requirements

Meaningful verification should preserve:

- verification method
- responsible authority
- evidence references
- confidence estimate
- unresolved uncertainty
- operational state
- consequence tier

Verification without evidence lineage is weak verification.

---

# Verification Failure

Verification failure occurs when:

- evidence is insufficient
- contradiction remains unresolved
- constraints were violated
- required artifacts are missing
- verification independence is inadequate
- uncertainty is concealed
- runtime behavior is inconsistent

Verification failure must emit explicit operational state.

---

# Verification and Consequence Tier

Higher consequence tiers require:

- stronger evidence
- greater independence
- lower uncertainty tolerance
- more durable audit trails
- stricter escalation sensitivity

Critical operations should never rely solely on self-verification.

---

# Verification Outcomes

Verification may conclude:

- VERIFIED
- FAILED
- UNCERTAIN
- BLOCKED

Verification does not assign final disposition.

Final disposition belongs to the complete operational flow.

---

# Constitutional Rule

Verification is not the manufacture of confidence.

Verification is the disciplined confrontation of uncertainty.
