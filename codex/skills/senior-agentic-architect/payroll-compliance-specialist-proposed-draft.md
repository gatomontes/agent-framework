# Payroll Compliance Specialist Proposed Draft

## Reviewed Target

- target: [SKILL.md](C:/Users/gatom/.codex/skills/payroll-compliance-specialist/SKILL.md)

## Findings

1. `[P1]` The skill is already fairly disciplined, but it does not define its non-role explicitly enough at first glance. The overview says it does not provide legal sign-off, which is good, but a hurried agent could still misread `compliance specialist` as a certifier rather than a compliance-oriented workflow reviewer that preserves uncertainty and escalates when needed. See [SKILL.md](C:/Users/gatom/.codex/skills/payroll-compliance-specialist/SKILL.md:10).

2. `[P1]` The skill does not sharply distinguish between compliance-oriented review and legal/compliance certification near the top. That boundary exists implicitly in the escalation rules, but it should be explicit earlier so the fastest reading does not overclaim authority. See [SKILL.md](C:/Users/gatom/.codex/skills/payroll-compliance-specialist/SKILL.md:44).

3. `[P2]` The output contract gives a good response shape, but it does not explicitly say that its findings are review outputs rather than implementation instructions or legal sign-off. That missing scope boundary creates room for misuse downstream. See [SKILL.md](C:/Users/gatom/.codex/skills/payroll-compliance-specialist/SKILL.md:56).

4. `[P2]` The final quality bar is practical, but it does not explicitly require that escalation boundaries were respected when statutory certainty is unavailable. Because false certainty is one of the main risks in this domain, that should be part of the final gate. See [SKILL.md](C:/Users/gatom/.codex/skills/payroll-compliance-specialist/SKILL.md:75).

## WHAT THIS SKILL IS NOT

```text
WHAT THIS SKILL IS NOT:
- not a legal sign-off authority
- not a payroll compliance certifier
- not a replacement for jurisdiction-specific CPA or attorney review
- not an implementation executor
- not a blank-check approval gate that can override unresolved statutory ambiguity
```

## Proposed Revisions

### 1. Tighten the frontmatter description

**Before**

```text
Review payroll features, workflows, calculations, payment-date recognition, YTD accumulation, reversals, and release decisions for statutory compliance risk. Use when a payroll change needs compliance-oriented supervision, release gating, exception handling, or explicit escalation instead of legal improvisation.
```

**After**

```text
Review payroll features, workflows, calculations, payment-date recognition, YTD accumulation, reversals, and release decisions for statutory compliance risk. Use when a payroll change needs compliance-oriented supervision, release gating, exception handling, or explicit escalation instead of legal improvisation, without treating the review as legal sign-off, formal certification, or implementation execution.
```

### 2. Tighten the overview

**Before**

```text
Review payroll product and engineering work for compliance-sensitive risk without pretending to provide legal sign-off.

Focus on payment recognition, annual wage attribution, YTD truthfulness, statutory bases, reversal handling, and release safety. Distinguish confirmed rule support from product inference, and escalate jurisdiction-specific uncertainty instead of guessing.
```

**After**

```text
Review payroll product and engineering work for compliance-sensitive risk without pretending to provide legal sign-off.

Focus on payment recognition, annual wage attribution, YTD truthfulness, statutory bases, reversal handling, and release safety. Distinguish confirmed rule support from product inference, and escalate jurisdiction-specific uncertainty instead of guessing.

Your job is to identify compliance-sensitive workflow risk, recommend the next operational action, and preserve uncertainty where statutory interpretation is unresolved. Your job is not to certify compliance, provide legal sign-off, or implement the fix directly.
```

### 3. Add a first-glance negative-boundary block after the overview

**Before**

```text
[no equivalent block]
```

**After**

```text
## WHAT THIS SKILL IS NOT

- Not a legal sign-off authority.
- Not a payroll compliance certifier.
- Not a replacement for jurisdiction-specific CPA or attorney review.
- Not an implementation executor.
- Not a blank-check approval gate that can override unresolved statutory ambiguity.
```

### 4. Strengthen the output-contract scope

**Before**

```text
Default response shape:

1. `Next course of action`
2. `Missing compliance items`
3. `Missing feature items`
4. `Urgency-ranked backlog`
5. `Assumptions and unknowns`
6. `Needs specialist escalation`
```

**After**

```text
Default response shape:

1. `Next course of action`
2. `Missing compliance items`
3. `Missing feature items`
4. `Urgency-ranked backlog`
5. `Assumptions and unknowns`
6. `Needs specialist escalation`

This output is a compliance-oriented review artifact. It does not by itself constitute legal sign-off, formal compliance certification, or implementation instructions unless the user explicitly asks for a different artifact.
```

### 5. Strengthen the final quality gate

**Before**

```text
- distinguish confirmed rules from assumptions
- identify whether payment-date recognition is explicit
- verify YTD and basis semantics are not ambiguous
- call out correction/reversal gaps if present
- preserve uncertainty instead of smoothing it away
- keep recommendations actionable for product and engineering follow-up
```

**After**

```text
- distinguish confirmed rules from assumptions
- identify whether payment-date recognition is explicit
- verify YTD and basis semantics are not ambiguous
- call out correction/reversal gaps if present
- preserve uncertainty instead of smoothing it away
- keep recommendations actionable for product and engineering follow-up
- confirm specialist-escalation boundaries were respected wherever statutory certainty was not available
```

## SCOPE BOUNDARY

- unchanged sections: `Required Inputs`, `Workflow`, `Rules`, `Escalation Rules`
- justification per unchanged section:
  - `Required Inputs`: already clear about what context should be gathered
  - `Workflow`: already ordered around compliance-sensitive facts and operational review
  - `Rules`: already encode important domain guardrails
  - `Escalation Rules`: already define the right triggers for specialist review

## GAP-CLOSURE TRAIL

- finding: the skill does not define its non-role explicitly enough at first glance
  changed lines or sections: frontmatter description, overview, new `WHAT THIS SKILL IS NOT` block
  before/after text: see `Tighten the frontmatter description`, `Tighten the overview`, and `Add a first-glance negative-boundary block after the overview`
  why this closes the gap: the role boundaries are now explicit before the reader reaches later escalation logic

- finding: compliance-oriented review and legal/compliance certification are not separated sharply enough near the top
  changed lines or sections: overview and new `WHAT THIS SKILL IS NOT` block
  before/after text: see `Tighten the overview` and `Add a first-glance negative-boundary block after the overview`
  why this closes the gap: the new wording states clearly that the skill reviews and escalates rather than certifies

- finding: the output contract does not clearly state what kind of artifact it is not
  changed lines or sections: `Output Contract`
  before/after text: see `Strengthen the output-contract scope`
  why this closes the gap: the output is now bounded as a review artifact rather than silently drifting into certification or implementation

- finding: the quality bar does not explicitly require escalation-boundary discipline
  changed lines or sections: `Quality Bar`
  before/after text: see `Strengthen the final quality gate`
  why this closes the gap: it turns avoidance of false statutory certainty into a required final check

## SIMULATED READER CHECK

- fastest likely interpretation: this skill reviews payroll changes for compliance-sensitive risk, recommends the next operational move, and escalates unresolved statutory questions instead of certifying compliance or signing off legally
- remaining misunderstanding risk: low
- revision needed: yes, because the live skill has not yet adopted these first-glance role and boundary clarifications

## COMPLETENESS DECLARATION

- All required output sections present: yes
- All findings have gap-closure trails: yes
- Simulated reader pass: PASS
- Scope boundary documented: yes
