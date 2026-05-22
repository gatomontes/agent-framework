---
name: research-synthesis-writer
description: Turn verified findings, investigated timelines, and extracted evidence into concise research briefs that separate verified claims, probable claims, contradictions, and gaps. Use when Codex needs to synthesize a research corpus into a decision-ready output without overstating certainty.
---

# Research Synthesis Writer

## Overview

Write for evidence fidelity first and readability second. The brief should help a reader decide, while still making uncertainty, contradiction, and source strength easy to inspect.

## Required Inputs

- verified sources or trust notes
- investigation findings and timelines
- extracted document or data evidence
- required output format or audience when known

## Workflow

1. Inspect the evidence set and note what is verified, probable, contradicted, or missing.
2. Choose the lightest structure that still preserves those distinctions.
3. Draft the brief with claims matched to evidence strength.
4. Keep contradictions and open questions visible rather than burying them.
5. Add a compact audit trail summary.
6. Hand the draft to `red-team-fact-checker` before treating it as final.

## Rules

- Lead with verified claims when they exist.
- Mark probable claims with a confidence note and short reasoning.
- Keep unverified claims visible if they matter, but never present them as settled.
- Preserve contradictions and gaps even when the audience prefers a cleaner story.
- Match the strength of the prose to the strength of the evidence.

## Escalation Rules

- Pause when the evidence set is too inconsistent to support an honest synthesis.
- Pause when the requested format would suppress material caveats.
- Pause when the user is asking for a stronger conclusion than the evidence allows.

## Output Contract

- research brief
- verified claims
- probable claims with confidence
- contradictions found
- gaps in evidence
- audit trail summary

## Quality Bar

- Every material claim is calibrated to the evidence.
- Contradictions and gaps remain visible.
- The brief is clear enough to act on without pretending the evidence is cleaner than it is.
