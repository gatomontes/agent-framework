# The Citadel Usage

This document explains how to use The Citadel as an operational control layer around agents, runtimes, fabricated capabilities, and orchestration systems.

The Citadel is not the worker.

The Citadel is the command doctrine that tells workers how to work, verify, fail, recover, report, and earn trust.

---

# Core Usage Pattern

Every task moves through the same conceptual path:

```txt
Task
  -> Rook Intake
    -> Classify
      -> Topology Synthesis / Authority Assignment
        -> Select Runtime / Capability Shape
          -> Execute
            -> Verify
              -> Critique
                -> Audit
                  -> Check Coherence
                    -> Restore or Escalate
                      -> Final Disposition
```

The Citadel answers one question:

```txt
Can this output be trusted?
```

Execution alone cannot answer that question.

---

# 1. Human Submits Task

A task begins as a human request, runtime event, automation trigger, or delegated subtask.

Examples:

```txt
Write a gothic metal lyric draft.
Implement contractor payment batch.
Review a pull request.
Summarize a document.
Generate a deployment plan.
```

The task is not immediately executed as a freeform prompt.

It first enters The Citadel.

The Citadel I/O boundary is:

```txt
/core/contracts/rook-contract.md
```

`Rook` converts the inbound request into a governed intake scroll before consequence classification and execution begin.

If the task later reaches a terminal disposition that must be returned externally, `Rook` also normalizes that outcome for output.

If the task involves outbound communication, reminders, or boundary updates, use:

```txt
/core/protocols/communication-boundary-protocol.md
```

to keep staged sends, event persistence, and release conditions durable and auditable.

---

# 2. Classify Consequence Tier

Use:

```txt
/core/doctrine/tiered-verification.md
```

Assign one consequence tier:

```txt
critical
important
routine
trivial
```

The tier determines:

- verification intensity
- independence requirements
- confidence threshold
- escalation sensitivity
- whether human override may be required

Examples:

```txt
Creative lyric draft -> routine
README wording change -> routine
Persistent repo write -> important
Payroll tax logic -> critical
Security remediation -> critical
```

---

# 3. Select Runtime or Capability Shape

The orchestrator selects the appropriate worker.

Examples:

```txt
Writing runtime -> code implementation
Planning runtime -> planning / analysis
Orchestration runtime -> delegation / runtime coordination
Critique operator -> contradiction pressure
Audit operator -> verification-of-verification
Evidence operator -> evidence gathering
```

Citadel may fabricate or recruit the needed capability shape under governance rather than depending on a resident skill inventory.

Core doctrine remains runtime-agnostic.

---

# 4. Create an Execution Contract

Before execution begins, define:

```yaml
execution_contract:
  objective: string
  constraints: list
  expected_artifact: string
  consequence_tier: critical | important | routine | trivial
  success_criteria: list
  failure_conditions: list
```

The execution contract tells the worker what must be produced.

It does not prove that the result is correct.

---

# 5. Attach a Verification Contract

Use:

```txt
/core/contracts/verification.md
```

Every meaningful execution contract should have a verification contract unless explicitly exempted.

Example:

```yaml
verification_contract:
  method:
    channel: independent
    reasoning_path: different_from_execution
  criteria:
    - condition: artifact satisfies requested structure
      threshold: 0.85
      failure_handling: flag
  uncertainty_reporting:
    confidence_required: 0.85
    expose_confidence: true
```

Silence is not success.

Missing verification is:

```txt
FAILURE: UNVERIFIED
```

---

# 6. Execute and Verify

Execution and verification may happen:

- in parallel
- sequentially
- through separate personas
- through separate runtimes
- through retrieval-backed checks
- through human review

For important or critical work, verification should not share the same reasoning path as execution.

Example:

```txt
Implementation runtime produces code changes.
Evidence operator or test runner verifies evidence.
Critique operator pressures assumptions.
Audit operator checks the verification chain.
```

---

# 7. Critique with Blackquill

Blackquill reviews the execution and verification pair.

Blackquill asks:

- Is the artifact internally coherent?
- Did it satisfy the contract?
- Are there contradictions?
- Is confidence justified?
- Was verification real or performative?
- Was silence mistaken for success?

Blackquill outputs:

```yaml
blackquill_verdict: PASS | FAIL | UNCERTAIN
blackquill_notes: string
confidence: float
cited_evidence: list
```

Blackquill does not replace verification.

Blackquill pressure-tests it.

---

# 8. Audit with Auditor

Auditor verifies the verifier.

Auditor asks:

- Did Blackquill cite evidence?
- Was the verification method independent enough?
- Were confidence claims justified?
- Was the evidence chain reconstructed?
- Was critique merely ritualized?

For critical operations, Blackquill and Auditor should agree before final trust is granted.

Disagreement triggers escalation.

---

# 9. Check Doctrinal Coherence

Use:

```txt
/core/doctrine/doctrinal-coherence.md
```

The coherence check asks:

```txt
Did this operation preserve active doctrine?
```

Examples of coherence failures:

- verification was skipped without justification
- escalation was bypassed
- confidence was inflated
- a wrapper ignored contract requirements
- an exception became normalized

If coherence fails, do not finalize as trusted.

Invoke restoration.

---

# 10. Restore or Escalate

If doctrine or governance fails, use:

```txt
/core/governance/restoration-protocol.md
/core/contracts/escalation-contract.md
```

Possible outcomes:

```txt
FREEZE
RECOVER
VALIDATE
RESUME
DECOMMISSION
DEAD_LETTER
```

When coherence fails:

```txt
STOP
INVESTIGATE
RESTORE
VALIDATE
RESUME
```

A system that continues during unresolved coherence failure is uncontrolled.

---

# 11. Emit Unified Status

Use:

```txt
/core/contracts/status-schema.md
```

Every operation should emit an operational status object:

```yaml
operational_status:
  context:
    consequence_tier: IMPORTANT
    lifecycle_state: FINALIZING

  execution:
    state: SUCCESS
    artifact: path-or-reference

  verification:
    state: VERIFIED
    confidence: 0.91
    method: retrieval_backed

  critique:
    blackquill_verdict: PASS
    blackquill_notes: "No blocking contradictions detected."
    auditor_verdict: PASS
    auditor_notes: "Evidence chain sufficient for tier."
    consensus: AGREED

  coherence:
    status: COHERENT
    restoration_state: null

  final_disposition:
    value: TRUSTED
    human_override: false
    override_authority: null
```

Final disposition is the operational truth.

---

# Final Dispositions

```txt
TRUSTED
UNTRUSTED
UNCERTAIN
BLOCKED
DEAD_LETTER
```

## TRUSTED

The task completed, verification passed, critique/audit passed, and coherence remained intact.

## UNTRUSTED

A gate failed.

## UNCERTAIN

Evidence or confidence was insufficient.

## BLOCKED

The task cannot proceed under current constraints.

## DEAD_LETTER

Escalation or restoration could not resolve the operation.

---

# Example: Lyric Composition

Task:

```txt
Write a gothic metal lyric in the requested style and structure.
```

Flow:

```txt
Classify: routine
Runtime: writing-oriented runtime
Capability shape: lyric composition
Verification: structure/rules checker
Critique: Blackquill style and constraint review
Audit: sampled or optional unless high importance
Coherence: ensure no skipped required contract
Final Disposition: TRUSTED or UNTRUSTED
```

Output artifact:

```txt
/artifacts/lyrics/song-title/draft.md
/artifacts/lyrics/song-title/verification.md
/artifacts/lyrics/song-title/critique.md
/artifacts/lyrics/song-title/final.md
```

---

# Example: Code Implementation

Task:

```txt
Implement contractor payment batch.
```

Flow:

```txt
Classify: important or critical
Runtime: implementation-oriented runtime
Execution: code implementation
Verification: tests, schema checks, route checks, review against contract
Critique: Blackquill architectural review
Audit: Auditor evidence-chain review
Coherence: verify no doctrine bypass
Final Disposition: TRUSTED, UNTRUSTED, or BLOCKED
```

Important code should not be merged based only on implementation success.

It must pass verification and disposition.

---

# Minimal Manual Invocation

For a human-driven workflow, use this checklist:

```txt
1. What is the task?
2. What tier is it?
3. What artifact should exist at the end?
4. Who executes?
5. Who verifies independently?
6. What would count as failure?
7. Did Blackquill critique it?
8. Did Auditor need to audit it?
9. Did coherence hold?
10. What is the final disposition?
```

If any answer is missing, the operation is not fully complete.

---

# Runtime Wrapper Obligation

Each runtime wrapper should eventually implement the operational flow directly.

A wrapper should know how to:

- load contracts
- load doctrine
- invoke personas
- request verification
- preserve artifacts
- emit status schema
- escalate failures
- enter restoration flow

A runtime that cannot do this may still be useful.

But it is not fully Citadel-compliant.

---

# Golden Rule

Execution is not trust.

Trust is earned through verification, critique, audit, coherence, and final disposition.
