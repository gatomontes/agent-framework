# Communication Boundary Protocol

## Status

Canonical AFW protocol.

This protocol governs how Citadel-adjacent runtimes and adapters prepare, persist, route, and release boundary-crossing communications and reminders.

---

# Purpose

This protocol exists to prevent:
- external messages being sent directly from ambiguous internal state
- boundary-crossing communication losing auditability
- reminder and event state existing only in transient chat
- delivery behavior being improvised at send time
- communication requests bypassing authority and staging rules

---

# Core Principle

Drafting is not sending.

Scheduling is not delivery.

Boundary-crossing communication should be staged, inspectable, and governable before release.

---

# Communication Boundary Object

When a communication-bearing mission crosses the wall, it should be representable through a durable boundary object that preserves:
- message objective
- intended recipient or channel class
- authority basis
- source request
- staged payload
- release conditions
- delivery status
- audit references

Serialization may vary.

Semantic recoverability must remain intact.

---

# Staged Outbox Rule

Boundary-facing communications should use a staged outbox or equivalent durable holding surface before external send when:
- the message has external consequence
- a file, payload, or rendered artifact must be transmitted
- release timing matters
- multiple actors may inspect or approve the send

The staged object should preserve:
- payload reference
- destination reference
- creation time
- release status
- cleanup rule

Staging prevents send-time improvisation from becoming invisible institutional action.

---

# Update Routing Rule

Incoming communication updates, events, or callbacks should be normalized before they affect active work.

Routing should preserve:
- source identity when available
- update class
- payload reference
- continuity reference
- ambiguity or parse failure
- recommended next action

Unparsed or ambiguous updates must remain visible as uncertainty rather than disappearing into best-effort handling.

---

# Request Template Rule

Communication-capable adapters may use templates, payload scaffolds, or request playbooks.

Templates may guide consistency.

They do not replace authority, verification, or release conditions.

---

# Reminder And Event Persistence Rule

Reminders, scheduled follow-ups, and future events should persist as durable workspace data rather than transient conversational promises.

Persistence should preserve:
- event identity
- human-readable intent
- scheduled time or trigger
- reminder offsets when applicable
- status
- mutation history when materially changed

Scheduling metadata should remain reconstructable.

---

# Release Rule

No external send should occur unless:
- external communication authority exists
- staged payload is coherent enough to release
- destination or channel class is explicit enough to audit
- required approval or verification gates have been satisfied

If these conditions are missing, the communication should remain staged, be escalated, or be returned through `Rook` as blocked.

---

# Cleanup Rule

After confirmed delivery, staged communication artifacts may be cleaned up, archived, or superseded according to mission requirements.

Cleanup must not erase:
- proof that something was staged
- proof that it was released or withheld
- relevant audit references

---

# Constitutional Rule

Communication across the wall is an institutional act.

It must remain staged, durable, and auditable enough to govern.
