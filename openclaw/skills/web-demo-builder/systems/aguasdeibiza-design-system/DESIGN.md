# Design System Inspired by Aguas de Ibiza

## 1. Visual Theme and Atmosphere

Aguas de Ibiza presents a soft luxury hospitality system built around whiteness, air, calm blue-gray accents, and booking-aware utility layered into a premium resort brand. The sampled pages suggest a visual identity that wants to feel serene, wellness-adjacent, and elevated without becoming starkly minimal. The system balances editorial mood, event storytelling, family/community content, and direct booking or inquiry moments.

Unlike a nightlife or fast-casual system, this one uses quiet contrast and spacious composition to express refinement. White surfaces, muted watery blue-gray tones, and restrained interaction structures support a premium hotel narrative while still allowing forms, gift cards, event pages, and contact flows to feel integrated rather than bolted on.

**Key Characteristics:**
- Soft luxury white-first surface system
- Muted blue-gray accent palette with calm resort tonality
- Premium editorial mood with booking-oriented utility
- Layered hospitality chrome including toggles, modals, and form surfaces
- Wellness, family, and event content that stays inside one coherent visual world

## 2. Coverage Map

| Page Class | URL or Source | Why Included | Key Patterns Found | Confidence |
|------------|---------------|--------------|--------------------|------------|
| Home | `https://www.aguasdeibiza.com` | Captures overall hotel atmosphere and booking-aware chrome | Buttons, links, toggles, modals | High |
| Gallery | `https://www.aguasdeibiza.com/aguas-de-ibiza-image-gallery` | Captures image-led hospitality presentation | Buttons, links, toggles, modals | High |
| Offers | `https://www.aguasdeibiza.com/aguas-de-ibiza-offers` | Captures premium promotional treatment | Buttons, links, toggles, modals | High |
| Blog | `https://www.aguasdeibiza.com/blog` | Captures editorial content treatment | Buttons, links, toggles, modals | High |
| Events | `https://www.aguasdeibiza.com/events` and `https://www.aguasdeibiza.com/weddings-ibiza` | Captures venue and event sales surfaces | Buttons, links, toggles, modals | High |
| Contact Form | `https://www.aguasdeibiza.com/contact` | Captures inputs, validation-related categories, and tabs or alerts | Buttons, links, inputs, checkboxes, toggles, modals, tabs, alerts | High |
| Community / Family | `https://www.aguasdeibiza.com/kids-club` | Captures softer family/community extension of the brand | Buttons, links, toggles, modals | High |
| Gift Cards | `https://www.aguasdeibiza.com/gift-cards` | Captures transactional gifting surface | Buttons, links, toggles, modals | High |

**Coverage Notes:**
- The system spans editorial, promotional, event, community, and transactional surfaces without obvious brand fragmentation.
- Hospitality chrome appears consistently enough to treat booking-like overlays and toggles as part of the core pattern language.
- The blog page inflated raw button counts, so button styling below stays grounded in linked CSS and observed page chrome rather than sampler frequency alone.

## 3. Color Palette and Roles

### Primary
- **Pure White** (`#FFFFFF` / `#fff`): dominant background and surface role
- **Watery Blue-Gray** (`#94B2BB`): signature accent that supports calm, coastal luxury

### Interactive
- **Dark Neutral Text** (`#32373c`): primary readable contrast
- **Warm Utility Accent** (`rgb(255,105,0)`): minor supporting accent visible in theme markup

### Text
- **Primary Dark Text** (`#32373c`): main reading and interface text
- **Muted Copy** (`#6b7780`): supportive copy tone inferred from observed contrast system

### Surface and Variants
- **White Surface** (`#FFFFFF`): main page body and panels
- **Soft Surface** (`#f7fbfc`): airy hospitality panel treatment
- **Overlay Shadow** (`rgba(0, 0, 0, 0.2)`): subtle modal and layered separation

### Feedback
- **Success** (`#dcefe6`): success state treatment derived from observed success coverage
- **Error** (`#f9e3e0`): validation and negative feedback treatment derived from observed error coverage
- **Warning**: not clearly observed

### Shadows and Overlays
- **Soft Premium Shadow** (`0 24px 58px rgba(0,0,0,0.10)`): restrained premium depth for elevated panels

## 4. Typography Rules

### Font Family
- **Display**: `berlingske`
- **Body**: `gt-america`
- **Mono or Data**: not observed
- **Notes**: linked theme font CSS exposes `berlingske` and `gt-america` as the site's actual font families. `gt-america` is applied on `html, body`; `berlingske` is used for display scales and luxury title treatments.

### Font Table

| Role | Family | Weight | Source | Status | Notes |
|------|--------|--------|--------|--------|-------|
| Display | `berlingske` | 300 | linked CSS + `@font-face` | verified | Used for display scales and premium titles |
| Supporting Display | `berlingske` | 300 | linked CSS + `@font-face` | verified | Used for modal and promotional title treatments |
| Body | `gt-america` | 100 | linked CSS + `@font-face` | verified | Applied on `html, body` in theme CSS |
| Button | `gt-america` | 100 | linked CSS + selector usage | verified | Consistent with body and interface utility typography |
| Label | `gt-america` | 100 | linked CSS + selector usage | verified | Used for interface and form-related supporting copy |

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display | berlingske | Large | 300 | Spacious | Controlled | Supports premium hospitality mood |
| Section Heading | berlingske | Medium-large | 300 | Airy | Mild tracking | Used for offers, events, and editorial content |
| Card Title | berlingske | Medium | 300 | Standard | Neutral | Used for content and promotional modules |
| Body | gt-america | Base | 100 | Comfortable | Neutral | Calm readable luxury copy |
| Button | gt-america | Base | 100 | Compact | Slight refinement | Booking, inquiry, or promotional CTA use |
| Label | gt-america | Small | 100 | Compact | Slight tracking | Form labels and utility copy |
| Micro | gt-america | Small | 100 | Standard | Neutral | Metadata and footer-like informational elements |

### Principles
- **Calm elegance**: typography should feel refined and breathable, not loud.
- **Hospitality editorial blend**: the system mixes brochure-style display with clean operational body text.
- **Utility without breaking mood**: forms and booking flows should not visually detach from the premium tone.

## 5. Component Families

### Buttons
**Premium Hospitality CTA**
- Background: white or softly tinted surface, with occasional blue-gray fill for emphasis
- Text: dark neutral or white on filled CTA
- Padding: medium and generous enough to feel premium
- Radius: fully rounded capsule
- Border: restrained blue-gray line
- Font: `gt-america`, body-adjacent utility styling
- Hover: not directly observed
- Active: not directly observed
- Focus: not directly observed
- Disabled: not observed
- Use: offers, event inquiries, bookings, gift cards, and contact actions

**Button Evidence Note**
- Button treatment is kept conservative here because raw button counts were inflated by the blog page. The showcase reflects the verified rounded hospitality CTA language seen across the sampled chrome rather than inventing extra button variants.

### Navigation
- Background: white or translucent luxury shell integrated into the page
- Height: moderate hospitality header band
- Positioning: standard top-site navigation with overlay/modal-aware behavior
- Mobile behavior: not directly observed
- Special effects: modals and toggles suggest layered navigation behavior

### Cards and Containers
- Background: white or lightly elevated panels
- Border: subtle and low-contrast
- Radius: soft and refined
- Shadow: gentle, controlled, premium
- Padding: generous
- Hover: not observed

### Links
**Editorial / Hospitality Link**
- Color: dark or blue-gray aligned to the core palette
- Decoration: not directly observed
- Hover: not observed
- Focus: not observed

### Modals and Toggles
- These appeared consistently enough to count as structural, not incidental.
- Their presence suggests booking, inquiry, or layered navigation flows are important to the system.

### Tabs and Alerts
- Captured directly on the contact form surface.
- Treat them as valid but under-documented utility patterns.

## 6. Forms and Input Patterns

### Text Inputs
- Inputs were directly observed on the contact page.
- Background: white field surfaces
- Border: subtle and premium
- Radius: softly rounded
- Placeholder: not directly observed
- Focus: not directly observed
- Error: observed as a category
- Success: observed elsewhere as a category

### Selection Controls
- **Checkboxes**: observed
- **Selects**: not directly observed in the sample set
- **Radios**: not observed
- **Toggles**: observed across multiple pages and part of the hospitality chrome

### Form Layout
- Label position: not directly observed
- Help text: not clearly observed
- Validation messaging: inferred from error-state presence
- Submit zone: restrained and aligned with premium hospitality CTA patterns

## 7. Data Display and Feedback Patterns

### Tables, Lists, or Rows
- Lists or grouped editorial blocks are more important than dense data tables in this system.
- Density: moderate and airy
- Dividers: subtle
- Header treatment: refined and understated
- Row states: not observed

### Feedback Components
- Alerts or notices: observed in form-related sampling
- Toasts: not observed
- Badges: not observed
- Empty states: not observed
- Loading states: observed

## 8. Layout Principles

### Spacing System
- Base unit: not directly observed
- Scale: inferred generous spacing cadence
- Notable characteristics: the system uses whitespace as part of premium perception

### Grid and Container
- Max content width: not directly observed
- Grid behavior: centered hospitality content layout with editorial sections
- Container padding: moderate to generous
- Breakpoints: not observed

### Whitespace Philosophy
- **Air and calm**: whitespace helps communicate relaxation and exclusivity.
- **Luxury moderation**: the system avoids both clutter and sterile emptiness.
- **Utility within serenity**: functional overlays and forms are integrated without collapsing the mood.

### Border Radius Scale
- Micro: not observed
- Standard: soft rounded treatment on fields and panels
- Large: generous panel rounding
- Pill: used in navigation chips and primary CTA shells
- Circle: used sparingly for marks or icon containers

## 9. Depth, Motion, and Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | White base surfaces | Main page backgrounds |
| Subtle | Soft shadow and overlay | Cards, modals, elevated panels |
| Medium | Modal and overlay layering | Booking and form-related chrome |
| High | Not clearly observed | Unverified |

**Shadow Philosophy**: depth should feel soft and expensive, not loud or app-like.

**Motion Notes**:
- Loading was observed.
- Error and success state categories were observed.
- Hover and focus animation remain unverified.

## 10. State Coverage and Gaps

| State | Observed? | Where Seen | Notes |
|-------|-----------|------------|-------|
| Default | Yes | All sampled pages | Base hospitality system observed |
| Hover | No | Not observed | Gap |
| Focus | No | Not observed | Gap |
| Active | No | Not observed | Gap |
| Disabled | No | Not observed | Gap |
| Error | Yes | Contact flow | Styling not fully documented |
| Success | Yes | Gift cards / system cues | Styling not fully documented |
| Empty | No | Not observed | Gap |
| Loading | Yes | Contact flow / system cues | Styling not fully documented |

**Coverage Gaps:**
- Exact field-level interaction styling remains partially unverified.
- More direct visual capture of nav, footer, and field styling would improve fidelity.
- Responsive behavior needs a targeted follow-up pass if exact implementation is required.

## 11. Do's and Don'ts

### Do
- Keep the system white, calm, and editorially refined.
- Use blue-gray as a hospitality accent rather than a loud brand signal.
- Let overlays and modals feel integrated and gentle.
- Preserve a luxury resort tone across offers, events, family, and forms.
- Use whitespace to communicate ease and quality.

### Don't
- Darken the system into nightlife or club language.
- Introduce harsh app-like UI chrome that breaks the resort mood.
- Use saturated, playful accents in ways that undermine serenity.
- Make forms feel operationally detached from the premium brand.
- Collapse the editorial and transactional surfaces into unrelated styles.

## 12. Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | Not observed | Likely stacked content and simplified overlay/navigation behavior |
| Tablet | Not observed | Likely broader spacing with content regrouping |
| Desktop | Not observed | Full premium editorial presentation |

### Touch Targets
- Primary CTAs: should remain generous and calm
- Navigation items: should stay legible without feeling dense
- Form controls: should remain refined and easy to activate

### Collapsing Strategy
- Typography: unverified
- Layout: likely graceful vertical stacking
- Navigation: likely toggle or overlay-driven on smaller screens
- Forms and modals: likely simplified but still brand-consistent

## 13. Showcase Recommendations

Build these blocks or pages to prove the system is well captured:

1. Luxury hotel hero with airy navigation
2. Offers or promotional cards
3. Event or wedding inquiry section
4. Contact form with premium field styling
5. Gift card or transactional hospitality section
6. Gallery-led editorial block
7. Community or family block such as kids club

**Why this showcase set matters:**
- It captures the real breadth of the sampled site.
- It respects the blend of editorial luxury and hospitality utility.
- It avoids forcing the brand into a generic travel, SaaS, or lifestyle template.
