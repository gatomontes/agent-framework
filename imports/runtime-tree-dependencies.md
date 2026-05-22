# Runtime Tree Dependencies

This file records the tree-level dependency patterns that still make `openclaw/` and `codex/` non-deletable.

## 1. OpenClaw Dependency Families

### Workspace-agent operating shell

Source cluster:

- `openclaw/AGENTS.md`
- `openclaw/USER.md`
- `openclaw/HEARTBEAT.md`
- `openclaw/MEMORY.md`
- `openclaw/TOOLS.md`

Dependency value:

- workspace bootstrap order
- heartbeat-driven background maintenance
- split between daily notes and curated memory
- internal vs external action boundary

Deletion impact if unextracted:

- Citadel loses the strongest in-repo model for workspace-state discipline

### Messaging and reminder surfaces

Source cluster:

- communication-boundary skill families
- `openclaw/skills/reminder/`

Dependency value:

- update-routing patterns
- request templates
- staged outbox pattern for external sending
- reminder/event persistence patterns

Deletion impact if unextracted:

- communication-boundary patterns vanish
- workspace outbox pattern disappears

### Publishing and extraction utilities

Source cluster:

- `openclaw/skills/here-now/`
- `openclaw/skills/design-system-extractor/`
- `openclaw/skills/web-demo-builder/`
- `openclaw/skills/youtube-transcript-fetcher/`
- `openclaw/skills/tiktok-scraping/`
- `openclaw/skills/vps-connect/`

Dependency value:

- publish-script pattern
- same-origin sampling pattern
- reference/example-driven skill shape
- utility-script coupling patterns

Deletion impact if unextracted:

- Citadel loses concrete examples of how a boundary-facing skill owns scripts, references, and output assets

## 2. Codex Dependency Families

### Execution-discipline and orchestration kernel

Source cluster:

- `codex/skills/senior-agentic-architect/`
- `codex/skills/ceo/`
- `codex/skills/chief-of-staff/`
- `codex/skills/project-loader/`
- `codex/skills/project-manager-kernel/`

Dependency value:

- ambiguity suppression
- negative-boundary discipline
- ownership/handoff rules
- execution-shape and routing decomposition
- evidence-first project resumption

Deletion impact if unextracted:

- Citadel loses its strongest repository-local execution governance patterns

### Research desk family

Source cluster:

- `codex/skills/web-research-lead/`
- `codex/skills/researcher/`
- `codex/skills/web-discovery-researcher/`
- `codex/skills/source-verification-analyst/`
- `codex/skills/open-web-osint-researcher/`
- `codex/skills/data-document-researcher/`
- `codex/skills/research-synthesis-writer/`
- `codex/skills/red-team-fact-checker/`

Dependency value:

- multi-role research desk decomposition
- release-threshold logic
- provenance and evidence-separation patterns

Deletion impact if unextracted:

- Citadel loses the cleanest in-repo example of governed research as a system rather than a search prompt

### Conversion and publishing chain

Source cluster:

- `codex/skills/persona-builder/`
- `codex/skills/persona-publisher/`
- `codex/skills/persona-to-skill/`

Dependency value:

- artifact-to-capability conversion
- activation vs installation distinction
- builder/publisher separation

Deletion impact if unextracted:

- Citadel loses a reusable model for converting governed artifacts into reusable operational capabilities

### Tool-backed skill families

Source cluster:

- `codex/skills/design-system-extractor/`
- `codex/skills/ui-kit-builder/`
- `codex/skills/material-kit-pro-local-elements/`
- `codex/skills/soft-ui-design-system-pro-local-elements/`
- `codex/skills/token-gen/`
- `codex/skills/here-now/`
- `codex/skills/nomina-db-backup/`
- `codex/skills/nomina-db-restore/`

Dependency value:

- reference plus script plus asset bundle pattern
- local system/tool coupling examples
- operational utility-skill structure

Deletion impact if unextracted:

- Citadel loses practical reference shapes for tool-backed skill packaging

## 3. Deletion Rule

Neither tree should be removed until the surviving value above is either:

- translated into Citadel-owned doctrine
- reissued as generic adapter guidance
- or deliberately abandoned with awareness of the loss
