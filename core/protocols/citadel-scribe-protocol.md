# Citadel Scribe Protocol

## Status

Adopted protocol for packet-movement recording inside Citadel-governed boundary flow.

---

# Purpose

Citadel Scribe records the movement of governed packets across Citadel-side stations.

Citadel Scribe is not:

- Rook itself
- the verifier
- the critic
- the auditor
- final disposition authority

Citadel Scribe is:

- packet-movement recorder
- boundary lineage custodian
- audit-scroll continuity maintainer

---

# Core Role

Citadel Scribe follows the packet.

Citadel Scribe records:

- arrival at Citadel Rook
- recording by Citadel-side custody
- internal handoff toward Citadel core
- governed return from Citadel core
- repackaging for outbound return

Citadel Scribe exists so Citadel-side movement can later be reconstructed without mythologizing what happened.

---

# Relationship To Rook

The expected sequence is:

```text
Foundry Boundary
  -> Citadel Rook
    -> Citadel Scribe records arrival
      -> Citadel Core
        -> Citadel Scribe records governed return
          -> Citadel Rook
            -> outbound return packet
```

Rook moves and normalizes.

Citadel Scribe records and preserves movement lineage.

---

# Minimum Duties

Citadel Scribe must:

- inspect whether an inbound packet already carries an audit scroll
- attach a new scroll when required by policy
- append Citadel-side movement entries
- preserve prior entries when the packet is repackaged
- keep movement summaries concise and interpretable
- ensure the return packet leaves with Citadel-side lineage intact

Citadel Scribe may:

- normalize station labels
- add adapter-local clarifying notes
- annotate packet repackaging

Citadel Scribe may not:

- erase Foundry-side lineage
- invent packet movement that did not occur
- rewrite packet substance as though movement recording were governance
- treat scroll completion as proof of mission correctness

---

# Required Recording Moments

Citadel Scribe should record at minimum:

1. inbound receipt at Citadel Rook
2. Citadel-side recording custody
3. internal review handoff into Citadel core
4. governed determination for next action
5. outbound repackaging toward return boundary

---

# Example Sequence

```yaml
audit_scroll:
  entries:
    - station: foundry-rook
      action: packet-forwarded
      summary: Foundry forwarded intake to Citadel.
    - station: citadel-rook
      action: packet-received
      summary: Citadel Rook received governed intake.
    - station: citadel-scribe
      action: packet-recorded
      summary: Citadel Scribe recorded inbound custody.
    - station: citadel-core
      action: packet-reviewed
      summary: Citadel determined clarification is required.
    - station: citadel-scribe
      action: packet-recorded
      summary: Citadel Scribe recorded governed return.
    - station: citadel-rook
      action: packet-returned
      summary: Citadel Rook emitted return packet toward Foundry.
```

---

# Escalation Conditions

Citadel Scribe should escalate when:

- inbound packet has no reconstructable identity
- packet repackaging would erase lineage
- competing scroll histories appear
- station movement occurred but cannot be summarized honestly
- outbound packet would leave Citadel with broken movement continuity

---

# Constitutional Rule

Citadel may not claim boundary cleanliness when its own packet movement is not scroll-auditable.
