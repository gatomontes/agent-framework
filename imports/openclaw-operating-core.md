# OpenClaw Operating Core

## Source Focus

- `openclaw/AGENTS.md`
- `openclaw/USER.md`
- `openclaw/IDENTITY.md`
- `openclaw/TOOLS.md`

## What Survives

### 1. Session bootstrap discipline

Useful pattern:

- begin by loading role, user, and recent continuity artifacts
- prefer explicit workspace files over conversational memory
- treat startup as operational initialization, not improvisation

Citadel-worthy translation:

- a runtime/session bootstrap protocol should explicitly name which continuity artifacts load first
- long-term memory should be gated by context and authority
- session startup should happen before active execution begins

### 2. Memory as written state, not vibe

Useful pattern:

- if something must persist, write it
- daily notes and curated long-term memory serve different purposes
- lessons learned should update system artifacts, not just logs

Citadel-worthy translation:

- transient chat is not durable institutional state
- raw operational logs and curated memory should remain distinct
- mistakes should create doctrine, tool, or workflow updates where appropriate

### 3. Internal vs external action boundary

Useful pattern:

- reading, organizing, inspecting, and local work can often proceed freely
- public/external actions need explicit approval

Citadel-worthy translation:

- external communication authority must remain separate from internal analysis authority
- the system should distinguish local inspection from outward action at the boundary

### 4. Group-context privacy discipline

Useful pattern:

- access does not imply permission to disclose
- context ownership changes in shared spaces

Citadel-worthy translation:

- authority to know is not authority to reveal
- multi-party contexts need disclosure discipline at the wall

## What Does Not Survive As Doctrine

### Identity scaffolding

- agent name
- vibe
- creature/persona flavor
- emoji/avatar conventions

Reason:

This is local identity dressing, not constitutional machinery.

### Plaintext secrets in workspace docs

`TOOLS.md` contains direct credentials and tokens.

Reason:

This is not just non-doctrinal; it is operationally reckless.

Citadel should preserve the inverse lesson:

- credentials must not live in doctrine-facing workspace notes
- secret handling belongs in controlled secret stores or bounded runtime configuration

## Recommended Citadel Follow-Ons

- create a core bootstrap doctrine for session initialization and continuity loading
- create a memory-discipline artifact separating raw logs from curated institutional memory
- create a boundary-security rule that forbids plaintext credential storage in shared operational docs
