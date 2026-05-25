# Source Verification Protocol

## Status

Adopted Citadel protocol.

This protocol governs how Citadel evaluates the provenance, freshness, independence, and trust posture of sources used in evidence-bearing operations.

---

# Purpose

Citadel must not treat all cited material as equally trustworthy merely because it is available.

This protocol exists to ensure that source-backed claims remain:
- provenance-aware
- freshness-aware
- contradiction-preserving
- independence-conscious
- auditable

---

# Core Principle

A cited source is not automatically a trusted source.

Evidence quality depends on:
- what the source is
- where it came from
- how directly it supports the claim
- whether it is independent of other cited material
- whether it is current enough for the consequence tier

---

# Verification Requirements

When a source materially supports an operational claim, the verifying actor should assess:
- source identity
- authorship or originating authority when available
- publication or revision date when available
- proximity to the underlying fact
- independence from other cited sources
- whether the source is primary, secondary, or derivative
- whether contradictory sources exist

When these attributes cannot be fully determined, the uncertainty must be preserved rather than concealed.

---

# Source Classes

Citadel may classify sources as:

```txt
PRIMARY
SECONDARY
DERIVATIVE
OPERATIONAL
UNVERIFIED
```

- `PRIMARY` means the source is close to the originating event, record, system, or authority.
- `SECONDARY` means the source interprets or summarizes primary material.
- `DERIVATIVE` means the source largely repeats or reformats other reporting.
- `OPERATIONAL` means the source is an internal runtime artifact, log, contract, scroll, or report.
- `UNVERIFIED` means provenance or independence could not be established sufficiently.

---

# Freshness Rule

Source freshness must scale with consequence and subject matter.

For time-sensitive claims, stale but otherwise reputable sources may still be inadequate.

When freshness is uncertain or insufficient, the verifier should:
- preserve the source with a caveat
- narrow the claim
- seek a fresher source
- or escalate the uncertainty

---

# Independence Rule

Multiple citations do not constitute independent support when they collapse to the same upstream source.

Verification should note when apparent corroboration is actually:
- syndicated repetition
- shared derivation
- circular citation
- or common-source amplification

---

# Contradiction Rule

Conflicting sources must not be silently reconciled.

When contradiction appears, Citadel should preserve:
- the contradiction itself
- the confidence impact
- the likely reasons for divergence when inferable
- and the resulting release constraint

---

# Output Expectations

Source verification should emit a durable artifact or embedded section that records:
- the claim under review
- the cited sources
- source class
- freshness assessment
- independence assessment
- known contradictions
- residual uncertainty
- verifier conclusion

Serialization may vary, but auditability must remain intact.

---

# Final Rule

Source-backed trust requires more than citation density.

Citadel must care not only that a claim was sourced, but that the source itself was fit to bear consequence.
