# Citadel Operational State Machine

## Purpose

The Operational State Machine defines the canonical lifecycle states for Citadel-governed operations.

States exist to prevent ambiguity.

Every meaningful operation must emit explicit state.

---

# Core Principle

Silence is not success.

Missing state is operational uncertainty.

---

# Primary Operational States

## PENDING

The operation has been accepted but execution has not yet started.

## INTAKING

The operation is crossing the institutional boundary and being normalized for governed handling.

## CLASSIFYING

The system is determining:

- consequence tier
- runtime selection
- required authority
- verification requirements
- escalation sensitivity

## ASSEMBLING

Topology, authority, verification routing, and mission structure are being assembled.

## AUTHORIZING

Authority is being assigned and validated before execution may begin.

## READY

Contracts are established.

Execution may begin.

## EXECUTING

The worker is actively performing the task.

## VERIFYING

Verification is evaluating the artifact.

## CRITIQUING

Critique systems are pressure-testing coherence, assumptions, and structural integrity.

## AUDITING

Audit systems are validating the verification and critique chain.

## COHERENCE_CHECK

The operation is being checked against active doctrine before finalization.

## RESTORING

The operation entered a recovery or coherence restoration path.

## WAITING_ON_BLOCKER

The operation cannot continue until a blocking condition is resolved.

Blocking reasons may include:

- missing information
- insufficient authority
- failed verification
- unresolved contradiction
- runtime failure
- unavailable dependency

## UNDER_ESCALATION

The operation requires higher authority or human intervention and is awaiting that routing.

## FINALIZING

The operation is resolving final disposition and preserving required terminal records.

## ARCHIVED

Post-disposition preservation has completed.

## FAILURE

Execution or operational flow failed before terminal governance resolution completed.

---

# Final Dispositions

Final disposition is separate from lifecycle state.

Allowed final dispositions are:

```txt
TRUSTED
UNTRUSTED
UNCERTAIN
BLOCKED
DEAD_LETTER
```

- `TRUSTED` is an earned terminal determination, not a mid-flow state.
- `UNTRUSTED` is a terminal determination that a required gate failed.
- `UNCERTAIN` is a terminal determination that confidence or evidence remained insufficient.
- `BLOCKED` is a terminal determination when the mission cannot proceed under current constraints.
- `DEAD_LETTER` is a terminal determination when restoration or escalation cannot recover the mission.

---

# State Transition Rules

## Allowed Example Flow

```txt
PENDING
  -> INTAKING
    -> CLASSIFYING
      -> ASSEMBLING
        -> AUTHORIZING
          -> READY
            -> EXECUTING
              -> VERIFYING
                -> CRITIQUING
                  -> AUDITING
                    -> COHERENCE_CHECK
                      -> FINALIZING
                        -> ARCHIVED
```

## Failure Example

```txt
EXECUTING
  -> VERIFYING
    -> FAILURE
      -> RESTORING
        -> UNDER_ESCALATION
```

## Uncertain Example

```txt
VERIFYING
  -> COHERENCE_CHECK
    -> UNDER_ESCALATION
```

---

# Transition Constraints

1. Final disposition may only be assigned after required lifecycle gates resolve.
2. Critical operations may require audit before `TRUSTED`.
3. RESTORING may transition back into READY.
4. `DEAD_LETTER` is terminal as a disposition, not as a mid-flow lifecycle state.
5. UNDER_ESCALATION requires external authority resolution.
6. Execution success without verification remains operationally incomplete.

---

# Consequence Tier Interaction

Higher consequence tiers require:

- stricter verification
- stronger evidence
- more independent reasoning
- lower tolerance for uncertainty
- more aggressive escalation behavior

---

# State Emission Requirement

Every operation must emit:

- current state
- previous state
- transition reason
- responsible authority
- timestamp
- active consequence tier
- final disposition when terminal

Operational history must remain reconstructable.

---

# Constitutional Rule

Operational clarity is mandatory.

Ambiguous state is governance failure.
