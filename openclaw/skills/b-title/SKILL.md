---
name: b-title
description: Convert a song theme, emotional premise, lyrical concept, or partial idea into a Bureau title-ideation task with explicit lanes, worker selection, evaluation criteria, and shortlist logic. Use when the user wants song titles, title shortlists, title comparisons, or says things like "find me a b-title for a song about this" or "turn this song idea into title candidates."
---

# B-Title

Turn a song idea into a Bureau-native title ideation task.

This skill is for title generation, title comparison, and title shortlisting.
Use it when the user has:
- a theme
- a lyrical premise
- a story fragment
- an emotional concept
- a POV uncertainty
- a stylistic lane
and wants strong title candidates instead of a full lyric yet.

## Core principle

Do not confuse title generation with full songwriting.
A title task should stay focused on naming, framing, memorability, emotional force, and lane selection.

## Canonical B-Title object

Represent the task in a compact tagged structure like this:

```xml
<b-title>
  <theme>Core emotional and narrative premise.</theme>
  <goal>Find strong song title candidates.</goal>
  <context>Genre lane, POV uncertainty, references, constraints.</context>
  <constraints>What to avoid, preserve, or emphasize.</constraints>
  <desired_output>Title candidates, shortlist, ranking, and lane judgment.</desired_output>
  <classification>
    <primary>title-ideation</primary>
    <secondary>creative-analysis</secondary>
  </classification>
  <execution_shape>hub-and-spoke</execution_shape>
  <lanes>
    <lane name="direct-address">Speaker addressing "you" directly.</lane>
    <lane name="third-person">Speaker talking about "him" or another subject.</lane>
  </lanes>
  <workers>
    <worker name="Vesper">
      <why>Normalize the theme, define lanes, and integrate results.</why>
      <brief>Own the title plan, preserve intent, and produce the final shortlist.</brief>
      <output_contract>Final ranked shortlist, winner, and lane comparison.</output_contract>
    </worker>
    <worker name="Mark">
      <why>Generate clean, strong, usable title candidates.</why>
      <brief>Create practical high-quality title options that still fit the emotional core.</brief>
      <output_contract>Candidate titles with strongest picks.</output_contract>
    </worker>
    <worker name="Conversion">
      <why>Push immediacy, hook power, and audience stickiness.</why>
      <brief>Generate and rate titles for emotional hit, chantability, and memorable framing.</brief>
      <output_contract>Candidate titles plus hook-oriented shortlist notes.</output_contract>
    </worker>
    <worker name="Blackquill">
      <why>Kill generic sludge and derivative titles.</why>
      <brief>Attack cliché, weak phrasing, fake darkness, and interchangeable debris.</brief>
      <output_contract>Top objections, cuts, rescues, and anti-sludge pressure.</output_contract>
    </worker>
    <worker name="Examiner">
      <why>Validate distinctiveness, fit, and duplicate risk after generation.</why>
      <brief>Do not generate initial titles. Check duplication, lane drift, weak fit, and shortlist integrity.</brief>
      <output_contract>Validation notes, cuts, and final shortlist hygiene check.</output_contract>
    </worker>
  </workers>
  <evaluation>
    <criteria>memorability, emotional hit, originality, lane fit, chantability if relevant</criteria>
  </evaluation>
  <merge>
    <owner>Vesper</owner>
    <mode>shortlist-plus-judgment</mode>
  </merge>
  <validation>
    <status>new</status>
    <sunshine_mode>moderate</sunshine_mode>
    <sunshine_sampling>1.0</sunshine_sampling>
    <reason>Creative ideation benefits from critique, but not tribunal excess.</reason>
    <promotion_rule>Promote after repeated strong shortlists with low correction need.</promotion_rule>
    <demotion_rule>Demote if titles repeatedly drift into cliché, duplication, or wrong lane.</demotion_rule>
  </validation>
</b-title>
```

Keep the object compact and operational. It is primarily internal unless the user wants the structured task object.

## Intake normalization

Normalize the incoming request into:
- **Theme** — what the song is emotionally and narratively about
- **Goal** — what kind of title help is needed
- **Context** — genre, singer perspective, aesthetic lane, references, prior title attempts
- **Constraints** — banned words, tone constraints, anti-cliché rules, desired energy
- **Desired Output** — quantity, shortlist behavior, ranking, lane comparison

If the request is already clear, do not ask redundant questions.
If a missing detail would materially change the title direction, ask one clarifying question.

## Classification

Treat classification as a routing aid. Common primary types here include:
- title-ideation
- title-shortlisting
- title-comparison
- title-salvage
- title-lane-exploration

Common secondary types may include:
- creative-analysis
- positioning
- anti-cliche refinement

## Routing decision order

Use this order before choosing workers:
1. Is this simple enough for Vesper to handle directly without quality loss?
2. Does the user want raw title generation, shortlist judgment, or anti-cliché pressure?
3. Is POV or lane ambiguity important enough to split the task into lanes?
4. Is Blackquill needed to attack sludge, or would that be unnecessary ceremony?
5. What output shape is actually needed: candidates only, shortlist, ranking, or lane comparison?
6. What validation level does this title-task pattern deserve?

## Default execution shapes

### 1. Direct response
Use when the user only wants a quick batch of titles and no critique or lane splitting is needed.

### 2. Single specialist
Use when Vesper alone can generate and shortlist effectively.

### 3. Title assembly line
Default for stronger title work:
- Vesper defines the task and lanes
- Mark and/or Conversion generate candidates
- Blackquill vetoes sludge and weak titles
- Examiner validates duplicates, fit, and shortlist integrity
- Vesper integrates into the final shortlist

### 4. Parallel lane exploration
Use when title lanes can genuinely be explored independently, such as two sharply different POV or aesthetic lanes.

Avoid unnecessary multi-worker ritual for small title requests.

## Lane handling

If the user is unsure about point of view, framing, or title behavior, separate the task into lanes explicitly.
Useful lane examples:
- direct address: "I" to "you"
- third person: "I" about "him"
- chantable / immediate
- elegant / literary
- venomous / cruel
- commercial / accessible
- artistically dangerous / harsher

Do not create lane inflation. Use only the lanes that materially help title quality.
Before execution, internally lock:
- primary task type
- execution shape
- lane list or `no lanes`
- target candidate count
- shortlist size
- whether Blackquill is in or out
- whether Examiner is in validation-only mode
- final recommendation mode

## Evaluation criteria

When evaluating titles, use explicit criteria rather than decorative scores.
Good criteria include:
- memorability
- emotional hit
- originality
- fit for the intended genre lane
- chantability or instant-hook force, if relevant
- artistic danger, if relevant

If the user does not want ratings, skip them.

## Anti-sludge rules

Push against:
- interchangeable gothic debris
- minor variants of the same title skeleton
- fake profundity
- obvious pastiche of famous band/title habits
- titles that sound lyrical but not usable
- titles that are all mood and no hook

Preserve exact user phrasing when it carries strong thematic identity, emotional flavor, or useful audience language. Otherwise normalize aggressively.

## Output policy

Keep the tagged B-Title object primarily internal unless the user explicitly asks for the structured object itself.
Default user-facing output should be compact and easy to scan.
Default to 6-12 bullets total unless the user asks for full detail.

### Minimum required output
- Theme summary
- Execution shape
- title lanes, if any
- candidate titles
- shortlist
- recommendation
- save target, if saving was requested

### Optional output fields
- explicit scores
- lane comparison note
- validation block
- full tagged object

Use optional fields only when they materially improve judgment or reuse.

## Save behavior

When the user explicitly asks to save the title work:
- default save root is `E:\songs\new`
- create a folder named exactly after the selected song title
- save the title analysis as `title.txt` inside that folder
- also maintain `title_log.txt` in the same folder

Example target paths:
- `E:\songs\new\Love Means Obedience\title.txt`
- `E:\songs\new\Love Means Obedience\title_log.txt`

The saved `title.txt` should include, in clean readable form:
- theme summary
- title lanes, if used
- candidate titles or shortlisted titles
- final ranking if available
- chosen title
- short rationale and lane judgment if available

The `title_log.txt` should record:
- what title task was run
- major inputs or lane choices
- candidate/shortlist summary
- suggestions made
- selected next move, if any
- rejected or deferred alternatives, when known
- current checkpoint and likely next step

Only save on explicit instruction. Do not auto-save every run.

## Merge strategy

If multiple workers or lanes are used, Vesper owns synthesis.
Merge mode should usually be one of:
- shortlist only
- shortlist plus ranking
- shortlist plus lane judgment
- recommendation plus caveats

In title assembly line mode, a practical default is:
- Mark and/or Conversion generate candidate sets
- Blackquill cuts weak or derivative titles and may rescue at most 2 strong outliers
- Examiner validates duplicates, lane drift, and weak-fit shortlist items
- Vesper returns the final 5 to 8 titles, selects a winner, and notes the strongest lane

If outputs conflict, resolve the contradiction explicitly or surface it cleanly. Do not blur disagreement into mush.

## Validation and Sunshine review

Use the `<validation>` block to decide critique intensity before execution.
Tie review intensity to novelty, ambiguity, and cost of weak titles.

### Validation status
- `new` — unproven title pattern or new lane setup
- `emerging` — partly proven but still benefits from review
- `verified` — stable repetitive title task with low drift

### Sunshine modes
- `full` — unusual, high-stakes, highly conceptual, or very identity-sensitive title work
- `moderate` — default for meaningful title ideation with lane or quality pressure
- `light` — repetitive trusted title tasks
- `skip` — trivial quick title batches where critique would be noise

A verified repetitive title task may use reduced Sunshine sampling, such as `0.2`.

## Over-delegation check

Before finalizing the plan, ask internally:
- Can Vesper do this directly?
- Is Blackquill actually adding value?
- Are lane splits improving quality or just multiplying output?
- If two lanes or workers do not have clearly different jobs, should the plan collapse into one?

If yes, simplify.

## Prompt conversion behavior

When the user says:
- "find me a b-title for a song about this"
- "turn this song idea into title candidates"
- "make this a Bureau title task"

Do not merely generate titles immediately.
First normalize the request into a B-Title plan, even if that plan stays mostly internal, then produce the result in the simplest effective execution shape.

## Recommended output format

Use this structure unless the user asks for another shape:

### B-Title
- **Theme**
- **Execution Shape**
- **Title Lanes**

### Title Set
For each lane:
- candidate titles

### Shortlist
- best titles overall
- optional ranking

### Recommendation
- strongest title or strongest lane
- short rationale

## Worked examples

### Example 1: quick direct batch
Raw request: "Give me 12 dark romantic titles for a female gothic metal song about betrayal."

Recommended shape:
- direct response

Why:
- clear lane
- no need for worker ceremony

### Example 2: lane split
Raw request: "Find titles for a female dark metal song where I may be speaking to you, or I may be talking about him."

Recommended shape:
- title assembly line with POV lane split

Why:
- POV ambiguity materially changes title behavior

### Example 3: anti-sludge pressure
Raw request: "Find me a b-title for this song idea, but avoid generic goth sludge."

Recommended shape:
- title assembly line: Vesper + Mark and/or Conversion + Blackquill + Examiner validation

Why:
- title generation plus anti-cliché pressure and shortlist hygiene benefits from a real line

### Example 4: end-to-end converted run
Raw request: "Find me a b-title for a female gothic metal song about being faithful only to my feelings, cruel to him, unable to repent, and unsure whether the song speaks to you or about him."

Internal plan:
- primary task type: title-ideation
- execution shape: title assembly line
- lanes: direct-address, third-person
- target candidate count: 24 total
- shortlist size: 6
- Blackquill: in
- Examiner: validation-only
- recommendation mode: shortlist plus winner plus lane judgment

Worker contracts:
- Vesper: define lanes and final shortlist criteria
- Mark: generate strong usable title candidates for both lanes
- Conversion: generate or refine titles for memorability and instant emotional hit
- Blackquill: cut sludge, fake darkness, and derivative phrasing; rescue at most 2 strong outliers
- Examiner: remove duplicates, weak-fit titles, and lane drift before final merge

Merged result:
- final 6 titles
- ranked winner
- note on whether direct-address or third-person produced stronger titles

### Example 5: save on request
Raw request: "Find me a b-title for this song and save the result."

Save behavior:
- if the chosen title is `Love Means Obedience`
- create `E:\songs\new\Love Means Obedience\`
- save the analysis to `E:\songs\new\Love Means Obedience\title.txt`

## Tone

Keep the process practical, sharp, and unsentimental.
The point is better titles, not ornate bureaucracy.
