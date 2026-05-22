# Cross-Tree Couplings

This file extracts the places where `openclaw/` and `codex/` are not merely parallel trees, but actively depend on each other or reflect the same capability in duplicated form.

## 1. Direct Cross-Tree References

### Codex -> OpenClaw doctrine path

Observed in:

- `codex/skills/web-research-lead/SKILL.md`

Pattern:

- a Codex skill explicitly points to doctrine in an OpenClaw environment path

Citadel consequence:

- doctrine should not live in one runtime family and be imported by path into another

Required extraction:

- capture the surviving research-desk doctrine in Citadel-owned form

### Shared Here-Now client identity references

Observed in:

- `codex/skills/here-now/references/REFERENCE.md`
- `openclaw/skills/here-now/references/REFERENCE.md`

Pattern:

- both trees preserve the same integration family with runtime-specific client identity variants

Citadel consequence:

- the shared integration contract should survive as one Citadel-owned adapter reference, not two sibling runtime copies

## 2. Duplicated Capability Families

Observed in both trees:

- `blackquill`
- `persona-builder`
- `design-system-extractor`
- `here-now`

Pattern:

- same conceptual capability appears twice with different local idioms and dependency surfaces

Citadel consequence:

- duplicate trees are concealing a canonicalization problem

Required extraction:

- identify the strongest surviving rule set
- keep one Citadel-owned canonical version
- record adapter-specific deviations only when truly necessary

## 3. Codex Tree Internal Dependency Hotspots

Observed in:

- `ceo/` -> `references/persona-factory-reference.md`
- `persona-builder/` -> `references/builder-reference.md`
- `persona-publisher/` -> `references/publisher-reference.md`
- `persona-to-skill/` -> `references/conversion-reference.md`
- `researcher/` -> `references/researcher-revised.md`

Pattern:

- the codex tree contains small local ecosystems that are self-consistent and useful, but deletion will break them unless the reference bundles are preserved

## 4. OpenClaw Tree Internal Dependency Hotspots

Observed in:

- communication reference sets
- `design-system-extractor/` scripts plus references
- `web-demo-builder/` systems and assets
- `here-now/` scripts plus references
- `tiktok-scraping/` scripts

Pattern:

- openclaw contains more operationally messy but still valuable bundles where scripts, references, and assets form one capability

## 5. Canonical Migration Rule

When the same capability exists in both trees:

1. do not preserve both
2. do not average them into mush
3. choose the stronger constitutional pattern
4. preserve the better supporting references/scripts
5. reissue one Citadel-owned canonical artifact

That is how you extract value without importing schizophrenia.
