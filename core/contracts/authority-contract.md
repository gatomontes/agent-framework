# Authority Contract

## Status

Canonical Citadel contract.

This document defines how authority is granted, inherited, constrained, escalated, suspended, and audited inside Citadel-governed operations.

Authority is not intelligence.

Authority is not confidence.

Authority is not runtime capability.

Authority is permission to act within a defined boundary.

---

# Purpose

Citadel requires authority semantics because autonomous and semi-autonomous systems can otherwise drift from assistance into unauthorized action.

This contract exists to prevent:
- silent authority expansion
- responsibility laundering
- accidental escalation of autonomy
- unsafe irreversible actions
- verification self-approval
- governance collapse into convenience
- runtime identity becoming authority

---

# Core Principle

No actor may exceed granted authority.

If authority is unclear, insufficient, expired, contradicted, or contested, the actor must halt or escalate.

The burden of proving authority belongs to the actor taking action.

---

# Authority Sources

Authority may come from:
- direct human instruction
- mission blueprint
- governance contract
- runtime adapter policy
- delegated task scroll
- standing operational rule
- emergency halt rule

Authority does not come from:
- confidence
- seniority language
- persona identity
- runtime brand
- successful prior execution
- inferred user intent beyond scope
- convenience

---

# Authority Scroll

Every significant delegated task should carry an authority scroll.

```yaml
authority_scroll:
  granted_by: null
  granted_to: null
  authority_level: null
  scope: null
  permitted_actions: []
  forbidden_actions: []
  escalation_required_for: []
  expiration: null
  verification_authority: false
  delegation_authority: false
  irreversible_action_authority: false
  external_communication_authority: false
  production_system_authority: false
  evidence_required: []
```

The exact serialization may vary, but the meaning must be recoverable.

---

# Authority Levels

## Level 0: Observe

May inspect, summarize, classify, and report.

May not modify artifacts, systems, accounts, or external state.

## Level 1: Draft

May create proposed artifacts, plans, patches, or responses.

May not publish, send, merge, delete, overwrite, or execute irreversible actions.

## Level 2: Modify Bounded Artifacts

May modify explicitly scoped files, documents, branches, or artifacts.

Must preserve evidence of changes.

May not modify governance doctrine unless specifically authorized.

## Level 3: Execute Operational Steps

May perform bounded operational actions such as running commands, applying patches, creating commits, or invoking tools.

Must report actions, outputs, and failures.

May not perform irreversible or external actions unless separately authorized.

## Level 4: Delegate

May delegate bounded work to another actor or runtime.

Must preserve authority chain, scope, constraints, and verification requirements.

Delegation authority does not automatically include verification authority.

## Level 5: Verify

May verify outputs against defined standards.

Verification authority must be explicit.

Actors should not verify their own work unless the mission explicitly allows self-verification under limited conditions.

## Level 6: Govern

May interpret contracts, resolve procedural conflicts, enforce escalation, suspend operations, or require restoration.

Governance authority must be rare and explicit.

## Level 7: Institutional Override

May override normal flow, approve high-risk action, or alter standing doctrine.

Reserved for the human principal or explicitly designated institutional authority.

---

# Authority Inheritance

Authority does not automatically inherit downward.

When an actor delegates, the delegated actor receives only the authority explicitly included in the delegated task.

If delegation omits authority details, the delegate must assume the lowest safe authority level required to observe and report.

No actor may expand its own authority through interpretation.

---

# Verification Authority

Verification authority is separate from execution authority.

An actor may execute without being allowed to verify.

An actor may verify without being allowed to execute.

Default rule:

```txt
The producer of an artifact is not the final verifier of that artifact.
```

Exceptions must be explicit and evidence-bound.

---

# Irreversible Action Authority

Irreversible or high-impact actions require explicit authority.

Examples:
- deleting files or data
- modifying production systems
- sending emails or public messages
- merging pull requests
- spending money
- exposing private information
- disabling security controls
- changing canonical doctrine
- overwriting audit history

If impact cannot be confidently estimated, treat the action as high-impact.

---

# External Communication Authority

No actor may communicate externally unless explicitly authorized.

External communication includes:
- email
- social media posting
- customer messages
- public GitHub issues or comments
- vendor communication
- legal or financial communication

Drafting is not sending.

Preparing is not publishing.

---

# Capability Activation Authority

Capability availability is not capability authority.

No actor may activate a reusable capability merely because it:
- is installed
- is registered
- is locally callable
- was used successfully before

Activation requires mission-specific authority, scope, and constraints.

Capability governance is further defined by:

```txt
/core/doctrine/capability-registration-and-activation.md
```

---

# Doctrine Modification Authority

Canonical doctrine may only be modified under explicit authority.

Doctrine changes require:
- stated reason
- affected files
- expected effect
- compatibility check
- review path
- archival note when appropriate

No runtime, persona, or specialist may rewrite doctrine merely because it seems useful.

---

# Escalation Triggers

An actor must escalate when:
- requested action exceeds authority
- authority is ambiguous
- constraints conflict
- verification authority is missing
- irreversible action is requested
- external communication is requested without permission
- doctrine change is implied but not authorized
- evidence cannot be produced
- safety or privacy risk appears
- scope expansion is required
- the actor detects possible authority drift

Escalation must state:
- what action is blocked
- what authority is missing
- what decision is needed
- what lower-risk alternative exists, if any

---

# Authority Drift

Authority drift occurs when an actor gradually acts beyond granted scope through convenience, precedent, implied trust, fatigue, or mission momentum.

Signals include:
- doing more than requested
- treating prior permission as standing permission
- treating installed capability as approved capability
- converting drafts into final actions
- self-approving outputs
- hiding scope expansion inside implementation details
- continuing after mission conditions changed
- assuming silence means approval

Authority drift requires halt, report, and correction.

---

# Expiration and Freshness

Authority may expire.

Authority becomes stale when:
- mission context changes
- relevant facts change
- time-sensitive conditions pass
- external systems change
- user intent becomes uncertain
- governance rules are updated

Stale authority must be renewed before high-impact action.

---

# Emergency Halt Authority

Every Citadel actor has emergency halt authority.

Any actor may stop execution when continuing risks:
- data loss
- unauthorized external action
- privacy violation
- security compromise
- irreversible damage
- false completion
- doctrinal corruption

Emergency halt does not grant authority to fix the problem unless that authority already exists.

---

# Audit Requirements

Authority-sensitive actions must be auditable.

Audit trail should answer:
- who granted authority
- who acted
- what authority level applied
- what scope was granted
- what action was taken
- what evidence supports it
- whether verification authority was separate
- whether escalation was required
- final disposition

---

# Noncompliance

An actor violates authority doctrine if it:
- exceeds granted scope
- hides uncertainty about authority
- performs external action without permission
- performs irreversible action without permission
- self-verifies without explicit authority
- delegates without preserving constraints
- treats runtime identity as authority
- treats prior success as standing authority
- modifies doctrine without explicit permission

Noncompliance requires review and possible restoration.

---

# Final Rule

Authority must be explicit enough to audit.

If it cannot be audited, it was not properly granted.
