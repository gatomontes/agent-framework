---
name: design-system-extractor
description: Distill a website's design language into a reusable design package rather than a raw site mirror. Use when asked to extract, document, or analyze a design system from a URL, website, or visual reference, especially when the goal is to capture tokens, components, states, layout rules, and page patterns agents can reliably reuse.
---

# Design System Extractor

Extract a reusable design package from websites and visual references.

## Overview

This skill converts a website, set of pages, or visual reference into structured design documentation that coding agents can actually use. The primary output is not a downloaded site. The primary output is a distilled design package:

- a design-system folder bundle rather than loose files
- a `DESIGN.md`-style system document
- an `index.html` showcase demonstrating the extracted system
- external `assets/css/*.css` and `assets/js/*.js` files used by the showcase
- a page coverage map
- a component and state inventory
- a showcase recommendation set covering real UI patterns such as forms, tables, dialogs, inputs, empty states, and error states
- a visible source reference back to the original site when the source is a URL

If the source is a live website, crawling is optional and only exists to improve coverage. Use it to observe more pages and components, not to reproduce or redistribute the site wholesale.

Important interaction rule:

- After sampling, coverage review, and discrepancy review, pause and ask the user whether to proceed with building the full design system artifact unless they explicitly asked for the final design system document already.
- If the user asks to inspect additional pages after the first pass, extend the coverage map and continue from that expanded sample instead of restarting from scratch.

## When to Use

- User provides a URL and asks to extract or document the design system
- User wants to reverse-engineer a site's visual style and reusable UI rules
- User asks to analyze UI patterns from a specific website
- User provides screenshots and wants structured design documentation
- User wants broader coverage than a single landing page, including forms, tables, and app states

## Operating Principles

- Distill, do not mirror. Treat the source as evidence, not as the product.
- Prefer public, permitted, and minimally sufficient extraction.
- Capture reusable rules, not copyrighted page copy or full asset libraries.
- Separate verified observations from inferred patterns.
- If coverage is incomplete, say so and identify the missing page types or states.
- Do not claim behavior you did not observe.
- Always preserve traceability to the original source site when the source is a URL.

## Safety Gate

Before any crawl or multi-page fetch, check:

1. Is the target public and accessible without authentication?
2. Is the requested extraction limited to design analysis rather than redistribution?
3. Can the task be completed with a few representative pages instead of a full mirror?

If the site appears private, authenticated, or clearly unsuitable for crawling, do not proceed with broad extraction. Fall back to:

- screenshot-based analysis
- user-provided HTML or assets
- a limited single-page review

If a broad crawl would create obvious legal, contractual, or privacy risk, say so briefly and switch to a narrower extraction plan.

## Modes

Choose one mode explicitly.

### Mode A: Single-Page Distillation

Use when:
- the user gives one page
- the page already contains the dominant visual system
- speed matters more than exhaustiveness

Output:
- `DESIGN.md`-style system document
- component list limited to observed patterns
- explicit gaps section

### Mode B: Representative Multi-Page Distillation

Use when:
- the user wants broader coverage
- forms, inputs, tables, dialogs, and app states matter
- one page is not representative enough

Target a representative set of pages, not a raw full-site clone. Prefer page classes such as:

- home or landing
- pricing or plans
- docs or content page
- auth flow
- dashboard or settings
- form-heavy page
- table or list page
- modal, dialog, or drawer state
- empty, success, and error states if observable

Output:
- `DESIGN.md`-style system document
- page coverage map
- component and state inventory
- showcase page recommendation set

## Workflow

### Step 1: Define Extraction Scope

Identify:

- source type: URL, screenshots, local files, or mixed
- extraction mode: single-page or representative multi-page
- target artifact: design system only, or design system plus showcase inventory
- constraints: time, legal limits, authentication, or page cap

If no scope is provided, default to representative multi-page distillation with a small page cap.

### Step 2: Gather Source Material

**If URL provided:**
1. Fetch the initial page HTML and visible CSS signals
2. Capture one or more screenshots for visual confirmation
3. Record the original source URL explicitly so it can be included in the final markdown artifact
4. Scan the primary navigation areas for coverage candidates. Use this discovery order unless the page proves otherwise: navbar or primary header navigation first, sidebar or app menu second, footer navigation third, then sitemap links and other internal hubs last.
5. Identify likely page classes from navigation, footer links, sitemap hints, or internal links
6. If broader coverage is needed, fetch a small representative sample of pages
7. When helpful, use `scripts/sample_site.py` to gather a conservative same-origin page sample and a first-pass coverage summary
8. If the site belongs to a recognizable family, use `references/site-families.json` or `--site-family` to apply family-specific page typing first, and boilerplate suppression only where that family genuinely needs it
9. Review sampler discrepancy hints after a run. Treat them as prompts to improve family definitions rather than as automatic truth.
10. For typography, inspect linked CSS, custom CSS, and `@font-face` declarations before concluding that a font is unknown or local-only.
11. If typography is central to the source identity and the discovered fonts are publicly loadable, use them in the generated HTML showcase instead of approximating with local fallbacks.
12. If the user later requests additional pages, extend the representative sample with those pages, add them to the coverage map, and clearly label them as user-requested additions.

**If screenshots or images provided:**
1. Analyze typography, colors, spacing, density, and component patterns
2. Note visual characteristics such as contrast, whitespace, radii, shadows, and motion cues
3. Mark structural rules as inferred unless supported by additional evidence

**If local reference files provided:**
1. Read the files directly
2. Look for CSS variables, component markup, utility patterns, and documented tokens

### Step 3: Build a Coverage Map

For multi-page extraction, create a simple coverage map:

| Page Class | URL or Source | Why Included | Key Patterns Found | Confidence |
|------------|---------------|--------------|--------------------|------------|

This prevents overclaiming from a single hero page.

Additional rule:
- If a navbar exists, sample from the navbar before following generic internal links or guessing URLs.
- If a sidebar or app menu exists, sample from the sidebar before guessing component, dashboard, or utility URLs.
- Only guess URLs after explicit navigation structures have been checked or shown to be incomplete.
- If the user asks for extra pages, append them to the same coverage map rather than replacing earlier evidence.

### Step 4: Extract Visual Theme and Brand Atmosphere

Analyze the overall design philosophy:

- mood and positioning
- background treatment
- imagery or illustration treatment
- typography personality
- density and whitespace
- motion or interaction character if observable

Write 1-2 short paragraphs that explain the design logic, not just the appearance.

### Step 5: Extract Tokens and Foundations

Document reusable foundations:

- color roles and variants
- typography stacks and hierarchy
- spacing scale and container widths
- border radius scale
- elevation and shadow system
- iconography style if distinctive
- motion cues if visible

Prefer named roles over raw dumps. If exact values are unavailable, label them as estimated.
Always include a compact font table when typography information is available or partially inferable.

### Step 6: Extract Component Families

Document recurring UI patterns with observed variants and states.

Minimum component families to check:

- buttons
- links
- cards and containers
- navigation
- form inputs
- selects, checkboxes, radios, toggles
- tables, lists, rows, or data cards
- badges, alerts, toasts, or notices
- modals, drawers, or popovers
- tabs, filters, pagination, or segmented controls

For each component, capture:

- visual treatment
- variants
- interactive states
- accessibility cues if visible
- usage context

Button-specific rule:

- Be stricter with buttons than with general layout mood.
- Do not invent a premium, SaaS, pill, ghost, or rounded CTA style unless that exact treatment is supported by source evidence.
- If button styling is under-observed, say so explicitly in the markdown and keep the showcase button treatment restrained or mark it as inferred.
- Prefer underclaiming button styling over substituting a fashionable default.

### Step 7: Extract State Coverage

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

Do not invent states you did not observe. If a state is missing, call it out as a coverage gap.

### Step 8: Extract Layout and Page Patterns

Document:

- grid and container behavior
- navigation layout
- hero structure
- content modules
- form layout patterns
- dashboard or settings page structure
- responsive shifts if observable

Treat page patterns as reusable templates, not page copies.

### Step 9: Synthesize Distinctive Rules

Write concise design rules:

- what makes the system recognizable
- what must remain consistent
- what can flex safely
- what would break the identity

This section should help a coding agent make good tradeoffs when details are missing.

### Step 10: Produce the Design Package

Generate a package with these sections:

1. design-system folder bundle
2. `DESIGN.md`-style system document
3. `index.html` showcase
4. `assets/css/*.css`
5. `assets/js/*.js`
6. `Coverage Map`
7. `Component Inventory`
8. `State Coverage`
9. `Showcase Recommendations`

Default bundle structure:

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

The bundle should be the default export shape unless the user explicitly asks for a different structure.

The markdown design system should include a dedicated font table such as:

| Role | Family | Weight | Source | Status | Notes |
|------|--------|--------|--------|--------|-------|

Use:
- `Source`: `inline CSS`, `linked CSS`, `custom CSS`, `@font-face`, `external font service`, or `inferred`
- `Status`: `verified` or `inferred`

The markdown artifact should also include:
- a `Source reviewed` or equivalent section near the top
- the original site URL when the source is a URL
- any additional pages explicitly requested by the user, labeled as added coverage
- a dedicated `Added Coverage` section whenever the user asks to inspect additional pages after the initial pass

The showcase should:

- live at the bundle root as `index.html`
- demonstrate the extracted colors, typography, buttons, cards, navigation, form controls, data-display elements, and feedback states when those patterns are available
- use the extracted design language rather than generic defaults
- prefer directly observed component and page-chrome variants over invented alternatives
- avoid adding extra variants that were not observed unless they are clearly labeled as inferred or exploratory
- apply a strict evidence standard to button styling; do not let buttons drift into generic modern defaults when the source evidence is thin
- load its styling from `./assets/css/showcase.css`
- load its behavior from `./assets/js/showcase.js`
- remain suitable for opening locally in a browser without a build step
- prioritize representative breadth over visual polish alone

The CSS and JS should be lightweight and purpose-built:

- create `assets/css/showcase.css` even if the file is small
- create `assets/js/showcase.js` even if behavior is minimal
- keep the bundle static and dependency-free unless the user asked otherwise
- if no interactivity is needed, the JS can provide light progressive enhancement or a documented no-op scaffold

After creating the bundle, open `index.html` in the default browser so the user can review it immediately.

### Step 11: Confirm Before Final Synthesis

If the user did not explicitly ask for the final design-system markdown artifact, stop after presenting the sampling findings and ask a concise confirmation question such as:

- `Proceed to build the full design system from this coverage?`

Only generate the final `DESIGN.md`-style document immediately when:

- the user explicitly asked for the design system itself
- or the user clearly asked for extraction plus documentation in one step

When you do proceed, generate both:

- the bundled markdown design system artifact at `DESIGN.md`
- the bundled showcase artifact at `index.html`
- the bundled stylesheet at `assets/css/showcase.css`
- the bundled script at `assets/js/showcase.js`

Then open `index.html` in the default browser.
6. `Discrepancy Hints` when the sampler sees repeated page-shape mismatches

## Output Contract

### Primary Artifact: Design System Markdown

Generate a markdown file following this structure:

```markdown
# Design System Inspired by [Source Name]

Source reviewed:
- [original URL]
- [additional sampled page URLs]

## 1. Visual Theme and Atmosphere

## 2. Coverage Map

## 3. Color Palette and Roles

## 4. Typography Rules

## 5. Component Families

## 6. Forms and Input Patterns

## 7. Data Display and Feedback Patterns

## 8. Layout Principles

## 9. Depth, Motion, and Elevation

## 10. State Coverage and Gaps

## 11. Do's and Don'ts

## 12. Responsive Behavior

## 13. Added Coverage

Use this section only when the user asks to inspect additional pages after the first sample. List each added page, why it was added, and what new evidence it contributed.

## 14. Showcase Recommendations
```

### Secondary Artifact: Interactive HTML Showcase Bundle

**Default Behavior:** After extracting a design system, automatically create a design-system folder bundle that demonstrates the system's key components and patterns.

The default artifact layout is:

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

The showcase bundle should include:

- Live color palette with swatches and hex values
- Typography hierarchy with real text samples
- Interactive component demonstrations (buttons, cards, forms)
- Layout examples showing grid and spacing
- Do's and Don'ts section with visual examples
- Responsive behavior demonstration
- Separate CSS and JS files inside the bundle
- No build step and no external runtime dependencies unless explicitly requested

**File Naming:**
- folder: `[source-name]-design-system`
- markdown: `DESIGN.md`
- HTML entry: `index.html`
- stylesheet: `assets/css/showcase.css`
- script: `assets/js/showcase.js`

**Implementation Guidelines:**
- Use CSS custom properties (CSS variables) for colors and spacing
- Include responsive breakpoints that match the design system
- Make components interactive where appropriate (hover states, etc.)
- Keep the bundle static and locally browsable
- Use system fonts as fallbacks for proprietary fonts
- Include clear section navigation
- Include the original site link somewhere visible in the bundle or markdown when the source is a URL

### Tertiary Artifact: Showcase Recommendations

Recommend a small set of showcase blocks or pages that would best demonstrate the extracted system, such as:

- hero and navigation
- auth form
- settings form
- table or list view
- modal or dialog
- alerts and validation states
- empty, loading, and success states

The goal is to prove coverage of the system's reusable elements, especially the ones that landing pages omit.

## Extraction Heuristics

- Prefer representative breadth over raw page count.
- Prefer system tokens and recurrent patterns over isolated one-off flourishes.
- Prefer reusable structural examples over copied marketing copy.
- Treat scripts, trackers, analytics, and duplicated assets as noise unless they reveal design tokens.
- When using crawl-like tools, limit collection to what improves component and state coverage.
- If a navbar or sidebar exists, treat it as the highest-signal starting point for page discovery.
- When the user asks for additional pages, treat that as a coverage expansion request, not a restart.

## Quality Bar

Before finalizing, check:

- The output reflects observed evidence, not generic taste.
- The coverage map makes clear which page types were sampled.
- The original site link is included when the source is a URL.
- Navbar-first and sidebar-second discovery order was followed unless there is explicit evidence that those structures were absent or unhelpful.
- Forms, inputs, and stateful components are either documented or explicitly absent.
- The artifact helps an agent build new pages in the style, rather than reproduce the old site.
- Safety and permission limits were respected.
- Any inferred details are labeled as inferred.
- Any user-requested additional pages are clearly represented in coverage.

## References

See:

- `assets/template.md` for the target structure
- `assets/showcase-template.html` for the single-page showcase scaffold
- `references/example-output.md` for a full example
- `references/extraction-guide.md` for extraction patterns and heuristics
- `references/site-families.json` for family-specific page classes and boilerplate rules
- `scripts/sample_site.py` for conservative representative-page sampling and signal extraction


