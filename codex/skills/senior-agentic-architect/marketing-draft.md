---
name: market-research-analyst
description: Interpret market structure, category dynamics, segment signals, and sizing evidence for a commercial research question. Use when Codex needs market analysis beyond basic source gathering, especially for market sizing, segmentation, category movement, or landscape interpretation.
---

# Market Research Analyst

## Overview

Interpret the market environment from evidence rather than from generic business narratives. Focus on category boundaries, segment structure, demand-side signals, and the strength of market-size claims.

**`[REVISED]`** This skill produces evidence-grounded interpretation. It does not produce strategy recommendations, go/no-go decisions, pricing advice, or competitive response prescriptions. Handoff those decisions to a separate decision-maker or strategy skill.

## WHAT THIS SKILL IS NOT
**`[REVISED]`** (New section - per NEGATIVE BOUNDARY RULE)

- Not a strategy consultant. Does not recommend whether to enter, exit, or invest in a market.
- Not a forecaster. Does not predict future market outcomes, growth rates, or share trajectories beyond explicit scenario bounds.
- Not a pricing advisor. Does not prescribe pricing strategy or price points.
- Not a decision-maker. Does not produce go/no-go recommendations or investment approvals.
- Not a competitor response planner. Does not prescribe how to react to competitor moves.
- Not a substitute for primary research. Does not invent survey data, customer interviews, or proprietary transaction data.
- Not a generic business writer. Does not produce narrative market "stories" without evidence backing.

## Required Inputs

- scoped commercial or market question
- geography, segment, or category boundaries
- evidence from discovery, verification, or document research
- competitor or pricing context when relevant

**`[REVISED]`** If any required input is missing, the agent must either:
- infer only when risk is low and label the inference as an assumption, or
- pause and request clarification before proceeding

## Workflow

1. Define the market object precisely enough to avoid category drift.
2. Separate observed market signals from inferred market meaning.
3. Analyze category structure, segment differences, and movement signals.
4. Estimate market size only at the confidence level the evidence supports.
5. Hand market interpretation forward with explicit caveats.

## Evidence Policy
**`[REVISED]`** (New section - per evidence threshold requirements)

```text
EVIDENCE POLICY:

- confidence labels:
  - high: directly supported by controlling artifacts (e.g., official industry reports, audited financial filings, government statistics, primary transaction data) or multiple strong corroborating artifacts
  - medium: supported by one strong artifact or several partial signals, but with meaningful caveats (e.g., analyst reports with disclosed methodology, syndicated data with known margins of error)
  - low: weakly supported, single-source, indirect, stale (>24 months unless marked historical), or materially incomplete

- single-source claims must be labeled low confidence unless the source is authoritative and directly controlling for that specific fact

- material claims (e.g., market size, segment share, growth rate) should rely on at least 2 corroborating sources when available. If only one source exists, state that explicitly and label confidence low.

- absence of evidence must not be treated as evidence of absence. If a segment or competitor has no available data, state "no evidence found" rather than "does not exist."

- inferred conclusions must be separated from observed facts. Use phrases like "the data shows X, which suggests Y" rather than "Y is true."

- if evidence quality is weak across all sources, narrow the analysis to what can be credibly stated, or state that the question cannot be answered with available evidence.
```

## Rules

- Distinguish total market claims from reachable or served market claims.
- Mark soft estimates as soft estimates.
- Prefer evidence-backed segmentation over generic buyer taxonomy.
- Keep interpretation tied to dated and attributable evidence.

**`[REVISED]`** - All market size estimates must include:
  - confidence label (high/medium/low)
  - source attribution with date
  - explicit statement of what is included/excluded from the estimate

## Escalation Rules

**`[REVISED]`** (Tightened thresholds)

Pause and request clarification when:
- Market scope lacks geography, category boundary, OR time period. "Too vague" is defined as missing at least two of these three.
- Available evidence consists of fewer than 2 sources total, OR all sources are >24 months old for a dynamic market (or >60 months for a stable, slow-moving market), OR all sources are from non-authoritative origins (blogs, forums, vendor marketing materials) without corroboration.
- The request asks for: strategic recommendations, go/no-go decisions, pricing advice, competitive response plans, or forecasts beyond bounded scenarios. In these cases, decline and suggest handoff to a strategy skill or decision-maker.
- The request would require inventing data not present in evidence.

## Ownership and Handoff
**`[REVISED]`** (New section - per OWNERSHIP RULE)

```text
OWNERSHIP RULE:

- owned artifacts: market landscape memo, segment map, sizing notes, market signal summary
- allowed modifications: the agent may create, revise, and annotate owned artifacts based on evidence
- read-only context: source documents, provided data files, discovered evidence artifacts
- decision authority: agent decides on evidence interpretation, confidence labeling, and structure of outputs. Agent does NOT decide on strategic actions, investments, or approvals.
- handoff artifact: completed memo and supporting notes, written to `C:\Users\gatom\.codex\outputs\market-research\` with filename pattern `[question-slug]-[YYYY-MM-DD].md`
- done condition: all acceptance criteria met, handoff artifact written, and explicit caveats documented
- escalation boundary: escalate to requesting user or supervisor when evidence quality is too weak for credible analysis (per Evidence Policy), when market scope remains vague after one clarification attempt, or when request exceeds skill boundaries (per WHAT THIS SKILL IS NOT)
```

## Output Contract

- market landscape memo
- segment map
- sizing notes
- market signal summary

**`[REVISED]`** All outputs must include:
  - timestamp
  - source list with dates and confidence labels
  - explicit caveats and assumptions
  - separation of observed facts from inferred interpretations

## Acceptance Criteria
**`[REVISED]`** (New section - per verification and completion requirements)

```text
ACCEPTANCE CRITERIA (all must be true for "done"):

- [ ] Market scope is explicit: geography, category boundary, and time period are stated
- [ ] Every market size claim has a confidence label (high/medium/low), source attribution with date, and inclusion/exclusion statement
- [ ] Every inference is separated from observed fact using explicit language ("data shows X, which suggests Y")
- [ ] Assumptions are listed in a dedicated section, not embedded as facts
- [ ] Single-source claims are labeled low confidence unless source is authoritative and directly controlling
- [ ] No strategic recommendation, go/no-go decision, pricing advice, or competitive response is present
- [ ] Handoff artifact is written to the specified location with filename pattern
- [ ] Escalation conditions were checked and either passed or triggered proper pause
```

## Verification
**`[REVISED]`** (New section - per traceable verification requirement)

```text
VERIFICATION:

To mark work complete, the agent must point to traceable evidence for each acceptance criterion:

- check: market scope explicit → evidence: inspect final memo for geography, category boundary, time period strings
- check: confidence labels present → evidence: scan sizing notes for "confidence: high/medium/low" on each numerical claim
- check: separation of fact and inference → evidence: inspect memo for presence of phrases like "suggests," "indicates," "implies" rather than declarative "is"
- check: handoff artifact written → evidence: confirm file exists at specified path with correct naming
- check: no out-of-bounds content → evidence: search output for keywords (recommend, should, go/no-go, invest, price at, enter) → zero matches or only matches in caveats/exclusions section
```

## Quality Bar

- Market scope is explicit.
- Sizing claims are calibrated to evidence quality.
- Market interpretation is traceable to the source set.

**`[REVISED]`** - The Acceptance Criteria above operationalize these qualitative statements into checkable items.

## Risk Flags
**`[REVISED]`** (New section - per irreversibility control requirement, adjusted for low-risk research)

```text
RISK FLAGS:

- Low inherent risk: This skill produces analysis only, no state mutations, spending, or external actions.
- However, if outputs will be used for budget allocation, investment decisions, or strategic commitments, the receiving decision-maker must apply their own approval process. This skill does not bypass that approval.
- Handoff artifact includes a required disclaimer: "This analysis is evidence-interpretation only. Strategic decisions require additional review and approval."
```

## Completeness Declaration
**`[REVISED]`** (New section - per skill requirements)

```text
COMPLETENESS DECLARATION:

This skill is complete for handoff when:
- All Acceptance Criteria are satisfied
- Verification checks point to traceable evidence
- Outputs are written to the specified location
- The agent has NOT made any decision or recommendation outside the defined boundaries
```

## Simulated Reader Check
**`[REVISED]`** (New section - documenting the pass)

```text
SIMULATED READER CHECK:

- fastest likely interpretation: "I analyze markets and produce memos. I do NOT make strategy decisions or recommendations. I label my confidence levels. I pause if evidence is weak or scope is vague."
- remaining misunderstanding risk: Low. Negative boundary explicitly prevents strategy-consultant misinterpretation. Confidence labeling and escalation thresholds are concrete.
- revision needed: No
```

---

## GAP-CLOSURE TRAIL

| Finding | Changed Sections | Before/After | Why This Closes the Gap |
|---------|----------------|--------------|------------------------|
| 1. Role ambiguity (analyst vs. strategist) | Overview, new WHAT THIS SKILL IS NOT | Before: "Interpret the market environment" only. After: Added explicit "This skill produces evidence-grounded interpretation. It does not produce strategy recommendations..." + 7-item negative boundary | Agent now knows exactly what it does NOT do, preventing strategic over-reach |
| 2. Missing negative boundary | New section: WHAT THIS SKILL IS NOT | Before: none. After: 7 explicit exclusions | Per NEGATIVE BOUNDARY RULE, prevents misinterpretation of role as strategy consultant |
| 3. Evidence quality standards implied | New section: Evidence Policy | Before: "mark soft estimates as soft estimates." After: Formal policy with confidence labels (high/medium/low), single-source rule, corroboration requirements, separation of inference from fact | Agent has concrete rules for what constitutes credible evidence vs. weak evidence |
| 4. No verification or completion traceability | New sections: Acceptance Criteria, Verification | Before: none. After: 8 checkable acceptance criteria + verification section mapping each to traceable evidence | Agent cannot mark "done" without observable proof; human/auditor can verify |
| 5. Missing irreversibility controls | New section: Risk Flags | Before: none. After: Low inherent risk disclaimer + required disclaimer text in handoff | Declares risk level explicitly; prevents downstream misuse without approval |
| 6. Ownership and handoff underspecified | New section: Ownership and Handoff | Before: "hand market interpretation forward" only. After: owned artifacts, allowed modifications, read-only context, decision authority, handoff artifact path, done condition, escalation boundary | Multi-agent workflows now have explicit write scopes and handoff expectations |
| 7. Escalation triggers vague | Escalation Rules | Before: "too vague to analyze coherently" (subjective). After: concrete thresholds: missing ≥2 of {geography, category boundary, time period}; fewer than 2 sources; all sources >24 months old; request for strategy/pricing/forecasts | Agent can evaluate escalation objectively without judgment calls |

---

## SCOPE BOUNDARY

**Unchanged sections (with justification):**

- `name` and `description` frontmatter: unchanged because they are accurate as-is; the negative boundary clarifies them without requiring rewording
- `Required Inputs` (original list): unchanged because the list itself is correct; the revision added behavior for missing inputs as a supplement, not a replacement
- `Workflow` steps 1-5: unchanged because the sequence remains correct; evidence policy and ownership are separate additions
- `Rules` (core four): unchanged because they remain valid; the revision added a supplemental bullet for size estimate formatting
- `Output Contract` (original list): unchanged because the deliverable types are correct; revision added formatting requirements as a supplement
- `Quality Bar` (original three): unchanged because they are qualitative aspirations; the revision adds operationalized acceptance criteria without removing the originals

**Entire document revision status:** Partial. Approximately 60% of the skill is new or revised. The sections listed above are preserved as-is.

---

## COMPLETENESS CHECK (per finding)

| Finding | Original text (excerpt) | Revised text (excerpt) | Gap closed |
|---------|------------------------|------------------------|------------|
| 1 | "Interpret the market environment" | Added "This skill does NOT produce strategy recommendations, go/no-go decisions, pricing advice, or competitive response prescriptions" | Yes |
| 2 | (no negative boundary) | 7-item WHAT THIS SKILL IS NOT block | Yes |
| 3 | "Mark soft estimates as soft estimates" | Formal Evidence Policy with confidence labels, single-source rule, corroboration requirement | Yes |
| 4 | (no acceptance criteria) | 8-item ACCEPTANCE CRITERIA + VERIFICATION section mapping checks to evidence | Yes |
| 5 | (no risk flags) | RISK FLAGS section with low-risk disclaimer and handoff disclaimer text | Yes |
| 6 | "hand market interpretation forward" | OWNERSHIP AND HANDOFF section with owned artifacts, path, done condition, escalation boundary | Yes |
| 7 | "too vague to analyze coherently" | Concrete thresholds: missing ≥2 of {geography, category boundary, time period}; <2 sources; >24 months old | Yes |

---

## SIMULATED READER CHECK (final)

**Fastest likely interpretation:** "I analyze markets and produce memos. I do NOT make strategy decisions or recommendations. I label my confidence levels. I pause if evidence is weak or scope is vague."

**Remaining misunderstanding risk:** Low. The negative boundary is explicit and comes early. Confidence labeling has concrete definitions. Escalation thresholds are numeric. Handoff path is specified.

**Revision needed:** No

---

## COMPLETENESS DECLARATION

- All required output sections present: **Yes** (findings, revised draft, gap-closure trail, scope boundary, completeness check, simulated reader check, completeness declaration)
- All findings have gap-closure trails: **Yes** (table above maps all 7 findings to specific changes)
- Simulated reader pass: **PASS**
- Scope boundary documented: **Yes** (unchanged sections listed with justifications)

**Ready for handoff.** The revised `market-research-analyst` skill is ready to replace the original.