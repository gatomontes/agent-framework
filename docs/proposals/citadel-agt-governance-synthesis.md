# Proposal: Citadel Governance Synthesis with Microsoft Agent Governance Toolkit Patterns

## Status

Proposed.

This proposal is not adopted doctrine.

It records recommendations for strengthening Citadel governance after comparing Citadel's current constitutional governance architecture with Microsoft's Agent Governance Toolkit (AGT).

---

# Executive Summary

Citadel is strongest as a constitutional governance institution.

Microsoft Agent Governance Toolkit is strongest as an executable enforcement layer.

Citadel currently governs missions, institutional memory, boundary discipline, verification, critique, restoration, notarial return, final disposition, and authority semantics.

AGT governs runtime actions through deterministic policy enforcement, approval gates, identity, session state, audit logging, and structural denial before agent intent reaches external systems.

The recommended direction is not to replace Citadel with AGT-style machinery.

The recommended direction is to add a Citadel-owned executable policy projection layer that can emit, adapt, or inspire AGT-style runtime enforcement while preserving Citadel's constitutional identity.

In short:

```text
Citadel should define the law.
Runtime adapters should enforce the law.
AGT-style mechanisms show how enforcement should work.
```

---

# Core Finding

Citadel and AGT govern different units.

```text
Citadel governs missions.
AGT governs actions.
```

A mission may be classified, scoped, constrained, delegated, verified, critiqued, restored, escalated, notarized, archived, and given final disposition.

An action may be allowed, denied, approved, blocked, logged, sandboxed, rate-limited, or killed.

Citadel should not collapse itself into an action policy engine.

But Citadel needs a bridge that turns constitutional mission law into executable runtime policy.

---

# Current Citadel Strengths

## 1. Constitutional governance

Citadel already defines itself as a governance layer for orchestrating, validating, critiquing, governing, restoring, and evolving interoperable AI agent systems.

It separates:

- universal operational doctrine
- runtime-specific implementation
- orchestration behavior
- critique systems
- verification systems
- governance semantics
- restoration and escalation protocols
- operational flow topology
- delegation contracts
- validation methodology
- authority boundaries
- runtime admission rules
- memory and artifact discipline

This is broader than AGT's primary enforcement posture.

Citadel is not just deciding whether a tool call may execute.

Citadel is deciding whether governed work may become trusted institutional output.

## 2. Rook boundary discipline

Rook is one of Citadel's strongest governance surfaces.

Its core principle is correct:

```text
Input is not yet a mission.
Output is not yet trust.
```

Rook preserves raw inbound request shape, ambiguity, authority clues, consequence clues, constraints, referenced artifacts, and continuity references.

This prevents the institution from laundering ambiguity into false certainty at the boundary.

## 3. Audit scroll movement lineage

The audit scroll is stronger than ordinary logging because it records scroll movement across stations, not merely final outcomes.

It preserves:

- where a scroll traveled
- who recorded the transition
- what transition occurred
- why the transition happened

The constitutional principle is valuable:

```text
If scroll movement cannot be reconstructed, boundary trust is degraded even when scroll contents appear complete.
```

## 4. Notarial return discipline

The Notarial Protocol gives Citadel a substantive return-memory layer.

It preserves station findings, evidence references, proposed actions, blocked actions, unresolved questions, required actions, human decisions, and archival references before Rook emits a return scroll.

This is a governance capability AGT does not foreground.

AGT can prove whether an action was allowed or denied.

Citadel can explain what the institution learned, what remains unresolved, and what must happen before safe continuation.

---

# Current Citadel Weaknesses

## 1. Doctrine is not yet executable enough

Citadel contains many correct obligations:

- must preserve
- must inspect
- must escalate
- must not invent
- must not suppress ambiguity
- must attach audit scroll
- must create archival copy
- must validate final disposition

But these are mostly constitutional obligations, not yet canonical executable policy rules.

Citadel needs a policy grammar that can express enforceable decisions such as:

```yaml
if: audit_scroll.entries is empty
action: BLOCK_RETURN
```

```yaml
if: verification.status != PASSED and consequence_tier in [HIGH, CRITICAL]
action: REQUIRE_RESTORATION
```

```yaml
if: action.type == external_send and session.data_sensitivity in [CONFIDENTIAL, RESTRICTED]
action: REQUIRE_APPROVAL
```

## 2. Missing canonical policy action vocabulary

Citadel has rich governance states, but it should define a canonical action vocabulary for runtime enforcement.

Recommended initial action vocabulary:

```text
ALLOW
DENY
BLOCK
REQUIRE_APPROVAL
REQUIRE_VERIFICATION
REQUIRE_CRITIQUE
REQUIRE_NOTARIAL_RECORD
REQUIRE_ARCHIVAL_COPY
REQUIRE_RESTORATION
REQUIRE_HUMAN_DECISION
DEAD_LETTER
RETURN_UNTRUSTED
RETURN_UNCERTAIN
```

## 3. Human approval gates need operational contracts

Citadel already has escalation and human decision concepts.

It should add explicit approval contracts with:

- approver identity or role
- approval scope
- timeout behavior
- fail-safe behavior
- approval reason
- denial reason
- audit binding
- notarial preservation

The default rule should be:

```text
If approval is required and cannot be obtained, the operation fails closed.
```

## 4. Session state and monotonic ratchets are not yet explicit enough

AGT's attribute-ratchet pattern is highly relevant.

Citadel should define session or mission attributes that can only increase in risk during a governed run.

Examples:

```text
consequence_tier: LOW -> MODERATE -> HIGH -> CRITICAL
sensitivity_tier: PUBLIC -> INTERNAL -> CONFIDENTIAL -> RESTRICTED
authority_tier: NONE -> DECLARED -> VERIFIED -> ELEVATED
trust_tier: UNTRUSTED -> UNCERTAIN -> CONDITIONALLY_TRUSTED -> TRUSTED
```

Some of these may be monotonic upward only.

For example, once a mission touches restricted information, it should not be allowed to downgrade itself to public in the same session without explicit restoration, review, or new boundary packaging.

## 5. Identity and authority binding need runtime representation

Citadel speaks correctly about authority boundaries.

But runtime enforcement requires identity-bound action decisions.

Citadel should define how these identities appear in policy contexts:

- requesting human
- originating system
- Rook instance
- orchestrator
- delegated agent
- runtime adapter
- tool executor
- verifier
- critic
- notary
- approver

This should support future integration with DID, SPIFFE, mTLS, signed artifacts, or simpler local identity handles.

---

# Proposed New Citadel Layer

Add a new core policy layer:

```text
/core/policy/
  citadel-policy-spec.md
  policy-action-vocabulary.md
  policy-context-schema.md
  consequence-tier-policy.md
  authority-policy.md
  verification-gate-policy.md
  return-readiness-policy.md
  session-ratchet-policy.md
  approval-gate-policy.md
  runtime-policy-projection.md
```

This layer should not replace existing doctrine.

It should translate doctrine into enforceable decision structures.

---

# Proposed Architecture

```text
Human or System Intent
  -> Rook Intake
    -> Citadel Classification
      -> Mission Governance Contract
        -> Citadel Policy Projection
          -> Runtime Adapter
            -> AGT-style Enforcement
              -> Execution
                -> Verification
                  -> Critique
                    -> Audit
                      -> Coherence
                        -> Restoration or Escalation
                          -> Final Disposition
                            -> Notary
                              -> Rook Return
```

The key addition is:

```text
Mission Governance Contract -> Citadel Policy Projection -> Runtime Adapter
```

This lets Citadel preserve institutional doctrine while still producing enforceable runtime constraints.

---

# Citadel Policy Context Schema

Every enforceable decision should receive a policy context.

Initial proposed shape:

```yaml
citadel_policy_context:
  context_id: null
  mission_id: null
  scroll_id: null
  audit_scroll_id: null
  created_at: null

  actor:
    actor_id: null
    actor_type: human | agent | adapter | tool | system | station
    role: null
    authority_tier: null
    identity_verified: false

  action:
    type: null
    target: null
    tool_name: null
    external_effect: false
    irreversible: false
    data_access: []

  mission:
    objective: null
    consequence_tier: null
    sensitivity_tier: null
    declared_scope: null
    current_phase: null

  session:
    consequence_tier: null
    sensitivity_tier: null
    trust_tier: null
    touched_sensitive_data: false
    externalized_data: false

  evidence:
    verification_status: null
    critique_status: null
    audit_status: null
    notarial_status: null
    archival_status: null
    evidence_refs: []

  boundary:
    ingress_rook: null
    egress_rook: null
    return_capable: false
    external_return_requested: false

  continuity:
    prior_scrolls: []
    restoration_reference: null
    unresolved_questions: []
```

---

# Citadel Policy Rule Shape

Citadel rules should be serializable into YAML or another adapter-friendly format.

Initial proposed shape:

```yaml
citadel_policy_rule:
  id: null
  name: null
  version: 1
  scope: mission | action | return | restoration | approval | archive
  stage: intake | classification | pre_execution | post_execution | verification | critique | final_disposition | pre_return
  priority: 100
  condition: null
  action: null
  required_roles: []
  required_artifacts: []
  fail_behavior: fail_closed
  reason: null
```

Example:

```yaml
id: return-requires-notarial-record
name: Return requires notarial record
scope: return
stage: pre_return
priority: 1000
condition: "boundary.external_return_requested == true and evidence.notarial_status != 'complete'"
action: BLOCK
required_artifacts:
  - notarial_record
fail_behavior: fail_closed
reason: "No governed return scroll should leave Citadel without preserved notarial substance."
```

---

# Recommended Policy Families

## 1. Consequence Tier Policy

Purpose:

Govern escalation, verification depth, approval burden, and final disposition requirements according to mission consequence.

Example:

```yaml
id: high-consequence-requires-verification
stage: final_disposition
condition: "mission.consequence_tier in ['HIGH', 'CRITICAL'] and evidence.verification_status != 'PASSED'"
action: REQUIRE_RESTORATION
reason: "High-consequence work cannot receive trusted disposition without passed verification."
```

## 2. Authority Policy

Purpose:

Prevent agents or adapters from self-authorizing scope expansion, irreversible actions, external sends, or privileged tool calls.

Example:

```yaml
id: irreversible-action-requires-human-authority
stage: pre_execution
condition: "action.irreversible == true and actor.authority_tier != 'HUMAN_APPROVED'"
action: REQUIRE_APPROVAL
reason: "Irreversible actions require explicit human authority."
```

## 3. Verification Gate Policy

Purpose:

Make verification requirements executable rather than advisory.

Example:

```yaml
id: failed-verification-blocks-trust
stage: final_disposition
condition: "evidence.verification_status == 'FAILED'"
action: RETURN_UNTRUSTED
reason: "Failed verification blocks trusted final disposition."
```

## 4. Critique Gate Policy

Purpose:

Ensure critique is required for certain classes of generated plans, external recommendations, or high-risk outputs.

Example:

```yaml
id: strategic-plan-requires-critique
stage: pre_return
condition: "action.type == 'external_return' and mission.current_phase == 'strategic_plan' and evidence.critique_status != 'PASSED'"
action: REQUIRE_CRITIQUE
reason: "Strategic plans require critique before external return."
```

## 5. Return Readiness Policy

Purpose:

Prevent premature Rook return.

Example:

```yaml
id: return-requires-audit-lineage
stage: pre_return
condition: "boundary.external_return_requested == true and audit_scroll.entries.length == 0"
action: BLOCK
reason: "Return scroll lacks movement lineage."
```

## 6. Notarial Policy

Purpose:

Require station findings, proposed actions, blocked actions, unresolved questions, and archival references before return.

Example:

```yaml
id: notarial-archive-required
stage: pre_return
condition: "evidence.notarial_status == 'complete' and evidence.archival_status != 'copied'"
action: REQUIRE_ARCHIVAL_COPY
reason: "Notarial return summary must be archived before external return."
```

## 7. Session Ratchet Policy

Purpose:

Prevent risk downgrades inside the same mission/session.

Example:

```yaml
session_attributes:
  sensitivity_tier:
    ordering: [PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED]
    monotonic: true
    initial: PUBLIC

rules:
  - id: restricted-data-blocks-external-send
    stage: pre_execution
    condition: "action.type == 'external_send' and session.sensitivity_tier == 'RESTRICTED'"
    action: REQUIRE_APPROVAL
    reason: "External send after restricted data access requires approval."
```

## 8. Approval Gate Policy

Purpose:

Make human-in-the-loop governance explicit and fail-safe.

Example:

```yaml
id: external-write-requires-owner-approval
stage: pre_execution
condition: "action.external_effect == true and action.type in ['send_email', 'push_commit', 'delete_file', 'charge_payment']"
action: REQUIRE_APPROVAL
required_roles:
  - owner
fail_behavior: fail_closed
reason: "External side effects require explicit approval."
```

---

# Runtime Projection

Citadel policy does not need to be identical to AGT policy.

Instead, Citadel should define a projection layer.

```text
Citadel Policy Rule
  -> Runtime Policy Projection
    -> Adapter-Specific Enforcement
```

Possible projection targets:

- AGT YAML policy
- OPA/Rego
- Cedar
- local Python policy evaluator
- TypeScript middleware
- Symfony middleware
- GitHub workflow guard
- MCP gateway policy
- shell command allowlist/denylist

This keeps Citadel runtime-portable.

---

# Proposed Adapter Contract

Add a runtime adapter contract:

```yaml
runtime_policy_projection:
  projection_id: null
  source_policy_ids: []
  target_runtime: null
  target_format: null
  generated_at: null
  generated_by: null

  guarantees:
    deterministic_enforcement: false
    fail_closed: false
    audit_emitted: false
    approval_supported: false
    session_ratchets_supported: false

  unsupported_semantics:
    - policy_id: null
      unsupported_feature: null
      consequence: null
      mitigation: null
```

Key rule:

```text
If a runtime adapter cannot enforce a Citadel policy faithfully, the unsupported semantic must be explicit.
```

No silent downgrade.

---

# Implementation Plan

## Phase 1: Policy specification

Create:

```text
/core/policy/citadel-policy-spec.md
/core/policy/policy-action-vocabulary.md
/core/policy/policy-context-schema.md
```

Goal:

Define Citadel's own policy language without binding it to a specific runtime.

## Phase 2: Gate policies

Create:

```text
/core/policy/verification-gate-policy.md
/core/policy/return-readiness-policy.md
/core/policy/approval-gate-policy.md
```

Goal:

Make existing Citadel doctrine enforceable at the critical gates.

## Phase 3: Ratchets and identity

Create:

```text
/core/policy/session-ratchet-policy.md
/core/policy/authority-policy.md
```

Goal:

Prevent risk downgrades and bind actions to explicit authority.

## Phase 4: Runtime projection

Create:

```text
/core/runtime/runtime-policy-projection-contract.md
/core/runtime/adapter-enforcement-requirements.md
```

Goal:

Define how Citadel law is projected into AGT-style enforcement or other runtime mechanisms.

## Phase 5: Reference examples

Create:

```text
/examples/policies/high-consequence-return.yaml
/examples/policies/external-side-effect-approval.yaml
/examples/policies/sensitive-data-ratchet.yaml
/examples/policies/notarial-return-readiness.yaml
```

Goal:

Give implementers concrete examples.

---

# Adoption Criteria

This proposal should not become adopted doctrine until Citadel has:

1. A canonical policy context schema.
2. A canonical policy action vocabulary.
3. At least three policy gates expressed in the new grammar.
4. At least one runtime projection contract.
5. A failure rule for unsupported policy semantics.
6. A return-readiness policy that binds Rook, Audit Scroll, Notary, and Archives.
7. A human approval policy with fail-closed behavior.
8. A session ratchet policy for sensitivity or consequence.

---

# Design Principles

## 1. Do not shrink Citadel into a tool-call firewall

Tool-call governance is necessary but insufficient.

Citadel governs institutional trust, not just calls.

## 2. Do not rely on prompt obedience for governance

Any policy that must be enforced should be enforceable outside the model's voluntary compliance.

Prompt instructions are doctrine.

Runtime gates are law enforcement.

## 3. Preserve unsupported semantics

If an adapter cannot enforce a Citadel rule, it must say so.

Silent policy loss is doctrinal erosion.

## 4. Fail closed for authority, approval, and return readiness

When in doubt, block external side effects and external returns until governance requirements are satisfied.

## 5. Keep Rook clean

Rook should not become the whole workflow.

Rook normalizes ingress and egress.

Policy gates should operate inside the governed flow and before final return.

## 6. Keep Notary substantive

Notary should not become a decorative summary.

It should preserve material station findings, contradictions, blocked actions, unresolved questions, and archival references.

---

# Recommended Constitutional Addition

Add this principle to Citadel doctrine after policy adoption:

```text
A governance rule that cannot be projected, enforced, or explicitly marked unsupported is not runtime law.

It remains doctrine until a governed enforcement surface exists.
```

This preserves the distinction between constitutional doctrine and executable governance.

---

# Final Recommendation

Citadel should absorb AGT's best operational patterns:

- deterministic pre-action enforcement
- executable policy grammar
- allow / deny / require approval decisions
- fail-closed approval behavior
- audit-bound decision records
- session-state ratchets
- identity-bound actions
- runtime projection contracts
- unsupported-semantics disclosure

But Citadel should keep its own institutional frame:

- Rook boundary discipline
- mission classification
- authority semantics
- verification doctrine
- critique doctrine
- restoration semantics
- audit scroll movement lineage
- notarial return substance
- archival continuity
- final disposition

The target is not AGT inside Citadel.

The target is Citadel doctrine made enforceable through AGT-grade runtime law.

```text
Citadel defines what must be true.
Runtime governance enforces what must not be violated.
Notary preserves what the institution learned.
Rook controls what may enter and leave.
```
