# Rook Contract

## Status

Adopted for initial Citadel intake surface.

This document defines `Rook`, the Citadel I/O surface responsible for receiving inbound requests and emitting a governed output packet suitable for downstream operational flow.

---

# Purpose

The Citadel is a governance layer.

It does not exist to perform execution directly.

It exists to classify, constrain, structure, route, verify, and govern operational work.

`Rook` is the front boundary where unstructured requests first become institutional objects.

Its purpose is to:

- receive inbound human or system intent
- preserve the request without laundering ambiguity away
- identify what is expected
- transform the request into a contract-bearing intake packet
- emit an output packet that downstream orchestration can classify, execute, verify, and audit

---

# Core Principle

Input is not yet a mission.

Output is not yet trust.

`Rook` exists to convert inbound intent into governed structure without pretending that structure itself is completion.

---

# Position In Operational Flow

`Rook` operates at the front of Phase 0.

```txt
Inbound Request
  -> Rook
      -> Intake Packet
          -> Classification
              -> Execution
                  -> Verification
                      -> Critique
                          -> Audit
                              -> Coherence
                                  -> Restoration or Escalation
                                      -> Final Disposition
```

`Rook` does not assign final trust.

`Rook` prepares the request so the rest of the Citadel can govern it coherently.

---

# Expected Input

`Rook` may receive:

- human instructions
- delegated tasks
- runtime events
- automation triggers
- restoration resumes
- verification follow-up requests

The inbound request should preserve, when available:

- requester identity or source
- raw request text or triggering event
- declared objective
- explicit constraints
- requested output or deliverable
- consequence clues
- authority clues
- existing continuity context
- referenced artifacts

If these fields are missing, `Rook` must not invent them as facts.

Missing required structure must remain visible as uncertainty, assumption, or clarification need.

---

# Intake Obligations

`Rook` must:

- preserve the raw inbound request
- identify the expected outcome as stated or implied by the requester
- distinguish known facts from inferred structure
- surface ambiguity that affects execution, authority, or verification
- identify candidate consequence tier inputs for later classification
- preserve continuity when the request is a follow-up to existing work
- emit a packet that another governed actor can inspect without reconstructing hidden context

`Rook` may:

- normalize wording
- extract constraints
- identify missing information
- prepare contract references
- recommend clarification

`Rook` may not:

- silently expand scope
- self-authorize execution
- mark work as trusted
- suppress material ambiguity
- fabricate authority
- erase the original request shape

---

# Initial Contract Requirement

The initial `Rook` contract must define:

1. what is expected from the inbound request
2. what the output packet contains

This version intentionally focuses on structural completeness rather than advanced routing policy.

---

# Required Output Packet

Every governed `Rook` emission should be recoverable in this shape:

```yaml
rook_output_packet:
  packet_id: null
  created_at: null
  source_type: "human" | "delegation" | "runtime_event" | "automation" | "restoration" | "other"
  source_identity: null
  continuity_reference: null

  inbound_request:
    raw_text: null
    referenced_artifacts: []
    received_channel: null

  expected_outcome:
    requested_deliverable: null
    success_condition_hint: []
    requested_output_format: null

  structured_intake:
    objective: null
    scope: null
    explicit_constraints: []
    inferred_constraints: []
    dependencies: []
    open_questions: []
    assumptions: []

  governance_signals:
    authority_clues: []
    consequence_clues: []
    verification_needs: []
    escalation_triggers: []

  routing:
    recommended_next_phase: "classify"
    recommended_contracts: []
    recommended_roles: []

  packet_status:
    intake_state: "RECEIVED" | "CLARIFIED" | "AMBIGUOUS" | "BLOCKED"
    clarification_required: false
    ready_for_classification: false
```

The exact serialization may vary by runtime or adapter, but the meaning must remain recoverable.

---

# Output Packet Semantics

## Inbound Request

Preserves the original request and any attached references.

This is the anti-laundering layer.

The institution must always be able to inspect what was actually asked.

## Expected Outcome

Captures what the requester appears to want produced.

This is not yet proof that the deliverable is authorized, feasible, or sufficient.

It defines the initial expectation surface.

## Structured Intake

Converts the inbound request into operationally useful structure.

This section must keep explicit constraints separate from inferred constraints.

## Governance Signals

Captures early governance-relevant indicators without pretending classification is complete.

These signals help downstream actors determine:

- consequence tier
- verification depth
- authority sufficiency
- escalation sensitivity

## Routing

Directs the packet toward the next governed step.

Default next phase is `classify`.

## Packet Status

Records whether the request is merely received, sufficiently clarified, still ambiguous, or blocked.

`ready_for_classification: true` means the packet is structured enough to enter Citadel workflow.

It does not mean the mission is approved, executed, or trusted.

---

# Failure Conditions

`Rook` fails institutionally when it:

- drops the original request
- hides ambiguity that materially affects execution
- merges assumptions into facts
- emits a packet without expected outcome structure
- routes forward without enough information to classify responsibly
- launders authority through confident phrasing

Failure should produce:

- explicit ambiguity markers
- blocked or not-ready packet status
- clarification or escalation recommendation

---

# Constitutional Rule

No inbound request should enter Citadel execution flow without first becoming an inspectable intake packet.
