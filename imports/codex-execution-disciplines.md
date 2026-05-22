# Codex Execution Disciplines

## Source Focus

- `codex/skills/senior-agentic-architect/SKILL.md`
- `codex/skills/project-loader/SKILL.md`

## What Survives

### 1. Ambiguity suppression before execution

Useful pattern from `senior-agentic-architect`:

- rewrite vague tasks into executable task statements
- make assumptions explicit up front
- separate confirmed facts, assumptions, open questions, and blocked items
- force done criteria instead of implied completion

Citadel-worthy translation:

- execution-facing instructions should minimize guesswork before work begins
- runtime-facing contracts should suppress hidden decisions and unstated scope

### 2. Evidence policy inside the instruction

Useful pattern:

- confidence labels should be tied to evidence quality
- single-source claims should degrade confidence
- absence of evidence should not be upgraded into certainty

Citadel-worthy translation:

- evidence thresholds belong inside operational instructions, not only in review after the fact
- inference and observation should remain separate throughout execution

### 3. Irreversibility controls

Useful pattern:

- high-impact tasks require approval boundary, rollback thinking, pre-checkpoints, and stop conditions

Citadel-worthy translation:

- irreversible actions should trigger a higher-control instruction form
- approval protocol should name approver, scope, evidence, and forbidden remainder

### 4. State-transition hygiene

Useful pattern:

- do not mutate lifecycle state without explicit transition rules
- inspect current state, allowed next states, and forbidden transitions first

Citadel-worthy translation:

- lifecycle corruption is worse than incomplete progress
- read-only fallback is preferable when state rules are unclear

### 5. Ownership boundaries in multi-agent work

Useful pattern:

- define owned artifacts, allowed modifications, handoff artifacts, done conditions, and escalation edges

Citadel-worthy translation:

- delegated concurrency needs disjoint write scopes whenever possible
- ownership ambiguity should collapse concurrency or force coordination

### 6. Evidence-first project resumption

Useful pattern from `project-loader`:

- reconstruct state from local artifacts, not conversation memory
- inspect root, high-signal docs, recent files, then targeted search
- recover current phase, active thread, blockers, and next step

Citadel-worthy translation:

- restoration/resumption should privilege artifacts over recollection
- current state recovery should stop once enough evidence exists to proceed responsibly

## What Does Not Survive As Doctrine

- machine-specific path assumptions like `E:\ai\projects\...`
- local workspace-specific exclusions unless rewritten generically

Reason:

Those are implementation details, not constitutional truths.

## Recommended Citadel Follow-Ons

- define a generic instruction-hardening doctrine
- strengthen restoration/resumption doctrine with evidence-first recovery order
- add explicit lifecycle-transition controls to operational mutation contracts
