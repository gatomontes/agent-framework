# Blackquill Review Gate

## Purpose

The Blackquill Review Gate exists to pressure-test operational artifacts before trust is granted.

It is not an execution worker.

It is an oversight instrument.

## Operational Role

Blackquill governs:
- contradiction exposure
- assumption pressure-testing
- verification scrutiny
- structural integrity review
- doctrinal drift detection
- repair-condition issuance

Blackquill does not replace verification.

Blackquill pressures the trustworthiness of execution and verification together.

## Invocation Timing

Blackquill should activate:
- after execution,
- after initial verification,
- before final disposition.

Example:

```txt
Execute
  -> Verify
    -> Blackquill Review Gate
      -> Auditor
        -> Final Disposition
```

## Required Inputs

A Blackquill invocation should receive:
- execution artifact
- execution contract
- verification artifact
- consequence tier
- operational context
- uncertainty declarations

## Expected Outputs

```yaml
blackquill_verdict:
  PASS | FAIL | UNCERTAIN | BLOCKED

repair_conditions:
  - explicit remediation requirements

structural_findings:
  - contradictions
  - unsupported assumptions
  - verification weaknesses
  - doctrinal inconsistencies

confidence:
  float
```

## Core Principle

Critique without repair conditions is noise.

Every major rejection should define:
- why the artifact fails,
- what structural weakness exists,
- what evidence is missing,
- what conditions permit acceptance.

## Architectural Separation

Citadel owns the operational interface.

The Blackquill repository owns:
- Hall doctrine,
- authorities,
- tone/language,
- product structure,
- monetization,
- ceremonial review identity.

Do not duplicate Blackquill worldbuilding inside Citadel.

Citadel invokes.
Blackquill governs.
