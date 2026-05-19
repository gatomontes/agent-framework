# Tiered Verification Doctrine

**Status:** Adopted  
**Classification:** Core Doctrine  
**Effective:** Immediately

---

# Principle

Not all operations require the same verification intensity.

Verification requirements must scale according to consequence.

The framework therefore defines consequence tiers governing:
- verification depth
- independence requirements
- confidence thresholds
- escalation behavior
- exemption policy

---

# Consequence Tiers

```yaml
critical:
  description: "Life, legal, financial, security, or reputation-impacting operations"
  verification_required: "full_independent_channel"
  independence_minimum: "different_runtime"
  confidence_required: 0.95
  exemption: false

important:
  description: "Architecture decisions, persistent state changes, external API writes"
  verification_required: "retrieval_backed"
  independence_minimum: "different_persona"
  confidence_required: 0.85
  exemption: "requires written justification"

routine:
  description: "Internal transformations, formatting, non-critical reads"
  verification_required: "sampling"
  sampling_rate: 0.10
  confidence_required: 0.70
  exemption: "default allowed"

trivial:
  description: "Logging, status checks, no-side-effect operations"
  verification_required: "none"
  confidence_required: 0.0
  exemption: "automatic, but logged"
```

---

# Verification Tracking

```yaml
verification_tracking:
  - log_all_skipped_verifications
  - alert_if_skip_rate_exceeds: 0.30
  - require_review_if_critical_skip_attempted
```

---

# Independence Philosophy

Verification quality depends on independence.

The following are considered weak verification patterns:
- same runtime
- same session
- same reasoning path
- same memory context
- same persona assumptions

Higher-consequence operations require greater cognitive separation.

---

# Operational Rule

Verification cost is acceptable.

Unverified critical operations are not.

The framework prioritizes:
- trustworthiness over speed
- evidence over convenience
- resilience over throughput
