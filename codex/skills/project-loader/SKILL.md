---
name: project-loader
description: Resume a project stored under `E:\ai\projects\[project-name]` by reconstructing its current state from local project artifacts. Use when the user says `load project x`, `resume project x`, `open project x`, `continue project x`, or asks to pick back up where work left off without starting coding. Inspect the most relevant notes, plans, decisions, logs, and recent files, recover the current phase and likely next step, and continue in non-coding mode unless the user explicitly switches to coding time.
---

# Project Loader

Interpret `load project x` as `E:\ai\projects\x` unless the user explicitly provides a different base path.

## Core Workflow

1. Resolve the target project folder.
2. Inspect only enough of the project to recover the current state.
3. Prefer planning, notes, decisions, logs, and recent artifacts over code.
4. Treat `E:\htdocs` as off-limits unless the user explicitly says it is coding time.
5. Reconstruct project state from current folder evidence, not from conversation memory alone.
6. Prioritize the most recent actionable thread of work over general project summaries.
7. Stop once there is enough evidence to resume the work responsibly.

## Inspect In This Order

1. List the project root.
2. Read obvious high-signal root files such as:
   - `README*`
   - `ROADMAP*`
   - `PLAN*`
   - `TODO*`
   - `NOTES*`
   - `MEMORY*`
   - `STATUS*`
   - `NEXT*`
   - `BRIEF*`
   - other high-signal `*.md` files
3. Check high-signal subfolders such as:
   - `docs`
   - `notes`
   - `planning`
   - `research`
   - `strategy`
   - `specs`
   - `drafts`
   - `artifacts`
   - `decisions`
   - `logs`
4. Review the most recently modified relevant files.
5. Use targeted text search only when needed to resolve ambiguity or find the latest thread of work.
6. Read supporting files only if they clarify the current direction.

Ignore bulky, generated, dependency, cache, export, or archive-heavy folders unless they are clearly part of the active working context.

## Recover

Recover these points from the project artifacts:

- project purpose
- current phase
- active workstream
- last meaningful decisions
- open questions or blockers
- pending next actions
- important constraints
- whether the project is still in planning mode or has moved into coding mode
- last active thread of work (what exactly was being worked on most recently)

When artifacts conflict, prefer the most recent explicit source and briefly note the uncertainty.

## Respond

After loading, respond with:

1. A short statement of what the project is
2. A concise summary of where work left off
3. The most likely next step
4. Any ambiguity, missing context, or conflicting evidence worth flagging

Keep the response brief, practical, and action-oriented.

## Rules

- Do not touch `E:\htdocs` during project loading unless the user explicitly switches to coding time.
- Never summarize from memory before inspecting the project folder.
- Do not assume the project is code-first.
- Do not ask broad open-ended questions if the local artifacts already imply the next step.
- Make reasonable assumptions from the files and state them briefly.
- If the target folder does not exist, say so plainly and ask for the correct project name or path.
- If multiple folders plausibly match, present the best match and mention brief alternatives.

## Search Heuristics

Prefer:

- root listing first
- recent files second
- targeted text search third

Look for terms such as:

- `next step`
- `open questions`
- `decision`
- `pending`
- `blocked`
- `resume`
- `mvp`
- `phase`
- `scope`

On Windows PowerShell, prefer commands in this style:

- `Get-ChildItem -LiteralPath 'E:\ai\projects\<project-name>'`
- `Get-ChildItem -Recurse -LiteralPath 'E:\ai\projects\<project-name>' -File | Sort-Object LastWriteTime -Descending`
- `Get-ChildItem -Recurse -LiteralPath 'E:\ai\projects\<project-name>' -Include *.md | Select-String -Pattern 'next step|open questions|decision|pending|blocked|phase|scope'`

Prioritize identifying the "latest thread" of work over general project summaries.

## Default Interpretation

Interpret:
- `load project nominasconflow`

As:
- inspect `E:\ai\projects\nominasconflow`
- recover state from project artifacts
- summarize where work left off
- continue in non-coding mode unless told otherwise
