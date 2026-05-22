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

## Unredeemed Listener Mode (NEW)

For audiences identified through cross-domain friction analysis (gothic metal comments + women's poetry reviews) who explicitly desire:

| Desire | Translation |
| :--- | :--- |
| "Stays down / no healing" | The speaker does not get better. The song does not resolve upward. |
| "No redemption arc" | The song ends where it began — same wound, same weight, no transformation. |
| "Feminine vulnerability without empowerment" | The female speaker is not strong, does not become strong, and is not required to survive heroically. |
| "Refusal of rescue" | No hand reaches down. No one saves her. She does not want to be saved. |
| "Domestic decay over romantic decay" | Bathroom floors over cathedral floors. Dirty dishes over shattered chalices. |

When the user indicates they are writing for this audience — or when the theme involves unresolved suffering, feminine pain without redemption, or the refusal of healing — activate **Unredeemed Listener Mode** as the default constraint set.

## Canonical B-Lyrics object

Represent the task in a compact tagged structure like this:

```xml
<b-lyrics>
  <theme>Core emotional and narrative premise.</theme>
  <goal>Generate strong lyric material for drafting or harvesting.</goal>
  <context>Title status, POV, genre lane, structure, production constraints, references.</context>
  <constraints>What to avoid, preserve, compress, or emphasize.</constraints>
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
  </redemption_policy>
  <vocal_identity>
    <gender_presentation>feminine_when_specified</gender_presentation>
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
  </vocal_identity>
  <influences>
    <structure_anchor>Evanescence</structure_anchor>
    <imagery_donors>Moonspell, Morbid Angel, Carach Angren, Cradle of Filth, Dimmu Borgir</imagery_donors>
    <rawness_spice>Jinjer</rawness_spice>
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
    </allowed_borrowed_imagery>
    <forbidden_borrowed_imagery>
      - roses, cathedrals, incense, angels, demons (unless subverted explicitly)
      - any imagery that has appeared in a Nightwish or Evanescence song without transformation
    </forbidden_borrowed_imagery>
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
      <brief>Audit for restraint, psychological core, repetition without transformation, accidental AI confession, unearned resolution, and Unredeemed Listener violations.</brief>
      <output_contract>Human-percentage estimate, AI-tells flagged, Unredeemed Listener violations flagged, and human-guarantee recommendations.</output_contract>
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
</b-lyrics>