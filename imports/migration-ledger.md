# Migration Ledger

This ledger explains why `./imports` is now sufficient to rebuild or retire the surviving value in `openclaw/` and `codex/` without re-opening those trees.

## What Was Captured

### 1. Distilled extraction artifacts

The following files preserve the surviving patterns, rules, and dependency classes:

- `openclaw-operating-core.md`
- `openclaw-routing-and-critique.md`
- `codex-execution-disciplines.md`
- `research-and-persona-conversion.md`
- `runtime-tree-dependencies.md`
- `environment-and-secret-dependencies.md`
- `reference-and-script-dependencies.md`
- `cross-tree-couplings.md`
- `rejected-material.md`

### 2. Frozen source snapshots

The following directories preserve the original source material needed for exact reconstruction work:

- `source-openclaw/`
- `source-codex/`

These are local import archives, not living constitutional namespaces.

Their purpose is to let Citadel rebuild, translate, or discard artifacts without consulting the original trees again.

### 3. Machine-readable manifests

- `source-openclaw-manifest.json`
- `source-codex-manifest.json`

These manifests preserve file paths and sizes for audit, comparison, and completeness checks.

## What Was Redacted

Known plaintext secret-bearing material was preserved only in redacted form inside:

- `source-openclaw/TOOLS.md`

The redaction preserves dependency knowledge without preserving live credentials.

## Sufficiency Standard

`./imports` should be treated as sufficient for the next phase if the team needs to:

- reconstruct useful doctrine from the old trees
- rebuild surviving skill/reference/script bundles
- compare duplicate capability families and choose canonical winners
- preserve provenance while deleting the original trees
- audit what was intentionally rejected

## Remaining Work

This archive does **not** mean the migration is complete.

It means the source trees no longer need to remain open as active dependency surfaces.

The remaining work is:

1. translate surviving patterns into Citadel-owned artifacts
2. canonicalize duplicate capability families
3. scrub repo references to `openclaw/` and `codex/`
4. delete the original trees
5. remove `./imports` only after Citadel-owned replacements are stable

## Counts

- `source-openclaw/`: 86 files
- `source-codex/`: 115 files

## Verdict

`./imports` is now a working extraction archive rather than a partial notes folder.

If `openclaw/` and `codex/` are later deleted, the migration should proceed from `./imports`, not by reopening those trees.
