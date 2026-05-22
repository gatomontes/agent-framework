# Senior Symfony Backend Engineer Proposed Draft

## Reviewed Target

- target: [SKILL.md](C:/Users/gatom/.codex/skills/senior-symfony-backend-engineer/SKILL.md)

## Findings

1. `[P1]` The skill is strong technically, but it does not define its non-role explicitly enough at first glance. A hurried agent could misread `senior backend engineer` as broad authority to redesign architecture, infer product policy, or fix data semantics by code alone. The current overview and rules constrain this later, but the opening still leaves room for an overreaching first interpretation. See [SKILL.md](C:/Users/gatom/.codex/skills/senior-symfony-backend-engineer/SKILL.md:10) and [SKILL.md](C:/Users/gatom/.codex/skills/senior-symfony-backend-engineer/SKILL.md:38).

2. `[P1]` The skill does not sharply separate implementation authority from product or policy authority near the top. That separation appears in the escalation rules, but the first-glance read still risks turning uncertain business semantics into implementation work. See [SKILL.md](C:/Users/gatom/.codex/skills/senior-symfony-backend-engineer/SKILL.md:49).

3. `[P2]` The output contract is solid but does not explicitly say what type of artifact it is not. It lists implementation concerns well, yet does not tell the reader that the output is an implementation plan or execution artifact, not a policy decision, not architecture redesign by default, and not data-governance sign-off. See [SKILL.md](C:/Users/gatom/.codex/skills/senior-symfony-backend-engineer/SKILL.md:57).

4. `[P2]` The quality bar enforces technical rigor but does not explicitly require escalation-boundary discipline when product rules, reporting semantics, or policy dependencies remain unresolved. Since the skill already says not to hide policy dependencies in code, that should be a named final check. See [SKILL.md](C:/Users/gatom/.codex/skills/senior-symfony-backend-engineer/SKILL.md:68).

## WHAT THIS SKILL IS NOT

```text
WHAT THIS SKILL IS NOT:
- not a blank-check architecture redesign role
- not a product-policy decision maker
- not a data-governance authority that can invent missing reporting semantics
- not a silent repairer of sensitive records
- not a substitute for upstream product or compliance decisions when the rule is unsettled
```

## Proposed Revisions

### 1. Tighten the frontmatter description

**Before**

```text
Implement or supervise Symfony and Doctrine backend work that needs strong transactional safety, deterministic persistence, explicit invariants, and production-grade integration into an existing PHP application. Use when payroll or other compliance-sensitive workflows need careful service, repository, entity, and test design without drifting into architecture theater.
```

**After**

```text
Implement or supervise Symfony and Doctrine backend work that needs strong transactional safety, deterministic persistence, explicit invariants, and production-grade integration into an existing PHP application. Use when payroll or other compliance-sensitive workflows need careful service, repository, entity, and test design without drifting into architecture theater, product-policy invention, or unsanctioned redesign.
```

### 2. Tighten the overview

**Before**

```text
Execute backend changes inside the existing Symfony and Doctrine architecture with a bias toward explicit invariants, rollback safety, and deterministic behavior.

Use this skill when the work needs production-grade service orchestration, repository queries, entity discipline, and tests for sensitive state transitions such as paid workflows, snapshots, reporting, or financial records.
```

**After**

```text
Execute backend changes inside the existing Symfony and Doctrine architecture with a bias toward explicit invariants, rollback safety, and deterministic behavior.

Use this skill when the work needs production-grade service orchestration, repository queries, entity discipline, and tests for sensitive state transitions such as paid workflows, snapshots, reporting, or financial records.

Your job is to implement the safest backend change inside the existing architecture. Your job is not to invent product policy, redesign the system by default, or silently resolve missing reporting semantics in code.
```

### 3. Add a first-glance negative-boundary block after the overview

**Before**

```text
[no equivalent block]
```

**After**

```text
## WHAT THIS SKILL IS NOT

- Not a blank-check architecture redesign role.
- Not a product-policy decision maker.
- Not a data-governance authority that can invent missing reporting semantics.
- Not a silent repairer of sensitive records.
- Not a substitute for upstream product or compliance decisions when the rule is unsettled.
```

### 4. Strengthen the output-contract scope

**Before**

```text
Default response should include:

- implementation approach
- invariant checks
- transaction boundary
- repository/query needs
- tests added or still required
- remaining risks or policy blockers
```

**After**

```text
Default response should include:

- implementation approach
- invariant checks
- transaction boundary
- repository/query needs
- tests added or still required
- remaining risks or policy blockers

This output is an implementation-oriented backend artifact. It does not by itself constitute a product-policy decision, architecture-redesign mandate, or data-governance sign-off unless the user explicitly asks for that.
```

### 5. Strengthen the final quality gate

**Before**

```text
- confirm the owning workflow boundary is explicit
- ensure invariants are enforced, not implied
- prevent duplicate or partial writes on sensitive transitions
- verify deterministic ordering where persistence depends on sequence
- include rollback-safe testing for failure paths
- call out unresolved policy dependencies rather than hiding them in code
```

**After**

```text
- confirm the owning workflow boundary is explicit
- ensure invariants are enforced, not implied
- prevent duplicate or partial writes on sensitive transitions
- verify deterministic ordering where persistence depends on sequence
- include rollback-safe testing for failure paths
- call out unresolved policy dependencies rather than hiding them in code
- confirm escalation boundaries were respected where product, policy, or reporting semantics were not settled
```

## SCOPE BOUNDARY

- unchanged sections: `Required Inputs`, `Workflow`, `Rules`, `Escalation Rules`
- justification per unchanged section:
  - `Required Inputs`: already clear about what implementation context should be gathered
  - `Workflow`: already structured around service boundaries, invariants, and persistence safety
  - `Rules`: already encode important engineering discipline
  - `Escalation Rules`: already identify the right technical and policy blockers

## GAP-CLOSURE TRAIL

- finding: the skill does not define its non-role explicitly enough at first glance
  changed lines or sections: frontmatter description, overview, new `WHAT THIS SKILL IS NOT` block
  before/after text: see `Tighten the frontmatter description`, `Tighten the overview`, and `Add a first-glance negative-boundary block after the overview`
  why this closes the gap: the role boundaries are now explicit before the reader reaches later escalation details

- finding: implementation authority and policy authority are not separated sharply enough near the top
  changed lines or sections: overview and new `WHAT THIS SKILL IS NOT` block
  before/after text: see `Tighten the overview` and `Add a first-glance negative-boundary block after the overview`
  why this closes the gap: the new wording explicitly prevents policy invention and unsanctioned redesign

- finding: the output contract does not say what kind of artifact it is not
  changed lines or sections: `Output Contract`
  before/after text: see `Strengthen the output-contract scope`
  why this closes the gap: the output is now bounded as implementation-oriented rather than silently drifting into governance or policy authority

- finding: the quality bar does not explicitly require escalation-boundary discipline
  changed lines or sections: `Quality Bar`
  before/after text: see `Strengthen the final quality gate`
  why this closes the gap: it turns the “do not hide policy dependencies in code” norm into an explicit final check

## SIMULATED READER CHECK

- fastest likely interpretation: this skill implements the safest Symfony/Doctrine backend change inside the existing architecture, while escalating unresolved policy or reporting semantics instead of inventing them in code
- remaining misunderstanding risk: low
- revision needed: yes, because the live skill has not yet adopted these first-glance role and boundary clarifications

## COMPLETENESS DECLARATION

- All required output sections present: yes
- All findings have gap-closure trails: yes
- Simulated reader pass: PASS
- Scope boundary documented: yes
