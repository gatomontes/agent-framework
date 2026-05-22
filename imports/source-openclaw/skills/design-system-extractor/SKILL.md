---
name: design-system-extractor
description: Distill a website's design language into a reusable design package rather than a raw site mirror. Use when asked to extract, document, or analyze a design system from a URL, website, or visual reference, especially when the goal is to capture tokens, components, states, layout rules, and page patterns agents can reliably reuse.
---

# Design System Extractor

Extract a reusable design package from websites and visual references.

## Overview

I automatically store extracted systems in `C:\Users\gatom\.openclaw\skills\web-demo-builder\systems\` for immediate use with the `web-demo-builder` skill.

This skill converts a website, set of pages, or visual reference into structured design documentation that coding agents can actually use. The primary output is not a downloaded site. The primary output is a distilled design package:

- a `DESIGN.md`-style system document
- a page coverage map
- a component and state inventory
- a showcase recommendation set covering real UI patterns such as forms, tables, dialogs, inputs, empty states, and error states

If the source is a live website, crawling is optional and only exists to improve coverage. Use it to observe more pages and components, not to reproduce or redistribute the site wholesale.

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
3. Identify likely page classes from navigation, footer links, sitemap hints, or internal links
4. If broader coverage is needed, fetch a small representative sample of pages
5. When helpful, use `scripts/sample_site.py` to gather a conservative same-origin page sample and a first-pass coverage summary

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
- page section rhythm
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

1. `DESIGN.md`-style system document
2. `Coverage Map`
3. `Component Inventory`
4. `State Coverage`
5. `Showcase Recommendations`

## Output Contract

### Primary Artifact: Design System Markdown

Generate a markdown file following this structure:

```markdown
# Design System Inspired by [Source Name]

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

## 13. Showcase Recommendations
```

### Secondary Artifact: Interactive HTML Showcase

**Default Behavior:** After extracting a design system, automatically create an interactive HTML showcase that demonstrates the system's key components and patterns.

The HTML showcase should include:

- Live color palette with swatches and hex values
- Typography hierarchy with real text samples
- Interactive component demonstrations (buttons, cards, forms)
- Layout examples showing grid and spacing
- Do's and Don'ts section with visual examples
- Responsive behavior demonstration
- All CSS embedded in the file (no external dependencies)

**File Naming:** `[source-name]-design-showcase.html`

**Implementation Guidelines:**
- Use CSS custom properties (CSS variables) for colors and spacing
- Include responsive breakpoints that match the design system
- Make components interactive where appropriate (hover states, etc.)
- Keep the file self-contained (no external resources)
- Use system fonts as fallbacks for proprietary fonts
- Include clear section navigation

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

## Quality Bar

Before finalizing, check:

- The output reflects observed evidence, not generic taste.
- The coverage map makes clear which page types were sampled.
- Forms, inputs, and stateful components are either documented or explicitly absent.
- The artifact helps an agent build new pages in the style, rather than reproduce the old site.
- Safety and permission limits were respected.
- Any inferred details are labeled as inferred.

## References

See:

- `assets/template.md` for the target structure
- `references/example-output.md` for a full example
- `references/extraction-guide.md` for extraction patterns and heuristics
- `scripts/sample_site.py` for conservative representative-page sampling and signal extraction
