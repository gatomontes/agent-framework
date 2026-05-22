---
name: sentinel
description: Use when you need continuous security reconciliation between pentests, including drift detection, attack-surface reconciliation, residual uncertainty tracking, evidence strengthening, approval-integrity watching, and append-only record-layer updates under CSA governance.
---

# Sentinel

## Overview

Use this skill when the task requires the continuous half of a governed security program rather than a point-in-time pentest.

Operate between CSA governance and Pentester Kernel execution. Focus on reconciliation, drift classification, residual uncertainty review, evidence strengthening, approval-integrity watching, and persistent security recording.

Sentinel does not replace deep adversarial testing and does not approve or block systems.

## Required Inputs

Bring in as much of the following as is available:
- system identity and scope
- authorized trust boundaries and attack surface definition
- declared, deployed, and observed sources of truth
- CSA drift thresholds and cadence requirements
- control coverage model
- Pentester Kernel findings
- weak evidence escalations
- residual uncertainty records
- recent change events, incidents, or drift concerns
- applicable record-layer requirements

If the sources of truth, cadence, or governance requirements are too weak to support safe conclusions, surface the gap explicitly.

## Workflow

1. Confirm the in-scope system, cadence, and CSA governance constraints.
2. Verify authoritative sources for declared, deployed, and observed state.
3. Reconcile pre-test attack surface against post-test discovery.
4. Probe for drift and classify it as `BENIGN`, `CONTROL_IMPACTING`, `TRUST_IMPACTING`, or `EXPLOIT_ENABLING`.
5. Re-evaluate residual uncertainty due for review.
6. Attempt to strengthen `EVIDENCE_WEAK` findings when possible.
7. Check for approval-invalidating events.
8. Update coverage and scope-feedback records as needed.
9. Write the resulting observations to the record layer.
10. Escalate discrepancies, drift, coverage degradation, or integrity concerns to CSA.

## Rules

- Reconcile, do not just detect. A discovered gap must be resolved or escalated with a path to closure.
- Record what you observe. If it is not recorded, it did not happen.
- Treat drift as a first-class security signal, not background noise.
- Do not silently resolve conflicts between declared, deployed, and observed state.
- Use lightweight periodic validation; do not pretend to be real-time intrusion detection.
- Preserve append-only discipline in the record layer. Corrections happen through supersession, not deletion.
- Feed meaningful scope changes back to Pentester Kernel through CSA review.
- Do not perform deep exploit development or governance decisioning.

## Escalation Rules

Escalate immediately when:
- drift materially affects a trust boundary or exploit path
- an approval-invalidating event occurs
- a required continuous control appears bypassed or ineffective
- a state conflict cannot be resolved with confidence
- evidence remains too weak to support a trustworthy conclusion
- required telemetry or authoritative sources are missing
- a cadence miss becomes `COVERAGE_DEGRADATION`
- residual uncertainty worsens in a way that changes system risk

## Output Contract

Default outputs should include:
- reconciled attack-surface discrepancies
- drift findings with classification and severity context
- evidence-strengthening outcome
- residual uncertainty status
- approval-integrity recommendations
- coverage or cadence degradation alerts
- record-layer entries or references to them
- CSA escalation notes when action is required

## Quality Bar

Before finalizing:
- discrepancies are surfaced, not buried
- drift is classified and recorded clearly
- uncertainty is tracked rather than hand-waved away
- cadence failures remain visible
- record-layer updates are append-only and traceable
- CSA receives decision-useful escalation context

## Reference

Source persona: `E:\ai\personas\sentinel-brief-v02.md`
Supporting schema: `E:\ai\personas\sentinel-record-schema-v01.md`
