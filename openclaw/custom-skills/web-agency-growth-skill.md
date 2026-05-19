# OpenClaw Skill: Web Agency Growth Engine (Design + Redesign)

## Skill Metadata

| Property | Value |
|----------|-------|
| Skill ID | WA-GROWTH-01 |
| Version | 1.0 |
| Last Updated | 2026-04-09 |
| Trigger | "build a cash-printing website", "redesign for conversions", "growth audit", "new site from scratch" |
| Dependencies | BI Analyst, CRO Strategist, Direct-Response Copywriter, Growth Engineer, Project Manager |
| Output | Production-ready, validated website with instrumentation and experiment framework |

---

## Skill Overview

This skill orchestrates a multi-persona workflow to build or rebuild websites that function as **conversion-first revenue engines**. It applies to:

- **Greenfield (Design from Zero):** No existing site, no baseline data. Start with market research, competitor analysis, and conversion-first wireframes.
- **Brownfield (Redesign):** Existing site with data. Start with audit, leak detection, and hypothesis-driven experimentation.

The workflow is non-linear but follows a logical sequence: **Diagnose → Hypothesize → Persuade → Execute → Validate → Scale**.

---

## Persona Roles & Responsibilities

| Persona | Role in This Skill |
|---------|---------------------|
| **BI Analyst (The Auditor)** | Data audit, leakage quantification, LTV:CAC calculation, revenue reconciliation, scaling signal |
| **CRO Strategist** | Hypothesis formation, heatmap/session analysis, A/B test design, experiment validation |
| **Direct-Response Copywriter** | Psychological messaging, headline/CTA architecture, objection handling, offer stacking |
| **Growth Engineer** | Technical implementation, feature flags, instrumentation, performance optimization |
| **Project Manager** | Workflow orchestration, stakeholder signoff, timeline management |

---

## Workflow: Greenfield (Design from Zero)

*Use this path when there is no existing website or no meaningful traffic data.*

### Stage 0: Market & Competitor Research (BI + CRO)

**BI Analyst:**
- Identify 5-10 direct competitors. Pull traffic estimates, pricing models, and funnel structures.
- Calculate industry benchmark conversion rates (by vertical: ecomm, SaaS, lead gen).
- Define target LTV:CAC ratio (minimum 3:1 for profitability).

**CRO Strategist:**
- Analyze competitor funnels. Map their checkout flows, upsell sequences, and form fields.
- Conduct 5-7 user interviews with target audience. Identify top 3 objections and top 3 desires.
- Create a baseline hypothesis: *"A new site in this vertical should convert at X% based on competitor averages and user expectations."*

**Output:** Market benchmark report + user objection list + target conversion baseline.

---

### Stage 1: Conversion-First Wireframing (CRO + Copywriter)

**CRO Strategist:**
- Design wireframes for key pages: Homepage, Product/Landing, Checkout/Cart, Thank You/Upsell.
- Apply CRO heuristics: F-pattern layout, friction audits (minimize fields/click), mobile-first.
- Flag placement for social proof, trust badges, guarantee, and risk reversal.

**Direct-Response Copywriter:**
- Draft headline frameworks for each page before visual design begins.
- Write objection-handling sections: FAQs, guarantees, comparison tables.
- Define primary CTA and 2-3 secondary CTAs per page.

**Output:** Wireframes with copy placeholders + headline library + CTA hierarchy.

---

### Stage 2: Technical Architecture (Growth Engineer)

**Growth Engineer:**
- Select stack optimized for conversion speed: sub-200ms Time to First Byte, sub-1.5s Largest Contentful Paint.
- Implement feature flag system from day zero (for future A/B tests).
- Build instrumentation layer: track all events (pageview, click, form start, form submit, checkout initiation, payment success).
- Set up server-side event validation to prevent tracking pollution.

**Output:** Deployed staging environment + instrumentation schema + feature flag infrastructure.

---

### Stage 3: Copy & Creative Production (Copywriter + CRO)

**Direct-Response Copywriter:**
- Expand headlines into full page copy. Write for skimmers (subheads, bullets, bold) and readers (story, detail).
- Draft 5-7 testimonials (if real customers exist) or placeholder structure for future collection.
- Write email follow-up sequence: abandoned cart, post-purchase, winback.

**CRO Strategist:**
- Review copy against friction principles. Remove jargon, passive voice, and weak CTAs.
- Test headline variations on a small audience (paid social or early access list) before full build.

**Output:** Production-ready copy + email sequence drafts + headline test results.

---

### Stage 4: Build & Instrumentation (Growth Engineer)

**Growth Engineer:**
- Implement all pages with performance budgets enforced.
- Deploy event tracking: every button, form field, and navigation click is instrumented.
- Set up A/B testing framework (server-side preferred) with kill switches.
- Implement multi-tenant architecture (if applicable) with tenant-specific flag overrides.

**Output:** Production build + instrumentation validation report + A/A test confirming tool accuracy.

---

### Stage 5: Pre-Launch Validation (CRO + BI)

**CRO Strategist:**
- Run usability tests with 5-8 target users. Record sessions. Identify confusion points.
- Run an A/A test (same page vs. itself) to confirm experimentation tool has <5% false positive rate.
- Soft-launch to 5-10% of traffic (or beta users). Monitor conversion and anomaly detection.

**BI Analyst:**
- Validate instrumentation: all events fire correctly, no duplicate or missing data.
- Set up baseline dashboards: conversion funnel, LTV:CAC tracking, cohort retention.
- Configure alerts for data freshness, volume anomalies, and reconciliation failures.

**Output:** Usability test recordings + A/A test confirmation + baseline dashboards + launch go/no-go.

---

### Stage 6: Launch & Scale (All Personas)

**Project Manager:** Coordinates launch window and rollback plan.

**Growth Engineer:** Monitors performance (Core Web Vitals) and error rates.

**CRO Strategist:** Begins first experiment post-launch (typically pricing or CTA test).

**BI Analyst:** Tracks actual vs. benchmark conversion. Signals when to scale traffic.

**Output:** Live site + first experiment running + scaling trigger defined (e.g., "at 500 conversions, increase ad spend 20%").

---

## Workflow: Brownfield (Redesign of Existing Site)

*Use this path when an existing site has traffic data and historical performance.*

### Stage 0: Data Audit & Leak Detection (BI + CRO)

**BI Analyst:**
- Pull 6-12 months of conversion data by channel, device, and segment.
- Calculate drop-off rates at each funnel step. Identify the single biggest leakage point.
- Run cohort analysis: does conversion decline after week 1? Is retention the problem, not acquisition?
- Reconcile analytics data against payment processor data. Flag any discrepancies.

**CRO Strategist:**
- Deploy heatmaps and session recordings (if not already present). Watch 50-100 sessions.
- Identify specific friction points: confusing UI elements, unexpected costs, form abandonment at specific fields.
- Quantify the opportunity: *"Fixing the payment step drop-off from 60% to 40% would increase revenue by 33%."*

**Output:** Leakage report with quantified opportunity + session recording highlights + heatmap screenshots.

---

### Stage 1: Hypothesis Formation (CRO + Copywriter)

**CRO Strategist:**
- Write falsifiable hypotheses for each leakage point:

> *"If we move shipping cost display to the cart page (currently at payment), then checkout completion will increase by 15% because users abandon when surprised by costs."*

- Prioritize hypotheses by potential impact vs. implementation effort (PIE framework or ICE scoring).

**Direct-Response Copywriter:**
- Review existing copy at leakage points. Identify weak headlines, buried benefits, missing objection handling.
- Draft challenger copy: stronger guarantees, more specific proof, urgent but honest CTAs.

**Output:** Ranked hypothesis backlog + challenger copy drafts.

---

### Stage 2: Experiment Design (CRO + Growth Engineer)

**CRO Strategist:**
- Define success metrics (primary + guardrail metrics).
- Calculate required sample size for statistical significance (95% confidence, 80% power).
- Determine test duration (minimum 1-2 full business cycles to avoid day-of-week bias).

**Growth Engineer:**
- Implement challenger variant behind a feature flag.
- Ensure instrumentation captures both control and variant events with consistent naming.
- Set up automated result calculation (daily lift, confidence intervals).

**Output:** Experiment plan + feature flag deployed + sample size calculation.

---

### Stage 3: Test Execution (All Personas)

**CRO Strategist:**
- Ramp traffic: 50/50 split or lower if risk is high.
- Monitor early data for extreme negative impact (kill switch threshold: e.g., >10% drop at 95% confidence).
- Do NOT peek and declare winners early.

**BI Analyst:**
- Run daily data quality checks. Ensure no tracking errors or pipeline delays.
- Alert team if experiment data diverges from baseline reconciliation.

**Copywriter:** (Standing by) Prepares additional copy variants if initial test is inconclusive.

**Output:** Running experiment + daily monitoring logs + data quality pass/fail.

---

### Stage 4: Analysis & Decision (CRO + BI)

**CRO Strategist (after planned sample size reached):**
- Calculate lift, confidence intervals, p-value, practical significance.
- Analyze by segment: mobile vs. desktop, new vs. returning, traffic source.
- Make decision: **Implement** (stat sig win), **Iterate** (inconclusive), **Kill** (stat sig loss), **Retest** (low power).

**BI Analyst:**
- Validate that segment differences are statistically robust (not overfitting).
- Check guardrail metrics: did retention, support tickets, or refunds change?
- Sign off on revenue impact calculation.

**Output:** Experiment readout + decision + segment analysis + guardrail check.

---

### Stage 5: Rollout or Rollback (Growth Engineer)

**Growth Engineer (if Implement):**
- Remove feature flag, make challenger the new control.
- Clean up dead flag code.
- Update instrumentation if event names changed.

**Growth Engineer (if Kill):**
- Immediately remove challenger flag. Revert to control.
- Document negative result in experiment library.

**Output:** Production deployment + flag cleanup + experiment library update.

---

### Stage 6: Scaling & Next Experiment (BI + CRO)

**BI Analyst:**
- Reconcile reported lift against actual revenue movement over 2-4 weeks.
- Update LTV:CAC calculations if conversion improvements changed customer quality.
- Signal when to increase ad spend: *"The site now converts at X%. You can spend up to Y per acquisition."*

**CRO Strategist:**
- Move to next hypothesis in backlog.
- Maintain experiment velocity: one test every 1-2 weeks minimum.

**Output:** Revenue reconciliation + scaling signal + next experiment queued.

---

## Combined Workflow Diagram (Text)
