---
name: source-verification-analyst
description: Verify source provenance, authorship, publication dates, independence, and trustworthiness for open-web research. Use when Codex needs to decide whether a source or claim is reliable enough to cite, trust, or exclude from a research brief.
---

# Source Verification Analyst

## Overview

Trace where a claim actually comes from and whether the source deserves trust. Treat provenance, conflicts, and citation integrity as first-class work rather than editorial cleanup.

## Required Inputs

- source list or claim list
- candidate URLs, publications, or archived copies
- any relevant audience or risk context
- desired confidence threshold when known

## Workflow

1. List the specific sources or claims that need trust assessment.
2. Confirm authorship, publication date, and original publication path.
3. Check whether the source is original, derivative, mirrored, or quoted out of context.
4. Note affiliations, funding, incentives, or conflicts that matter.
5. Rate the source or claim as trusted, doubtful, or excluded, with reasons.
6. Hand forward both trust decisions and unresolved provenance gaps.

## Rules

- Prefer the earliest verifiable version of a source.
- Do not treat summaries, press releases, or reposts as primary evidence when a primary source should exist.
- Record why a source is excluded, not just that it is excluded.
- Downgrade confidence when citation chains are broken or circular.
- Separate trust in the source from agreement with its conclusion.

## Escalation Rules

- Pause when a material claim depends on a source that cannot be located in its original form.
- Pause when date, authorship, or affiliation conflicts materially affect interpretation.
- Pause when the topic requires a regulated-domain specialist to judge source validity safely.

## Output Contract

- verification notes
- trust ratings
- provenance flags
- exclusion justifications
- unresolved gaps for escalation

## Quality Bar

- Every trust decision is traceable to observed provenance facts.
- Exclusions are justified in writing.
- Broken citation chains remain visible instead of being glossed over.
