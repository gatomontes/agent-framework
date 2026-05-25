# Citadel Scribe Protocol

## Status

Adopted protocol for scroll-movement recording inside Citadel-governed boundary flow.

---

# Purpose

Citadel Scribe records the movement of governed scrolls across Citadel-side stations.

Citadel Scribe is not:

- Rook itself
- the verifier
- the critic
- the auditor
- final disposition authority

Citadel Scribe is:

- scroll-movement recorder
- boundary lineage custodian
- audit-scroll continuity maintainer

---

# Core Role

Citadel Scribe follows the scroll.

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
            -> outbound return scroll
```

Rook moves and normalizes.

Citadel Scribe records and preserves movement lineage.

---

# Minimum Duties

Citadel Scribe must:

- inspect whether an inbound scroll already carries an audit scroll
- attach a new scroll when required by policy
- append Citadel-side movement entries
- preserve prior entries when the scroll is repackaged
- keep movement summaries concise and interpretable
- ensure the return scroll leaves with Citadel-side lineage intact

Citadel Scribe may:

- normalize station labels
- add adapter-local clarifying notes
- annotate scroll repackaging

Citadel Scribe may not:

- erase Foundry-side lineage
- invent scroll movement that did not occur
- rewrite scroll substance as though movement recording were governance
- prepare substantive station findings in place of Notary
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
      action: scroll-forwarded
      summary: Foundry forwarded intake to Citadel.
    - station: citadel-rook
      action: scroll-received
      summary: Citadel Rook received governed intake.
    - station: citadel-scribe
      action: scroll-recorded
      summary: Citadel Scribe recorded inbound custody.
    - station: citadel-core
      action: scroll-reviewed
      summary: Citadel determined clarification is required.
    - station: citadel-scribe
      action: scroll-recorded
      summary: Citadel Scribe recorded governed return.
    - station: citadel-rook
      action: scroll-returned
      summary: Citadel Rook emitted return scroll toward Foundry.
```

---

# Escalation Conditions

Citadel Scribe should escalate when:

- inbound scroll has no reconstructable identity
- scroll repackaging would erase lineage
- competing scroll histories appear
- station movement occurred but cannot be summarized honestly
- outbound scroll would leave Citadel with broken movement continuity

---

# Constitutional Rule

Citadel may not claim boundary cleanliness when its own scroll movement is not scroll-auditable.
