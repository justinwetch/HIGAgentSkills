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
- Test on different devices (True Tone iPhones/iPads/Macs; tvOS on multiple TV brands/settings). Reading, photo, video, and game apps can tune white-point adaptivity with `UIWhitePointAdaptivityStyle`. Use P3 and sRGB profiles on Mac via System Settings > Displays.
- Consider how artwork and translucency affect nearby colors — map-mode vs. satellite-mode color scheme switching is a good example.
- Use system color pickers (`ColorPicker`) when letting people choose colors.
- Never rely on color alone to differentiate, convey interactivity, or communicate info — provide text labels or glyph shapes as alternatives.
- Avoid insufficient contrast between text/icons and backgrounds.
- Research cultural color meanings per locale (e.g., red = danger vs. positive in different cultures).

## System Colors

- Never hard-code system color values — they change between releases. Use `Color` API.
- Dynamic system colors are semantically defined (purpose, not appearance). Don't repurpose them (e.g., don't use `separator` for text or `secondaryLabel` for background).

## Liquid Glass Color

- Liquid Glass has no inherent color by default — it takes on colors from behind it.
- Smaller elements (toolbars, tab bars) can adapt between light/dark appearance based on underlying content; symbols/text default to monochrome, dark over light content and light over dark content.
- Larger elements (sidebars) appear more opaque to preserve legibility over complex backgrounds and support richer content on the material surface.
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

### System colors

| Name | SwiftUI API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
| --- | --- | --- | --- | --- | --- |
| Red | [red](https://developer.apple.com/documentation/SwiftUI/Color/red) | [Image: R-255,G-56,B-60] | [Image: R-255,G-66,B-69] | [Image: R-233,G-21,B-45] | [Image: R-255,G-97,B-101] |
| Orange | [orange](https://developer.apple.com/documentation/SwiftUI/Color/orange) | [Image: R-255,G-141,B-40] | [Image: R-255,G-146,B-48] | [Image: R-197,G-83,B-0] | [Image: R-255,G-160,B-86] |
| Yellow | [yellow](https://developer.apple.com/documentation/SwiftUI/Color/yellow) | [Image: R-255,G-204,B-0] | [Image: R-255,G-214,B-0] | [Image: R-161,G-106,B-0] | [Image: R-254,G-223,B-67] |
| Green | [green](https://developer.apple.com/documentation/SwiftUI/Color/green) | [Image: R-52,G-199,B-89] | [Image: R-48,G-209,B-88] | [Image: R-0,G-137,B-50] | [Image: R-74,G-217,B-104] |
| Mint | [mint](https://developer.apple.com/documentation/SwiftUI/Color/mint) | [Image: R-0,G-200,B-179] | [Image: R-0,G-218,B-195] | [Image: R-0,G-133,B-117] | [Image: R-84,G-223,B-203] |
| Teal | [teal](https://developer.apple.com/documentation/SwiftUI/Color/teal) | [Image: R-0,G-195,B-208] | [Image: R-0,G-210,B-224] | [Image: R-0,G-129,B-152] | [Image: R-59,G-221,B-236] |
| Cyan | [cyan](https://developer.apple.com/documentation/SwiftUI/Color/cyan) | [Image: R-0,G-192,B-232] | [Image: R-60,G-211,B-254] | [Image: R-0,G-126,B-174] | [Image: R-109,G-217,B-255] |
| Blue | [blue](https://developer.apple.com/documentation/SwiftUI/Color/blue) | [Image: R-0,G-136,B-255] | [Image: R-0,G-145,B-255] | [Image: R-30,G-110,B-244] | [Image: R-92,G-184,B-255] |
| Indigo | [indigo](https://developer.apple.com/documentation/SwiftUI/Color/indigo) | [Image: R-97,G-85,B-245] | [Image: R-109,G-124,B-255] | [Image: R-86,G-74,B-222] | [Image: R-167,G-170,B-255] |
| Purple | [purple](https://developer.apple.com/documentation/SwiftUI/Color/purple) | [Image: R-203,G-48,B-224] | [Image: R-219,G-52,B-242] | [Image: R-176,G-47,B-194] | [Image: R-234,G-141,B-255] |
| Pink | [pink](https://developer.apple.com/documentation/SwiftUI/Color/pink) | [Image: R-255,G-45,B-85] | [Image: R-255,G-55,B-95] | [Image: R-231,G-18,B-77] | [Image: R-255,G-138,B-196] |
| Brown | [brown](https://developer.apple.com/documentation/SwiftUI/Color/brown) | [Image: R-172,G-127,B-94] | [Image: R-183,G-138,B-102] | [Image: R-149,G-109,B-81] | [Image: R-219,G-166,B-121] |

visionOS system colors use the default dark color values.

### iOS, iPadOS system gray colors

| Name | UIKit API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
| --- | --- | --- | --- | --- | --- |
| Gray | [systemGray](https://developer.apple.com/documentation/UIKit/UIColor/systemGray) | [Image: R-142,G-142,B-147] | [Image: R-142,G-142,B-147] | [Image: R-108,G-108,B-112] | [Image: R-174,G-174,B-178] |
| Gray (2) | [systemGray2](https://developer.apple.com/documentation/UIKit/UIColor/systemGray2) | [Image: R-174,G-174,B-178] | [Image: R-99,G-99,B-102] | [Image: R-142,G-142,B-147] | [Image: R-124,G-124,B-128] |
| Gray (3) | [systemGray3](https://developer.apple.com/documentation/UIKit/UIColor/systemGray3) | [Image: R-199,G-199,B-204] | [Image: R-72,G-72,B-74] | [Image: R-174,G-174,B-178] | [Image: R-84,G-84,B-86] |
| Gray (4) | [systemGray4](https://developer.apple.com/documentation/UIKit/UIColor/systemGray4) | [Image: R-209,G-209,B-214] | [Image: R-58,G-58,B-60] | [Image: R-188,G-188,B-192] | [Image: R-68,G-68,B-70] |
| Gray (5) | [systemGray5](https://developer.apple.com/documentation/UIKit/UIColor/systemGray5) | [Image: R-229,G-229,B-234] | [Image: R-44,G-44,B-46] | [Image: R-216,G-216,B-220] | [Image: R-54,G-54,B-56] |
| Gray (6) | [systemGray6](https://developer.apple.com/documentation/UIKit/UIColor/systemGray6) | [Image: R-242,G-242,B-247] | [Image: R-28,G-28,B-30] | [Image: R-235,G-235,B-240] | [Image: R-36,G-36,B-38] |

In SwiftUI, the equivalent of `systemGray` is [gray](https://developer.apple.com/documentation/SwiftUI/Color/gray).
