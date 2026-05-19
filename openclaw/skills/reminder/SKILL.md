---
name: reminder
description: Capture natural-language reminders, meetings, birthdays, deadlines, and upcoming plans; store event data in the workspace; schedule reminder delivery via OpenClaw cron; answer upcoming-schedule queries. Use when the user asks to remember something for later, requests a reminder, mentions an event/date to keep, or asks what is coming up.
---

# Reminder

Capture reminders and future events into workspace data, then schedule actual reminder delivery with `cron`.

## Data location

Store user reminder data in:
- `C:\Users\gatom\.openclaw\workspace\reminders\events.yml`

If the file does not exist, create it from the template in `assets/events.template.yml`.

## Core behavior

When the user asks for a reminder or mentions a future event:

1. Parse the event as tightly as possible:
   - title
   - date/time
   - timezone
   - notes (optional)
   - reminder offsets (optional)
   - recurrence (optional)
2. If essential information is ambiguous, ask only the minimum clarifying question.
3. Write or update the structured event in `reminders/events.yml`.
4. Create real `cron` jobs for reminder delivery.
5. Confirm briefly with the resolved time and what was scheduled.

## Timezone

Default to the session/user timezone unless the user explicitly gives another timezone.
Do not default to Shanghai or any unrelated timezone.

## Reminder delivery rules

- Prefer real `cron` scheduling for reminders.
- Never fake reminders with `sleep`, local timers, or delayed shell commands.
- If `cron` is unavailable in the current session, say so plainly.
- Reminder text written into `cron` should read naturally as a reminder when it fires.

## Suggested default offsets

If the user does not specify offsets, use context-appropriate defaults:
- short event: one reminder near the event time
- important appointment: multiple reminders may be appropriate
- birthday/deadline: choose reasonable advance notice

Do not over-schedule without reason.

## Queries

If the user asks what is coming up, read `reminders/events.yml`, interpret timestamps in the active timezone, and summarize upcoming items clearly.

## Changes and cancellations

When an event changes:
- update the stored event
- replace or remove affected cron jobs
- confirm what changed

When an event is cancelled:
- remove or disable associated reminder jobs
- confirm cancellation clearly

## Safety and quality

- Keep reminder data in workspace files, not in the skill itself.
- Do not store secrets in reminder files.
- Keep replies brief and concrete.
- Prefer one solid reminder over several noisy ones unless the user asked for multiple.
