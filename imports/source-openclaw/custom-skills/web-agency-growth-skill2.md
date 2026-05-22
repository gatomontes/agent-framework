## Pre-Flight Capability Assessment

**Do not begin Stage 0 without running this assessment.**

### Step 0.0: Reality Check

Answer these questions honestly before committing to a workflow:

| Question | If NO, degraded mode applies |
|----------|------------------------------|
| Does the client have >5,000 monthly sessions? | Use **Low-Traffic Protocol** (Bayesian, not frequentist) |
| Does the client have clean event tracking? | Use **Data Triage** before any audit |
| Does the team have a dedicated BI analyst? | Use **Simplified Metrics** (focus on one number) |
| Does the team have a CRO specialist? | Use **Heuristic Audit** instead of experimentation |
| Is client budget >$15K for this engagement? | Use **Solo Mode** (skip orchestration, focus on one lever) |

### Step 0.1: Capability Mapping

Map available *humans* (not personas) to roles:

| Actual Human | Can Execute | Cannot Execute |
|--------------|-------------|----------------|
| [Name] | [list roles] | [list gaps] |
| [Name] | ... | ... |

**If a role has no human and no budget to hire:**
- Do not simulate the role. Use the **Degraded Mode** for that function.
- Document the gap in the client's proposal.

### Step 0.2: Degraded Mode Selection

| Missing Role | Degraded Mode |
|--------------|---------------|
| No BI Analyst | Use spreadsheet-based LTV:CAC with 90% confidence = "educated guess" |
| No CRO Strategist | Use heuristic audit (CRO checklist) instead of experimentation |
| No Copywriter | Use client's existing copy + one headline A/B test |
| No Growth Engineer | Use no-code A/B tools (Google Optimize alternative) + manual instrumentation |
| No Project Manager | Use single-threaded owner (one person wears all hats — but set expectations) |

### Step 0.3: Kill Criteria (Pre-Engagement)

Do not take the engagement if:

- Client refuses to share analytics access
- Client budget is <$5K AND the ask is "full redesign with A/B testing" (impossible)
- Client expects guaranteed results ("You will 2X our revenue")
- Client cannot provide 2-4 hours per week for stakeholder feedback

**Ethical off-ramp template:**
> *"Based on our assessment, your budget does not align with the scope you've requested. Here is what we can deliver for $X. If that doesn't work, no hard feelings."*