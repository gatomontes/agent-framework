# Runtime Independence Doctrine

Citadel must never depend on a single runtime outside its boundary wall.

The framework exists above runtimes.

Runtimes are interchangeable execution substrates.

Doctrine is the invariant.

This does not mean Citadel is internally uncoupled.

It means Citadel remains externally decoupled from the runtimes and implementations attached through adapters and boundary surfaces.

This doctrine does not require the repository layout to look implementation-neutral.

Citadel may keep concrete adapter families in-repo while those implementations remain:

- boundary-scoped
- replaceable
- non-authoritative with respect to doctrine
- subordinate to the constitutional core

## Canonical Position

```txt
Citadel
  -> doctrine
  -> contracts
  -> governance
  -> orchestration semantics
  -> verification semantics

Runtime Adapters
  -> interactive coding runtime
  -> orchestration runtime
  -> retrieval-backed runtime
  -> future runtimes
```

Strategic Operators are doctrinal roles, not runtime identities.

Persona Factory compiles organizational topology, not runtime-specific personalities.

All runtime references inside Citadel must remain:
- replaceable
- adapter-oriented
- non-authoritative
- implementation-scoped
