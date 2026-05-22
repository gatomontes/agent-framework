---
name: chat-gateway
description: OpenClaw skill for designing Chat Gateway Bot API workflows and command-driven conversations using direct HTTPS requests (no SDKs).
---

# Chat Gateway Bot Skill (Advanced)

## Purpose
Provide a clean, production-oriented guide for building Chat Gateway bot workflows via the Bot API, focusing on command UX, update handling, and safe operations using plain HTTPS.

## Best fit
- You want a command-first bot that behaves professionally.
- You need a reliable update flow (webhook or polling).
- You prefer direct HTTP calls instead of libraries.

## Not a fit
- You require a full SDK or framework integration.
- You need complex media uploads and streaming in-process.

## Quick orientation
- Read `references/chat-gateway-bot-api.md` for endpoints, update types, and request patterns.
- Read `references/chat-gateway-commands-playbook.md` for command UX and messaging style.
- Read `references/chat-gateway-update-routing.md` for update normalization and routing rules.
- Read `references/chat-gateway-request-templates.md` for HTTP payload templates.
- Keep this SKILL.md short and use references for details.

## Required inputs
- Bot token and base API URL.
- Update strategy: webhook or long polling.
- Command list and conversation tone.
- Allowed update types and rate-limit posture.

## Expected output
- A clear command design, update flow plan, and operational checklist.

## Operational notes
- Prefer strict command routing: `/start`, `/help`, `/settings`, `/status`.
- Always validate incoming update payloads and chat context.
- Handle 429s with backoff and avoid message bursts.

## Security notes
- Never log tokens.
- Use webhooks with a secret token header when possible.

