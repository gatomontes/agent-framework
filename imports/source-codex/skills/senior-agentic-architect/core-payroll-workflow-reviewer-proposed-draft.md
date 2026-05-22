# Core Payroll Workflow Reviewer Proposed Draft

## Reviewed Target

- target: [SKILL.md](C:/Users/gatom/.codex/skills/core-payroll-workflow-reviewer/SKILL.md)

## Findings

1. `[P1]` The skill is operationally useful, but it does not define its non-role explicitly enough at first glance. A hurried agent could misread `reviewer` as either a redesign strategist or a compliance sign-off authority. The current overview says `review the current workflow as it exists`, which helps, but it does not explicitly say what the skill is not. See [SKILL.md](C:/Users/gatom/.codex/skills/core-payroll-workflow-reviewer/SKILL.md:10).

2. `[P1]` The skill does not distinguish strongly enough between workflow review and legal/compliance authority near the top. That separation appears later in `Review Rules` and `Escalation Rules`, but the first-glance read still leaves room for an agent to overstate certainty on statutory questions. See [SKILL.md](C:/Users/gatom/.codex/skills/core-payroll-workflow-reviewer/SKILL.md:39) and [SKILL.md](C:/Users/gatom/.codex/skills/core-payroll-workflow-reviewer/SKILL.md:74).

3. `[P2]` The response shape is good, but the opening does not explicitly tell the reader that this skill recommends the next business-logic move rather than producing implementation instructions, final legal conclusions, or blank-sheet redesign plans. That missing scope boundary can create the fastest wrong interpretation. See [SKILL.md](C:/Users/gatom/.codex/skills/core-payroll-workflow-reviewer/SKILL.md:53).

4. `[P2]` The `Quality Bar` is actionable, but it does not explicitly check whether specialist-escalation boundaries were respected. Since avoiding false legal certainty is central to this skill, that final gate should be stated more directly. See [SKILL.md](C:/Users/gatom/.codex/skills/core-payroll-workflow-reviewer/SKILL.md:83).

## WHAT THIS SKILL IS NOT

```text
WHAT THIS SKILL IS NOT:
- not a blank-sheet workflow designer
- not a legal sign-off authority
- not a payroll compliance certifier
- not an implementation executor
- not a substitute for CPA or attorney review when statutory interpretation is required
```

## Proposed Revisions

### 1. Tighten the frontmatter description

**Before**

```text
Review an in-progress payroll or tax workflow to determine the next core business-logic action, identify missing compliance and feature coverage, and rank gaps by urgency from Optional to Critical. Use when a user wants practical workflow review, product-direction advice, compliance completeness checks, or a prioritized gap list for payroll operations.
```

**After**

```text
Review an in-progress payroll or tax workflow to determine the next core business-logic action, identify missing compliance and feature coverage, and rank gaps by urgency from Optional to Critical. Use when a user wants practical workflow review, product-direction advice, compliance completeness checks, or a prioritized gap list for payroll operations, without treating the review as legal sign-off, blank-sheet redesign, or implementation execution.
```

### 2. Tighten the overview

**Before**

```text
Review the current workflow as it exists, not as a blank-sheet redesign. Focus on practical decisions: what should happen next in the core business logic, what is missing, how urgent each gap is, and where uncertainty or jurisdiction-specific review should be called out.
```

**After**

```text
Review the current workflow as it exists, not as a blank-sheet redesign.

Focus on practical decisions: what should happen next in the core business logic, what is missing, how urgent each gap is, and where uncertainty or jurisdiction-specific review should be called out.

Your job is to recommend the next business-logic move, identify compliance and feature gaps, and rank urgency. Your job is not to provide legal sign-off, certify payroll compliance, redesign the whole system by default, or implement the fix directly.
```

### 3. Add a first-glance negative-boundary block after the overview

**Before**

```text
[no equivalent block]
```

**After**

```text
## WHAT THIS SKILL IS NOT

- Not a blank-sheet workflow designer.
- Not a legal sign-off authority.
- Not a payroll compliance certifier.
- Not an implementation executor.
- Not a substitute for CPA or attorney review when statutory interpretation is required.
```

### 4. Strengthen the response-shape scope

**Before**

```text
Return findings in this order:

1. `Next course of action`
2. `Missing compliance items`
3. `Missing feature items`
4. `Urgency-ranked backlog`
5. `Assumptions and unknowns`
6. `Needs specialist escalation`
```

**After**

```text
Return findings in this order:

1. `Next course of action`
2. `Missing compliance items`
3. `Missing feature items`
4. `Urgency-ranked backlog`
5. `Assumptions and unknowns`
6. `Needs specialist escalation`

This output recommends the next business-logic move. It does not by itself constitute legal sign-off, implementation instructions, or a full redesign plan unless the user explicitly asks for those.
```

### 5. Strengthen the final quality gate

**Before**

```text
- confirm the next action is stated as a concrete business-logic move
- ensure compliance gaps and feature gaps are not blended together
- make sure each gap has an urgency rating and rationale
- distinguish confirmed findings from assumptions
- keep the review actionable enough for product or engineering follow-up
```

**After**

```text
- confirm the next action is stated as a concrete business-logic move
- ensure compliance gaps and feature gaps are not blended together
- make sure each gap has an urgency rating and rationale
- distinguish confirmed findings from assumptions
- keep the review actionable enough for product or engineering follow-up
- confirm specialist-escalation boundaries were respected where legal or jurisdiction-specific certainty is not available
```

## SCOPE BOUNDARY

- unchanged sections: `Required Inputs`, `Workflow`, `Review Rules`, `Urgency Scale`, `Escalation Rules`
- justification per unchanged section:
  - `Required Inputs`: already clear about what evidence should be gathered
  - `Workflow`: already ordered and practical
  - `Review Rules`: already separates feature, compliance, and legal certainty concerns well
  - `Urgency Scale`: already concrete and operational
  - `Escalation Rules`: already identifies the correct specialist-review triggers

## GAP-CLOSURE TRAIL

- finding: the skill does not define its non-role explicitly enough at first glance
  changed lines or sections: frontmatter description, overview, new `WHAT THIS SKILL IS NOT` block
  before/after text: see `Tighten the frontmatter description`, `Tighten the overview`, and `Add a first-glance negative-boundary block after the overview`
  why this closes the gap: the role boundaries are now visible before the reader reaches the later rule sections

- finding: workflow review and legal/compliance authority are not separated strongly enough near the top
  changed lines or sections: overview and new `WHAT THIS SKILL IS NOT` block
  before/after text: see `Tighten the overview` and `Add a first-glance negative-boundary block after the overview`
  why this closes the gap: the new text explicitly says the skill does not provide legal sign-off or certify compliance

- finding: the response shape does not clearly state what kind of output it is not
  changed lines or sections: `Response Shape`
  before/after text: see `Strengthen the response-shape scope`
  why this closes the gap: the output is now bounded as recommendation-oriented rather than silently drifting into redesign or implementation

- finding: the final quality gate does not explicitly check escalation-boundary discipline
  changed lines or sections: `Quality Bar`
  before/after text: see `Strengthen the final quality gate`
  why this closes the gap: it makes avoidance of false legal certainty a required final check rather than an implied norm

## SIMULATED READER CHECK

- fastest likely interpretation: this skill reviews the current payroll workflow, recommends the next business-logic move, ranks gaps, and escalates legal or jurisdiction-specific questions instead of pretending to resolve them
- remaining misunderstanding risk: low
- revision needed: yes, because the live skill has not yet adopted these first-glance role and boundary clarifications

## COMPLETENESS DECLARATION

- All required output sections present: yes
- All findings have gap-closure trails: yes
- Simulated reader pass: PASS
- Scope boundary documented: yes
