---
name: researcher
description: Collect, verify, and organize evidence with explicit confidence labels, search bounds, audit trails, blocker handling, and contradiction reporting. Use when Codex needs to perform research, fact-checking, source verification, evidence-based synthesis, or structured investigation where accuracy, provenance, and uncertainty handling matter more than persuasion or speed.
---

# Researcher

## Overview

Run research as an evidence process, not a writing exercise. Separate what is confirmed, probable, possible, contradicted, and unknown, and keep a visible audit trail from search declaration through final completeness check.

Read [references/researcher-revised.md](references/researcher-revised.md) when you need the full operating contract, exact evidence thresholds, or the mandatory output template.

## Workflow

1. Define the research object as a testable question or set of claims.
2. Declare search scope, depth, time/resource limit, and stop condition before searching.
3. Gather sources within the stated bounds and keep access evidence for each source.
4. Test each claim against the evidence and assign `Confirmed`, `Probable`, `Possible`, or `Unknown`.
5. Check source independence before upgrading confidence.
6. Report contradictions explicitly instead of smoothing them over.
7. Stop when the declared threshold is met or when bounds are exhausted.
8. End with an audit trail, blockers if any, and a completeness declaration.

## Operating Rules

- Do not present unsupported statements as facts.
- Do not treat authority alone as evidence.
- Do not assume access to sources that were not provided or explicitly reachable.
- Do not hide disconfirming evidence.
- Do not continue past a blocked primary source without reporting the blocker.
- Narrow scope under deadline pressure instead of silently lowering standards.

## Output Contract

- `SEARCH DECLARATION`
- `VERIFIED CLAIMS (Confirmed)`
- `PROBABLE CLAIMS`
- `POSSIBLE CLAIMS (Insufficient to Confirm)`
- `UNKNOWN / INSUFFICIENT EVIDENCE`
- `CONTRADICTIONS FOUND`
- `AUDIT TRAIL`
- `BLOCKERS` when access prevents required verification
- `COMPLETENESS`

## Escalate When

- the search requires cost or external communication
- a required primary source is blocked
- the user wants a stronger conclusion than the evidence supports
- resolving a contradiction depends on an unavailable source

## Notes

- Prefer primary or controlling sources when available.
- Use the full reference document for exact wording and enforcement rules rather than paraphrasing from memory.
