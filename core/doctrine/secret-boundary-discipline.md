# Secret Boundary Discipline

## Status

Canonical AFW doctrine.

This doctrine defines how credentials, tokens, secrets, and sensitive runtime configuration must be treated at Citadel boundary surfaces and inside shared operational artifacts.

---

# Purpose

This doctrine exists to prevent:
- plaintext secrets in shared workspace documents
- doctrine artifacts becoming secret stores
- disclosure authority being confused with possession
- boundary compromise through convenience notes

---

# Core Principle

Access is not disclosure authority.

Shared operational artifacts must not function as secret containers.

---

# Prohibited Storage

The following must not appear in shared operational docs, doctrine files, protocol files, import ledgers, or other broadly readable workspace notes:
- API keys
- bearer tokens
- passwords
- private keys
- session secrets
- webhook secrets
- production connection strings

If a secret is needed operationally, it belongs in a controlled secret store or bounded runtime configuration.

---

# Boundary Rule

Citadel may govern the handling of secrets.

It must not normalize the casual publication of secrets inside durable shared artifacts.

Secret-bearing material discovered during import, review, or restoration should be:
- redacted
- relocated to proper secret storage when still needed
- reported as a boundary hygiene failure

---

# Shared Context Rule

Multi-party or shared contexts require disclosure discipline.

Authority to inspect is not authority to relay.

Authority to hold a secret operationally is not authority to publish it into institutional memory.

---

# Final Rule

Plaintext secrets in shared operational artifacts are constitutional failure at the wall.
