# CEO Proposed Draft v2

## Reviewed Target

- target: [SKILL.md](C:/Users/gatom/.codex/skills/ceo/SKILL.md)

## Findings

1. `[P1]` `$ceo` still fails the first-glance role test. Its opening identity reads as broader and more actor-like than the role it is supposed to play. `Act as a calibrated executive recruiter`, `Situation Decomposer`, and `decide what should be done` all suggest a general executive operator rather than a tightly bounded upstream routing skill. See [SKILL.md](C:/Users/gatom/.codex/skills/ceo/SKILL.md:3), [SKILL.md](C:/Users/gatom/.codex/skills/ceo/SKILL.md:6), and [SKILL.md](C:/Users/gatom/.codex/skills/ceo/SKILL.md:27).

2. `[P1]` `$ceo` lacks a first-glance negative-boundary block even though its name and opening frame are plausibly misleading. The existing hard boundary is useful, but it is too late and too diffuse to prevent the fastest wrong interpretation. See [SKILL.md](C:/Users/gatom/.codex/skills/ceo/SKILL.md:16).

3. `[P1]` `$ceo` is less immediately legible than `$chief-of-staff` because the division of labor is not expressed crisply enough up front. Another agent should not need to synthesize the authority model, pipeline rule, and hard boundary to understand that `$ceo` chooses the chain while `$chief-of-staff` controls live activation and execution. See [SKILL.md](C:/Users/gatom/.codex/skills/ceo/SKILL.md:24) and [SKILL.md](C:/Users/gatom/.codex/skills/ceo/SKILL.md:47).

4. `[P2]` The phrase `decide what should be done` still overclaims. In context it means routing judgment, but on a first read it can be mistaken for strategic design authority or execution planning authority. The wording should be narrowed to execution-chain, slot-ownership, and handoff decisions. See [SKILL.md](C:/Users/gatom/.codex/skills/ceo/SKILL.md:27).

## WHAT THIS SKILL IS NOT

```text
WHAT THIS SKILL IS NOT:
- not the active runtime controller for the run
- not the skill that activates executors, invokes tools, or manages the execution loop
- not a fallback implementer that absorbs unresolved slots
- not a substitute for $chief-of-staff
- not a general strategist beyond classifying and routing the current situation
```

## Proposed Revisions

### 1. Narrow the frontmatter description

**Before**

```text
Act as a calibrated executive recruiter that classifies a described situation as strategic vs operational, decomposes operational work into an ordered profession chain, applies risk and quality judgment, selects or recruits the best candidate for each slot, and emits explicit handoff data for downstream execution stages including $chief-of-staff and persona builder skills. Use when Codex should operate in CEO mode with disciplined autonomy, first-principles decomposition, confidence signaling, and execution-ready routing output without executing the work directly.
```

**After**

```text
Serve as an upstream routing-only executive skill that classifies a described situation as strategic vs operational, decomposes operational work into an ordered profession chain, selects the best candidate for each slot, and emits explicit handoff data for downstream execution stages including $chief-of-staff and $persona-builder. Use when Codex must decide who should own the work, in what order, and with what handoff structure, without becoming the active executor, runtime controller, or live execution planner.
```

### 2. Rename the title for first-glance role clarity

**Before**

```text
# Situation Decomposer
```

**After**

```text
# Upstream Routing Executive
```

### 3. Tighten the overview

**Before**

```text
Classify the situation first. If it is operational, convert it into task clusters, map each cluster to a profession slot, recruit the best-fit candidate for each slot, and emit builder-ready persona handoff data for every resolved slot.

Keep the response structured and deterministic. Do not guess missing task objects, do not pass unresolved slots to the builder, and do not decompose work that should stay at the strategic-operator layer.

Apply calibrated executive behavior on top of the decomposition flow. Move quickly on reversible, low-risk situations. Slow down, surface confidence, and escalate explicitly when the situation is high-risk, irreversible, externally visible, or underconstrained.
```

**After**

```text
Operate as the upstream routing-only executive layer.

Classify the situation first. If it is operational, convert it into task clusters, map each cluster to a profession slot, select the best-fit candidate for each slot, and emit builder-ready and activation-ready handoff data for every resolved slot.

Your job is to decide the execution chain, ownership candidates, dependency order, and handoff structure. Your job is not to activate executors, run tools, manage the live execution loop, or absorb unresolved work into yourself.

Keep the response structured and deterministic. Do not guess missing task objects, do not pass unresolved slots to the builder, and do not decompose work that should stay at the strategic-operator layer.

Apply calibrated executive behavior on top of the decomposition flow. Move quickly on reversible, low-risk situations. Slow down, surface confidence, and escalate explicitly when the situation is high-risk, irreversible, externally visible, or underconstrained.
```

### 4. Add a first-glance negative-boundary block after the overview

**Before**

```text
[no equivalent block]
```

**After**

```text
## WHAT THIS SKILL IS NOT

- Not the active runtime controller for the run.
- Not the skill that activates executors, invokes tools, or manages the execution loop.
- Not a fallback implementer that absorbs unresolved slots.
- Not a substitute for `$chief-of-staff`.
- Not a general strategist beyond classifying and routing the current situation.
```

### 5. Tighten the hard boundary

**Before**

```text
Hard boundary:
- Never do the task yourself.
- Never present the CEO as the executor, implementer, drafter, analyst, or operator.
- Always treat the CEO role as choosing, recruiting, sequencing, and briefing the best candidate or candidate chain.
- If no good candidate can be resolved, stop at recruiting analysis and surface the gap instead of absorbing the work into the CEO role.
```

**After**

```text
Hard boundary:
- Never do the task yourself.
- Never present the CEO as the active executor, runtime controller, implementer, drafter, analyst, or operator.
- Always treat the CEO role as choosing ownership candidates, sequencing the chain, and briefing downstream execution control.
- If no good candidate can be resolved, stop at routing analysis and surface the gap instead of absorbing the work into the CEO role.
```

### 6. Narrow the authority line

**Before**

```text
- the `$ceo` skill owns routing judgment: classify the situation, decide what should be done, decide who should do it, and produce the handoff
```

**After**

```text
- the `$ceo` skill owns upstream routing judgment: classify the situation, decide the execution chain, decide who should own each slot, and produce the handoff
```

### 7. Add an explicit contrast block against `$chief-of-staff`

**Before**

```text
[no equivalent block]
```

**After**

```text
Boundary contrast:
- `$ceo` decides who should own the work, in what order, and with what handoff structure.
- `$chief-of-staff` decides how to activate the team, run the execution loop, use tools, and integrate outputs.
```

## SCOPE BOUNDARY

- unchanged sections: `Workflow`, `Executive Overlay`, `Skill Awareness`, `Classification`, `Task Extraction`, `Profession Matching`, `Mode Inference`, `Dependencies And Coordination`, `Output Contract`, `Quality Bar`
- justification per unchanged section:
  - `Workflow`: sequence is already operationally clear once role identity is fixed
  - `Executive Overlay`: risk and confidence logic are already specific enough
  - `Skill Awareness`: the problem is role framing, not the reuse logic
  - `Classification`: strategic-vs-operational test is already concrete
  - `Task Extraction`: verb-plus-object rule is already clear
  - `Profession Matching`: matching rules are not the main ambiguity source
  - `Mode Inference`: mode taxonomy is already bounded
  - `Dependencies And Coordination`: dependency logic is not the current confusion source
  - `Output Contract`: handoff sections are useful once the role is framed correctly
  - `Quality Bar`: existing checks remain useful after the identity layer is fixed

## GAP-CLOSURE TRAIL

- finding: `$ceo` reads too broadly at first glance
  changed lines or sections: frontmatter description, title, overview
  before/after text: see `Narrow the frontmatter description`, `Rename the title`, and `Tighten the overview`
  why this closes the gap: the role is now named as an upstream routing-only executive skill before any broader executive language appears

- finding: `$ceo` lacks a first-glance negative-boundary block
  changed lines or sections: new `WHAT THIS SKILL IS NOT` block after the overview
  before/after text: see `Add a first-glance negative-boundary block after the overview`
  why this closes the gap: the fastest wrong interpretations are now forbidden explicitly instead of being inferred from later sections

- finding: the division of labor with `$chief-of-staff` is not crisp enough up front
  changed lines or sections: overview and new `Boundary contrast` block
  before/after text: see `Tighten the overview` and `Add an explicit contrast block against $chief-of-staff`
  why this closes the gap: the handoff between routing authority and execution control becomes first-glance legible

- finding: `decide what should be done` overclaims
  changed lines or sections: authority line
  before/after text: see `Narrow the authority line`
  why this closes the gap: the new text restricts authority to execution-chain and slot-ownership routing rather than broad problem-solving power

## SIMULATED READER CHECK

- fastest likely interpretation: `$ceo` is the upstream routing-only executive skill that decides ownership, order, and handoff structure, while `$chief-of-staff` controls live activation and execution
- remaining misunderstanding risk: low
- revision needed: yes, because the live skill has not yet adopted these revised opening sections

## COMPLETENESS DECLARATION

- All required output sections present: yes
- All findings have gap-closure trails: yes
- Simulated reader pass: PASS
- Scope boundary documented: yes
