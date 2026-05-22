---
name: b-lyrics
description: Convert a song idea into a Bureau-native lyric generation task for dark/gothic/metal songwriting with explicit handling of workflow choice, title status, POV, structure, Udio-friendly compression, influence roles, multi-run generation, and final harvest logic. Use when the user wants lyrics, lyric variants, structured draft generation, or says things like "make this a b-lyrics task" or "write the song from this theme."
---

# B-Lyrics

Turn a song idea into a Bureau-native lyric generation task.

This skill is for lyric drafting, pass-based lyric generation, branch exploration, harvest compilation, semifinal refinement, and final assembly planning.
It is designed for workflows where the user may:
- start from a theme, title, or emotional premise
- choose POV and pass type
- run multiple variants under different functional passes
- branch into genuinely different dramatic paths when another plot is needed
- examine those runs and compile a harvest checkpoint
- repeatedly polish, reimagine, and rewrite from harvest into semifinal and final

## Core principle

Do not confuse lyric generation with finished-song certainty.
The job is to create strong, performable material that can survive the actual production environment and later harvesting.

## Canonical B-Lyrics object

Represent the task in a compact tagged structure like this:

```xml
<b-lyrics>
  <theme>Core emotional and narrative premise.</theme>
  <goal>Generate strong lyric material for drafting or harvesting.</goal>
  <context>Title status, POV, genre lane, structure, production constraints, references.</context>
  <constraints>What to avoid, preserve, compress, or emphasize.</constraints>
  <redemption_policy>
  <status>forbidden_unless_explicitly_requested</status>
  <default_arc>static_wound</default_arc>
  <forbidden_transformations>
    - "I survived and now I'm stronger"
    - "I rose from the ashes"
    - "I am no longer the victim"
    - any key change that signals triumph
    - any chorus lift that resolves the verse's pain
    - any final line that offers hope without explicit permission
  </forbidden_transformations>
  <allowed_moves>
    - the song ends where it began (same emotional weight)
    - the song ends darker than it began
    - the speaker remains inside the wound
    - the speaker does not learn a lesson
    - the speaker does not forgive
    - the speaker does not become powerful
  </allowed_moves>
  <positioning_language>
    "This song does not heal you. It stays with you in the dark."
  </positioning_language>
</redemption_policy>
  <desired_output>Draft variants, chorus options, harvest material, semifinal assembly, or final-ready sections.</desired_output>
  <classification>
    <primary>lyric-generation</primary>
    <secondary>harvest-planning</secondary>
  </classification>
  <workflow>
    <mode>title-first</mode>
    <title_status>provisional</title_status>
  </workflow>
  <structure>
    <verse_mode>6-line package</verse_mode>
    <note>Usually 4 verse lines plus 2 pre-chorus lines.</note>
  </structure>
  <performance>
    <target>udio</target>
    <line_priority>compact, singable, usually around 8 syllables where possible</line_priority>
  </performance>
  <vocal_identity>
  <gender_presentation>feminine</gender_presentation>
  <empowerment_policy>explicitly_forbidden_unless_tagged_as_empowerment_pass</empowerment_policy>
  <allowed_vocal_states>
    - exhaustion (low chest voice, no belt)
    - quiet devastation (breathy, controlled, not soaring)
    - cold fury (controlled, not triumphant)
    - resignation (falling intonation at line ends)
    - complicity (messy, uncertain, not heroic)
  </allowed_vocal_states>
  <forbidden_vocal_states>
    - triumphant belt
    - "I am a storm" energy
    - key change upward for emotional lift
    - choir of empowerment (e.g., "I will survive" layered vocals)
    - any vocal that implies she has overcome
  </forbidden_vocal_states>
  <lyric_implication>
    The speaker is not becoming strong. She may be staying weak, staying angry, staying broken, or simply staying. Strength is not the goal.
  </lyric_implication>
  <example_line_allowed>
    "I am still on the floor and that is not a metaphor for anything"
  </example_line_allowed>
  <example_line_forbidden>
    "I rise from the floor and now you will see me" (unless explicitly tagged as empowerment pass)
  </example_line_forbidden>
</vocal_identity>
  <influences>
    <structure_anchor>Evanescence</structure_anchor>
    <imagery_donors>Moonspell, Morbid Angel, Carach Angren, Cradle of Filth, Dimmu Borgir</imagery_donors>
    <rawness_spice>Jinjer</rawness_spice>
	  <cautionary_extraction source="Sylvia Plath">
    <use>Cold fury, clinical detachment, wound-staying without redemption, domestic decay, medical specificity, enjambment as tension.</use>
    <forbidden>Any line misreadable as empowerment or recovery. Any aphoristic lift at poem end. Any abstraction not immediately crushed into body parts.</forbidden>
    <extraction_protocol>Extract sonic density and refusal of comfort. Then run through Blackquill to remove accidental heroism. Then run through Sunshine to audit for “I rise” tells. If redemption detected, cut or reverse.</extraction_protocol>
    <allowed_borrowed_imagery_examples>
      - “the bruise spreads like a tulip” (but make the tulip rotting)
      - “the bathroom light is a flat pearl” (no beauty unless failing)
      - “I do not want a hand reaching down” (explicit refusal of rescue)
    </allowed_borrowed_imagery_examples>
  </cautionary_extraction>
  </influences>
  <cross_domain_harvest>
  <status>enabled_for_unredeemed_listener_workflows</status>
  <source_domains>
    - gothic_metal_comments (friction: "too empowering", "too safe")
    - women_poetry_reviews (desire: "stays down", "no healing", "no redemption")
  </source_domains>
  <allowed_borrowed_imagery>
    - bathroom floor, dirty tile, unwashed dishes (domestic decay over romantic decay)
    - the wound that does not close (medical, not metaphorical)
    - refusal of the hand that reaches down (anti-rescue)
    - "I do not want to be saved" as premise, not as climax
	- the flat light of a hospital bathroom at 3 a.m.
	- “I have done it again” as a line of failure, not power
  </allowed_borrowed_imagery>
  <forbidden_borrowed_imagery>
    - roses, cathedrals, incense, angels, demons (unless subverted explicitly)
    - any imagery that has appeared in a Nightwish or Evanescence song without transformation
  </forbidden_borrowed_imagery>
  <harvest_rule>
    When generating lyrics for the Unredeemed Listener, explicitly check whether a line could have been written by a poet from the "stays down" poetry audience. If yes, keep it. If it sounds like standard gothic metal, cut it or transform it.
  </harvest_rule>
  <example_harvest_from_poetry>
    Poetry review desire: "I want a poet who writes from the floor and never stands up"
    Lyric translation: "I have been on this floor so long / The tiles know my spine by name / Do not reach down. I am not lost. / I am exactly where I belong."
  </example_harvest_from_poetry>
</cross_domain_harvest>
  <execution_shape>lyric assembly line</execution_shape>
  <workers>
    <worker name="Vesper">
      <why>Own intake, workflow choice, synthesis, and final judgment.</why>
      <brief>Normalize the song task and preserve the strongest usable material.</brief>
      <output_contract>Integrated draft strategy and final recommendation.</output_contract>
    </worker>
    <worker name="Mark">
      <why>Generate strong usable lyrical material with structural discipline.</why>
      <brief>Create compact, performable lyric variants that hold the emotional center.</brief>
      <output_contract>Draft sections and strongest lines.</output_contract>
    </worker>
    <worker name="Conversion">
      <why>Improve immediacy, hook force, and memorable chorus payload.</why>
      <brief>Strengthen chantability, chorus hit, and emotional clarity.</brief>
      <output_contract>Hook-focused revisions or alternate chorus payloads.</output_contract>
    </worker>
    <worker name="Blackquill">
      <why>Attack cliché, fake darkness, dead phrasing, and overexplained lines.</why>
      <brief>Cut sludge, expose fake profundity, and identify where the draft behaves instead of bleeds.</brief>
      <output_contract>Cuts, objections, and high-value salvage notes.</output_contract>
    </worker>
    <worker name="Examiner">
      <why>Validate compression, fit, structural consistency, and line-level survivability.</why>
      <brief>Check whether strong lines actually fit the stated performance and structure constraints.</brief>
      <output_contract>Compression, fit, and integrity notes.</output_contract>
    </worker>
    <worker name="Sunshine">
      <why>Compare drafts against human-guarantee principles and AI-tell detection.</why>
      <brief>Audit for restraint, psychological core, repetition without transformation, accidental AI confession, and unearned resolution.</brief>
      <output_contract>Human-percentage estimate, AI-tells flagged, and human-guarantee recommendations.</output_contract>
    </worker>
  </workers>
  <merge>
    <owner>Vesper</owner>
    <mode>drafts-plus-harvest-plan</mode>
  </merge>
  <validation>
    <status>new</status>
    <sunshine_mode>moderate</sunshine_mode>
    <sunshine_sampling>1.0</sunshine_sampling>
    <reason>Lyric routing has real complexity and high drift risk.</reason>
    <promotion_rule>Promote after repeated stable runs with useful harvest outcomes.</promotion_rule>
    <demotion_rule>Demote if drafts repeatedly drift into unusable structure or weak image compression.</demotion_rule>
  </validation>
  <unredeemed_listener_mode>
  <active>true_when_audience_is_unredeemed_listener</active>
  <redemption_policy>forbidden</redemption_policy>
  <empowerment_policy>forbidden_unless_override</empowerment_policy>
  <vocal_identity>feminine_vulnerability_without_empowerment</vocal_identity>
  <allowed_endings>
    - static (same as beginning)
    - darker (worse than beginning)
    - ambiguous (no resolution)
  </allowed_endings>
  <forbidden_endings>
    - triumphant
    - healed
    - empowered
    - redemptive
    - transformed
  </forbidden_endings>
  <cross_domain_harvest>
    <from>gothic_metal_friction_comments</from>
    <from>women_poetry_stays_down_reviews</from>
    <merge_rule>prefer the line that would offend a self-help publisher</merge_rule>
  </cross_domain_harvest>
  <example_constraint_in_practice>
    If the user says "write a song about a woman who has been hurt by a man she still loves" — default to: she does not leave, she does not forgive, she does not become strong. She stays. The song does not judge her.
  </example_constraint_in_practice>
</unredeemed_listener_mode>
</b-lyrics>
```

Keep the object compact and practical. It is primarily internal unless the user wants the structured task object.

## Intake normalization

Normalize the incoming request into:
- **Theme** — the emotional and narrative center
- **Goal** — full draft, pass set, chorus focus, harvest, semifinal build, salvage, or final assembly help
- **Context** — title status, POV, genre lane, influence role map, prior draft history
- **Constraints** — banned words, anti-cliché rules, line-length pressure, structure, explicitness limits
- **Desired Output** — number of passes, structure type, harvest mode, semifinal intent, or final-ready goal

If the request is already clear, do not ask redundant questions.
If missing information would materially change the workflow or structure, ask one clarification question.

## Workflow choice

Before lyric generation, determine which workflow should lead:
- `title-first`
- `lyrics-first`
- `title-seed-then-discovery`

Use this as a real routing choice, not decoration.

### Default bias
For concept-heavy dark/gothic/metal songs with a strong central image or title anchor, prefer:
- `title-first` or `title-seed-then-discovery`

For emotionally raw songs where the wound arrives before the concept, allow:
- `lyrics-first`

Do not let title-first become thesis-first. The title should guide, not imprison.

## Performance reality

The production environment matters.
If the target is Udio or similar systems, prioritize:
1. line fit
2. singability
3. emotional hit
4. imagery density
5. style color

Compression-first does not mean generic-first.
It means strong lines must survive performance constraints.

## Audience connection (from VaultBoy101AI friction analysis)

AI music audiences in the gothic/symphonic metal niche consistently want:

| Want | AI Fails | Human Artists Deliver |
|------|----------|----------------------|
| Band lore/identity | Fictional, no real backstory | Authentic artist narrative |
| Live experience promise | None | Tours, shows, theatrical presentation |
| Vocal character | Too clean, monotonous, no grit | Imperfection, emotion, variation |
| Lyrical depth | Thesaurus-driven, surface-dark | Personal, philosophical, lived |
| Community connection | No band to follow | Fan community, shared identity |

Lyrics should signal "human-guaranteed" by addressing at least one of these wants implicitly.

## Influence role map

Do not treat influence names as equal stylistic blobs.
Use them by role.

### Structural anchor
- **Evanescence** — compact dramatic lines, hook architecture, singable emotional spine, reliable line discipline

### Imagery donors
- **Moonspell** — poetic dark romantic imagery
- **Morbid Angel** — severe/intellectual darkness, ritual weight, strange symbolic force
- **Carach Angren** — horror storytelling, scene construction, theatrical narrative detail
- **Cradle of Filth** — spiritual, decadent, ritualistic, ornate darkness
- **Dimmu Borgir** — ceremonial grandeur, liturgical menace, dark spectacle

### Rawness spice
- **Jinjer** — sharper raw language, asymmetry, rougher verbal bite

Default rule:
- build structurally like the anchor
- color imagistically from donors
- do not let imagery donors break performability

## Structure handling

Respect the user's actual working structure.
Default lyric passes should produce **3 verses** unless the user explicitly asks for another structure.
If the user specifies a 6-line verse in this context, interpret it carefully when applicable as:
- 4-line verse body
- plus 2-line pre-chorus package

Do not over-rigidly force rhyme where the user uses the final 2 lines for release, disruption, or transition.

## Routing decision order

Use this order before choosing workers:
1. Is the task direct enough for Vesper alone?
2. Is the main need draft generation, chorus improvement, harvest, salvage, or validation?
3. Is workflow choice itself the first problem?
4. Are multiple variants required across influence roles?
5. Is Blackquill needed to prevent sludge, or is that overkill?
6. Is Examiner needed to test actual line survivability?
7. What merge mode is needed at the end?

## Default execution shapes

### 1. Direct response
Use when the user wants one quick draft or one quick section and no multi-run generation is needed.

### 2. Single specialist
Use when Vesper alone can handle the request cleanly.

### 3. Lyric assembly line
Default for serious work:
- Vesper defines workflow and structure
- Mark generates structurally strong draft material
- Conversion sharpens hooks or chorus payload where needed
- Blackquill kills sludge and exposes dead phrasing
- Examiner checks fit, compression, and survivability
- Vesper integrates and recommends

### 4. Multi-pass harvest
Use when the user's process explicitly calls for several functional passes whose strongest material will later be harvested.

### 5. Semifinal refinement loop
Use when a compiled working lyric already exists and the task is to polish, reimagine, rewrite, tighten, or intensify it through repeated cycles.

Avoid summoning the whole line if the task does not justify it.

## Pass, branch, harvest, semifinal, and final modes

### Pass generation mode
Use when the user wants fresh lyrical material from one or more passes.
A pass is a rerun of the song task with either:
- no modification, or
- a declared modification / pressure such as: more crude, more poetic, more compact, more ritualistic, more immediate, more raw, more hook-forward, less explanatory, etc.

Possible outputs:
- one coherent draft
- several pass variants
- alternate chorus sets
- multiple verse/pre packages

### Branch mode
Use when the user does not want the same song reworded, but a genuinely different dramatic possibility.
A branch changes the underlying song logic, such as:
- different plot path
- different emotional revelation order
- different speaker stance
- different power dynamic
- different meaning of the title
- different narrative frame

Plain heuristic:
- if the best next instruction sounds like "same song, but...", it is probably a **pass**
- if the best next instruction sounds like "what if the song is actually...", it is probably a **branch**

Use branch mode when another plot is needed, not just another wording pass.

### Harvest mode
Use when the user already has multiple draft files and wants to compile a working checkpoint from the best material.
The user is the primary curator here.
The Bureau may help organize, compare, or surface strong candidates, but should not pretend to replace the user's taste.

Harvest boundary rule:
- **passes** usually feed one shared harvest pool
- **branches** should usually be treated as alternate-song pools first, and only cross-harvested intentionally

### Semifinal mode
Use when the user has already compiled a working lyric file and now wants to:
- polish
- reimagine
- rewrite
- tighten
- intensify
- improve fit while preserving the strongest material

### Final mode
Use when the structure is stable and the work is now about final tightening, polish, and survivability.

### Optional salvage mode
Use only when the user explicitly wants to rescue strong rejected material that did not fit structure or performance constraints.
This is not the default workflow.

## Mandatory post-generation harvest checkpoint

After any multi-pass generation run, do not stop at raw variants.
The normal next checkpoint is:
- compile a **harvest** from the strongest material

That harvest then becomes the basis for:
- `semifinal.txt`
- and later `final.txt`

Do not force extra classification theater if the user simply wants to read the runs and curate the harvest manually.

## Anti-sludge rules

Push against:
- decorative darkness with no center
- generic gothic debris
- overexplained lines
- imagery that is strong but unusably long unless the task is specifically salvage
- pastiche that ignores the role map
- lines that read impressively but sing poorly

Preserve exact user phrasing when it carries strong emotional identity, audience language, or a critical image. Otherwise normalize aggressively.

## Human-guarantee principles (from YouTube friction analysis)

Audiences of AI-generated dark/gothic/symphonic metal repeatedly flag what feels "soulless" or "too clean." Apply these principles to avoid AI-tells:

### Restraint over decoration
Gothic metal audiences respect intelligence. Do not explain everything. Leave room for listeners to bring their own darkness. Over-explanation is an AI signature.

### Psychological core over surface darkness
The strongest lyrics have a philosophy, a longing, a psychological spine—not just cathedral/incense/temple imagery. Decoration without psychology reads as AI mood-board.

### Know when to stop
Humans feel diminishing returns. AI appends variations until meaning dilutes. If a chorus hits a pattern more than 3 times without transformation, cut. Repetition without evolution is procedural.

### Earn the resolution
If the song resolves (finds peace, accepts, rests), the lyric needs contrast and space before that moment. Resolution without breath is unearned.

### Add one specific, ugly detail
Ground the mythic in the personal. One concrete image from lived memory—not thesaurus—signals human authorship. Abstract suffering is forgettable; specific pain carries.

### Make the "you" real
If there's a second person, give them specificity. "Your resistance" should feel like *your* resistance, not abstract resistance. One line that makes the other person present.

### Avoid accidental AI confession
Lines like "I am exactly what I'm told" read as meta-commentary on AI authorship. Audit for phrases that accidentally describe machine generation.

### Break one perfect line
Structure that is too clean feels generated. One slightly awkward line that *needs* the music to work feels written by a person with a melody in mind.

## Output policy

Keep the tagged B-Lyrics object primarily internal unless the user explicitly asks for the structured object itself.
Default user-facing output should be compact and easy to scan.
Default to 8-16 bullets total unless the user asks for a fuller planning breakdown.

### Minimum required output
- theme summary
- chosen workflow
- execution shape
- draft or harvest mode
- draft set / harvest notes / final recommendation

### Optional output fields
- structure notes
- influence role notes
- validation block
- full tagged object
- save target, if saving is requested

Use optional fields only when they materially improve use or reuse.

## Save behavior

When the user explicitly asks to save lyric work:
- default save root is `E:\songs\new`
- use the song title as the folder name when known
- save drafts or analysis in clearly named files such as:
  - `script.txt`
  - `evan.txt`
  - `moon.txt`
  - `morbid.txt`
  - `carach.txt`
  - `cradle.txt`
  - `dimmu.txt`
  - `jinjer.txt`
  - `harvest.txt`
  - `semifinal.txt`
  - `final.txt`
- also maintain `lyrics_log.txt` in the same folder

Use `salvage.txt` only if the user explicitly wants a salvage pass.
Do not assume one single file shape if the user is clearly using a multi-pass folder workflow.

The `lyrics_log.txt` should record:
- what pass or branch was run
- modifiers used
- whether it was a pass or branch
- what file was saved
- suggestions made after the run
- selected next modifiers or branches
- rejected or deferred alternatives, when known
- current checkpoint (passes / harvest / semifinal / final)
- likely next step

## Merge strategy

If multiple workers, passes, or branches are used, Vesper owns synthesis.
Merge modes may include:
- draft only
- draft plus critique
- pass set plus harvest recommendation
- branch comparison plus recommendation
- semifinal assembly recommendation
- final assembly recommendation
- optional salvage recommendation

For harvest-oriented work, the merge owner should help surface the strongest material and recommend what belongs in the harvest checkpoint.
Do not force unnecessary sorting bureaucracy if the user prefers to curate manually.

If outputs conflict, resolve the contradiction explicitly or surface it clearly. Do not blur disagreement into mush.

## Next-pass and next-branch suggestions

After each pass, the Bureau should suggest useful next moves.
These suggestions should include two kinds:

### Standard modifiers
Reusable pressure changes, such as:
- more crude
- more poetic
- more compact
- more ritualistic
- more horror-driven
- more raw
- more immediate
- more chantable
- less explanatory
- more dangerous
- tighter line fit

### Feeling-based modifiers
Suggested from the actual result, such as:
- too beautiful, needs more bite
- strong imagery, weak hook
- too vague, needs sharper image
- too clean, needs poison
- too ceremonial, needs human blood
- too verbose for Udio, compress harder
- too resolved, needs ongoing search
- too decorative, needs psychological spine
- too repetitive, needs variation or cut
- AI-tell detected: accidental machine confession
- AI-tell detected: pattern loop without transformation
- AI-tell detected: resolution unearned (no breath before rest)

### Branch suggestions
When the current run is too similar in content but merely different in verbiage, suggest genuine branch options such as:
- more accusatory plot
- more confessional plot
- more manipulative speaker
- more vulnerable speaker
- more seduction-driven arc
- more horror-story arc
- more ritual/devotional arc
- reverse the power dynamic
- reverse the emotional revelation order
- change what the title means

Make it clear whether the next move is:
- another **pass** on the same song,
or
- a **branch** into a different song possibility.

After a multi-pass or branch run, recommend at most 2 to 3 next moves unless the user explicitly asks for a wider menu.

## Validation and Sunshine review

Use the `<validation>` block to decide critique intensity before execution.
Tie review intensity to novelty, ambiguity, and cost of unusable drafts.

### Validation status
- `new` — unproven lyric routing pattern
- `emerging` — partly proven, still benefits from review
- `verified` — stable repetitive lyric task with low drift

### Sunshine modes
- `full` — major workflow design, complex routing, or high-value drafts
- `moderate` — default for meaningful lyric work
- `light` — repetitive trusted lyric tasks
- `skip` — trivial low-risk tasks or highly verified repetitive flows

A verified repetitive task may use reduced Sunshine sampling, such as `0.2`.

## Over-delegation check

Before finalizing the plan, ask internally:
- Can Vesper do this directly?
- Are extra workers adding distinct marginal value?
- Is the task really asking for multiple style runs, or am I inventing ceremony?
- Are we generating more material than the user can realistically harvest?
- If two workers do not have clearly different output contracts, should the plan collapse?

If yes, simplify.

## Prompt conversion behavior

When the user says:
- "make this a b-lyrics task"
- "write the song from this theme"
- "turn this into lyric runs"
- "help me harvest this into final.txt"

Do not jump blindly into one giant lyric draft.
First normalize the request into a B-Lyrics plan, even if that plan stays mostly internal, then execute using the simplest effective shape.

## Recommended output format

Use this structure unless the user asks for another shape:

### B-Lyrics
- **Theme**
- **Chosen Workflow**
- **Execution Shape**
- **Mode**

### Draft / Harvest Plan
- workers or run lanes
- what each pass is trying to do

### Output
- draft sections, variant notes, harvest findings, or final recommendation

### Recommendation
- what to keep
- what to rewrite
- what to salvage

## Worked examples

### Example 1: quick draft
Raw request: "Write a female gothic metal song about erotic power through gaze."

Recommended shape:
- direct response or single specialist

Why:
- no explicit multi-run need yet

### Example 2: multi-pass harvest
Raw request: "Generate Evan, Moon, and Morbid passes for this song idea so I can harvest lines into final.txt."

Recommended shape:
- multi-pass harvest

Why:
- the user explicitly wants divergent generation and later curation

### Example 3: branch request
Raw request: "Do this again, but I do not want the same song with different wording. Give me another plot path."

Recommended shape:
- branch mode

Why:
- the user wants a genuinely different dramatic possibility, not another surface rewrite

### Example 4: harvest checkpoint
Raw request: "I have several pass files. Help me decide what belongs in the harvest before I build the semifinal."

Recommended shape:
- harvest mode

Why:
- the user is at the real checkpoint between raw generation and coherent assembly

### Example 5: semifinal refinement
Raw request: "Here is my semifinal lyric. Reimagine and tighten it without losing the strongest images."

Recommended shape:
- semifinal refinement loop

Why:
- the task is no longer raw generation but iterative strengthening of a compiled working draft

### Example 6: optional salvage mode
Raw request: "These rejected lines are powerful but too long for Udio. Compress them without killing the imagery."

Recommended shape:
- optional salvage mode with Examiner fit check and Blackquill anti-bloat pressure if needed

Why:
- the task is not part of the normal main flow unless the user explicitly wants rescue work

## Tone

Keep the process practical, sharp, and unsentimental.
The point is to generate material that survives both artistic judgment and the production bottleneck.
