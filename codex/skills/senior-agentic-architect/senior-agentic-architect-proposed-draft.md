# Senior Agentic Architect Proposed Draft

## Reviewed Target

- target: [SKILL.md](C:/Users/gatom/.codex/skills/senior-agentic-architect/SKILL.md)

## Findings

1. `[P1]` The skill now has strong controls, but its own final-check layer is diffuse and partially duplicative. The `Quality Bar` contains overlapping checks such as negative-boundary and simulated-reader requirements more than once, which weakens first-glance legibility for the very standard it is trying to enforce. See [SKILL.md](C:/Users/gatom/.codex/skills/senior-agentic-architect/SKILL.md:516), [SKILL.md](C:/Users/gatom/.codex/skills/senior-agentic-architect/SKILL.md:528), and [SKILL.md](C:/Users/gatom/.codex/skills/senior-agentic-architect/SKILL.md:530).

2. `[P1]` The output contract for revision work is incomplete relative to the newer standard. It includes `WHAT THIS SKILL IS NOT`, `COMPLETENESS CHECK`, `GAP-CLOSURE TRAIL`, and `SIMULATED READER CHECK`, but it does not yet require a `COMPLETENESS DECLARATION` block in the output itself. That means the skill demands a final declaration in the Quality Bar without giving revision outputs an explicit place to put it. See [SKILL.md](C:/Users/gatom/.codex/skills/senior-agentic-architect/SKILL.md:467), [SKILL.md](C:/Users/gatom/.codex/skills/senior-agentic-architect/SKILL.md:475), and [SKILL.md](C:/Users/gatom/.codex/skills/senior-agentic-architect/SKILL.md:543).

3. `[P2]` The top-level `WHAT THIS SKILL IS NOT` block is useful, but it is not framed as a reusable pattern for the skill’s own future revisions. The workflow says to include such a block when role confusion is plausible, but the live skill’s own block sits as static content and does not explain that it is the reference pattern for downstream revisions. A hurried reader can still treat it as local prose rather than a model. See [SKILL.md](C:/Users/gatom/.codex/skills/senior-agentic-architect/SKILL.md:18) and [SKILL.md](C:/Users/gatom/.codex/skills/senior-agentic-architect/SKILL.md:467).

4. `[P2]` The `Quality Bar` mixes checklist bullets with full procedural subsections, which hurts scanability. A tired agent looking for the final gate has to switch from bullet validation to prose policy mid-section. That is workable, but not ideal for first-glance enforcement. See [SKILL.md](C:/Users/gatom/.codex/skills/senior-agentic-architect/SKILL.md:507).

## WHAT THIS SKILL IS NOT

```text
WHAT THIS SKILL IS NOT:
- not a generic writing improver that optimizes for style over operational safety
- not a runtime executor that carries out the target task itself
- not a substitute for domain truth when the source facts are missing
- not a self-certifying reviewer that can call work complete without explicit evidence and declarations
```

## Proposed Revisions

### 1. Tighten the top-level negative-boundary block

**Before**

```text
## WHAT THIS SKILL IS NOT

- Not a general-purpose editor. It rewrites for operational clarity, not style or compression.
- Not a task executor. It produces instruction sets, not completed work.
- Not a substitute for domain expertise. It structures what it is given; it does not fill missing domain facts.
- Not a runtime controller. It produces handoffs; it does not activate them.
- Not a validator of its own outputs unless explicitly invoked in verification mode.
```

**After**

```text
## WHAT THIS SKILL IS NOT

- Not a general-purpose editor. It rewrites for operational clarity, not style or compression.
- Not a task executor. It produces instruction sets, not completed work.
- Not a substitute for domain expertise. It structures what it is given; it does not fill missing domain facts.
- Not a runtime controller. It produces handoffs; it does not activate them.
- Not a self-certifying validator. It does not declare its own revisions complete without explicit verification, scope boundary, and completeness declaration outputs.
```

### 2. Add an explicit revision-output completeness declaration block

**Before**

```text
When a revision is being delivered rather than merely suggested, include the `SIMULATED READER CHECK` in the output.
```

**After**

```text
When a revision is being delivered rather than merely suggested, include all of:
- `WHAT THIS SKILL IS NOT` when role confusion is plausible
- `COMPLETENESS CHECK`
- `SCOPE BOUNDARY`
- `GAP-CLOSURE TRAIL`
- `SIMULATED READER CHECK`
- `COMPLETENESS DECLARATION`
```

### 3. Add a concrete completeness declaration template to the Output Contract

**Before**

```text
Before finalizing a revision, mentally run:

SIMULATED READER CHECK:
- fastest likely interpretation: [...]
- remaining misunderstanding risk: [...]
- revision needed: [yes/no]
```

**After**

```text
Before finalizing a revision, include:

SIMULATED READER CHECK:
- fastest likely interpretation: [...]
- remaining misunderstanding risk: [...]
- revision needed: [yes/no]

COMPLETENESS DECLARATION:
- All required output sections present: yes/no
- All findings have gap-closure trails: yes/no
- Simulated reader pass: PASS/FAIL
- Scope boundary documented: yes/no
```

### 4. De-duplicate and compress the Quality Bar

**Before**

```text
- potentially confusing skills include negative boundary definitions
- completed prescriptions include before/after text tied to a diagnosed gap
- first-glance simulated-reader risk has been checked and resolved
- revisions include exact before/after text, negative boundary block, simulated-reader check, and finding-to-change trail
...
- negative boundaries are explicit where name or description could mislead
- prescription completeness includes before/after text and gap-closing statement
- simulated first-glance read identified zero remaining misunderstandings
```

**After**

```text
- revisions include exact before/after text
- negative boundaries are explicit where name or description could mislead
- scope boundary is documented for unchanged sections
- each finding has a gap-closure trail tied to changed text
- simulated first-glance read identified zero remaining misunderstandings
- completeness declaration is present and passes
```

## SCOPE BOUNDARY

- unchanged sections: `Evidence Policy`, `Irreversibility Rule`, `State Safety`, `Ownership Rule`
- justification per unchanged section:
  - `Evidence Policy`: already concrete and operational
  - `Irreversibility Rule`: already includes required safeguards
  - `State Safety`: already defines transition checks clearly
  - `Ownership Rule`: already defines delegation boundaries clearly

## GAP-CLOSURE TRAIL

- finding: final-check layer is diffuse and duplicative
  changed lines or sections: `Quality Bar`
  before/after text: see `De-duplicate and compress the Quality Bar`
  why this closes the gap: it turns repeated requirements into a single enforceable checklist

- finding: revision outputs lack a defined place for completeness declaration
  changed lines or sections: `Output Contract`
  before/after text: see `Add an explicit revision-output completeness declaration block` and `Add a concrete completeness declaration template`
  why this closes the gap: it aligns the required final declaration with the actual output shape

- finding: top-level negative boundary block does not yet reinforce self-governance strongly enough
  changed lines or sections: top-level `WHAT THIS SKILL IS NOT`
  before/after text: see `Tighten the top-level negative-boundary block`
  why this closes the gap: it makes self-certification boundaries explicit at first glance

- finding: quality gate mixes bullets and prose in a way that reduces scanability
  changed lines or sections: `Quality Bar`
  before/after text: see `De-duplicate and compress the Quality Bar`
  why this closes the gap: it gives the rushed reader a cleaner pass/fail checklist

## SIMULATED READER CHECK

- fastest likely interpretation: this skill audits and revises instructions, but cannot call the revision complete unless it emits the full evidence and declaration package
- remaining misunderstanding risk: low
- revision needed: yes, because the live skill has not yet adopted these specific compressions and output requirements

## COMPLETENESS DECLARATION

- All required output sections present: yes
- All findings have gap-closure trails: yes
- Simulated reader pass: PASS
- Scope boundary documented: yes
