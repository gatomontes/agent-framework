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

## CLASSIFYING

The system is determining:

- consequence tier
- runtime selection
- required authority
- verification requirements
- escalation sensitivity

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

## RESTORING

The operation entered a recovery or coherence restoration path.

## BLOCKED

The operation cannot continue under current constraints.

Blocking reasons may include:

- missing information
- insufficient authority
- failed verification
- unresolved contradiction
- runtime failure
- unavailable dependency

## ESCALATED

The operation requires higher authority or human intervention.

## SUCCESS

Execution completed successfully.

This is not equivalent to TRUSTED.

## FAILURE

Execution or operational flow failed.

## UNCERTAIN

Evidence or confidence was insufficient to establish trust.

## TRUSTED

Execution, verification, critique, audit, and coherence checks completed successfully.

## UNTRUSTED

A required gate failed.

## DEAD_LETTER

The operation could not be recovered or meaningfully continued.

---

# State Transition Rules

## Allowed Example Flow

```txt
PENDING
  -> CLASSIFYING
    -> READY
      -> EXECUTING
        -> VERIFYING
          -> CRITIQUING
            -> AUDITING
              -> TRUSTED
```

## Failure Example

```txt
EXECUTING
  -> VERIFYING
    -> FAILURE
      -> RESTORING
        -> ESCALATED
```

## Uncertain Example

```txt
VERIFYING
  -> UNCERTAIN
    -> ESCALATED
```

---

# Transition Constraints

1. TRUSTED may only occur after verification.
2. Critical operations may require audit before TRUSTED.
3. RESTORING may transition back into READY.
4. DEAD_LETTER is terminal.
5. ESCALATED requires external authority resolution.
6. SUCCESS without verification remains operationally incomplete.

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

Operational history must remain reconstructable.

---

# Constitutional Rule

Operational clarity is mandatory.

Ambiguous state is governance failure.
