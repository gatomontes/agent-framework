# Reference And Script Dependencies

This file extracts the dependency pattern where a skill is not self-contained, but depends on nearby references, scripts, assets, or generated support files.

That pattern is everywhere, and if ignored, deleting `openclaw/` and `codex/` will quietly amputate useful machinery.

## 1. Reference-Driven Skill Pattern

Observed in both trees:

- `references/*.md`
- `references/*.json`
- `references/*.yml`

Common value:

- output templates
- composition rules
- protocol examples
- site family heuristics
- command playbooks
- conversion mappings

Citadel extraction:

- many reusable capabilities need a small executable core plus a reference shelf
- doctrine should permit reference-backed skill design without confusing references for core law

## 2. Script-Backed Skill Pattern

Observed in both trees:

- `scripts/sample_site.py`
- `scripts/build_inventory.py`
- `scripts/generate_token.py`
- `scripts/fetch_transcript.py`
- `scripts/publish.sh`
- `scripts/vps-exec.py`

Common value:

- skills often rely on one or two concrete utilities to avoid prompt-only handwaving
- script-backed skills are more durable than prose-only instructions for repeatable operations

Citadel extraction:

- preserve the packaging pattern:
  - `SKILL.md`
  - `references/`
  - `scripts/`
  - optional `assets/`
- require that script dependency be explicit in the skill contract

## 3. Generated-Artifact Dependency Pattern

Observed in:

- `references/inventory.md`
- generated inventory notes
- sample-site coverage outputs implied by extractor skills

Common value:

- some capabilities rely on generated support artifacts that summarize a larger source tree

Citadel extraction:

- generated artifacts are legitimate supporting surfaces when:
  - their provenance is clear
  - their regeneration path is explicit
  - they are not mistaken for source of truth

## 4. Asset-Bundle Pattern

Observed in:

- extractor templates
- showcase CSS/JS/HTML bundles
- demo-builder systems

Common value:

- skills sometimes need bundled assets to produce repeatable outputs

Citadel extraction:

- bundled assets may survive as adapter assets or tool assets
- they should not be treated as doctrine, but neither should they be ignored as disposable noise

## 5. What Must Be Preserved Before Tree Deletion

Before deleting `openclaw/` or `codex/`, decide for every surviving capability whether Citadel will keep:

- the reference pattern
- the script pattern
- the asset-bundle pattern
- the generated-artifact pattern

If not, deletion is not extraction. It is just amnesia wearing a clean shirt.
