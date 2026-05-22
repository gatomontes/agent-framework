---
name: web-discovery-researcher
description: Discover relevant open-web sources for a research question by mapping the search space, testing multiple query angles, and producing a reproducible source shortlist with a search log. Use when Codex needs to find evidence efficiently before verification, investigation, or synthesis.
---

# Web Discovery Researcher

## Overview

Search broadly, log the path, and hand downstream roles a source set worth checking. Optimize for coverage and relevance without pretending discovery alone establishes trust.

## Required Inputs

- research question with an explicit object
- named entities, topics, or time bounds
- language, geography, or source-type constraints
- any must-check sites, archives, or exclusions

## Workflow

1. Restate the research object in searchable terms.
2. Generate multiple query frames:
   - direct queries
   - synonyms and aliases
   - time-bounded queries
   - site-specific queries
   - contradiction-seeking queries
3. Search across the open web and note where results cluster or go thin.
4. Build a source shortlist with one-line reasons for inclusion.
5. Record the search trail so someone else can reproduce or challenge it.
6. Hand off candidate sources and blind spots to verification and lead roles.

## Rules

- Prefer original materials over secondary commentary when feasible.
- Treat query diversity as mandatory when early hits reflect only one frame.
- Label low-trust or derivative sources instead of discarding them silently.
- Separate source finding from source validation.
- Flag search blind spots and dead ends explicitly.

## Escalation Rules

- Pause when entity names, aliases, or terms are ambiguous enough to contaminate results.
- Pause when the search space is dominated by mirrors, scraped copies, or low-trust summaries.
- Pause when key evidence appears inaccessible, deleted, or geoblocked.

## Output Contract

- search log
- query variants
- source shortlist
- initial evidence map
- blind spots and exclusions

## Quality Bar

- A teammate could rerun the search from the log.
- The shortlist covers more than one obvious angle unless the domain itself is narrow.
- Candidate sources are grouped clearly enough for downstream verification.
