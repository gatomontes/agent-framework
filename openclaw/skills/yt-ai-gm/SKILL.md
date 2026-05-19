---
name: yt-comment-friction-miner
description: Mine YouTube comments for recurring pain, confusion, objections, unmet needs, and audience language, specifically tuned for identifying underserved audiences in cultural niches (e.g., gothic metal, dark romance, genre gaps). Now includes AI-generated music friction analysis, using AI failures as diagnostic tools to clarify what audiences truly want. Use when the user wants to find what listeners/consumers are missing, what current solutions fail to deliver, and how to position a product, lyric, band, or service into the gap.
---

# YT Comment Friction Miner

Turn YouTube comment sections into structured market intelligence for underserved audiences.

This skill is designed for founders, product builders, artists, and strategists who need to go beyond creator narratives and find what real audiences keep complaining about, wishing for, or failing to find.

The target use case in this configuration is **identifying underserved gothic metal fans** — listeners who want unresolved relational pain, no faux-empowerment, and a gap between "safe" gothic metal and "gory" death metal. The skill now also accommodates **AI-generated music friction**, using AI's documented failures (thesaurus-driven lyrics, clean resolution, perfect but hollow vocals) as a diagnostic tool to clarify the underserved gap. The skill can be adapted to any cultural or commercial niche.

## Core Principle

Comments reveal what the video itself leaves unresolved.

One dramatic comment is noise. Repeated patterns across videos and channels are signal. The job is to extract friction that is **operational, emotional, aesthetic, relational, structural, somatic, or functional** — and translate it into opportunity.

**New insight from AI friction analysis:** AI-generated music acts as a **diagnostic tool**. What AI cannot do well (unresolved endings, relational specificity, imperfect vocals, genuine pain) is exactly what the underserved audience wants. Use AI failures as negative space to define the opportunity.

## Worker Roles

| Worker | Role | Responsibility |
| :--- | :--- | :--- |
| **Vesper** | CEO | Owns the mining objective, synthesis, final judgment, and decides what gets actioned. Sets the strategic frame. |
| **Researcher** | Data Collector | Gathers comment threads, logs recurring phrases, identifies patterns across videos (including AI vs. human comparisons), and organizes evidence. |
| **Mark** | Marketing Specialist | Translates friction into audience language, positioning hooks, and messaging that resonates with the underserved. Now includes "Human-Guaranteed" and "Not AI" positioning. |
| **Conversion** | Customer Conversion Specialist | Turns friction into offer design: what product, service, lyric pack, or band positioning would convert the identified desire into action. Includes anti-AI differentiation. |
| **Blackquill** | Critic | Attacks weak evidence, overgeneralization, fake patterns, and emotional reasoning disguised as data. Kills noise. Specifically flags when "AI is soulless" is used as vague critique without specificity. |
| **Examiner** | Validator | Checks whether the identified friction is dense enough to act on, and whether proposed responses actually fit the evidence. Includes AI vs. human comparative validation. |

## Canonical YT Comment Friction Miner Object

```xml
<yt-comment-friction-miner>
  <objective>What kind of underserved audience or friction we are hunting for</objective>
  <scope>One video, one channel, or several related videos (including AI-generated music channels)</scope>
  <friction_focus>Confusion, failure, objection, wish, constraint, language, absence, or AI-comparative</friction_focus>
  <workers>
    <worker name="Vesper">CEO: owns objective, synthesis, final judgment</worker>
    <worker name="Researcher">Data: gathers comments, logs patterns, includes AI vs. human contrasts</worker>
    <worker name="Mark">Marketing: audience language, positioning hooks, "Human-Guaranteed" framing</worker>
    <worker name="Conversion">Offer design: turns friction into product/service, including anti-AI differentiation</worker>
    <worker name="Blackquill">Critic: kills weak patterns and noise, flags vague "soulless" critiques</worker>
    <worker name="Examiner">Validator: checks density, fit, and AI vs. human comparative validity</worker>
  </workers>
  <target_niche>e.g., underserved gothic metal fans, AI-music listeners, genre-gap hunters</target_niche>
  <target_friction_type>e.g., emotional, aesthetic, relational, genre-boundary, somatic, functional-demotion</target_friction_type>
</yt-comment-friction-miner>