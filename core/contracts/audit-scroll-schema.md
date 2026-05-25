# Audit Scroll Schema

## Status

Canonical Citadel contract.

This schema defines the traveling audit companion that follows a scroll across boundary stations, governed routing surfaces, review points, and return flow.

The audit scroll exists so scroll movement remains reconstructable without relying on recollection, chat fragments, or inferred timeline repair.

---

# Purpose

Citadel already requires:

- inspectable scrolls
- artifact lineage
- audit continuity
- recoverable state

The audit scroll binds those requirements to scroll movement itself.

It records:

- where a scroll traveled
- who recorded it
- what transition occurred
- why the transition happened

The audit scroll is not a replacement for evidence artifacts, verification reports, or status schemas.

It is the movement lineage layer for governed scrolls.

---

# Core Principle

A scroll that crosses stations without preserved movement lineage has boundary ambiguity.

Boundary ambiguity weakens:

- audit reconstruction
- restoration
- escalation legitimacy
- return-scroll trustworthiness

Therefore:

```text
scroll movement must remain scroll-bearing
```

---

# Scroll Scope

An audit scroll may accompany:

- rook intake scrolls
- rook return scrolls
- delegation scrolls
- restoration scrolls
- verification-bearing scrolls
- boundary clarification scrolls
- production-ready mission orders returned to implementation layers

The exact serialization may vary by runtime or adapter.

The semantic burden may not disappear.

---

# Required Schema

Every governed audit scroll should be recoverable in this shape:

```yaml
audit_scroll:
  scroll_id: null
  attached_scroll_id: null
  mission_id: null
  entries:
    - at: null
      station: null
      action: null
      summary: null
```

---

# Required Entry Fields

## `scroll_id`

Stable identity for the scroll itself.

## `attached_scroll_id`

Current scroll identity the audit scroll is attached to.

If the scroll is repackaged, the audit scroll should preserve continuity rather than resetting.

## `mission_id`

Mission identity when available.

## `entries`

Ordered movement records.

Each entry should preserve:

- timestamp
- station
- action
- human-readable summary

---

# Recognized Stations

The initial station vocabulary should support at least:

```text
foundry-boundary
foundry-rook
foundry-scribe
citadel-rook
citadel-scribe
citadel-core
verification
critique
audit
restoration
return-boundary
```

Adapters may add runtime-local stations if they remain interpretable and auditable.

---

# Recognized Actions

The initial action vocabulary should support at least:

```text
scroll-created
scroll-forwarded
scroll-received
scroll-recorded
scroll-reviewed
scroll-repackaged
scroll-returned
```

Additional action classes are allowed when they improve reconstruction without obscuring meaning.

---

# Scroll Rules

The audit scroll must:

- travel with the scroll
- preserve prior entries during repackaging
- remain append-only during ordinary operation
- remain inspectable by auditors
- remain available to restoration processes

The audit scroll may not:

- silently discard prior movement history
- overwrite earlier entries for convenience
- split into multiple incompatible histories without explicit arbitration
- masquerade as verification evidence by itself

---

# Relationship To Rook

`Rook` owns boundary normalization.

The audit scroll owns boundary movement continuity.

Rook should attach or preserve the audit scroll before:

- forwarding intake into Citadel
- returning terminal outcomes
- repackaging clarification-bearing traffic

---

# Failure Conditions

Audit scroll failure includes:

- scroll crosses boundary with no scroll
- scroll is repackaged with erased prior entries
- station movement occurs without recorded entry
- return scroll lacks inbound lineage continuity
- scroll exists but is too vague to reconstruct movement

---

# Constitutional Rule

If scroll movement cannot be reconstructed, boundary trust is degraded even when scroll contents appear complete.
