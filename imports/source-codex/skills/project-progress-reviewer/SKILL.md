---
name: project-progress-reviewer
description: Review a past project brief against the current local project state and write a new dated Markdown progress note. Use when a user wants to assess progress since an earlier brief, resume understanding after time away, or document current status from notes, plans, recent files, and code artifacts.
---

# Project Progress Reviewer

## Overview

This skill reconstructs where a project started, where it is now, and what changed in between. It is for progress review and status documentation, not for writing a brand-new brief or doing implementation work.

## Use This When

Trigger this skill when the user asks to:

- review an old project brief against the current state
- evaluate progress on a project after time away
- document what has been completed, what is in progress, and what is blocked
- produce a new dated status or progress memo in Markdown
- compare planned scope to current artifacts, docs, or code

Common source artifacts:

- `BRIEF*.md`, `README*.md`, `PLAN*.md`, `ROADMAP*.md`, `SPEC*.md`
- `STATUS*.md`, `NOTES*.md`, `MEMORY*.md`, `NEXT*.md`, `TODO*.md`
- project docs folders such as `docs/`, `planning/`, `notes/`, `research/`, `decisions/`, `logs/`
- recent code, commits, and changed files when the current state is implementation-heavy

## Workflow

### 1. Resolve The Baseline Brief

Identify the original or most authoritative planning artifact first.

Prefer this order:

1. User-provided brief path
2. Explicit `BRIEF*`, `PROJECT-BRIEF*`, or `SPEC*` files
3. Recent high-signal planning docs such as `PLAN*`, `ROADMAP*`, or `README*`

If multiple plausible briefs exist, choose the one that looks most authoritative and recent enough to matter. Mention the assumption briefly instead of stopping unless the ambiguity changes the conclusion materially.

### 2. Reconstruct The Current State

Inspect only enough of the project to understand the present state responsibly.

Prefer evidence in this order:

1. Current status notes, decision logs, and recent project markdown
2. Recently modified files and active workstreams
3. Targeted search for objectives, milestones, blockers, and next steps
4. Code, configuration, or commits only when they materially clarify whether work is complete

For projects under `E:\ai\projects\...`, use the same artifact-first discipline as `$project-loader`: recover state from planning, notes, decisions, and recent artifacts before diving into implementation details.

### 3. Compare Brief Versus Reality

Extract the brief's intended outcomes, then compare them against the evidence you found.

At minimum, classify each major objective as:

- completed
- in progress
- not started
- unclear from evidence
- changed in scope

Also note:

- important decisions made since the brief
- blockers or risks
- meaningful scope drift
- the most likely next step

Do not overstate progress. If evidence is thin, say so plainly.

### 4. Write A New Dated Markdown Note

Create a fresh dated Markdown file instead of overwriting the prior brief.

Default filename pattern:

- `YYYY-MM-DD-project-progress.md`
- or `YYYY-MM-DD-<project-slug>-progress.md` when the project name is obvious

Default output location preference:

1. `docs/status/`
2. `status/`
3. `docs/`
4. project root

If the user specifies a destination, follow it. Otherwise, create the best-fit path that already matches the repo's structure.

Use the template in [references/progress-note-template.md](./references/progress-note-template.md).

## Response Expectations

After writing the file:

- report the exact file path created
- summarize the main conclusion in 2-4 sentences
- flag any important uncertainty, drift, or blockers

## Rules

- Prefer local evidence over memory or guesswork.
- Do not overwrite older status notes unless the user explicitly asks.
- Keep the note factual and decision-useful rather than decorative.
- If there is no credible brief, say that and fall back to a "current state snapshot" with the limitation stated clearly.
- If the project state is mostly code and there are few notes, inspect recent implementation evidence before concluding that work is stalled.
- Ask a question only when the missing information would materially change what counts as progress.
