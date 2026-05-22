# Environment And Secret Dependencies

This file extracts the environment-specific and secret-bearing dependencies found in `openclaw/` and `codex/`.

These are not doctrine.

They are dependency liabilities that must be either relocated, abstracted, or killed before the source trees can disappear safely.

## 1. Plaintext Secret Dependence

Observed in:

- `openclaw/TOOLS.md`
- messaging and external-service skill material inside `openclaw/`

Dependency pattern:

- skills assume secrets are stored in readable workspace prose
- downstream usage depends on that insecure storage habit

Citadel extraction:

- secrets must be externalized from repo docs
- any surviving skill should depend on named secret inputs, not embedded tokens
- boundary doctrine should explicitly forbid plaintext credentials in tracked workspace artifacts

## 2. Local Machine Path Dependence

Observed in:

- `C:\Users\gatom\.openclaw\...`
- `C:\Users\gatom\.codex\...`
- `E:\ai\openclaw\...`
- `E:\htdocs\nomina\codex\...`
- `~/.openclaw/...`

Dependency pattern:

- skill behavior is coupled to one operator’s filesystem
- instructions mix durable operating rules with local path residue

Citadel extraction:

- path assumptions must be rewritten as:
  - workspace-relative paths
  - configured adapter roots
  - explicit required inputs
- any surviving skill pattern should separate:
  - constitutional rule
  - adapter configuration
  - local operator path

## 3. Workspace-Service Dependence

Observed in:

- Chat Gateway outbox paths
- reminder event storage
- Mail Gateway workspace runtime
- Nomina backup/restore script paths

Dependency pattern:

- useful operational flows exist, but they are inseparable from local service placement

Citadel extraction:

- preserve the workflow pattern, not the machine-specific location
- rewrite as:
  - required service
  - required artifact locations by role
  - configurable adapter variables

## 4. External Header / Client Identity Dependence

Observed in:

- `X-HereNow-Client: codex/cli`
- `X-HereNow-Client: openclaw/direct-api`

Dependency pattern:

- external integrations preserve runtime/client identity at the HTTP boundary

Citadel extraction:

- boundary-facing integrations may need explicit client identity headers
- those headers belong in adapter contracts, not doctrinal truth

## 5. Security Verdict

The ugliest dependency in both trees is not runtime flavor.

It is the habit of mixing:

- secrets
- local machine paths
- active operational instructions

in the same tracked skill material.

That pattern should not survive deletion planning.

