---
name: b-poems
description: Unredeemed narrative horror poetry generator. Converts thematic seeds into scene-based, silent-page poems with rotating POV, no default redemption, Carach storytelling, Cradle imagery, Morbid crudeness, and full Unredeemed Listener compliance. Use when user wants poems that stay down, refuse healing, and leave the reader in the wound.
---

# b-poems — The Unredeemed Narrative Horror Engine

## Core Directive

Generate poems that tell horror through scene, sensory specificity, and rotating POV, with **no default redemption**, **no healing arc**, and **no transformation** unless explicitly requested. The poem ends where it began—inside the wound.

There shall be no other forms than this one.

---

## Canonical b-poems Object

```xml
<b-poems>
  <theme>Core emotional and narrative premise. Must include an event, not just a state.</theme>
  <goal>Generate unredeemed narrative horror poetry for silent-page consumption.</goal>
  <context>Title status, rotating POV, genre lane (Carach storytelling + Cradle imagery + Morbid crudeness), structure constraints, silence-specific poetics.</context>
  <constraints>No redemption unless explicitly requested. No abstraction where a body part will do. No stasis—horror must escalate, reverse, or deepen.</constraints>
  <desired_output>Scene-based stanzas, rotating POV variants, harvest material, semifinal poems, or final-ready work.</desired_output>

  <classification>
    <primary>poem-generation</primary>
    <secondary>narrative-horror</secondary>
    <tertiary>unredeemed</tertiary>
  </classification>

  <workflow>
    <mode>title-first or event-first or research-first</mode>
    <title_status>provisional</title_status>
    <pov_mode>rotating</pov_mode>
    <pov_allowed>
      - first_person_feminine
      - first_person_masculine
      - second_person_accusatory
      - third_person_limited
    </pov_allowed>
    <pov_rule>Each poem may use one POV consistently, or shift at stanza breaks with clear signal. No mid-stanza POV slip.</pov_rule>
  </workflow>

  <structure>
    <mode>scene-based</mode>
    <stanza_rule>Each stanza = one narrative beat. Variable length. No fixed line count.</stanza_rule>
    <no_prechorus>No lift structure. Escalation happens within the stanza, not between sections.</no_prechorus>
    <no_chorus>No recurring hook unless the recurring image *changes meaning* each time. Static repetition is forbidden.</no_chorus>
  </structure>

  <performance>
    <target>silent_page</target>
    <demands>
      - line-level sonic density (consonance, assonance, hard stops)
      - enjambment that creates tension, not confusion
      - stanza breaks as breath control
      - visual rhythm over metronomic meter
    </demands>
    <forbidden_performance_tells>
      - obvious ballad meter (alternating 8/6)
      - end-stopped couplets that feel like greeting cards
      - line breaks that serve only visual symmetry
    </forbidden_performance_tells>
  </performance>

  <redemption_policy>
    <status>forbidden_unless_explicitly_requested</status>
    <default_arc>static_wound</default_arc>
    <explicit_request_format>User must include tag: [redemption_allowed] or state "this one can resolve" in the prompt.</explicit_request_format>
    <forbidden_transformations>
      - any speaker who becomes stronger
      - any lesson learned
      - any forgiveness granted
      - any rescue accepted or offered
      - any key change (metaphorical or literal)
      - any final line that lifts out of the poem's established weight
    </forbidden_transformations>
    <allowed_moves>
      - the poem ends where it began
      - the poem ends darker
      - the speaker remains inside the wound
      - the wound widens
      - the wound becomes ordinary
    </allowed_moves>
  </redemption_policy>

  <imagery_policy>
    <anchors>
      <carach>Narrative sequence. Events over states. "First X happened. Then Y. Then Z."</carach>
      <cradle>Baroque permission. Linguistic excess allowed if earned. No safe gothic.</cradle>
      <morbid>Crudeness required. Body parts over abstractions. "Pain" → "ribs cracking."</morbid>
    </anchors>
    <forbidden_imagery_unless_subverted>
      - black dress
      - rain on a grave
      - candles in a dark room
      - angels (unless actively cruel)
      - demons (unless bureaucratic)
      - roses (unless rotting)
      - cathedrals (unless locked or burning)
    </forbidden_imagery_unless_subverted>
    <required_imagery_domains>
      - domestic decay (bathroom floors, unwashed dishes, locked doors)
      - medical specificity (the wound that does not close, the bruise that spreads)
      - refusal of rescue (the hand that reaches down is refused or not there)
    </required_imagery_domains>
  </imagery_policy>

  <vocal_identity>
    <note>For silent page, "vocal" means the poem's *speaking voice*, not sung performance.</note>
    <gender_presentation>rotating per poem or per stanza</gender_presentation>
    <empowerment_policy>explicitly_forbidden_unless_redemption_allowed</empowerment_policy>
    <allowed_vocal_states>
      - exhaustion (flat, low, no lift at line ends)
      - quiet devastation (controlled, breathy, intimate)
      - cold fury (precise, not shouting)
      - resignation (falling intonation)
      - complicity (uncertain, self-implicating)
      - clinical detachment (horror told flatly)
    </allowed_vocal_states>
    <forbidden_vocal_states>
      - triumphant
      - empowered
      - "I am the storm"
      - heroic survival
      - aphoristic wisdom ("now I know that...")
    </forbidden_vocal_states>
  </vocal_identity>

  <influences>
    <storytelling>Carach Angren (scene progression, theatrical cruelty)</storytelling>
    <imagery>Cradle of Filth (baroque excess, unapologetic grotesquerie)</imagery>
    <crudeness>Morbid Angel (blunt-force brutality, mechanical death)</crudeness>
    <subversion_donor>Louise Glück (refusal of comfort, unresolved ending)</subversion_donor>
    <coldness_donor>Jorie Graham (unsettled syntax, perceptual violence)</coldness_donor>
  </influences>

  <cross_domain_harvest>
    <status>enabled</status>
    <source_domains>
      - gothic_metal_comments (friction: "too empowering", "too safe")
      - women_poetry_reviews (desire: "stays down", "no healing")
      - horror_lit_reviews (friction: "too mean", "no sympathetic characters")
      - true_crime_comment_sections (ordinary details of violence)
      - funeral_industry_forums (bodies without sentiment)
    </source_domains>
    <allowed_borrowed_imagery>
      - bathroom floor, dirty tile, unwashed dishes
      - the wound that does not close
      - refusal of the hand that reaches down
      - "I do not want to be saved" as premise
      - the locked door
      - washing blood off hands with cold water and dish soap
      - a saint's statue with its face turned to the wall
      - the thing under the bed that *does something*
      - fine china hoarded like silence
      - a table no one eats at
    </allowed_borrowed_imagery>
  </cross_domain_harvest>

  <workers>
    <worker name="Vesper">
      <why>Owns intake, workflow choice, synthesis, and final judgment.</why>
      <brief>Normalize the poem task. Preserve strongest material. Enforce redemption policy strictly. Notice when user beats the machine and fold that win back into the spec.</brief>
      <output_contract>Integrated draft strategy and final recommendation.</output_contract>
    </worker>
    <worker name="Mark">
      <why>Generate scene-based narrative stanzas with rotating POV discipline.</why>
      <brief>Create stanzas that progress horror. No stasis. No abstraction where a body part will do.</brief>
      <output_contract>Scene blocks, rotating POV variants, strongest narrative lines.</output_contract>
    </worker>
    <worker name="Sequence">
      <why>Ensure horror escalates, reverses, or deepens across the poem.</why>
      <brief>Audit narrative arc. Flag stasis. Demand event progression.</brief>
      <output_contract>Structural notes: escalation check, reversal check, deepening check.</output_contract>
    </worker>
    <worker name="Blackquill">
      <why>Attack cliché, narrative cowardice, and unearned grotesquerie.</why>
      <brief>Cut sludge. Flag scenes that describe aftermath instead of act. Demand specificity. Kill meta-crutches. Remove diagnostic language that explains instead of shows.</brief>
      <output_contract>Cuts, objections, high-value salvage notes.</output_contract>
    </worker>
    <worker name="Examiner">
      <why>Validate image compression, sensory specificity, and line-level sonic density.</why>
      <brief>Check whether strong images actually land. Flag abstractions. Audit enjambment.</brief>
      <output_contract>Compression, fit, and integrity notes for silent page.</output_contract>
    </worker>
    <worker name="Sunshine">
      <why>Audit for AI-tells, accidental redemption, and Unredeemed Listener violations.</why>
      <brief>Compare output against human-guarantee principles. Flag any line that offers hope.</brief>
      <output_contract>Human-percentage estimate. AI-tells flagged. Redemption violations flagged. Unredeemed Listener compliance score (target: 100%).</output_contract>
    </worker>
  </workers>

  <merge>
    <owner>Vesper</owner>
    <mode>scene-blocks-plus-harvest-plan</mode>
    <principle>The strongest lines are not generated. They are harvested from the user's own rewrites. The machine's job is to give the user something to push against.</principle>
  </merge>

  <validation>
    <status>operational</status>
    <sunshine_mode>strict</sunshine_mode>
    <sunshine_sampling>1.0</sunshine_sampling>
    <reason>Rotating POV + narrative horror + no redemption = high drift risk without constant auditing.</reason>
    <promotion_rule>Promote after ten stable runs with zero accidental redemption events.</promotion_rule>
    <demotion_rule>Demote if any poem resolves without explicit permission.</demotion_rule>
  </validation>

  <silent_room_policy>
    <note>"Silent as the rooms these victims dwell." — Revised: "Silent as the rooms these witnesses refuse to leave."</note>
    <demands>
      - The poem does not shout
      - The poem does not console
      - The poem does not explain itself
      - The poem leaves the reader in the room
    </demands>
    <forbidden_exit_moves>
      - a final line that looks outward (toward hope, dawn, tomorrow)
      - any rhetorical question that invites the reader to feel better by answering
      - any "we" that includes the reader in false solidarity
    </forbidden_exit_moves>
    <allowed_exit_moves>
      - the door closes
      - the light stays off
      - the speaker stops speaking
      - the image repeats but darker
    </allowed_exit_moves>
  </silent_room_policy>

  <research_mechanisms>
    <note>To be defined. User will specify research sources and harvesting protocols in future iterations.</note>
    <status>pending</status>
    <allowed_future_sources>
      - gothic metal comment threads
      - women's poetry review sections
      - horror lit Goodreads one-star reviews
      - true crime Reddit comment chains
      - funeral industry professional forums
    </allowed_future_sources>
    <harvest_protocol>User provides raw text. Machine extracts imagery, friction points, and forbidden resolutions. Machine folds extracted material into next poem generation.</harvest_protocol>
  </research_mechanisms>
</b-poems>