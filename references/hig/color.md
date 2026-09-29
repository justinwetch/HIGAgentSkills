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

Color communicates status, feedback, brand and meaning. System colors can adapt automatically to appearance modes, vibrancy and accessibility settings.

## Best practices

- **Avoid using the same color to mean different things**, especially for status or interactivity: if your brand color marks borderless buttons as interactive, the same or similar color on noninteractive text is confusing.
- **Make sure all colors work in light, dark and increased contrast contexts.** When possible, use system colors, which define these variants. For custom colors, make sure to supply light and dark variants, each with a significantly more differentiated increased contrast option. Even in a single-appearance app, provide light and dark colors for Liquid Glass adaptivity.
- **Test your color scheme under a variety of lighting conditions**: bright and dim light and, in visionOS, varied physical surroundings; adjust for most use cases.
- **Test on different devices**, including tvOS apps on multiple brands of HD and 4K TVs and display settings. On a Mac, you can test profiles like P3 and sRGB in System Settings > Displays. Apps primarily for reading, photos, video and gaming can strengthen or weaken True Tone white-point adaptation with `UIWhitePointAdaptivityStyle`.
- **Consider how artwork and translucency affect nearby colors.** Artwork sometimes warrants changing nearby colors (Maps goes dark in satellite mode); colors can look different behind or on translucent elements like toolbars.
- **If people can choose colors, prefer system-provided color controls where available** (`ColorPicker`).

## Inclusive color

- **Avoid relying solely on color** to differentiate objects, indicate interactivity or communicate essential information; be sure to also convey it another way, like text labels or glyph shapes.
- **Avoid colors that make content hard to perceive**, like insufficient contrast or combinations people with color blindness might not distinguish.
- **Consider how colors are perceived in other cultures.** Red means danger in some, positive in others (Stocks: rising trends green in English, red in Chinese).

## System colors

- **Avoid hard-coding system color values**; they may fluctuate between releases and with environmental variables. Apply system colors with APIs like `Color`.
- iOS, iPadOS, macOS and visionOS *dynamic system colors* adapt automatically to light and dark and are defined by purpose (background levels, labels, links, separators), not appearance. **Avoid redefining their semantic meanings**: for example, don't use separator color for text or secondary label color as a background.

## Liquid Glass color

By default, Liquid Glass has no inherent color and takes on color from content behind it; symbols and text on it can have color (like a selected tab bar item). The system can adapt smaller elements like toolbars and tab bars between light and dark with the underlying content, with monochromatic symbols and text by default (darker over light content, lighter over dark). Larger elements like sidebars are more opaque, for legibility.

- **Apply color sparingly to the material and to symbols or text on it**, reserving it for elements that truly benefit from emphasis, like status indicators or primary actions. For a primary action, color the background, not symbols or text, as the system does with the accent color in prominent buttons like Done. Refrain from coloring multiple controls' backgrounds.
- **Avoid similar colors in control labels over a colorful background.** With colorful backgrounds or rich content, prefer monochromatic toolbars and tab bars, or a sufficiently differentiated accent color. With primarily monochromatic content, your brand color can be an effective accent color.
- **Be aware of color placement in the content layer.** Avoid overlapping similar colors in content and controls when possible; content may scroll under controls, but make sure the resting state, like the top of scrollable content, stays clearly legible.

## Color management

sRGB is standard; Display P3 is a wider gamut; images embed a *color profile*.

- **Apply color profiles to your images.** sRGB produces accurate colors on most displays.
- **Use wide color on compatible displays**; P3 is richer and more saturated than sRGB. When appropriate, use Display P3 at 16 bits per pixel (per channel) and export PNG. Designing wide color images and picking P3 colors requires a wide color display.
- **Provide color space-specific image and color variations if necessary**, which you can do in your Xcode asset catalog. P3 generally looks fine on sRGB displays, but very similar P3 colors can occasionally be indistinguishable and P3 gradients can appear clipped.

## Platform considerations

### iOS, iPadOS

In general, use grouped background colors (`systemGroupedBackground`, `secondarySystemGroupedBackground`, `tertiarySystemGroupedBackground`) for a grouped table view, and system background colors (`systemBackground`, `secondarySystemBackground`, `tertiarySystemBackground`) otherwise. Generally, primary is the overall view, secondary groups content within it, and tertiary groups within secondary elements.

Foreground dynamic colors (`UIColor`):

|API|Use for|
|---|---|
|`label`|Primary-content text|
|`secondaryLabel`|Secondary-content text|
|`tertiaryLabel`|Tertiary-content text|
|`quaternaryLabel`|Quaternary-content text|
|`placeholderText`|Placeholder text in controls or text views|
|`separator`|Separator that lets some underlying content show|
|`opaqueSeparator`|Separator that hides underlying content|
|`link`|Text that functions as a link|

### macOS

Dynamic system colors (`NSColor`):

|API|Use for|
|---|---|
|`alternateSelectedControlTextColor`|Text on a selected surface in a list or table|
|`alternatingContentBackgroundColors`|Alternating row or column backgrounds in a list, table or collection view|
|`controlAccentColor`|Accent color people select in System Settings|
|`controlBackgroundColor`|Background of a large element, such as a browser or table|
|`controlColor`|Control surface|
|`controlTextColor`|Text of an available control|
|`currentControlTint`|System-defined control tint|
|`disabledControlTextColor`|Text of an unavailable control|
|`findHighlightColor`|Find indicator|
|`gridColor`|Gridlines, such as in a table|
|`headerTextColor`|Table header cell text|
|`highlightColor`|Virtual onscreen light source|
|`keyboardFocusIndicatorColor`|Ring around the control focused via keyboard navigation|
|`labelColor`|Primary-content label text|
|`linkColor`|Link to other content|
|`placeholderTextColor`|Placeholder string in a control or text view|
|`quaternaryLabelColor`|Label text less important than tertiary, such as watermarks|
|`secondaryLabelColor`|Label text less important than primary, such as a subheading or additional information|
|`selectedContentBackgroundColor`|Selected content background in a key window or view|
|`selectedControlColor`|Selected control surface|
|`selectedControlTextColor`|Selected control text|
|`selectedMenuItemTextColor`|Selected menu text|
|`selectedTextBackgroundColor`|Selected text background|
|`selectedTextColor`|Selected text|
|`separatorColor`|Separator between content sections|
|`shadowColor`|Virtual shadow cast by a raised onscreen object|
|`tertiaryLabelColor`|Label text less important than secondary|
|`textBackgroundColor`|Background behind text|
|`textColor`|Document text|
|`underPageBackgroundColor`|Background behind a document's content|
|`unemphasizedSelectedContentBackgroundColor`|Selected content in a non-key window or view|
|`unemphasizedSelectedTextBackgroundColor`|Selected text background in a non-key window or view|
|`unemphasizedSelectedTextColor`|Selected text in a non-key window or view|
|`windowBackgroundColor`|Window background|
|`windowFrameTextColor`|Title bar area text|

**App accent colors.** Beginning in macOS 11, you can specify an *accent color* for your app's buttons, selection highlighting and sidebar icons. The system applies it when General > Accent color is *multicolor*; otherwise the person's chosen color replaces it, except in a sidebar icon you give a fixed color for meaning.

### tvOS

- **Consider a limited color palette that coordinates with your app logo**, using subtle color that defers to content.
- **Avoid using only color to indicate focus.** Subtle scaling and responsive animation are the primary indicators.

### visionOS

- **Use color sparingly, especially on glass**; physical surroundings show through glass. Prefer color that calls attention to important information or shows relationships between interface parts.
- **Prefer color in bold text and large areas**; in lightweight text or small areas it can be harder to see and understand.
- **In a fully immersive experience, keep brightness levels balanced.** Consider making content fully bright only when the rest of the context is also bright; for example, avoid a bright object on a very dark or black background, especially if it flashes or moves.

### watchOS

- **Use background color to support existing content or supply additional information**, not as a solely visual flourish. Avoid full-screen background color in views likely to remain onscreen for long periods, such as workout or audio-playing apps.
- **Recognize that people might prefer tinted mode over full color for graphic complications**, where the system can apply one color based on the wearer's selection to images, gauges and text.

## Specifications

### System colors

RGB values, for design reference only (avoid hard-coding); SwiftUI API is the lowercase name (`red`, `orange`...). visionOS uses the default dark values.

|Name|Light|Dark|Increased contrast light|Increased contrast dark|
|---|---|---|---|---|
|Red|255,56,60|255,66,69|233,21,45|255,97,101|
|Orange|255,141,40|255,146,48|197,83,0|255,160,86|
|Yellow|255,204,0|255,214,0|161,106,0|254,223,67|
|Green|52,199,89|48,209,88|0,137,50|74,217,104|
|Mint|0,200,179|0,218,195|0,133,117|84,223,203|
|Teal|0,195,208|0,210,224|0,129,152|59,221,236|
|Cyan|0,192,232|60,211,254|0,126,174|109,217,255|
|Blue|0,136,255|0,145,255|30,110,244|92,184,255|
|Indigo|97,85,245|109,124,255|86,74,222|167,170,255|
|Purple|203,48,224|219,52,242|176,47,194|234,141,255|
|Pink|255,45,85|255,55,95|231,18,77|255,138,196|
|Brown|172,127,94|183,138,102|149,109,81|219,166,121|

### iOS, iPadOS system gray colors

RGB values. In SwiftUI, the equivalent of `systemGray` is `gray`.

|UIKit API|Light|Dark|Increased contrast light|Increased contrast dark|
|---|---|---|---|---|
|`systemGray`|142,142,147|142,142,147|108,108,112|174,174,178|
|`systemGray2`|174,174,178|99,99,102|142,142,147|124,124,128|
|`systemGray3`|199,199,204|72,72,74|174,174,178|84,84,86|
|`systemGray4`|209,209,214|58,58,60|188,188,192|68,68,70|
|`systemGray5`|229,229,234|44,44,46|216,216,220|54,54,56|
|`systemGray6`|242,242,247|28,28,30|235,235,240|36,36,38|

## Resources

Source: [Color](https://developer.apple.com/design/human-interface-guidelines/color), captured 2026-09-12.
