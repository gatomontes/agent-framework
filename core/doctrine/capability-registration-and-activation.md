# Capability Registration And Activation

## Status

Canonical Citadel doctrine.

This document defines the distinction between creating a reusable capability, registering it as available infrastructure, and activating it for present operational use.

---

# Purpose

This doctrine exists to prevent:
- treating installation as permission
- hiding authority expansion inside reusable tooling
- confusing artifact conversion with operational authorization
- activating capabilities without mission fit
- runtime convenience masquerading as governance

---

# Core Principle

Capability existence is not capability authority.

Creation, registration, availability, delegation, and activation are separate governance events.

---

# Definitions

## Capability Artifact

A reusable operational object such as:
- skill
- protocol implementation
- automation template
- adapter wrapper
- verification utility
- execution scaffold

## Registration

Registration records that a capability exists, can be inspected, and may be selected in future work.

Registration does not authorize present use.

## Availability

Availability means the capability can be invoked by some runtime or adapter.

Availability does not authorize present use.

## Activation

Activation is the governed decision to use a capability in a specific mission, under explicit authority, scope, and constraints.

---

# Lifecycle Events

## 1. Creation

A capability may be created, converted, or imported as an artifact.

Creation answers:
- what it does
- what triggers it
- what outputs it produces
- what risks it carries
- what authority it assumes

## 2. Registration

A capability may be registered for future selection if its behavior is sufficiently documented.

Registration should preserve:
- capability identifier
- purpose
- expected inputs
- expected outputs
- supporting bundle components when materially required
- escalation conditions
- trust status
- provenance

## 3. Review

Capabilities with operational consequence should be reviewed before routine use.

Review may assess:
- behavioral clarity
- hidden authority assumptions
- evidence expectations
- failure modes
- doctrinal fit

## 4. Activation

Activation requires mission-specific authority.

Activation should answer:
- why this capability fits the mission
- who authorized its use
- what scope it may act within
- what outputs are expected
- what verification path will apply

## 5. Suspension Or Deprecation

Capabilities may be suspended, deprecated, or retired when they drift, conflict with doctrine, or no longer justify their risks.

---

# Conversion Rule

Converting a document, persona, workflow, or external artifact into reusable capability form is not the same as authorizing its current operational use.

Compression and conversion should preserve:
- triggers
- expected behavior
- outputs
- escalation paths

Presentation-only bulk should be discarded.

---

# Authority Rule

No actor may claim:
- "it is installed, therefore I may use it"
- "it exists, therefore it is approved"
- "it worked before, therefore it remains authorized"

Capability activation must be justified by mission authority, not local availability.

---

# Provenance Rule

Imported or converted capabilities should preserve enough provenance to answer:
- where it came from
- what was kept
- what was discarded
- what doctrinal changes were made

If the capability is bundle-backed, registration should also preserve the bundle structure defined by:

```txt
/core/doctrine/capability-bundle-governance.md
```

---

# Final Rule

Reusable infrastructure is governed inventory.

Inventory is not permission.
