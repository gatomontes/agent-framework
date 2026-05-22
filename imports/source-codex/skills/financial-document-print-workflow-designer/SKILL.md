---
name: financial-document-print-workflow-designer
description: Design and review controlled financial document output such as cheques, stubs, print previews, batch print flows, and reprint-safe PDF rendering. Use when a financial document must be laid out, rendered, and printed reliably with exact field placement and operator-safe print behavior rather than treated like ordinary UI.
---

# Financial Document and Print Workflow Designer

## Overview

Design controlled financial print artifacts that must render consistently and survive preview, batch printing, failure, and reprint conditions.

Focus on cheque face layout, stub content, page geometry, print tolerances, preview behavior, and rendering contracts. Use this skill when a document is part of a financial workflow and incorrect layout or print ambiguity would create operational or monetary risk.

## Required Inputs

Gather as much of this as is available:

- approved disbursement workflow and issue/reprint semantics
- desired cheque or document type
- stock assumptions such as blank or preprinted stock
- bank, alignment, margin, and signature constraints if known
- required face fields and stub fields
- local print environment assumptions

If some inputs are missing, proceed with explicit assumptions unless the missing context would make the review misleading.

## Workflow

1. Reconstruct the operational document flow from preview through printing and reprint.
2. Identify the rendering target such as PDF-first, browser print, or printer-specific output.
3. Define exact content zones:
   - document face
   - detachable stub
   - optional archive or duplicate copy
4. Define page geometry, margins, placement tolerances, and print invariants.
5. Define operator-visible states such as previewed, rendered, queued, printed, failed, and reprinted.
6. Check whether the current payroll model can supply all required stub fields cleanly.
7. Flag any reliance on uncontrolled browser behavior or printer variability.

## Rules

- Treat cheque output as a controlled document, not a decorative report.
- Prefer PDF-first rendering unless a stronger integration path is justified.
- Never depend on casual browser print behavior for placement-sensitive financial documents.
- Separate layout rules from issuance/control rules owned by the disbursement workflow.
- Design for repeatability across preview, first print, and reprint.
- Keep operator confidence high during batch printing and failure recovery.

## Escalation Rules

Pause and call for specialist review when:

- cheque stock type is unknown
- bank placement constraints or signature rules are missing
- the print environment is heterogeneous enough to threaten placement reliability
- stakeholders want exact alignment without a rendering contract
- the requested stub content exceeds what the current data model can provide safely

When escalating, say what is knowable now, what remains uncertain, and which specialist is needed.

## Output Contract

Default response shape:

1. `Current document workflow`
2. `Required rendering contract`
3. `Field and layout requirements`
4. `Unsafe print assumptions`
5. `Implementation backlog`
6. `Needs specialist escalation`

For each finding, include:

- what document or print behavior is being assessed
- why it matters operationally
- what risk follows if it is rendered incorrectly
- the minimum next step needed to support it safely
- the urgency rating

Use exactly these urgency labels:

- `Optional`
- `Important`
- `High`
- `Critical`

## Quality Bar

Before finishing:

- confirm the rendering target is explicit
- verify placement-sensitive fields have a defined contract
- identify preview, print, failure, and reprint states
- call out any data fields the payroll model cannot yet supply cleanly
- reject layouts that rely on uncontrolled print behavior
- keep the output actionable for engineering and operations
