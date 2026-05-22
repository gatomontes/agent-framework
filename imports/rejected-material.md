# Rejected Material Ledger

This file records what should *not* be imported into Citadel core.

## Rejection Classes

### 1. Plaintext secrets

Observed in:

- `openclaw/TOOLS.md`

Reason:

- operationally unsafe
- not doctrine
- not portable
- actively contaminating

Citadel lesson:

- secret handling should be governed by boundary controls and secure storage, never workspace prose

### 2. Identity theater

Observed in:

- `openclaw/IDENTITY.md`
- `openclaw/SOUL.md`
- related persona dressing at workspace root

Reason:

- local flavor is not constitutional machinery
- persona costume tends to smuggle authority through aesthetics

### 3. Local-path fetish

Observed throughout both trees.

Reason:

- hardcoded user-specific paths are implementation residue
- useful only when rewritten into abstract boundary or adapter rules

### 4. Runtime-specific mythology

Observed in:

- local role names
- family-specific orchestration language
- runtime-branded assumptions about behavior

Reason:

- Citadel should own the law, not inherit the accent

### 5. Duplicated or stale parallel skill variants

Observed in:

- custom prompt variants
- copied snapshots preserved for backward compatibility
- alternate wording files with overlapping purpose

Reason:

- they inflate noise
- they obscure the actual surviving rule

## Deletion Test

If a file disappeared tomorrow and the only loss would be:

- style
- nostalgia
- local convenience
- runtime-specific flavor
- duplicated wording

then it is not Citadel material.
