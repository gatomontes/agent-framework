# Runtime Contract

## Status

Canonical Citadel contract.

This document defines the minimum requirements for any runtime that participates in Citadel-governed work.

A runtime may be a coding agent, orchestration shell, local agent host, cloud agent, script runner, IDE assistant, workflow engine, or future execution substrate.

Citadel does not grant authority to a runtime because of its brand, interface, model, or apparent intelligence.

A runtime earns participation by satisfying this contract.

---

# Purpose

The Runtime Contract separates Citadel doctrine from runtime implementation.

Citadel owns:
- doctrine
- governance
- verification semantics
- delegation rules
- escalation rules
- mission lifecycle
- evidence expectations
- final disposition requirements

Runtimes provide:
- execution
- observation
- artifact production
- state reporting
- tool use
- adapter-specific capabilities

The runtime is a vessel.

Citadel is the law by which the vessel is used.

---

# Core Principle

No runtime is trusted by default.

Execution is not completion.

Output is not evidence.

Confidence is not verification.

A runtime must report what it did, what it changed, what it observed, what it assumed, what failed, and what remains uncertain.

---

# Participation Requirements

A runtime MAY participate in Citadel work only if it can support the following minimum capabilities.

## 1. Task Intake

The runtime must accept a task with:
- objective
- scope
- authority level
- constraints
- expected outputs
- verification requirements
- escalation conditions
- permitted tools
- forbidden actions

The runtime must preserve the task context during execution.

If the task originates outside Citadel governance, the runtime or adapter must not inject it directly into execution flow.

External requests must first pass through:

```txt
/core/contracts/rook-contract.md
```

and be represented as a recoverable `rook_intake_packet` or equivalent adapter representation.

Before active execution begins, the runtime should bootstrap from the appropriate continuity and authority artifacts as defined by:

```txt
/core/protocols/session-bootstrap-protocol.md
```

Communication-bearing intake and boundary updates should preserve the staging, routing, and persistence rules defined by:

```txt
/core/protocols/communication-boundary-protocol.md
```

## 2. State Reporting

The runtime must report its operational state using explicit status values.

Allowed minimum states:
- received
- interpreting
- executing
- blocked
- needs-human-decision
- needs-higher-authority
- completed-unverified
- failed
- halted

State reports must include enough context for another actor to resume or audit the work.

These runtime-local states do not replace institutional final disposition.

## 3. Artifact Emission

The runtime must emit durable artifacts when work produces lasting value.

Artifacts may include:
- source files
- markdown documents
- patches
- diffs
- logs
- plans
- reports
- test outputs
- screenshots
- structured records

Transient chat output is not sufficient for institutional work unless the mission explicitly defines chat as the artifact.

When a terminal outcome is returned externally, the runtime or adapter should preserve the normalized return artifact produced through `Rook`.

When a reusable capability depends on supporting references, scripts, generated artifacts, or assets, the runtime or adapter should preserve those dependencies as an explicit governed bundle rather than an invisible local assumption. See:

```txt
/core/doctrine/capability-bundle-governance.md
```

## 4. Evidence Emission

The runtime must provide evidence for claims of completion.

Evidence may include:
- changed file paths
- commit hashes
- command outputs
- test results
- logs
- screenshots
- citations
- before and after summaries
- reproduction steps

If evidence cannot be produced, the runtime must say so explicitly.

If the mission is research-bearing, the runtime or adapter should preserve the declared release threshold and scope boundary before broad evidence collection begins, as defined by:

```txt
/core/protocols/research-desk-protocol.md
```

## 5. Assumption Declaration

The runtime must declare assumptions that affect execution.

Assumptions must not be hidden inside confident prose.

If an assumption is material, the runtime must either:
- verify it
- ask for authority
- proceed with documented uncertainty
- halt

Execution-facing instructions should not leave material assumptions hidden. See:

```txt
/core/doctrine/instruction-hardening.md
```

## 6. Constraint Preservation

The runtime must preserve user constraints, mission constraints, governance constraints, and safety constraints.

A runtime may not silently reinterpret constraints for convenience.

If constraints conflict, the runtime must escalate or declare the conflict.

Locally available capabilities do not become authorized by convenience.

Activation of reusable capabilities must remain mission-bound as defined by:

```txt
/core/doctrine/capability-registration-and-activation.md
```

Shared operational docs and boundary-facing artifacts must not contain plaintext secrets, as defined by:

```txt
/core/doctrine/secret-boundary-discipline.md
```

## 7. Delegation Support

If the runtime delegates work, it must preserve:
- original objective
- delegated objective
- authority chain
- constraints
- expected outputs
- verification requirements
- return conditions

Delegation does not dissolve responsibility.

The delegating actor remains responsible for integrating and verifying returned work.

## 8. Escalation Support

The runtime must support escalation when:
- authority is insufficient
- requirements conflict
- evidence is missing
- execution becomes unsafe
- uncertainty exceeds mission tolerance
- irreversible actions are requested
- runtime capability is inadequate
- external dependency blocks progress

Escalation must identify the blocker and propose a next decision point.

## 9. Restoration Support

The runtime must support restoration after failure or drift.

Minimum restoration data:
- last known coherent state
- actions already taken
- artifacts changed
- unresolved assumptions
- failed attempts
- recommended recovery path

Restoration is mandatory when continuing would create uncontrolled damage, confusion, or false completion.

When continuity must be recovered, runtimes should prefer evidence-first reconstruction as defined by:

```txt
/core/protocols/continuity-reconstruction.md
```

## 10. Audit Visibility

The runtime must leave enough trace for audit.

An auditor should be able to answer:
- what was requested
- what was done
- what changed
- what evidence exists
- what remains uncertain
- who or what had authority
- why the final disposition was chosen

---

# Required Runtime Report Shape

Every significant runtime execution should be able to produce a report with this shape:

```yaml
runtime_report:
  mission_id: null
  runtime_name: null
  adapter_name: null
  actor_role: null
  rook_intake_reference: null
  authority_chain: []
  objective: null
  scope: null
  status: null
  actions_taken: []
  artifacts_created: []
  artifacts_modified: []
  evidence: []
  assumptions: []
  constraints_observed: []
  blockers: []
  unresolved_questions: []
  verification_status: null
  escalation_required: false
  restoration_required: false
  final_disposition: null
  rook_return_reference: null
```

The exact serialization may vary by adapter, but the information must remain recoverable.

---

# Verification Semantics

A runtime may claim:
- executed
- produced
- changed
- observed
- failed
- blocked

A runtime may not independently claim final trust unless the mission grants it verification authority.

Default final states:
- completed-unverified: work appears done, but independent verification has not occurred
- failed: runtime could not satisfy the objective
- blocked: runtime cannot proceed without external input or authority
- halted: runtime stopped to prevent damage, drift, or unauthorized action

Institutional final disposition remains governed by:

```txt
/core/contracts/status-schema.md
```

and resolves through:

```txt
TRUSTED
UNTRUSTED
UNCERTAIN
BLOCKED
DEAD_LETTER
```

---

# Authority Rules

A runtime must not exceed granted authority.

Examples of authority-sensitive actions:
- deleting files
- rewriting doctrine
- changing governance contracts
- modifying production systems
- sending external communications
- spending money
- exposing private data
- merging irreversible changes
- acting outside mission scope

When authority is unclear, the runtime must escalate.

---

# Adapter Responsibilities

Runtime adapters translate Citadel doctrine into runtime-specific operations.

An adapter must define:
- how tasks are injected
- how state is read
- how artifacts are retrieved
- how evidence is collected
- how failures are detected
- how escalation is surfaced
- how restoration data is preserved

Adapters must not weaken Citadel doctrine to match runtime convenience.

If a runtime cannot satisfy a requirement, the adapter must declare the gap.

---

# Noncompliant Runtime Conditions

A runtime is noncompliant if it:
- cannot report state
- cannot emit durable artifacts when required
- cannot provide evidence
- hides assumptions
- ignores constraints
- invents completion
- cannot surface blockers
- cannot support audit
- treats confidence as proof
- erases authority chains
- collapses governance into runtime preference

Noncompliant runtimes may still be used experimentally, but only under restricted authority and explicit supervision.

---

# Runtime Admission Levels

## Level 0: Untrusted Tool

Can be used manually.

Cannot own mission steps.

## Level 1: Assisted Executor

Can perform bounded tasks under direct supervision.

Must report artifacts and evidence.

## Level 2: Governed Runtime

Can own delegated mission steps.

Must satisfy reporting, evidence, escalation, and restoration requirements.

## Level 3: Strategic Runtime Substrate

Can host Strategic Operators or complex mission topologies.

Must support delegation, audit, restoration, and adapter-level governance.

## Level 4: Institutional Runtime

Can participate in long-running Citadel operations with persistent memory, traceability, audit chains, and formal verification routes.

No runtime receives Level 4 status by assumption.

---

# Prohibited Couplings

Citadel core doctrine must not:
- depend on a named runtime
- grant authority based on runtime identity
- define cognition as belonging to one execution substrate
- define verification as a runtime feature alone
- hide governance inside implementation details

Runtime names belong in adapter files, operational notes, or integration reports, not as doctrinal foundations.

---

# Final Rule

A runtime is replaceable.

A contract is portable.

Doctrine survives the vessel.
