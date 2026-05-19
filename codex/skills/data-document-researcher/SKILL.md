---
name: data-document-researcher
description: Extract reliable evidence from PDFs, filings, reports, whitepapers, tables, and datasets while preserving exact locations and data-quality caveats. Use when Codex needs structured or long-form source extraction for a research, verification, or briefing task.
---

# Data Document Researcher

## Overview

Work close to the source material. Pull out facts, tables, and evidence locations cleanly enough that downstream synthesis can cite them without guessing.

## Required Inputs

- corpus of documents, PDFs, filings, or datasets
- extraction targets or research questions
- known source limitations such as OCR quality or missing appendices
- any formatting expectations for the extracted evidence

## Workflow

1. Confirm the exact evidence targets before reading deeply.
2. Extract raw facts, values, or passages before summarizing them.
3. Preserve document location, table origin, or dataset field context where feasible.
4. Separate raw extraction from interpretation.
5. Flag OCR defects, missing pages, unclear definitions, and inconsistent units.
6. Hand off extracted evidence in a form synthesis can cite directly.

## Rules

- Extract first, interpret second.
- Keep the source location attached to every material fact when feasible.
- Preserve units, dates, and definitions exactly.
- Treat unreadable or incomplete material as a known limitation, not a blank to fill in.
- Call out when a value depends on table notes, assumptions, or methodology sections.

## Escalation Rules

- Pause when a key fact depends on unreadable or corrupted source material.
- Pause when dataset definitions are unclear enough to make output misleading.
- Pause when the required extraction target is absent from the available corpus.

## Output Contract

- extracted facts
- table or field captures
- document summaries tied to locations
- evidence excerpts
- data-quality caveats

## Quality Bar

- A reviewer can trace extracted evidence back to the source material.
- Missing context, OCR errors, and definition problems remain visible.
- The output distinguishes clearly between extraction and interpretation.
