---
topic: materials
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "material"
  - "glass"
  - "blur"
  - "vibrancy"
  - "translucent"
  - "frosted"
  - "Liquid Glass"
related:
  - color
  - accessibility
  - dark-mode
---
# Materials

A material is a visual effect that creates depth, layering, and hierarchy between foreground and background. Apple platforms provide two kinds: Liquid Glass, a dynamic functional layer for controls and navigation; and standard materials, which differentiate content-layer elements.

## Liquid Glass

- Use Liquid Glass for controls and navigation (such as tab bars and sidebars) floating above content. Let content scroll and peek through while preserving control and navigation legibility.
- **Don’t use Liquid Glass in the content layer.** Use standard materials for content-layer elements such as app backgrounds. The exception is a transient interactive control in that layer, such as a slider or toggle, which can take on Liquid Glass while activated.
- Use Liquid Glass effects sparingly on custom controls; system components provide the appearance and behavior automatically. Limit custom effects to the most important functional elements because the material should draw attention to underlying content. Developer reference: [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views).
- Liquid Glass has [regular](https://developer.apple.com/documentation/swiftui/glass/regular) and [clear](https://developer.apple.com/documentation/swiftui/glass/clear) variants, whose appearance can change with preferred-look, reduced-transparency, and increased-contrast settings. Regular blurs and adjusts background luminosity, and scroll-edge effects add blur and reduce opacity; it is the usual system choice. Use regular when background content might create legibility issues or components contain significant text, such as alerts, sidebars, or popovers. Regular appears darker over dark backgrounds and lighter over light backgrounds. **Only use clear over visually rich backgrounds.** Clear is highly translucent and prioritizes media visibility. For clear over bright content, consider a dark dimming layer at **35% opacity**; no additional layer is needed over sufficiently dark content or when standard AVKit playback controls provide their own.

## Standard materials and effects

Use [blur](https://developer.apple.com/documentation/uikit/uiblureffect), [vibrancy](https://developer.apple.com/documentation/uikit/uivibrancyeffect), and AppKit [blending modes](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode-swift.enum) to structure content beneath Liquid Glass. Choose by semantic meaning and recommended use, not the apparent color (system settings can change appearance). Use system-defined vibrant colors over any material to avoid dark, bright, saturated, or low-contrast results. Thicker, more opaque materials improve contrast for fine details; thinner, more translucent materials preserve context by showing more background. See [SwiftUI Material](https://developer.apple.com/documentation/swiftui/material).

### Platform considerations

**iOS, iPadOS:** Four standard content-layer materials are available: ultra-thin, thin, regular (default), and thick. Vibrancy defines label, fill, and separator hierarchy: default has highest contrast; quaternary, when available, lowest. Label styles work on any material except that quaternary is generally too low-contrast over thin and ultra-thin. Labels: [label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label), [secondaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondarylabel), [tertiaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiarylabel), [quaternaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/quaternarylabel). Fills work on all materials: [fill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/fill), [secondaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondaryfill), [tertiaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiaryfill). Separators use one default style on all materials; see [separator](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/separator).

**macOS:** Standard materials have designated purposes and all system colors have vibrant versions. Test custom views and controls across contexts and system settings before allowing vibrancy. Choose between [behind-window and within-window blending](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode-swift.enum); see [NSVisualEffectView.Material](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material-swift.enum).

**tvOS:** Liquid Glass appears throughout navigation and system experiences (including Top Shelf and Control Center); image views and buttons can adopt it on focus. Standard-material thickness controls how much content shows through:

| Material | Recommended for |
|---|---|
| [ultraThin](https://developer.apple.com/documentation/swiftui/material/ultrathin) | Full-screen views requiring a light color scheme |
| [thin](https://developer.apple.com/documentation/swiftui/material/thin) | Partial overlays requiring a light color scheme |
| [regular](https://developer.apple.com/documentation/swiftui/material/regular) | Partial overlays |
| [thick](https://developer.apple.com/documentation/swiftui/material/thick) | Partial overlays requiring a dark color scheme |

**visionOS:** Windows generally use unmodifiable adaptive *glass*, which lets light, the current Environment, virtual content, and surroundings show through while constraining background color for contrast. There is no distinct Dark Mode; glass adapts to behind-window luminance. Prefer translucency to opaque colors, which block the view and reduce awareness of surroundings. For custom components, thin can emphasize interactive elements, regular can separate sections (sidebar/grouped table), and thick can keep a dark element distinct over regular. visionOS applies vibrancy to text, symbols, and fills. Its hierarchy is [label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) for standard text, [secondaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondarylabel) for descriptive text, and [tertiaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiarylabel) for inactive elements only when text needn’t be highly legible; contrast decreases from primary to secondary to tertiary.

**watchOS:** Use material layers for context in full-screen modal views; don’t remove or replace default modal-sheet materials. Developer references include [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [glassEffect(_:in:)](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)), [UIVisualEffectView](https://developer.apple.com/documentation/uikit/uivisualeffectview), and [NSVisualEffectView](https://developer.apple.com/documentation/appkit/nsvisualeffectview).

Source: [Apple HIG — Materials](https://developer.apple.com/design/human-interface-guidelines/materials), captured 2026-09-12.
