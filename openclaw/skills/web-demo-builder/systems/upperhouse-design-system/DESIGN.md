# Design System Inspired by Upper House

## 1. Visual Theme and Atmosphere

Upper House presents as a quiet luxury hospitality system built on restraint, whitespace, and editorial pacing rather than decorative excess. The sampled pages consistently use a light, airy canvas with muted metallic accents, deep navy anchors, and typography that alternates between a graceful display face and a practical sans body. The effect is calm, premium, and culturally literate rather than loud or overtly opulent.

This is not a button-forward or card-heavy interface. Much of the identity comes from image-led layouts, elegant copy blocks, slim navigation, and reservation or registration flows that use understated structure. Interactive elements exist, but they are visually subordinated to typography, spacing, and photography.

**Key Characteristics:**
- Display typography is refined and elegant, with body text kept practical and readable.
- Color use is sparse: white and soft gray dominate, while navy and warm metallic tones provide hierarchy.
- Surfaces stay mostly flat or lightly layered rather than glossy or deeply shadowed.
- Spacing is generous, especially on landing and editorial pages.
- Brand cues feel architectural and hospitality-oriented, not productized or SaaS-like.

## 2. Coverage Map

| Page Class | URL or Source | Why Included | Key Patterns Found | Confidence |
|------------|---------------|--------------|--------------------|------------|
| Landing / Brand Hub | `https://www.upperhouse.com/en` | Main brand entry and global navigation | Light chrome, hero rhythm, restrained CTA use | High |
| Hotel Landing | `https://www.upperhouse.com/en/hongkong` | Property-specific luxury page | Editorial sections, muted palette, sparse CTAs | High |
| Restaurant Detail | `https://www.upperhouse.com/en/hongkong/restaurants-and-bars/salisterra` | Hospitality sub-brand page | Display typography, image-first layout, action links | High |
| Registration Form | `https://www.upperhouse.com/en/registration` | Best source for forms and state coverage | Inputs, selects, checkboxes, disabled, error, success | High |
| Editorial Story | `https://www.upperhouse.com/en/houses-not-hotels` | Narrative / long-form content | Text hierarchy, spacing cadence, buttons in context | High |
| Utility / Policy | `https://www.upperhouse.com/en/cookies-policy` | Utility structure and data-like content | Tables, legal density, loading/error cues | Medium |

**Coverage Notes:**
- Typography, palette, forms, and restrained CTA language were directly observed.
- The page taxonomy from the sampler is still coarse; several content pages landed in `dashboard`, so page labels here are normalized manually.
- Rich motion, hover detail, and deeper component families were not strongly exposed in the sampled HTML.

## 3. Color Palette and Roles

### Primary
- **Warm Metallic Taupe** (`#95855d`): Accent lines, elegant emphasis, understated luxury detail.

### Interactive
- **Deep House Blue** (`#163286`): Action links, selective emphasis, premium brand contrast.
- **Muted Indigo** (`#232a82`): Supporting interactive accent and layered brand depth.

### Text
- **Quiet Charcoal** (`#787b7f`): Default text and subdued copy treatment.
- **Soft White** (`#ffffff`): Primary light background and inverse text.

### Surface and Variants
- **Canvas White** (`#ffffff`): Dominant page surface.
- **Veil White** (`rgba(255,255,255,0.7)`): Overlay, soft separation, floating-light treatment.

### Feedback
- **Success** (`#718275`): Calm affirmative state.
- **Warning / Rich Accent** (`#968359`): Warm caution or emphasis-adjacent accent.
- **Error** (`#991B1E`): Form validation and negative feedback.

### Shadows and Overlays
- **Soft Veil** (`0 16px 40px rgba(0, 0, 0, 0.08)`): Minimal, low-contrast elevation for floating panels.

## 4. Typography Rules

### Font Family
- **Display**: `Belleza`, elegant display face from linked site CSS
- **Body**: `Amiko`, practical sans-serif from linked site CSS
- **Mono or Data**: Not observed
- **Notes**: Display use should stay selective. Body text, labels, and most utility controls should remain on Amiko for clarity.

### Font Table

| Role | Family | Weight | Source | Status | Notes |
|------|--------|--------|--------|--------|-------|
| Display | Belleza | 400 | linked Next.js CSS / `@font-face` | verified | Primary elegant headline face |
| Supporting Display | Belleza | 400 | linked Next.js CSS / `@font-face` | verified | Used for headings and restrained CTAs |
| Body | Amiko | 400 | linked Next.js CSS / `@font-face` | verified | Main paragraph and UI copy |
| Button | Belleza | 400 | linked site `.btn` rules | verified | Buttons use display typography, but styling remains restrained |
| Label | Amiko | 400-600 | linked Next.js CSS / body rules | verified | Form labels and support text should stay pragmatic |

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Belleza | 56-84px | 400 | 1.02 | 0.01em | Use sparingly on brand or destination statements |
| Section Heading | Belleza | 28-42px | 400 | 1.08 | 0.01em | Elegant section framing |
| Card Title | Belleza | 22-28px | 400 | 1.15 | 0.01em | Only when a panel needs elevated editorial tone |
| Body | Amiko | 16-18px | 400 | 1.7 | 0 | Default paragraph rhythm |
| Button | Belleza | 18-22px | 400 | 1.1 | 0.01em | Keep text elegant but do not over-style the container |
| Label | Amiko | 13-15px | 600 | 1.35 | 0.04em | Clear utility hierarchy |
| Micro | Amiko | 12-13px | 400 | 1.4 | 0.03em | Metadata and helper text |

### Principles
- **Display is selective**: Belleza should frame key brand statements, not every heading.
- **Body stays readable**: Amiko carries most interface and utility text.
- **Luxury comes from spacing**: Typography should breathe; avoid dense stacks and compressed blocks.

## 5. Component Families

### Buttons
**Primary / Bordered Hospitality CTA**
- Background: `transparent` or `#ffffff`
- Text: `#163286` or `#787b7f`
- Padding: `15px 30px`
- Radius: `0`
- Border: `1px solid rgba(120,123,127,0.35)` or similarly restrained line
- Font: `Belleza`, `18-22px`, `400`
- Hover: subtle color inversion or opacity shift only
- Active: minimal darkening
- Focus: clean outline or border reinforcement, not glow-heavy
- Disabled: lower contrast and reduced opacity
- Use: reservations, details, and luxury-action moments where typography carries more weight than the shape

**Button Evidence Note**
- The sampled site exposes real `.btn` rules using `Belleza` and `15px 30px` spacing. This system should not be translated into pills, chunky shadows, neon fills, or SaaS-style primary buttons without new evidence.

### Navigation
- Background: mostly white or transparent light overlay
- Height: generous, with airy vertical spacing
- Positioning: global chrome appears refined and minimal rather than aggressively sticky
- Mobile behavior: likely simplified menu structure, though not deeply observed in this pass
- Special effects: subtle veil/overlay treatment rather than obvious blur-heavy chrome

### Cards and Containers
- Background: `#ffffff`
- Border: light neutral lines when separation is needed
- Radius: `0-8px`
- Shadow: minimal or none
- Padding: `24-40px`
- Hover: not strongly observed; keep movement light

### Links
**Editorial / Utility Link**
- Color: `#163286` or `#787b7f`
- Decoration: subtle underline or clean text link
- Hover: mild contrast shift
- Focus: visible but quiet outline or underline reinforcement

## 6. Forms and Input Patterns

### Text Inputs
- Background: `#ffffff`
- Border: `1px solid rgba(120,123,127,0.28)`
- Radius: `0-6px`
- Placeholder: muted, low-contrast sans text
- Focus: border darkens or accent color appears
- Error: observed on registration-related flows
- Success: observed on registration-related flows

### Selection Controls
- Selects: simple bordered fields with understated chrome
- Checkboxes: observed on membership flow; keep them pragmatic and clear
- Radios: not observed
- Toggles: not clearly observed

### Form Layout
- Label position: top-aligned
- Help text: subdued, small sans copy
- Validation messaging: calm but visible, with red for errors and muted positive tones for success
- Submit zone: clean spacing below fields; CTA should remain restrained

## 7. Data Display and Feedback Patterns

### Tables, Lists, or Rows
- Density: relaxed
- Dividers: light rule-based separation
- Header treatment: quiet text emphasis, not boxed-grid heaviness
- Row states: not deeply observed; avoid overly interactive data-grid styling

### Feedback Components
- Alerts or banners: observed, but limited
- Toasts or inline notices: likely inline and quiet rather than loud
- Badges or status chips: not a dominant visual language
- Empty states: not observed
- Loading states: observed in utility flows

## 8. Layout Principles

### Spacing System
- Base unit: `8px`
- Scale: `8, 16, 24, 32, 48, 72`
- Notable characteristics: landing pages and stories open up quickly into generous vertical rhythm

### Grid and Container
- Max content width: roughly `1200-1320px`
- Grid behavior: editorial sections, image-led splits, and centered content blocks
- Container padding: `24-48px`
- Breakpoints: responsive behavior exists but exact thresholds were not captured

### Whitespace Philosophy
- **Breathing room matters**: luxury tone depends on large vertical intervals.
- **Let imagery and type lead**: components should not crowd the page.
- **Silence is part of the brand**: avoid over-filling empty space with utility clutter.

### Border Radius Scale
- Micro: `0-4px` for fields
- Standard: `6-8px` when a softer panel is needed
- Large: rare
- Pill: not evidenced for button language in this pass
- Circle: not a defining system trait

## 9. Depth, Motion, and Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | White surface, no shadow | Most layout surfaces |
| Subtle | Light border or faint shadow | Floating utilities or gentle separation |
| Medium | Soft shadow and overlay veil | Promotional or modal-like emphasis |
| High | Not strongly observed | Use sparingly if ever |

**Shadow Philosophy**: depth is supportive, not theatrical. The interface feels architectural and calm rather than glossy.

**Motion Notes**:
- Loading was observed in utility flows.
- Rich reveal motion was not directly captured from sampled markup.
- Hover and active motion should stay minimal.

## 10. State Coverage and Gaps

| State | Observed? | Where Seen | Notes |
|-------|-----------|------------|-------|
| Default | Yes | Across all sampled pages | Strongest evidence state |
| Hover | No | Not captured | Do not invent elaborate hover behaviors |
| Focus | No | Not clearly captured | Keep focus visible and restrained |
| Active | No | Not clearly captured | Use minor contrast shifts only |
| Disabled | Yes | Registration | Real form-state evidence exists |
| Error | Yes | Registration, cookies-policy | Clear validation and utility evidence |
| Success | Yes | Registration | Observed in member flow |
| Empty | No | Not observed | Keep any empty state understated |
| Loading | Yes | Cookies-policy / utility flow | Real asynchronous behavior hinted |

**Coverage Gaps:**
- Rich hover animation and detailed motion choreography were not verified.
- A more specialized hospitality family for multi-property luxury hotel brands would improve page taxonomy.

## 11. Do's and Don'ts

### Do
- Use Belleza selectively for elegant brand and section statements.
- Keep most supporting copy on Amiko.
- Favor white space, fine rules, and muted accents over dense decoration.
- Treat buttons as restrained hospitality CTAs, not bold product buttons.
- Keep forms calm, legible, and quietly premium.

### Don't
- Don't convert the CTA language into pills or glossy app-store buttons.
- Don't overuse Belleza for small utility text.
- Don't introduce heavy shadows, gradient blobs, or hyperactive cards.
- Don't saturate the palette beyond the observed navy and warm metallic accents.
- Don't force dashboard-style density onto editorial hotel pages.

## 12. Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | `<= 767px` | Typography scales down, navigation condenses, forms stack tightly |
| Tablet | `768px - 1023px` | Editorial blocks remain spacious, image/text splits simplify |
| Desktop | `>= 1024px` | Full luxury spacing and wider editorial composition |

### Touch Targets
- Primary CTAs: at least `44px` tall
- Navigation items: comfortable inline spacing rather than chip-like buttons
- Inputs: at least `44px` tall

### Collapsing Strategy
- Typography: preserve elegance, but reduce hero scale aggressively on small screens
- Layout: simplify into single-column editorial flow
- Navigation: collapse into minimal mobile menu treatment
- Forms and tables: stack fields and reduce visual chrome

## 13. Showcase Recommendations

Build these blocks or pages to prove the system is well captured:

1. Quiet luxury hero plus sparse global navigation
2. Property or destination cards with restrained borders
3. Registration form with disabled, error, and success states
4. Restaurants-and-bars editorial section
5. Utility table or policy block
6. Typography panel naming verified fonts

**Why this showcase set matters:**
- It proves the system across brand, editorial, hospitality, and form-heavy surfaces without inventing a more productized UI language than the site actually uses.
