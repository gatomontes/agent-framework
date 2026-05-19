# Composition Rules

## Goal

Build pages that look like they came from the local Soft UI Design System Pro mirror, not from a generic bootstrap mashup.

## Allowed Source Root

`E:\htdocs\httrack\softuipro\demos.creative-tim.com\soft-ui-design-system-pro`

## Preferred Inputs

- `presentation.html` for overall product framing
- `pages/*.html` and nested `pages/**.html` for full-page structure
- `sections/**/*.html` for reusable fragments
- `assets/css/*`, `assets/js/*`, `assets/img/*`, `assets/fonts/*`, and `img/*` for styling and media already bundled with the mirror

## Safe Working Pattern

1. Find the nearest source page.
2. Find any supplemental sections needed for hero, features, pricing, FAQ, forms, footer, or navigation.
3. Copy existing markup and trim it down.
4. Change content before changing structure.
5. Make the smallest possible structural edits needed for the request.

## Avoid

- New frameworks or package installs just to build UI
- New design tokens unrelated to the local theme
- Replacing the typography, icon, spacing, glassmorphism, shadows, or card language with a different system
- Pulling in off-theme snippets from unrelated project folders
- Depending on mirrored HTTrack artifact `.html` files that represent remote image URLs instead of actual sections

## Validation Checklist

- Every major section is traceable to a local page or section file.
- Referenced CSS and JS come from the local source tree or from links already present in the chosen template.
- The result still looks like Soft UI Design System Pro after content edits.
- There are no invented component APIs or class systems.
