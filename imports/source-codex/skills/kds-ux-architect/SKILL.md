---
name: kds-ux-architect
description: Design and review high-reliability, low-latency kitchen display system (KDS) interfaces for commercial food production. Use when Codex needs to create, critique, or refine ticket layouts, station workflows, bump interactions, routing views, SLA timers, or touchscreen ergonomics for fast kitchen environments where glanceability, error prevention, and greasy-hand usability matter.
---

# KDS UX Architect

## Overview

Design for speed, stress, and imperfect conditions. Favor decisions that reduce cognitive load, survive heat, glare, and messy input, and help a station complete the next correct action with minimal reading.

Use this skill for both net-new design and review work. Apply it to mockups, HTML/CSS prototypes, product specs, workflow maps, UX audits, or implementation plans for restaurant kitchen display systems.

Apply calibrated rigor based on stakes:
- For exploratory layouts or internal drafts, move quickly and state assumptions.
- For production, high-volume, or failure-sensitive kitchen flows, slow down, state confidence, and make risks explicit before recommending irreversible interaction patterns.

## Workflow

1. Identify the kitchen reality and operating stakes before designing.
2. State assumptions and confidence when the station context is incomplete.
3. Structure the ticket so the next action is obvious at a glance.
4. Choose interaction patterns that tolerate accidental or imprecise input.
5. Validate station-specific visibility so each role sees the right amount of information.
6. Review the design against timing, error-prevention, and environmental stress.

## Risk And Confidence

Before proposing major layout or workflow changes, decide:
- `risk_level`: `low`, `medium`, or `high`
- `confidence`: `high`, `medium`, or `low`

Use these rules:
- `low`: internal concept work, reversible layout experiments, low-volume scenarios
- `medium`: realistic service flow changes with moderate operational consequence
- `high`: production KDS changes that could cause missed items, remakes, routing failures, or service collapse under rush conditions

If confidence is not high:
- label the missing context
- state the assumption you are making
- avoid presenting speculative decisions as settled best practice

If risk is high:
- explain why the recommendation is safe enough to trial
- call out any interaction that should be prototyped or validated before rollout

## Model The Kitchen Reality

Capture the operating context before proposing UI changes.

Check these constraints first:
- Focus window: Assume about 0.8 seconds of focused vision. Optimize for glanceability, not prolonged reading.
- Input precision: Assume taps come from knuckles, greasy fingers, or accidental forearm contact. Avoid tiny targets and precision gestures.
- Lighting: Expect glare, heat lamps, reflections, and uneven brightness. Use strong contrast and avoid fragile low-contrast states.
- Pace: Expect split attention, interruptions, batching, and multitasking under time pressure.
- Consequence of error: Weight mistakes by kitchen impact. An accidental bump or hidden modifier can waste food, stall service, or force remakes.

When requirements are incomplete, infer and state the likely station context:
- Grill, fry, expo, pantry, and plating stations need different default visibility.
- High-volume lines prioritize scan speed and queue triage.
- Fine-dining or modifier-heavy flows may justify more context, but never at the expense of immediate actionability.

## Structure Tickets With The Pyramid

Organize information in strict visual priority. The goal is to let cooks identify what to make, how to make it, who it belongs to, and how urgent it is without searching.

### Layer 1: Critical

Show the primary production target first.
- Put the item name in the most prominent position.
- Use the largest type and strongest contrast.
- Keep it fixed and easy to parse from a distance.
- Example: `BURGER`

### Layer 2: Modifier

Show how the item must change.
- Surface modifiers directly beneath or adjacent to the item.
- Use condensed but still highly legible typography.
- Highlight dangerous or easy-to-miss changes first.
- Examples: `NO ONION`, `MED RARE`, `ALLERGY`, `SAUCE ON SIDE`

### Layer 3: Context

Show supporting service details without competing with production content.
- Include table, seat, server, order source, or course only when it changes behavior.
- De-emphasize visually, but keep it available.
- Example: `Table 42`, `Seat 3`, `Server: J. Smith`

### Layer 4: Meta

Communicate urgency through visuals first.
- Prefer elapsed-time bars, rings, or color transitions over timer text as the primary signal.
- Use text time only as secondary support when needed.
- Make SLA status readable in peripheral vision.

## Design For Glanceability

Favor patterns that answer these questions instantly:
- What is the next item to act on?
- What is unusual about it?
- Is it late?
- Is it mine?

Apply these rules:
- Keep the number of competing colors low and assign each color a single operational meaning.
- Avoid decorative icons unless they replace reading with faster recognition.
- Keep dense modifier blocks visually chunked.
- Preserve stable placement for core information so eyes learn where to look.
- Avoid long horizontal scans across the ticket.

If a layout looks attractive but increases scan time, reject it.

## Design For Zero-Precision Touch

Assume accidental input is common and expensive.

Use these interaction rules:
- Make primary tap areas large enough for imprecise contact.
- Separate destructive actions from routine actions.
- Require confirmation for high-cost actions such as full-ticket closure or recall.
- Do not rely on hover, tiny icons, or subtle affordances.
- Prefer single-purpose controls over overloaded gestures in high-pressure flows.

For OpenClaw-style workflows, preserve these defaults:
- Single bump: Remove one specific item from a multi-item ticket.
- Full ticket recall: Require swipe plus confirmation, or an equally deliberate multi-step action.

When proposing alternatives, explain how they protect against orphaned sides, accidental closes, and hidden dependencies.

## Validate Station-Specific Views

Not every station should see the full ticket in the same way.

Design masking and routing around role clarity:
- Show cooks the instructions they must execute directly.
- Show dependent prep tasks as dependency flags when another station owns the work.
- Hide irrelevant detail that slows decisions.
- Preserve enough shared context to coordinate timing across stations.

Use station-specific review questions:
- Does grill see only grill work plus the dependencies that affect firing?
- Does fry see prep dependencies without mistaking them for direct cook instructions?
- Does expo get the broadest coordination view?
- Can users switch between `show all` and `show my station only` without losing orientation?

## Use Functional Visual Language

Choose color and typography for operational signaling, not branding.

Recommended visual direction:
- Background: deep neutral dark surfaces that reduce glare.
- Primary text: very high luminance contrast.
- Critical alert: red reserved for SLA violation or severe blocking issues.
- Caution alert: amber for approaching thresholds.
- Ready/completed: green for completed or cleared states.
- Modifier typography: tall, legible faces with strong differentiation between similar characters.

Prefer system choices that reinforce function:
- Reserve boldest emphasis for item identity and urgent exceptions.
- Keep modifier styling readable under stress.
- Use motion sparingly and only to direct attention to newly urgent change.

## Review Checklist

Before finalizing a design, verify:
- Risk level and confidence are stated when context is incomplete or rollout stakes are high.
- The next required action is obvious within a glance.
- Critical modifiers cannot be mistaken for secondary context.
- Ticket urgency is visible without reading numeric timers.
- Hit targets tolerate messy, imprecise touch.
- Accidental destructive actions are hard to trigger.
- Each station sees an appropriate subset of information.
- Contrast remains readable under glare and uneven lighting.
- The interface reduces, rather than increases, cognitive load during rush periods.

## Output Expectations

When asked to design or review a KDS experience:
- Start with `RISK LEVEL` and `CONFIDENCE` when the recommendation affects live operations or the context is incomplete.
- State the assumed kitchen context and station roles.
- Identify the primary risks to speed or accuracy.
- Recommend a ticket hierarchy using critical, modifier, context, and meta layers.
- Specify bump and recall behavior with explicit error-prevention measures.
- Call out station masking rules.
- Suggest concrete UI changes in implementation-ready terms when possible.

When reviewing existing UI, prioritize operational failures over visual polish.

## Escalation Rules

Pause and call out the issue when:
- station ownership is unclear enough that masking or routing advice would be speculative
- the proposed interaction could create irreversible operational risk without validation
- the design depends on policy, staffing, or routing decisions that sit above screen design
- critical timing, modifier, or recall behavior is not specified

When the gap is minor and the change is reversible, proceed with labeled assumptions.
