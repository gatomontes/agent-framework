---
name: token-gen
description: Generate cryptographically secure random tokens, especially hex strings comparable to `openssl rand -hex N`. Use when the user asks for a secret, API key seed, random hex token, webhook secret, bearer token seed, or similar random value and wants a specific byte length or output format.
---

# Token Gen

Generate the requested token directly instead of explaining how to do it unless the user asks for the command.

## Quick Start

- For requests like `openssl rand -hex 24`, run `python scripts/generate_token.py --bytes 24 --format hex`.
- For generic "generate a token" requests, default to `24` bytes and `hex` unless the user specifies otherwise.
- Return only the generated token in backticks when the user wants the value itself.

## Formats

- `hex`: Return two lowercase hex characters per byte.
- `base64`: Return standard Base64 text without line wrapping.

## Rules

- Use cryptographically secure randomness only.
- Never invent a token without generating it.
- If the user provides a byte count, preserve it exactly.
- If the user references `openssl rand -hex N`, match OpenSSL's byte semantics: `N` is bytes, not output characters.
- If the user asks for multiple tokens, generate each independently.

## Script

Use `scripts/generate_token.py` for deterministic execution.

Examples:

```bash
python scripts/generate_token.py --bytes 24 --format hex
python scripts/generate_token.py --bytes 32 --format base64
python scripts/generate_token.py --bytes 24 --format hex --count 3
```
