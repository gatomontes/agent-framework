---
name: red-team-fact-checker
description: Challenge a research draft by hunting for unsupported claims, omitted contradictions, weak sourcing, and overconfident language before release. Use when Codex needs an adversarial fact-checking pass on a brief, memo, or synthesis artifact.
---

# Red-Team Fact Checker

## Overview

Apply an adversarial review after synthesis. Look first for why the draft might be wrong, incomplete, or stronger than the evidence allows, then show the release risk plainly.

## Required Inputs

- draft brief or memo
- visible claim-to-evidence links when available
- supporting source set or verification notes
- any stated release deadline or sensitivity

## Workflow

1. Isolate the draft's strongest claims and implied conclusions.
2. Check whether each material claim has direct support, clear qualification, or both.
3. Search for omitted contradictions, contrary evidence, and broken provenance.
4. Mark claims as supported, weakly supported, unsupported, or misleadingly phrased.
5. Produce a challenge memo and correction list.
6. Escalate release risk if material defects remain unresolved.

## Rules

- Treat missing support as a finding, not an editorial suggestion.
- Prefer disconfirming evidence over rhetorical smoothness.
- Challenge strong verbs when the evidence is only partial or probabilistic.
- Keep the review focused on claim quality, sourcing, and omissions.
- Do not pass a draft as safe to release if material unsupported claims remain.

## Escalation Rules

- Pause when the draft lacks enough evidence traceability to review responsibly.
- Pause when high-stakes claims remain unsupported after one correction pass.
- Pause when the release deadline would force shipping known material defects.

## Output Contract

- challenge memo
- disputed-claim list
- correction requests
- release-risk summary

## Quality Bar

- The review identifies material support gaps, not just wording issues.
- Unsupported claims are impossible to miss.
- Release risk is stated plainly enough for a lead to act on.
