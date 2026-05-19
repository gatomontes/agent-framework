---
name: junie-handoff
description: Prepare Junie-ready implementation prompts, coding briefs, review checklists, and pasteable handoff instructions when the user wants to delegate work to PhpStorm's Junie agent. Use when the user asks to "write this for Junie", "prepare a Junie prompt", "create a handoff", "make instructions for Junie", or wants output formatted for another coding agent rather than executed directly here.
---

# Junie Handoff

Junie cannot be controlled directly from here. Produce output that the user can paste into Junie with minimal editing.

## Core Workflow

1. Identify the real deliverable the user wants Junie to produce.
2. Gather only the context needed to make the handoff precise.
3. Convert that context into a Junie-ready prompt or brief.
4. Make scope, constraints, acceptance criteria, and file targets explicit.
5. Prefer narrow execution slices over broad, vague requests.

## Output Types

Choose the lightest format that fits the request:

- short pasteable prompt
- implementation brief in Markdown
- bug-fix handoff
- code review / verification checklist
- file-by-file task list
- follow-up prompt for continuing prior Junie work

## What To Include

When preparing a Junie handoff, include the pieces that matter:

- objective
- relevant files or paths
- source of truth docs
- required behavior
- constraints and non-goals
- acceptance criteria
- verification steps if useful

## What To Avoid

- do not pretend to message Junie directly
- do not omit critical constraints that were already established
- do not overload the prompt with unnecessary project history
- do not ask Junie to do multiple unrelated jobs in one handoff unless the user wants that
- do not invent files, entities, or architecture that are not grounded in the current project context

## Prompt Style

Write prompts for Junie that are:

- direct
- implementation-oriented
- explicit about scope
- easy to paste

Prefer sections like:

1. Objective
2. Context
3. Instructions
4. Constraints
5. Acceptance Criteria

## Default Behavior

If the user asks for Junie help without specifying format, default to a paste-ready Markdown brief.

If the task is small, default to a compact prompt block instead.

## Example Triggers

- `write a Junie prompt for the Organization entity`
- `prepare a handoff for Junie to build this CRUD`
- `turn this into instructions for Junie`
- `make a Junie-ready review checklist`
