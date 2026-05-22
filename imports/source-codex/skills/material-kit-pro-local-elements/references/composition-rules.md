# Composition Rules

## Goal

Build pages that look like they came from the local Material Kit Pro mirror, not from a generic bootstrap mashup.

## Allowed Source Root

`E:\htdocs\httrack\mk3pro\demos.creative-tim.com\material-kit-pro`

## Preferred Inputs

- `pages/*.html` and nested `pages/**.html` for full-page structure
- `sections/**/*.html` for reusable fragments
- `assets/css/*`, `assets/js/*`, `assets/img/*`, and `assets/fonts/*` for styling and media already bundled with the mirror

## Safe Working Pattern

1. Find the nearest source page.
2. Find any supplemental sections needed for hero, features, pricing, FAQ, forms, footer, or navigation.
3. Copy existing markup and trim it down.
4. Change content before changing structure.
5. Make the smallest possible structural edits needed for the request.

## Avoid

- New frameworks or package installs just to build UI
- New design tokens unrelated to the local theme
- Replacing the typography, icon, spacing, or card language with a different system
- Pulling in off-theme snippets from unrelated project folders
- Depending on mirrored HTTrack artifact `.html` files that represent remote image URLs instead of actual sections

## Validation Checklist

- Every major section is traceable to a local page or section file.
- Referenced CSS and JS come from the local `assets/` tree or from links already present in the chosen template.
- The result still looks like Material Kit Pro after content edits.
- There are no invented component APIs or class systems.
