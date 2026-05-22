# Design System Extraction Guide

## Purpose

Use this guide to extract a reusable design package from a website or visual reference. The goal is not to download or reproduce the site wholesale. The goal is to observe enough representative evidence to document the system's reusable rules, components, states, and page patterns.

## Core Operating Rules

- Distill, do not mirror.
- Prefer representative breadth over raw page count.
- Prefer public and minimally sufficient extraction.
- Separate observed evidence from inference.
- Capture tokens and patterns that agents can reuse to build new pages.
- Do not overclaim coverage from a single page.

## Safety and Scope Gate

Before broad extraction, check:

1. Is the target public and accessible without authentication?
2. Is the request for analysis and distillation rather than redistribution?
3. Can representative pages answer the question without a full mirror?

If the answer to any of these is no, narrow the scope. Prefer:

- single-page distillation
- screenshot-based review
- user-provided HTML, CSS, or assets
- a small representative sample rather than a broad crawl

## Recommended Extraction Modes

### Mode A: Single-Page Distillation

Use when:
- the page is strongly representative
- the user needs speed
- forms or app states are not the primary concern

Deliver:
- system overview
- foundational tokens
- observed component patterns
- explicit gaps

### Mode B: Representative Multi-Page Distillation

Use when:
- the system spans marketing and product surfaces
- the user wants forms, inputs, tables, dialogs, or state coverage
- a landing page alone would underrepresent the system

Deliver:
- system overview
- coverage map
- component inventory
- state coverage
- showcase recommendations

## Representative Page Sampling

For multi-page extraction, prefer page classes over arbitrary page count.

Try to cover:

- home or landing
- pricing or plans
- docs or content page
- auth page
- settings or profile page
- form-heavy page
- table or list page
- dialog, modal, or drawer context
- empty, success, error, or loading states if observable

If the site does not expose all of these, document what is missing rather than guessing.

## Coverage Map

Create a simple coverage map before synthesizing conclusions.

| Page Class | URL or Source | Why Included | Key Patterns Found | Confidence |
|------------|---------------|--------------|--------------------|------------|

Use the map to show where each important observation came from.

## Extraction Workflow

### Phase 1: Initial Scan

1. Fetch the initial page HTML or inspect the provided reference
2. Identify CSS variables, design tokens, and font sources
3. Capture visual evidence with screenshots when possible
4. Identify likely representative page classes from navigation, footer links, sitemap hints, or internal links

### Phase 2: Coverage Planning

1. Decide whether single-page or representative multi-page extraction is needed
2. Select a small representative sample of pages
3. Record the sample in a coverage map
4. Note any major page classes or states that are unobservable

When working from a public URL, you can use `scripts/sample_site.py` to collect a conservative same-origin sample and emit a starter JSON coverage map. Treat that output as a first pass to review, not as the finished design analysis.
If the site has a recognizable structure family, check `references/site-families.json` and use `--site-family` when you need stronger page classification. Prefer domain and page-shape families first, and reserve boilerplate suppression for narrower cases such as booking-heavy hospitality sites.
After each run, review any sampler discrepancy hints. Use those hints to refine the family config instead of hardcoding every new edge case into the extraction logic.

### Phase 3: Foundations and Tokens

Extract:

- color palette and semantic roles
- typography stacks and hierarchy
- spacing scale
- container widths and grid behavior
- border radius scale
- shadows and elevation
- iconography style if distinctive
- motion cues if visible

Prefer role-based summaries over raw value dumps.
When typography is available, produce a font table with at least:

| Role | Family | Weight | Source | Status | Notes |
|------|--------|--------|--------|--------|-------|

Mark each row as `verified` or `inferred`, and record where the font information came from.

### Phase 4: Component Family Analysis

Inspect recurring patterns, not just isolated examples.

Minimum families to check:

- buttons
- navigation
- links
- cards and containers
- text inputs
- selects, checkboxes, radios, toggles
- tables, lists, or data rows
- badges, alerts, banners, or toasts
- tabs, filters, pagination, or segmented controls
- modals, drawers, or popovers

For each family, capture:

- default treatment
- variants
- state behavior
- usage context
- accessibility cues if visible

### Phase 5: State Coverage

Look specifically for:

- default
- hover
- focus
- active
- disabled
- error
- success
- empty
- loading

If states are not visible, say `not observed`. Do not infer specific styling from common conventions.

### Phase 6: Layout and Page Pattern Analysis

Document:

- section rhythm
- hero structure
- navigation model
- form layout patterns
- list or table structure
- dashboard or settings scaffolding
- responsive shifts

Describe these as reusable patterns that could guide new pages, not copied page blueprints.

### Phase 7: Synthesis

Write the system in a way that helps a coding agent make decisions under uncertainty.

Make sure the output answers:

- what makes this system distinctive?
- which rules are foundational?
- which details are flexible?
- what important states or page classes remain unverified?

Before writing the final design-system markdown, confirm that the user wants to proceed unless they already asked for the finished artifact explicitly. The sampling report and coverage map should be treated as a review checkpoint, not an automatic commit to full synthesis.

When the user confirms, create two deliverables together:

- the markdown design-system document
- a browsable showcase bundle with `index.html`, `assets/css/showcase.css`, and `assets/js/showcase.js`

Prefer this output shape by default:

```text
[source-name]-design-system/
  DESIGN.md
  index.html
  assets/
    css/
      showcase.css
    js/
      showcase.js
```

After creating the showcase bundle, open `index.html` in the user's default browser for review.
When choosing which variants to render in the showcase, prefer the variants directly observed in source evidence. Do not add speculative alternates for nav, buttons, footer, or chrome unless they are explicitly marked as inferred.

## Detailed Extraction Heuristics

### Color Extraction Patterns

**CSS variable patterns:**
- `--color-*`, `--primary-*`, `--secondary-*`, `--accent-*`
- `--text-*`, `--background-*`, `--surface-*`
- `--gray-*`, `--neutral-*`
- `--brand-*`, `--theme-*`, `--success-*`, `--error-*`, `--warning-*`

**Inline and rule patterns:**
- `color`
- `background` and `background-color`
- `border-color`
- `fill` and `stroke`
- gradients, overlays, opacity variants

**Interpretation guidance:**
- distinguish decorative accent from primary interaction color
- note feedback colors separately from brand colors
- group similar values by role, not just frequency

### Typography Extraction Patterns

**Font family detection:**
- look for `font-family`
- inspect `@font-face`
- check external font includes
- note separate display, body, and mono stacks if present
- inspect linked site CSS and custom CSS, not just inline HTML
- when builders like Squarespace or Framer are in play, check theme CSS for uploaded fonts and page-specific type rules
- if discovered fonts are publicly loadable and central to the identity, use them in the generated showcase HTML

**Hierarchy detection:**
- identify heading levels actually used
- record label, metadata, and button typography when visible
- note density differences between marketing and product surfaces
- if headings appear distinctive but the sampler did not capture them, trace selectors in linked CSS and recover the real font family before synthesizing the showcase

**Font table guidance:**
- include display, body, and any meaningful supporting roles
- record the source of truth for each font
- do not present inferred fonts as verified

**Spacing and rhythm clues:**
- track line-height patterns
- record letter-spacing behavior
- note if large display text uses tighter tracking than body text

### Component Detection Patterns

**Buttons:**
- primary, secondary, tertiary, ghost, destructive, icon-only
- hover, active, focus, disabled
- only claim a button variant when the source actually supports it
- if exact button styling is unclear, document the uncertainty and use a restrained inferred treatment in the showcase

**Forms:**
- input borders or fills
- floating vs top labels
- placeholder treatment
- validation and help text
- grouped field layout

**Data display:**
- table density
- list row separators
- filtering controls
- pagination or tabs

**Feedback and overlays:**
- toasts
- alerts
- badges
- modals
- drawers
- confirmation or destructive flows

### Spacing and Layout Detection

**Base unit clues:**
- repeated 4px or 8px multiples
- utility scales
- consistent card, form, and section spacing

**Container clues:**
- max-width constraints
- content gutters
- multi-column versus single-column transitions

**Page rhythm clues:**
- hero spacing
- section padding cadence
- dashboard panel spacing
- form field grouping rules

## Output Quality Checklist

The final output should satisfy all of these:

- Colors are documented by semantic role, not just listed
- Typography captures hierarchy, not just the font stack
- Representative page coverage is explicit
- Forms and stateful components are documented when observed
- Missing states or page classes are clearly labeled as gaps
- The document helps agents build new UI in the style
- Any inferred details are clearly marked
- The HTML showcase demonstrates the key component families in one page
- The showcase bundle opens locally through `index.html` without a build step

## Common Failure Modes

### Failure: Landing-Page Bias

Symptom:
- output looks polished but misses forms, data tables, and stateful UI

Fix:
- sample one or two product-like pages
- add state coverage and showcase recommendations

### Failure: Raw Crawl Dump

Symptom:
- too much copied structure, too little design logic

Fix:
- compress repeated observations into named patterns
- discard trackers, duplicated assets, and non-design noise

### Failure: Generic Design Summary

Symptom:
- the write-up could apply to many brands

Fix:
- anchor every major claim in observed tokens, patterns, or page classes
- document what is distinctive and what would break the identity

### Failure: Imagined States

Symptom:
- focus, error, or loading behavior appears in the doc without evidence

Fix:
- mark the state as not observed
- list it under coverage gaps

### Failure: Generic Fancy Buttons

Symptom:
- showcase buttons look like fashionable defaults rather than source-derived components

Fix:
- verify button style from screenshots, linked CSS, or clear markup
- if evidence is thin, simplify and label the treatment as inferred
- never let buttons become the most speculative component in the showcase

## Troubleshooting

**If colors are hard to extract:**
- inspect screenshots visually
- check CSS variables and computed styles
- look for token definitions in JS or config files

**If typography is inconsistent:**
- separate dominant system rules from one-off exceptions
- note where marketing and app surfaces diverge

**If component coverage is thin:**
- look for secondary pages that contain forms or account settings
- prefer one representative internal page over many marketing variants

**If responsive behavior is unclear:**
- inspect media queries
- compare desktop and narrower viewport layouts if possible
- document only what can be observed

**If the sampler returns noisy or generic pages:**
- reduce the page cap and curate the URLs manually
- exclude legal, careers, or utility pages from synthesis
- keep the coverage map focused on representative page classes rather than volume
- add or refine a family entry in `references/site-families.json` instead of hardcoding another niche rule into the script
- if titles or paths consistently disagree with page classes, treat that as a family-definition gap and update the family config
