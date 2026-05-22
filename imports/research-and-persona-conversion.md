# Research And Persona Conversion

## Source Focus

- `codex/skills/web-research-lead/SKILL.md`
- `codex/skills/persona-to-skill/SKILL.md`

## What Survives

### 1. Research as a governed desk, not casual search

Useful pattern from `web-research-lead`:

- set scope and release threshold before collection
- split discovery, verification, OSINT, document extraction, synthesis, and red-team review
- release only when evidence quality still supports the conclusion after adversarial review

Citadel-worthy translation:

- research should be treated as a quality system
- search does not equal trust
- synthesis does not equal release

### 2. Deadline pressure narrows scope, not evidence standards

Useful pattern:

- when time compresses, reduce scope rather than silently lowering truth requirements

Citadel-worthy translation:

- throughput pressure must not secretly rewrite evidence policy

### 3. Conversion separate from activation

Useful pattern from `persona-to-skill`:

- converting an artifact into a reusable capability is not the same as invoking it
- installation does not transfer execution authority
- capability availability and active authority should remain distinct

Citadel-worthy translation:

- artifact creation, registration, and activation are separate governance events
- turning something into reusable infrastructure does not authorize its present use

### 4. Compression over verbatim cloning

Useful pattern:

- when converting large artifacts into reusable forms, preserve triggers, behavior, outputs, and escalation
- discard presentation-only bulk

Citadel-worthy translation:

- useful imports should be compressed into execution-relevant form, not copied wholesale

## What Does Not Survive As Doctrine

- source path references to external personal environments
- Codex-specific installation defaults as constitutional assumptions

Reason:

The governance lesson is durable; the local install path is trivia.

## Recommended Citadel Follow-Ons

- create a formal doctrine for capability registration vs activation
- create a research-desk protocol that makes release criteria explicit before evidence work begins
- use these same rules when converting surviving material from `openclaw/` and `codex/` into Citadel-native assets
