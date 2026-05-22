---
name: project
description: Convert a vague request, reusable prompt, or ongoing session into a Bureau project with explicit routing. Use when the user says "make this a project", "turn this into a project", "formalize this as a project", "make this a Bureau project", or when you need to decide whether to answer directly, use one specialist, or route work across multiple workers with clear briefs, output contracts, and merge ownership.
---

> **Note:** This skill was copied from b-task (snapshot from 2026-04-05). Both skills are maintained in parallel. b-task remains for backward compatibility.
---

# Project

Turn messy or broad work into a Bureau-ready task plan.

This skill is the Bureau intake and routing layer for Projects (formerly B-Tasks). Use it to:
- normalize a request into a clear work order
- classify the real task type
- decide whether delegation is even necessary
- choose the execution shape
- write concise worker briefs
- define merge strategy and output contracts
- decide how much Sunshine critique the task deserves before execution

## Core principle

Do not delegate by reflex.
Choose the smallest useful shape.

## Canonical B-Task object

Represent the task in a compact tagged structure like this:

```xml
<b-task>
  <task>What needs to be done.</task>
  <goal>What success looks like.</goal>
  <context>Relevant background and prior decisions.</context>
  <constraints>What must be preserved, avoided, or optimized for.</constraints>
  <desired_output>The result shape the user wants.</desired_output>
  <classification>
    <primary>research</primary>
    <secondary>critique</secondary>
  </classification>
  <execution_shape>parallel-specialists</execution_shape>
  <workers>
    <worker name="Research">
      <why>Recurring-signal scan.</why>
      <brief>Find repeated problems, weak current solutions, and supporting evidence.</brief>
      <output_contract>5 findings with confidence and open questions.</output_contract>
    </worker>
    <worker name="Blackquill">
      <why>Attack weak opportunity logic.</why>
      <brief>Identify false positives, hype risk, and bad assumptions.</brief>
      <output_contract>Top 5 objections and what would kill the thesis.</output_contract>
    </worker>
  </workers>
  <merge>
    <owner>Vesper</owner>
    <mode>recommendation-plus-caveats</mode>
  </merge>
  <validation>
    <status>new</status>
    <sunshine_mode>full</sunshine_mode>
    <sunshine_sampling>1.0</sunshine_sampling>
    <reason>New task pattern with unproven routing.</reason>
    <promotion_rule>Promote after repeated clean runs with low correction need.</promotion_rule>
    <demotion_rule>Demote if routing shifts materially or outputs degrade.</demotion_rule>
  </validation>
</b-task>
```

This structure is primarily internal. Keep it compact, explicit, and operational.

## Worker model

Use these role families unless the user defines others:

- **Vesper** — orchestrates, judges, integrates, owns synthesis. Does not execute as a worker. Only routes, reviews, and merges. Vesper is the CEO, not the specialist.
- **Research** — gathers evidence, recurring signals, comparisons, references, and factual structure
- **Blackquill** — attacks reasoning, strategy, framing, hype, and weak assumptions
- **Conversion** — extracts audience language, framing, hooks, positioning, and persuasive clarity
- **Examiner** — checks correctness, consistency, completeness, edge cases, and testability
- **Builder** — produces or edits the actual artifact: code, file changes, structures, templates, or systems

### Boundary notes

- Use **Research** to gather and organize evidence.
- Use **Blackquill** to challenge logic and positioning.
- Use **Examiner** to verify reliability and catch omissions or contradictions.
- Use **Conversion** when the task needs better framing, messaging, or language fit.
- Use **Builder** when something concrete must be created or changed.

If two workers appear to overlap, choose the one with the clearer marginal value.

## Intake normalization

When the user invokes a Bureau task, normalize the request into these internal fields:

- **Task** — what needs to be done
- **Goal** — what success looks like
- **Context** — relevant known background
- **Constraints** — what to avoid, preserve, or optimize for
- **Desired Output** — what kind of result the user wants
- **Available Workers** — default to the Bureau worker model unless the user narrows it

If the request is already clear, do not ask redundant questions.
If critical routing information is missing, ask one high-leverage clarification question.

## Classification

Classify the task before routing. Common primary task types:

- research
- critique
- positioning
- conversion/copy
- validation/testing
- implementation/build
- memory/context recall
- orchestration/multi-step project
- strategy/decision support
- creative analysis
- operational design

Treat classification as a routing aid, not a labeling exercise.
Use it to answer:
- what kind of thinking dominates?
- what artifact or outcome must come out?
- what dependency structure exists between workers, if any?

You may note secondary task types if helpful, but do not overcomplicate classification.

## Routing decision order

Use this order before choosing workers:
1. What specialist shape fits this task? (Vesper routes, does not execute.)
2. What is the dominant task type?
3. Does one specialist clearly dominate the job?
4. If more than one worker is useful, are their contributions independent or dependent?
5. What output shape must be merged at the end?
6. What validation level does this task pattern deserve?

## Quota conservation

Vesper runs on the default model, which may be a scarce resource. Route tasks to specialists deliberately — do not use Vesper's session for work that belongs to Research, Blackquill, Conversion, Examiner, or Builder. Vesper's role is synthesis and judgment, not execution.

## Clarification policy

Ask one clarification question only if the missing answer would materially change:
- routing
- selected workers
- execution shape
- output contract
- the final deliverable form

Otherwise, state the most important assumptions and proceed.

## Execution shapes

Choose one of these:

### 1. Direct Response
Use when the task has low ambiguity, no meaningful decomposition benefit, and can be answered coherently in one pass.
Avoid delegation if specialists would mostly restate the same problem.

### 2. Single Specialist
Use when one competency clearly dominates the task and a second perspective is unlikely to change the answer materially.

### 3. Parallel Specialists
Use when the sub-questions are independent and can be merged later.
Avoid this shape if one worker's output is needed to frame another worker's mission.
Examples:
- Research finds evidence while Blackquill attacks weak assumptions.
- Conversion extracts audience language while Examiner checks evidence gaps.

### 4. Sequential Specialists
Use when later work depends on earlier findings, drafts, or structure.
Examples:
- Research first, then Blackquill critiques the findings.
- Builder drafts, then Examiner checks edge cases.

### 5. Hub-and-Spoke
Use when one main worker should produce the core output and one or two others should challenge, validate, or refine it.
Avoid this shape if every worker seems equally primary.

## Worker brief generation

For each selected worker, write a tight brief containing:
- mission
- scope
- what to ignore
- output format
- success condition

Keep briefs much smaller and sharper than the original request.
Do not paste giant generic prompt frameworks unless truly necessary.

## Output contracts

Each worker must return something mergeable.
A good output contract is:
- scoped
- bounded
- non-redundant
- shaped for later synthesis

Good patterns include:
- 5 bullet findings with confidence
- 3 strongest objections only
- top opportunity hypotheses
- missing evidence table
- file changes plus rationale
- ranked options with caveats

Prefer outputs that also note assumptions or open questions when relevant.
Avoid vague “thoughts” unless the user explicitly asked for open-ended exploration.

## Merge strategy

Before delegation, decide how outputs should come back together. Common merge modes:
- synthesized answer
- findings then judgment
- ranked options
- recommendation plus caveats
- consensus plus dissent

Make the merge shape explicit.
If worker outputs conflict, resolve the contradiction explicitly or surface it as decision-relevant dissent. Do not blur disagreement into false consensus.

## Validation and Sunshine review

Use the `<validation>` block to decide critique intensity before execution.
Tie review intensity to novelty, ambiguity, and execution cost. Higher-cost mistakes deserve stronger critique.

### Validation status
- `new` — task pattern is unproven or materially different from prior runs
- `emerging` — task pattern is partly proven but still benefits from review
- `verified` — task pattern is stable, repetitive, and low-drift

### Sunshine modes
- `full` — use for new, ambiguous, high-value, or architecture-shaping tasks
- `moderate` — use for emerging tasks or tasks with some risk but known structure
- `light` — use for verified tasks that still deserve sampled skepticism
- `skip` — use for trivial or well-proven repetitive tasks where review would add more ceremony than value

### Promotion and demotion
Use simple heuristics to reduce drift:
- Promote `new` to `emerging` after 2 to 3 runs with the same routing shape and only minor brief or merge corrections.
- Promote `emerging` to `verified` after repeated stable outcomes with low correction and no major Sunshine objections.
- Demote a task if worker roster, execution shape, or merge mode changes repeatedly in a short span, or if critique finds nontrivial structural misses again.

A verified repetitive task may use reduced Sunshine sampling, such as `0.2`, instead of constant full critique.

## Over-delegation check

Before finalizing the plan, ask internally:
- Is this task truly synthesis-only (judgment, merge, routing), or does it require specialist execution?
- Would one specialist be enough?
- Is each extra worker adding distinct marginal value?
- Are we adding pageantry instead of signal?
- If two workers do not have clearly different output contracts, should the plan collapse into one worker?

If the task needs execution (research, critique, building, validation), delegate to a specialist. Do not have Vesper do the work directly.

## Prompt conversion behavior

When the user says:
- "turn this prompt into a Bureau task"
- "make this a B-Task"
- "formalize this session as a B-Task"

Do not merely restate the prompt.
Convert it into:
- normalized intake
- task classification
- execution shape
- worker selection
- worker briefs
- output contracts
- merge strategy

## Output policy

Keep the tagged B-Task object primarily internal unless the user explicitly wants the structured object itself.
Default user-facing output should be a compact human-readable task plan.

### Minimum required output
- Task
- Goal
- Classification
- Execution Shape
- Worker Plan
- Merge Plan
- Validation
- Recommendation

### Optional output fields
- Context
- Constraints
- Assumptions
- full tagged object

Use optional fields only when they materially improve routing clarity or future reuse.

## Recommended output format

Use this structure unless the user asks for another shape:

### Bureau Task
- **Task**
- **Goal**
- **Classification**
- **Execution Shape**

### Worker Plan
For each worker:
- role
- why selected
- brief
- output contract

### Merge Plan
- owner
- merge mode

### Validation
- status
- sunshine mode
- sunshine sampling
- short reason

### Recommendation
- proceed as planned, simplify, or ask one clarification question

## Worked examples

### Example 1: skip delegation
Raw request: "Give me a blunt opinion on whether this pricing is too low."

Recommended shape:
- direct response

Why:
- single judgment task
- no decomposition benefit
- critique can be done directly by Vesper without Bureau ceremony

### Example 2: one specialist
Raw request: "Extract the strongest buyer language from these comments."

Recommended shape:
- single specialist: Conversion

Why:
- framing/language task
- no need for multiple workers unless the user also wants validation or critique

### Example 3: parallel
Raw request: "Find viable YouTube niche opportunities around cheque workflows and attack weak ones."

Recommended shape:
- parallel specialists: Research + Blackquill

Why:
- signal gathering and skeptical challenge can run independently
- Vesper merges into a recommendation with caveats

### Example 4: sequential
Raw request: "Draft a feature plan for a cheque SaaS, then stress-test edge cases."

Recommended shape:
- sequential specialists: Builder -> Examiner

Why:
- edge-case testing depends on the produced plan

### Example 5: trap case that should stay direct
Raw request: "Tell me whether this idea sounds promising, and be blunt."

Tempting but wrong shape:
- parallel specialists with Research and Blackquill

Better shape:
- direct response

Why:
- the user asked for judgment, not a tribunal
- delegation would likely add ceremony before value

### Example 6: trap case that looks parallel but needs sequence
Raw request: "Find the best YouTube audience language for this niche, then test whether that language hides weak assumptions."

Tempting but wrong shape:
- parallel Conversion + Blackquill

Better shape:
- sequential specialists: Conversion -> Blackquill

Why:
- Blackquill needs the extracted language before attacking it

## Tone

Keep orchestration practical, compact, and unsentimental.
The point is to get better work with less drift.
