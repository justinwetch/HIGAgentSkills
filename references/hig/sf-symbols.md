---
topic: sf-symbols
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "SF Symbol"
  - "symbol"
  - "glyph"
  - "system icon"
  - "weight rendering"
related:
  - icons
  - typography
---
# SF Symbols

> Thousands of consistent, configurable symbols integrate with the San Francisco system font and automatically align with text at every weight and size.

Use symbols for objects or concepts wherever interface icons appear, including toolbars, tab bars, context menus, and text. Individual symbols and features depend on the target OS version; symbols introduced in a year aren't available on earlier systems. Download and browse the library in [SF Symbols](https://developer.apple.com/sf-symbols/). Its terms prohibit using symbols, or confusingly similar images, in app icons, logos, or other trademarked uses.

## Rendering modes

Paths are organized into layers; in `cloud.sun.rain.fill`, primary = cloud, secondary = sun and rays, tertiary = raindrops. The four modes are:

| Mode | Behavior |
|---|---|
| **Monochrome** | One color for every layer; paths use that color or form transparent shapes within a color-filled path. |
| **Hierarchical** | One color with opacity varying by each layer's hierarchy, producing depth. For `cloud.sun.rain.fill`: about 100% cloud, 50% sun, 25% raindrops. |
| **Palette** | Two or more colors, one per layer. With two colors for a three-level symbol, secondary and tertiary share the second color. |
| **Multicolor** | Intrinsic colors can add meaning (`leaf` green, `trash.slash` red); some layers accept additional colors. |

System-provided colors adapt automatically to accessibility accommodations and appearances such as vibrancy and Dark Mode. The `automatic` setting can obtain a symbol's preferred mode, but **confirm that the mode works in every context**: size and background contrast can make another mode clearer. For developer guidance, see SwiftUI `renderingMode(_:)`.

## Gradients (SF Symbols 7+)

Gradient rendering creates a smooth linear gradient from one source color. It works for system or custom colors, in every mode, at every size, and with custom symbols; larger sizes show it best.

## Variable color

Use variable color to represent a changing characteristic such as capacity or strength, regardless of rendering mode, applying color to layers as a value crosses thresholds from 0% to 100%. For example, `speaker.wave.3` can represent three sound ranges, expressed in decibels, plus no sound: at no sound, no wave is colored; otherwise the system places color at thresholds based on the number of nonzero states. A layer can opt out when it represents something unchanged (the speaker body); any number of layers may support variable color.

**Use variable color for change, not depth.** Use Hierarchical mode to distinguish foreground and background layers and convey depth.

## Weights and scales

- **Weights:** nine, ultralight through black, each matching a San Francisco font weight for precise symbol/text pairing.
- **Scales:** small, medium (default), and large, defined relative to the font's cap height. Scale changes emphasis against adjacent text without breaking weight matching at the same point size.

Developer APIs: SwiftUI `imageScale(_:)`, UIKit `UIImage.SymbolScale`, and AppKit `NSImage.SymbolConfiguration`.

## Design variants

Outline is the common, text-like variant; fill makes selected areas solid. Slash and enclosed (circle, square, rectangle) variants communicate unavailability or improve small-size legibility, and variants can combine (outline/fill with slash/enclosure).

| Use | Guidance |
|---|---|
| Outline | Toolbars, lists, and symbols beside text. |
| Enclosed | Can improve legibility at small sizes. |
| Fill | Visual emphasis in iOS tab bars, swipe actions, and accent-colored selection. |
| Slash | An unavailable item or action. |

The displaying view often chooses outline or fill automatically: an iOS tab bar prefers fill and a toolbar takes outline. Language/script variants — Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, Korean, Cyrillic, Devanagari, and several Indic numeral systems — adapt when the device language changes.

## Animations

Animations work on every library and custom symbol, rendering mode, weight, and scale. Configure one-shot or indefinite playback, speed, repeat, and reversal; developer APIs include the `Symbols` framework and `SymbolEffect`. Apply them judiciously: each movement should communicate the symbol's intent without confusing or overwhelming people, use visual space efficiently, and fit the app's tone and branding.

| Animation | Behavior and appropriate signal |
|---|---|
| **Appear / Disappear** | Layers gradually emerge / recede. |
| **Bounce** | Brief elastic scale up/down returns to the initial state; plays once by default and signals an action occurred or needs to occur. Layers can bounce individually. |
| **Scale** | Changes size and persists until a new scale or removal; can draw attention to a selection or acknowledge a choice. |
| **Pulse** | Varies opacity over time; pulses annotated layers (optionally all), useful for ongoing activity. |
| **Variable color** | Incrementally changes layer opacity, cumulatively (each layer remains changed through the cycle) or iteratively (one at a time); useful for progress, playback, connecting, or broadcasting. Autoreverse and hiding inactive layers are configurable. Repeating animations are **open loop** when linear layer endpoints don't meet and **closed loop** when they form a complete shape (such as a progress ring); closed loops play seamlessly. |
| **Replace** | Swaps arbitrary symbols across weights and modes: **down-up** scales outgoing down/incoming up for state change; **up-up** scales both up for forward progression; **off-up** hides outgoing immediately and scales incoming up to emphasize the next state. |
| **Magic Replace** | The default replacement for related shapes: slashes can draw on/off and badges appear/disappear or change independently. Unrelated symbols fall back to down-up; choose another fallback direction if desired. |
| **Wiggle** | Moves laterally, rotationally, or along an axis to highlight change, a call to action, or directional meaning. |
| **Breathe** | Smoothly changes opacity and size for status or ongoing activity (such as recording). Unlike Pulse, it changes both. |
| **Rotate** | Rotates the whole symbol or selected parts as an in-progress indicator or to imitate real behavior; a desk fan can use By Layer for its blades. |
| **Draw On / Draw Off (SF Symbols 7+)** | Draws along guide points from offscreen to onscreen or the reverse; draw all layers together, stagger them, or draw one layer at a time. Useful for progress or directional arrows. |

## Custom symbols

Export a similar symbol's template, modify it in a vector editor, and annotate each layer with a color or hierarchy (primary, secondary, tertiary). A custom symbol should match system symbols in detail, optical weight, alignment, position, and perspective; keep it simple, recognizable, inclusive, and directly related to its action/content. Depending on the rendering modes you support, choose a mode per instance as needed.

- Apple product/feature symbols may be displayed but cannot be customized; the SF Symbols app marks these copyrighted, restricted symbols with an Info badge, and its inspector describes their usage restrictions. Do not replicate Apple products.
- **If necessary**, assign negative side margins when a badge or other element increases width, to aid optical horizontal alignment (for example, align a stack of folders when some have badges). Name each margin for its configuration, such as `left-margin-Regular-M`.
- Annotate layers for variable color and, **if you want to animate by layer**, for animation. Z-order controls variable-color order (front-to-back or back-to-front), and layer groups can move together. Prefer whole shapes plus an offset path annotated as an erase layer for negative space (for example, a `person.2.fill`-like symbol) so animation retains layer information. Test every animation preset.
- Use the SF Symbols component library for common enclosures and badges instead of hand-making variants. Provide alternative text/accessibility labels for VoiceOver.

## Platform considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

## Resources

[Typography](https://developer.apple.com/design/human-interface-guidelines/typography) · [Icons](https://developer.apple.com/design/human-interface-guidelines/icons) · [SF Symbols](https://developer.apple.com/sf-symbols/) · [Symbols framework](https://developer.apple.com/documentation/symbols) · [Configuring and displaying symbol images](https://developer.apple.com/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui) · [Creating custom symbol images](https://developer.apple.com/documentation/uikit/creating-custom-symbol-images-for-your-app) · [WWDC25: SF Symbols](https://developer.apple.com/videos/play/wwdc2025/337)

Source: [Apple Human Interface Guidelines — SF Symbols](https://developer.apple.com/design/Human-Interface-Guidelines/sf-symbols), captured 2026-09-12.
