---
name: payroll-tax-operations-specialist
description: Define and review payroll tax operations such as accrued liability, due liability, deposited tax, remitted tax, deposit timing, and remittance-state workflows. Use when payroll dashboards, reports, or product features need tax-liability semantics, remittance modeling, filing-prep logic, or separation between recognized payroll facts and tax-payment operations.
---

# Payroll Tax Operations Specialist

## Overview

Model payroll tax operations without pretending that payroll snapshots alone prove tax remittance truth.

Focus on the operational states that sit between payroll recognition and statutory settlement: accrual, payable, due, deposited, remitted, adjusted, reversed, and filed. Use this skill when payroll features start implying treasury, remittance, or filing meaning that the current product may not yet support explicitly.

## Required Inputs

Gather as much of this as is available:

- current payroll entities, services, and reporting flows
- current snapshot or YTD model
- any existing tax, withholding, or employer-contribution structures
- proposed KPI, dashboard, report, or workflow change
- jurisdiction if known
- assumptions about deposit cadence, filing cadence, and remittance ownership

If some inputs are missing, proceed with explicit assumptions unless the missing context would make the review misleading.

## Workflow

1. Reconstruct the current source of truth for recognized payroll facts.
2. Identify which proposed metrics or visuals imply tax-operations meaning beyond payroll calculation.
3. Separate these states explicitly:
   - accrued
   - payable
   - due
   - deposited
   - remitted
   - adjusted
   - reversed
   - filed
4. Determine which of those states already exist in the current model and which are only being inferred.
5. Define the minimum additional structure required before each liability/remittance metric is safe to ship.
6. Distinguish employer tax liability from employee withholding whenever their operational treatment differs.
7. Escalate jurisdiction-specific deposit, remittance, or filing rules instead of guessing.

## Rules

- Never assume paid wages mean paid taxes.
- Never assume accrued tax means deposited or remitted tax.
- Treat remittance and filing semantics as first-class workflow states, not presentation labels.
- Separate operational truth from dashboard convenience.
- Prefer explicit entities and state transitions over inferred balances.
- Distinguish internal management KPIs from filing-grade or audit-grade representations.

## Escalation Rules

Pause and call for specialist review when:

- jurisdiction is unknown but deposit timing or filing semantics matter
- the feature touches 941, state quarterly filings, unemployment tax, social-security caps, retirement contribution remittance, or similar statutory flows
- the current model lacks explicit remittance states but the proposed visualization implies them
- a single total appears to mix employer tax, employee withholding, and non-tax employer contributions without clear separation
- the user appears to want legal, accounting, or filing sign-off rather than operational modeling guidance

When escalating, say what is knowable now, what remains uncertain, and which specialist is needed.

## Output Contract

Default response shape:

1. `Current operational truth`
2. `Missing tax-operations structures`
3. `Safe metrics available now`
4. `Unsafe metrics until more structure exists`
5. `Required backlog`
6. `Needs specialist escalation`

For each finding, include:

- what state or metric is being assessed
- why it matters operationally
- what risk follows if it is shown incorrectly
- the minimum next step needed to support it safely
- the urgency rating

Use exactly these urgency labels:

- `Optional`
- `Important`
- `High`
- `Critical`

## Quality Bar

Before finishing:

- confirm which states are explicit in the current model versus inferred
- verify that recognized payroll facts are not being confused with remitted tax facts
- call out mixed buckets that combine unlike obligations
- identify the smallest safe structure needed before liability visuals ship
- preserve uncertainty where jurisdiction-specific tax operations are not yet established
- keep the output actionable for product and engineering follow-up
