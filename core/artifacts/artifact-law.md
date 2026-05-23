# Citadel Artifact Law

## Purpose

Artifact Law defines the creation, classification, preservation, mutation, supersession, trust status, and operational role of artifacts inside The Citadel.

Artifacts are the durable operational memory of the institution.

---

# Core Principle

Conversation is transient.

Artifacts persist.

Institutional continuity depends on artifacts, not chat history.

---

# Artifact Definition

An artifact is any durable operational object created, modified, reviewed, verified, or preserved as part of Citadel-governed work.

Examples include:

- briefs
- findings
- contracts
- capability registrations
- critiques
- verification reports
- operational logs
- mission plans
- code patches
- architectural decisions
- restoration reports
- escalation records
- runtime reports
- staffing plans

---

# Artifact Classes

## Operational Artifact

Directly participates in active work.

Examples:
- execution contracts
- deployment plans
- implementation tasks

## Governance Artifact

Defines doctrine, policy, law, authority, or operational constraints.

Examples:
- authority model
- verification doctrine
- escalation protocol

## Evidence Artifact

Supports verification or audit.

Examples:
- test results
- citations
- runtime logs
- verification outputs

## Review Artifact

Evaluates another artifact.

Examples:
- Blackquill critique
- Auditor review
- architectural review

## Historical Artifact

Retained for continuity, lineage, or reconstruction.

Historical retention does not imply current validity.

Historical artifacts entering long-term custody should obey:

```txt
/core/memory/archives-doctrine.md
```

## Capability Artifact

Reusable operational infrastructure retained for future selection or activation.

Examples:
- skills
- protocol implementations
- adapter wrappers
- automation templates

Capability artifacts may also exist as bundles containing:
- primary capability artifact
- supporting references
- helper scripts
- generated support artifacts
- bundled assets

Such bundles remain governed artifacts rather than disposable packaging noise.

---

# Artifact Lifecycle States

## DRAFT

Incomplete and not yet verified.

## ACTIVE

Currently operational.

## VERIFIED

Verification completed successfully.

## CRITIQUED

Review completed.

## TRUSTED

The artifact passed required operational gates.

## SUPERSEDED

A newer artifact replaced operational authority.

## ARCHIVED

Retained for continuity.

Archived artifacts remain preserved, not automatically authoritative.

## DEPRECATED

Retained but discouraged for operational use.

## DEAD_LETTER

The artifact cannot be trusted or restored.

---

# Mutability Rules

## Mutable Artifacts

May evolve during active operational work.

Examples:
- drafts
- active plans
- implementation checklists

## Immutable Artifacts

Must not be silently modified after verification or final disposition.

Examples:
- audit reports
- final findings
- signed operational decisions
- verification outputs

If correction is required:
- preserve the original artifact
- create a successor artifact
- record lineage explicitly

---

# Artifact Lineage

Every meaningful artifact should preserve:

- parent artifact
- originating task
- responsible authority
- verification status
- critique status
- consequence tier
- timestamps
- supersession chain

Operational history must remain reconstructable.

Capability artifacts should also preserve:

- registration status
- activation history when materially used
- provenance for imported or converted behavior

---

# Artifact Trust

Artifacts do not become trusted merely because they exist.

Trust requires:

- verification
- critique when required
- audit when required
- coherence preservation
- valid operational lineage

Possible trust states:

- TRUSTED
- UNTRUSTED
- UNCERTAIN
- SUPERSEDED

---

# Silent Mutation Prohibition

Silent mutation of trusted artifacts is constitutional failure.

Changes to trusted artifacts must:

- preserve history
- preserve lineage
- preserve previous trust state
- identify the modifying authority
- identify the reason for change

---

# Artifact Retention

Retention intensity should scale with consequence tier.

Critical operations require stronger preservation:

- audit trails
- restoration history
- verification evidence
- escalation records
- final disposition history

Long-term retention and archival custody should remain governed by:

```txt
/core/memory/archives-doctrine.md
```

---

# Registration And Activation Rule

Creating or registering a capability artifact does not automatically make it active for a mission.

Capability availability, registration, and activation are separate events governed by:

```txt
/core/doctrine/capability-registration-and-activation.md
```

Artifact law preserves the object.

Authority doctrine governs whether it may be used now.

Bundle structure for reusable capabilities is governed by:

```txt
/core/doctrine/capability-bundle-governance.md
```

---

# Constitutional Rule

Artifacts are the durable memory of institutional cognition.

Without artifact discipline, operational continuity collapses.
