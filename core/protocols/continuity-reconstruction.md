# Citadel Continuity Reconstruction Protocol

## Purpose

The Continuity Reconstruction Protocol defines how a runtime or operator should recover the current state of work when continuity is uncertain, stale, or partially lost.

It exists to restore responsible continuation without pretending memory is sufficient.

---

# Core Principle

Reconstruction begins with artifacts, not recollection.

If continuity must be recovered, inspect the durable record before trusting memory or narrative.

---

# Reconstruction Order

Recover state in this order:

1. identify the active operation or project root
2. read high-signal root artifacts
3. inspect recent relevant artifacts
4. use targeted search to resolve ambiguity
5. read supporting materials only when they clarify the current direction

Prefer:

- current mission artifacts
- plans
- status notes
- decisions
- logs
- restoration packets
- recent review outputs

Avoid broad context loading when a smaller evidence surface is enough.

---

# Recovery Targets

Reconstruction should recover, when possible:

- project or operation purpose
- current phase
- active workstream
- last meaningful decisions
- open questions or blockers
- pending next actions
- important constraints
- whether the context is planning, execution, restoration, or review

When sources conflict, prefer the most recent explicit controlling artifact and preserve the uncertainty.

---

# Stop Condition

Reconstruction should stop once there is enough evidence to continue responsibly.

More context is not always better.

Loading irrelevant historical debris is another form of continuity failure.

---

# Constitutional Rule

If current state cannot be reconstructed from artifacts, continuity remains compromised and continuation should not masquerade as informed operation.
