---
topic: typography
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "font"
  - "type"
  - "text size"
  - "Dynamic Type"
  - "typeface"
  - "tracking"
  - "leading"
related:
  - sf-symbols
  - writing
  - accessibility
---
# Typography

> Typographic choices display legible text, convey hierarchy, communicate content, and express brand or style.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Ensuring Legibility

Minimum/default sizes by platform:

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 17pt | 11pt |
| macOS | 13pt | 10pt |
| tvOS | 29pt | 23pt |
| visionOS | 17pt | 12pt |
| watchOS | 16pt | 12pt |

- Thin-weight custom fonts: target larger than minimums.
- Prefer Regular, Medium, Semibold, or Bold weights. Avoid Ultralight, Thin, Light — especially at small sizes.

## Conveying Hierarchy

- Adjust font weight, size, and color to emphasize important content.
- Maintain relative hierarchy and visual distinction when people change text sizes.
- Minimize distinct typefaces — mixing too many obscures hierarchy and feels inconsistent.
- Prioritize important content when responding to text-size changes (e.g., tab titles don't need to grow when body text grows).

## System Fonts

**San Francisco (SF):** sans serif. Variants: SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew, SF Mono. All available in rounded variants for soft/rounded UI coordination.

**New York (NY):** serif. Designed to work well alongside SF.

Both available as **variable fonts** (single file combining styles, supporting interpolation for intermediate styles). Variable fonts support **dynamic optical sizes** — the system continuously interpolates glyph structure to the exact point size; no need to manually select discrete optical sizes (Text vs. Display) unless your design tool lacks variable font support.

SF weight range: Ultralight → Black. SF also offers Condensed and Expanded widths. SF Symbols match SF weights precisely for symbol+text weight pairing at any size.

**Don't embed system fonts in your app** — use the `default` API for SF, `serif` for NY.

**Text styles** (system-defined typographic attributes): specify font weight, point size, and leading for each text size. Support Dynamic Type and accessibility text scaling. Prefer built-in text styles.

**Modifying text styles with symbolic traits:**
- `bold` trait: adds weight (extra hierarchy level)
- Leading adjustment: loose (wide columns, long passages) or tight (constrained height, multi-line lists — but avoid tight leading for 3+ lines even when height is limited)

**Tracking in mockups:** the running app dynamically adjusts tracking at every point size. For accurate mockups, adjust tracking manually per the Specifications tracking tables.

## Custom Fonts

- Verify legibility at all sizes and weights.
- Implement Dynamic Type support and respond to Bold Text accessibility setting. For Unity games, use the Apple accessibility Unity plugin.

## Supporting Dynamic Type

Available in: iOS, iPadOS, tvOS, visionOS, watchOS (not macOS).

- Adapt layouts for all Dynamic Type sizes. Test largest and smallest, and enable Larger Accessibility Text Sizes in Settings › Accessibility › Display & Text Size › Larger Text on iPhone/iPad.
- Interface icons must also scale with Dynamic Type — SF Symbols do this automatically.
- Minimize text truncation at large font sizes in scrollable regions. Allow more lines in labels instead of truncation.
- At very large sizes in horizontally constrained contexts: consider stacked layouts (text above secondary items) and reduce column count to prevent truncation.
- Maintain consistent information hierarchy at all sizes (keep primary elements at top of view).

## Platform Considerations

### iOS, iPadOS
System font: SF Pro. NY also available.

### macOS
System font: SF Pro. NY available for Mac Catalyst. **macOS does not support Dynamic Type.**

For text matching system controls, use dynamic font variants:

| Variant | API |
|---|---|
| Control content | `controlContentFont(ofSize:)` |
| Label | `labelFont(ofSize:)` |
| Menu | `menuFont(ofSize:)` |
| Menu bar | `menuBarFont(ofSize:)` |
| Message | `messageFont(ofSize:)` |
| Palette | `paletteFont(ofSize:)` |
| Title bar | `titleBarFont(ofSize:)` |
| Tool tips | `toolTipsFont(ofSize:)` |
| User document text | `userFont(ofSize:)` |
| User fixed pitch | `userFixedPitchFont(ofSize:)` |
| Bold system | `boldSystemFont(ofSize:)` |
| System | `systemFont(ofSize:)` |

### tvOS
System font: SF Pro. NY also available.

### visionOS
System font: SF Pro. NY requires explicit type style specification.

- visionOS uses bolder body and title Dynamic Type styles; also adds Extra Large Title 1 and Extra Large Title 2 for editorial layouts.
- Prefer **2D text** — visual depth makes text harder to read. Small amounts of 3D text for attention-drawing is acceptable.
- Test that text remains legible when people scale windows.
- Default text color is white for contrast against glass material. If using another color, test in varied contexts.
- Text not on a background: make it bold; avoid shadows (physical space may not have a surface for accurate shadow casting).
- **Billboarding:** text associated with a 3D point in space should face the wearer at all times (rotate around y-axis as they move).

### watchOS
System font: SF Compact (SF Compact Rounded in complications). NY also available.

## Specifications

Emphasized variants use: Medium, Semibold, Bold, or Heavy. Apply via `bold()` in SwiftUI or `traitBold` in UIKit `UIFontDescriptor`.

### macOS Built-in Text Styles

| Text style | Weight | Size (pt) | Line height (pt) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

Based on 144 ppi (@2x).

### tvOS Built-in Text Styles

| Text style | Weight | Size (pt) | Leading (pt) | Emphasized weight |
|---|---|---|---|---|
| Title 1 | Medium | 76 | 96 | Bold |
| Title 2 | Medium | 57 | 66 | Bold |
| Title 3 | Medium | 48 | 56 | Bold |
| Headline | Medium | 38 | 46 | Bold |
| Subtitle 1 | Regular | 38 | 46 | Medium |
| Callout | Medium | 31 | 38 | Bold |
| Body | Medium | 29 | 36 | Bold |
| Caption 1 | Medium | 25 | 32 | Bold |
| Caption 2 | Medium | 23 | 30 | Bold |

Based on 72 ppi (@1x) / 144 ppi (@2x).

### macOS Tracking Values

| Size (pt) | Tracking (1/1000 em) | Tracking (pt) |
|---|---|---|
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | −6 | −0.08 |
| 14 | −11 | −0.15 |
| 15 | −16 | −0.23 |
| 16 | −20 | −0.31 |
| 17 | −26 | −0.43 |
| 18 | −25 | −0.44 |
| 19 | −24 | −0.45 |
| 20 | −23 | −0.45 |
| 21 | −18 | −0.36 |
| 22 | −12 | −0.26 |
| 23 | −4 | −0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28–30 | +14 | +0.38–0.40 |
| 31–36 | +10–13 | +0.37–0.41 |
| 37–54 | +6–10 | +0.31–0.38 |
| 56–72 | +1–6 | +0.07–0.30 |
| 76–96 | 0–+1 | 0–+0.07 |

### tvOS Tracking Values

Same values as macOS tracking table above. Based on 144 ppi (@2x) / 216 ppi (@3x).
