# Chief Of Staff Proposed Draft

## Reviewed Target

- target: [SKILL.md](C:/Users/gatom/.codex/skills/chief-of-staff/SKILL.md)
- comparison context: [`$ceo` SKILL.md](C:/Users/gatom/.codex/skills/ceo/SKILL.md)

## Findings

1. `[P1]` `$chief-of-staff` is clearer than the old `$ceo`, but it still lacks a first-glance negative-boundary block. Its opening says `Turn routing into execution`, which is strong, yet a hurried agent could still misread it as a general executor rather than an orchestration controller that may sometimes do direct work locally. See [SKILL.md](C:/Users/gatom/.codex/skills/chief-of-staff/SKILL.md:10).

2. `[P1]` The skill does not define its non-role sharply enough near the top. It says `Do not replace $ceo`, but it does not immediately say what it also does not replace: active executors, domain specialists, or every delegated worker. That omission leaves room for the fastest wrong interpretation: that `$chief-of-staff` is the universal doer once deployed. See [SKILL.md](C:/Users/gatom/.codex/skills/chief-of-staff/SKILL.md:12).

3. `[P2]` The phrase `Turn routing into execution` is effective but slightly overcompressed. On first read it can imply that `$chief-of-staff` personally executes the work rather than controlling activation, ownership, integration, and replan. The distinction exists later in the workflow and activation rules, but it is not fully resolved in the opening identity. See [SKILL.md](C:/Users/gatom/.codex/skills/chief-of-staff/SKILL.md:10) and [SKILL.md](C:/Users/gatom/.codex/skills/chief-of-staff/SKILL.md:72).

4. `[P2]` The output contract tells the user what sections appear, but it does not foreground the difference between `active controller` and `active executor` in the overview itself. Since the role’s core job is controlled activation rather than direct execution, this distinction should appear earlier and more explicitly. See [SKILL.md](C:/Users/gatom/.codex/skills/chief-of-staff/SKILL.md:23) and [SKILL.md](C:/Users/gatom/.codex/skills/chief-of-staff/SKILL.md:149).

5. `[P3]` The skill does not explicitly state who materializes personas when activation requires a newly materialized persona. The activation rules mention `newly materialized persona plus explicit activation`, but they do not say whether `$chief-of-staff` performs persona materialization directly or delegates it to `$persona-builder`. That leaves a minor but real authority ambiguity. See [SKILL.md](C:/Users/gatom/.codex/skills/chief-of-staff/SKILL.md:93).

## WHAT THIS SKILL IS NOT

```text
WHAT THIS SKILL IS NOT:
- not the upstream routing authority; that belongs to `$ceo`
- not a universal executor that personally performs every workstream
- not a substitute for domain specialists when specialist execution is the safer path
- not a passive status narrator; it must actively control activation and integration once approved
- not an excuse to blur active controller, active executor, and recommended candidate
```

## Proposed Revisions

### 1. Narrow the frontmatter description

**Before**

```text
Serve as the active execution controller for an approved run using structured routing output such as $ceo slot chains and persona handoffs. Use when Codex needs a single role to activate the execution team, assign ownership, sequence dependencies, invoke direct-fit skills or subagents, manage the execution loop, integrate outputs, and decide when to replan or close.
```

**After**

```text
Serve as the active execution-control skill for an approved run using structured routing output such as `$ceo` slot chains and persona handoffs. Use when Codex needs a single orchestration role to activate the execution team, assign ownership, sequence dependencies, invoke direct-fit skills or subagents, manage the execution loop, integrate outputs, and decide when to replan or close, without becoming the upstream routing authority or a universal hands-on executor.
```

### 2. Tighten the overview

**Before**

```text
Turn routing into execution. Read the upstream plan, decide which recommended operators become active for the current run, assign ownership, launch the work, track dependencies, integrate outputs, and decide whether the task is complete or needs replan.

Do not replace `$ceo`. `$ceo` decides what should be done and by whom. After approval, `$chief-of-staff` becomes the active execution controller for the run and decides how to activate the team and run the execution loop safely.
```

**After**

```text
Operate as the active execution controller after approval.

Turn upstream routing into controlled activation and execution management. Read the upstream plan, decide which recommended operators become active for the current run, assign ownership, launch the work, track dependencies, integrate outputs, and decide whether the task is complete or needs replan.

Do not replace `$ceo`. `$ceo` decides who should own the work, in what order, and with what handoff structure. After approval, `$chief-of-staff` decides how to activate the team, run the execution loop safely, and integrate outputs.

Your job is to control activation, ownership, sequencing, and integration. Your job is not to become the upstream routing authority or to personally absorb every workstream that should belong to an active executor.
```

### 3. Add a first-glance negative-boundary block after the overview

**Before**

```text
[no equivalent block]
```

**After**

```text
## WHAT THIS SKILL IS NOT

- Not the upstream routing authority; that belongs to `$ceo`.
- Not a universal executor that personally performs every workstream.
- Not a substitute for domain specialists when specialist execution is the safer path.
- Not a passive status narrator; it must actively control activation and integration once approved.
- Not an excuse to blur active controller, active executor, and recommended candidate.
```

### 4. Tighten the authority bullets

**Before**

```text
- `$ceo` owns upstream routing and candidate selection
- once deployed, `$chief-of-staff` is the active runtime controller for the run and owns actual tool use, skill invocation, subagent spawning, sequencing, ownership, tracking, integration, and replan triggers
```

**After**

```text
- `$ceo` owns upstream routing and candidate selection
- once deployed, `$chief-of-staff` is the active runtime controller for the run and owns activation decisions, tool use, skill invocation, subagent spawning, sequencing, ownership assignment, tracking, integration, and replan triggers
```

### 5. Add a contrast block inside the authority model

**Before**

```text
[no equivalent block]
```

**After**

```text
Boundary contrast:
- `$ceo` decides who should own the work, in what order, and with what handoff structure.
- `$chief-of-staff` decides which candidates become active now, how workstreams are sequenced, and how outputs are integrated.
- active executors perform the owned workstreams that `$chief-of-staff` activates.
```

### 6. Clarify persona materialization authority

**Before**

```text
4. newly materialized persona plus explicit activation
```

**After**

```text
4. newly materialized persona plus explicit activation

Persona materialization is delegated to `$persona-builder`; `$chief-of-staff` only activates the resulting artifact.
```

## SCOPE BOUNDARY

- unchanged sections: `Required Inputs`, `Workflow`, `Activation Rules`, `Ownership Rules`, `Execution Loop`, `Escalation Rules`, `Output Contract`, `Quality Bar`
- justification per unchanged section:
  - `Required Inputs`: input types are already explicit and operational
  - `Workflow`: the execution-loop sequence is already clear
  - `Activation Rules`: activation-order logic is already specific enough
  - `Ownership Rules`: ownership guardrails are already concrete
  - `Execution Loop`: closed-loop execution logic is already bounded
  - `Escalation Rules`: escalation triggers are already crisp
  - `Output Contract`: output sections are already usable once role identity is sharpened
  - `Quality Bar`: existing checks remain valid after the opening identity is clarified

## GAP-CLOSURE TRAIL

- finding: `$chief-of-staff` lacks a first-glance negative-boundary block
  changed lines or sections: new `WHAT THIS SKILL IS NOT` block after the overview
  before/after text: see `Add a first-glance negative-boundary block after the overview`
  why this closes the gap: the fastest wrong interpretations are now forbidden explicitly instead of being inferred from later workflow details

- finding: the skill does not define its non-role sharply enough near the top
  changed lines or sections: frontmatter description and overview
  before/after text: see `Narrow the frontmatter description` and `Tighten the overview`
  why this closes the gap: the opening now states both the orchestration role and the boundaries against routing authority and universal execution

- finding: `Turn routing into execution` is slightly overcompressed
  changed lines or sections: overview
  before/after text: see `Tighten the overview`
  why this closes the gap: the revised overview translates that phrase into concrete control actions instead of leaving it as a high-level slogan

- finding: the distinction between controller and executor appears too late
  changed lines or sections: authority bullets and new `Boundary contrast` block
  before/after text: see `Tighten the authority bullets` and `Add a contrast block inside the authority model`
  why this closes the gap: the role split between controller, routing authority, and active executors becomes first-glance legible

- finding: persona materialization authority is ambiguous
  changed lines or sections: `Activation Rules`
  before/after text: see `Clarify persona materialization authority`
  why this closes the gap: the draft now makes it explicit that `$persona-builder` materializes personas while `$chief-of-staff` activates the resulting artifact

## SIMULATED READER CHECK

- fastest likely interpretation: `$chief-of-staff` is the approved execution controller that activates the team, sequences workstreams, and integrates outputs, but does not replace `$ceo` or personally perform every workstream
- remaining misunderstanding risk: low
- revision needed: yes, because the live skill has not yet adopted these opening-role clarifications

## COMPLETENESS DECLARATION

- All required output sections present: yes
- All findings have gap-closure trails: yes
- Simulated reader pass: PASS
- Scope boundary documented: yes
