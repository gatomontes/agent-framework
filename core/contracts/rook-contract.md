# Rook Contract

## Status

Adopted as the Citadel bidirectional I/O boundary.

This document defines `Rook`, the Citadel I/O surface responsible for receiving inbound requests before operational governance begins and normalizing terminal outcomes after final disposition is reached.

`Rook` is the exclusive connecting surface between external request sources and Citadel governance flow.

---

# Purpose

The Citadel is a governance layer.

It does not exist to perform execution directly.

It exists to classify, constrain, structure, route, verify, and govern operational work.

`Rook` is the exclusive boundary surface where requests enter Citadel and terminal outcomes leave it.

Its purpose is to:

- receive inbound human or system intent
- preserve the request without laundering ambiguity away
- identify what is expected
- transform the request into a contract-bearing intake packet
- emit an intake packet that downstream orchestration can classify, execute, verify, and audit
- receive terminal rejections, blocked outcomes, and unsolved tasks back from Citadel
- normalize those outcomes into a consequent return packet

---

# Core Principle

Input is not yet a mission.

Output is not yet trust.

`Rook` exists to normalize ingress and egress without pretending that the boundary itself is the workflow.

---

# Position Relative To Operational Flow

`Rook` sits outside the operational flow as a bidirectional surface.

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
                                          -> Rook
                                              -> Consequent Output Packet
```

`Rook` does not assign final trust.

`Rook` prepares the request so Citadel can govern it coherently, and prepares terminal outcomes so they can leave Citadel coherently.

The operational flow still ends at final disposition.

`Rook` is the boundary that surrounds that flow, not an additional internal phase after it.

---

# Inbound Input

`Rook` may receive:

- human instructions
- delegated tasks
- runtime events
- automation triggers
- restoration resumes
- verification follow-up requests
- terminal rejections
- blocked operations
- dead-letter outcomes
- unsolved or unsatisfiable tasks

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

# Boundary Obligations

`Rook` must:

- preserve the raw inbound request
- identify the expected outcome as stated or implied by the requester
- distinguish known facts from inferred structure
- surface ambiguity that affects execution, authority, or verification
- identify candidate consequence tier inputs for later classification
- preserve continuity when the request is a follow-up to existing work
- emit a packet that another governed actor can inspect without reconstructing hidden context
- accept terminal outcomes handed back from downstream Citadel stages
- normalize institutional failure, rejection, and unsolved-task outcomes into a coherent return packet
- preserve the reason the task could not be completed, trusted, or continued

`Rook` may:

- normalize wording
- extract constraints
- identify missing information
- prepare contract references
- recommend clarification
- normalize boundary communication updates before downstream routing

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
2. what the intake packet contains
3. what the terminal return packet contains

This version intentionally focuses on structural completeness rather than advanced routing policy.

It also defines the minimum return behavior for terminal institutional outcomes.

---

# Required Intake Packet

Every governed `Rook` emission should be recoverable in this shape:

```yaml
rook_intake_packet:
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

# Required Return Packet

Terminal rejections or unsolved outcomes returned to the requester should be recoverable in this shape:

```yaml
rook_return_packet:
  packet_id: null
  created_at: null
  continuity_reference: null

  original_request:
    raw_text: null
    requested_deliverable: null
    source_identity: null

  terminal_outcome:
    final_disposition: "UNTRUSTED" | "UNCERTAIN" | "BLOCKED" | "DEAD_LETTER"
    outcome_class: "rejection" | "unsolved" | "authority_block" | "verification_failure" | "coherence_failure" | "dead_letter"
    originating_stage: null
    summary: null

  institutional_reasoning:
    blocking_factors: []
    failed_requirements: []
    unresolved_questions: []
    assumptions_preserved: []

  consequence_output:
    safe_next_actions: []
    clarification_required: []
    escalation_required: false
    human_decision_required: false
    resubmission_guidance: []

  return_status:
    normalized_by_rook: true
    ready_for_external_return: false
```

The return packet exists so terminal institutional outcomes are not emitted as raw runtime fragments, isolated status codes, or decontextualized refusal text.

If `UNTRUSTED` has no separately defined downstream recovery path, it should be treated as a final determination and handed to `Rook` for output normalization.

---

# Packet Semantics

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

If the request is communication-bearing, downstream handling should preserve the staging and persistence rules defined by:

```txt
/core/protocols/communication-boundary-protocol.md
```

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

## Intake Packet Status

Records whether the request is merely received, sufficiently clarified, still ambiguous, or blocked.

`ready_for_classification: true` means the packet is structured enough to enter Citadel workflow.

It does not mean the mission is approved, executed, or trusted.

## Return Packet

Normalizes final rejections and unsolved work into a coherent institutional output after final disposition has already been determined.

The return packet must preserve:

- what was originally requested
- why the operation could not be completed or trusted
- which institutional gate or stage produced the terminal outcome
- what safe next action remains available

This makes terminal failure inspectable and actionable instead of merely abrupt.

---

# Failure Conditions

`Rook` fails institutionally when it:

- drops the original request
- hides ambiguity that materially affects execution
- merges assumptions into facts
- emits a packet without expected outcome structure
- routes forward without enough information to classify responsibly
- launders authority through confident phrasing
- emits a terminal rejection without normalization
- returns a dead-letter or blocked result without preserved institutional reasoning

Failure should produce:

- explicit ambiguity markers
- blocked or not-ready packet status
- clarification or escalation recommendation

---

# Constitutional Rule

No inbound request should enter Citadel execution flow without first passing through `Rook` and becoming an inspectable intake packet.

No final rejection, blocked mission, or unsolved task should leave Citadel without first being handed back to `Rook` for normalization and consequent output.
