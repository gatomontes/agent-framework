# Audit Scroll Schema

## Status

Canonical Citadel contract.

This schema defines the traveling audit companion that follows a packet across boundary stations, governed routing surfaces, review points, and return flow.

The audit scroll exists so packet movement remains reconstructable without relying on recollection, chat fragments, or inferred timeline repair.

---

# Purpose

Citadel already requires:

- inspectable packets
- artifact lineage
- audit continuity
- recoverable state

The audit scroll binds those requirements to packet movement itself.

It records:

- where a packet traveled
- who recorded it
- what transition occurred
- why the transition happened

The audit scroll is not a replacement for evidence artifacts, verification reports, or status schemas.

It is the movement lineage layer for governed packets.

---

# Core Principle

A packet that crosses stations without preserved movement lineage has boundary ambiguity.

Boundary ambiguity weakens:

- audit reconstruction
- restoration
- escalation legitimacy
- return-packet trustworthiness

Therefore:

```text
packet movement must remain scroll-bearing
```

---

# Scroll Scope

An audit scroll may accompany:

- rook intake packets
- rook return packets
- delegation packets
- restoration packets
- verification-bearing packets
- boundary clarification packets
- production-ready mission orders returned to implementation layers

The exact serialization may vary by runtime or adapter.

The semantic burden may not disappear.

---

# Required Schema

Every governed audit scroll should be recoverable in this shape:

```yaml
audit_scroll:
  scroll_id: null
  packet_id: null
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

## `packet_id`

Current packet identity the scroll is attached to.

If the packet is repackaged, the scroll should preserve continuity rather than resetting.

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
packet-created
packet-forwarded
packet-received
packet-recorded
packet-reviewed
packet-repackaged
packet-returned
```

Additional action classes are allowed when they improve reconstruction without obscuring meaning.

---

# Scroll Rules

The audit scroll must:

- travel with the packet
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

- packet crosses boundary with no scroll
- packet is repackaged with erased prior entries
- station movement occurs without recorded entry
- return packet lacks inbound lineage continuity
- scroll exists but is too vague to reconstruct movement

---

# Constitutional Rule

If packet movement cannot be reconstructed, boundary trust is degraded even when packet contents appear complete.
