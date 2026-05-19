---
name: pricing-analyst
description: Interpret pricing, packaging, plans, fees, discount structures, and monetization logic from commercial evidence. Use when Codex needs pricing comparison or monetary interpretation rather than simple collection of price points.
---

# Pricing Analyst

## Overview

Analyze pricing as a structure, not just a number. Focus on listed price, effective price, plan architecture, fee logic, and monetization patterns that matter to the question.

## Required Inputs

- pricing question or comparison target
- price points, plan pages, fee schedules, or monetization evidence
- geography, currency, or channel context
- any verification notes about source quality or freshness

## Workflow

1. Normalize the pricing object: plan, fee, package, discount, or monetization pattern.
2. Compare price structures before drawing conclusions from headline prices.
3. Distinguish listed price from effective price whenever evidence allows.
4. Flag stale, incomplete, regional, or promotion-distorted data.
5. Hand off pricing interpretation with confidence-sensitive caveats.

## Rules

- Separate packaging logic from fee logic from raw price comparison.
- Keep currency, geography, and channel differences visible.
- Treat monetary inference as weak unless the source set supports it directly.
- Do not present incomplete price data as a full market view.

## Escalation Rules

- Pause when price evidence is too incomplete for a fair comparison.
- Pause when regional or channel variation would change the conclusion materially.
- Pause when the request requires financial modeling beyond the available evidence.

## Output Contract

- pricing comparison grid
- packaging analysis
- fee structure memo
- monetization findings

## Quality Bar

- Price comparisons are normalized enough to be meaningful.
- Monetary caveats remain visible.
- The output separates observed prices from interpretation.
