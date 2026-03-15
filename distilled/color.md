---
topic: color
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "color"
  - "palette"
  - "tint"
  - "accent color"
  - "semantic color"
  - "vibrancy"
related:
  - dark-mode
  - materials
  - accessibility
---
# Color

> Judicious use of color enhances communication, evokes brand, provides continuity, communicates status, and helps people understand information.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Best Practices

- Use color consistently — never use the same color to mean different things.
- Ensure all colors work in light, dark, and Increase Contrast modes. Supply light/dark variants for all custom colors plus an increased-contrast option for each. Even single-appearance apps need both for Liquid Glass adaptivity.
- Test under varied lighting (bright outdoor = colors look darker/muted; dark = bright/saturated). In visionOS, ambient physical surfaces affect color perception.
- Test on different devices (True Tone iPhones/iPads/Macs; tvOS on multiple TV brands/settings). Use P3 and sRGB profiles on Mac via System Settings › Displays.
- Consider how artwork and translucency affect nearby colors — map-mode vs. satellite-mode color scheme switching is a good example.
- Use system color pickers when letting people choose colors.
- Never rely on color alone to differentiate, convey interactivity, or communicate info — provide text labels or glyph shapes as alternatives.
- Avoid insufficient contrast between text/icons and backgrounds.
- Research cultural color meanings per locale (e.g., red = danger vs. positive in different cultures).

## System Colors

- Never hard-code system color values — they change between releases. Use `Color` API.
- Dynamic system colors are semantically defined (purpose, not appearance). Don't repurpose them (e.g., don't use `separator` for text or `secondaryLabel` for background).

## Liquid Glass Color

- Liquid Glass has no inherent color by default — it takes on colors from behind it.
- Apply color sparingly: reserve for status indicators or primary actions.
- To emphasize primary actions, color the **background** (not the symbol/text). System applies accent color to prominent button backgrounds (e.g., Done button).
- Don't color the background of multiple controls.
- If app has colorful content-layer backgrounds, prefer monochromatic toolbars/tab bars — too much color makes labels hard to read.
- Ensure content-layer's default/resting state maintains clear legibility beneath controls.

## Color Management

- A **color space** (e.g., sRGB, Display P3) defines the gamut of reproducible colors.
- A **color profile** maps colors to numerical representations so devices display them accurately.
- Apply color profiles to all images.
- Use **Display P3** (wide color, 16-bit/channel, PNG) for richer colors on compatible displays. Need a wide-color display to design P3 assets.
- Provide sRGB fallback variants when P3 gradients or similar colors look clipped on sRGB displays.

## Platform Considerations

### iOS, iPadOS

Two background color sets — **system** and **grouped** — each with primary/secondary/tertiary variants:
- Primary: overall view
- Secondary: grouping within view
- Tertiary: grouping within secondary elements

Use grouped set (`systemGroupedBackground`, `secondarySystemGroupedBackground`, `tertiarySystemGroupedBackground`) for grouped table views; system set otherwise.

Foreground dynamic colors:

| Color | Use for | UIKit API |
|---|---|---|
| Label | Primary text | `label` |
| Secondary label | Secondary text | `secondaryLabel` |
| Tertiary label | Tertiary text | `tertiaryLabel` |
| Quaternary label | Quaternary text | `quaternaryLabel` |
| Placeholder text | Control/text view placeholders | `placeholderText` |
| Separator | Visible-through separator | `separator` |
| Opaque separator | Opaque separator | `opaqueSeparator` |
| Link | Linked text | `link` |

### macOS

Full dynamic system color table (AppKit API):

| Color | Use for | AppKit API |
|---|---|---|
| Alternate selected control text | Text on selected list/table surface | `alternateSelectedControlTextColor` |
| Alternating content background | Alternating row/column backgrounds | `alternatingContentBackgroundColors` |
| Control accent | User-selected accent color | `controlAccentColor` |
| Control background | Large element background (browser, table) | `controlBackgroundColor` |
| Control | Control surface | `controlColor` |
| Control text | Available control text | `controlTextColor` |
| Current control tint | System control tint | `currentControlTint` |
| Unavailable control text | Unavailable control text | `disabledControlTextColor` |
| Find highlight | Find indicator | `findHighlightColor` |
| Grid | Gridlines (table, etc.) | `gridColor` |
| Header text | Table header cell text | `headerTextColor` |
| Highlight | Virtual light source | `highlightColor` |
| Keyboard focus indicator | Focus ring for keyboard navigation | `keyboardFocusIndicatorColor` |
| Label | Primary label text | `labelColor` |
| Link | Link text | `linkColor` |
| Placeholder text | Control/text view placeholder | `placeholderTextColor` |
| Quaternary label | Watermark-level text | `quaternaryLabelColor` |
| Secondary label | Subheading/additional info text | `secondaryLabelColor` |
| Selected content background | Selected content in key window | `selectedContentBackgroundColor` |
| Selected control | Selected control surface | `selectedControlColor` |
| Selected control text | Selected control text | `selectedControlTextColor` |
| Selected menu item text | Selected menu text | `selectedMenuItemTextColor` |
| Selected text background | Selected text background | `selectedTextBackgroundColor` |
| Selected text | Selected text | `selectedTextColor` |
| Separator | Section separator | `separatorColor` |
| Shadow | Virtual shadow of raised object | `shadowColor` |
| Tertiary label | Less important than secondary | `tertiaryLabelColor` |
| Text background | Background behind document text | `textBackgroundColor` |
| Text | Document text | `textColor` |
| Under page background | Background behind document content | `underPageBackgroundColor` |
| Unemphasized selected content background | Selected content in non-key window | `unemphasizedSelectedContentBackgroundColor` |
| Unemphasized selected text background | Selected text background in non-key window | `unemphasizedSelectedTextBackgroundColor` |
| Unemphasized selected text | Selected text in non-key window | `unemphasizedSelectedTextColor` |
| Window background | Window background | `windowBackgroundColor` |
| Window frame text | Title bar text | `windowFrameTextColor` |

**App accent colors (macOS 11+):** Specify an accent color for buttons, selection highlighting, and sidebar icons. System applies it when user's accent is set to Multicolor. If user picks a non-multicolor accent, it overrides yours — except fixed-color sidebar icons.

### tvOS

- Use a limited palette that coordinates with your app logo.
- Never use color alone to indicate focus — use scaling and animation.

### visionOS

- Use color sparingly on glass — physical environment shows through; color can conflict.
- Prefer color in bold text and large areas — lightweight text with color is hard to read.
- In fully immersive experiences, keep brightness balanced — avoid bright objects on very dark backgrounds, especially with flashing/movement.

### watchOS

- Use background color to communicate information, not as pure decoration.
- Avoid persistent full-screen background color in long-running views (workout, audio).
- Graphic complications: system may apply tinted mode (user's chosen color) instead of full color.

## Specifications

System colors (SwiftUI API): `red`, `orange`, `yellow`, `green`, `mint`, `teal`, `cyan`, `blue`, `indigo`, `purple`, `pink`, `brown`. visionOS uses default dark values.

iOS/iPadOS system gray colors (UIKit): `systemGray`, `systemGray2`, `systemGray3`, `systemGray4`, `systemGray5`, `systemGray6`. SwiftUI equivalent of `systemGray` is `gray`.
