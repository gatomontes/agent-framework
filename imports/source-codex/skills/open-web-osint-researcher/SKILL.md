---
name: open-web-osint-researcher
description: Reconstruct timelines, public traces, and entity relationships from open-web sources such as webpages, archives, handles, public records, and dated artifacts. Use when Codex needs OSINT-style investigation within public-source boundaries for a research or fact-finding task.
---

# Open-Web OSINT Researcher

## Overview

Investigate open-web evidence as a timeline and entity-resolution problem. Favor dated artifacts, explicit uncertainty, and public-source discipline over narrative convenience.

## Required Inputs

- named entities, aliases, handles, or domains
- time window when known
- specific claims to investigate
- any ethical or policy constraints already identified

## Workflow

1. Normalize the entity list and note ambiguity risks up front.
2. Gather public traces from relevant surfaces and archives.
3. Build a dated evidence trail before writing any narrative.
4. Resolve entity links carefully; keep uncertain matches separate from confident ones.
5. Record contradictions, anomalies, and missing intervals.
6. Hand off a timeline, trace log, and confidence notes to synthesis or review.

## Rules

- Stay within open-web and public-source boundaries.
- Prefer directly dated artifacts over retrospective summaries.
- Treat ambiguous identities as separate until the evidence supports merging them.
- Flag anomalies instead of forcing them into a neat story.
- Separate observed traces from inferred relationships.

## Escalation Rules

- Pause when multiple entities plausibly map to the same handle, name, or domain.
- Pause when the evidence is too sparse to support more than a weak inference.
- Pause when the request would cross ethical, legal, or policy boundaries for open-web investigation.

## Output Contract

- timeline map
- entity linkage notes
- trace evidence log
- contradiction register
- confidence notes on uncertain matches

## Quality Bar

- Timelines are evidence-led rather than story-led.
- Uncertain matches stay labeled as uncertain.
- Another researcher could inspect the trace log and challenge the inference path.
