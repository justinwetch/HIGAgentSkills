---
topic: dark-mode
tier: 1
platforms: [ios, ipados, macos, tvos]
category: foundations
triggers:
  - "dark mode"
  - "dark appearance"
  - "light mode"
  - "color scheme"
related:
  - color
  - materials
  - typography
---
# Dark Mode

> Dark Mode is a systemwide dark palette for comfortable low-light viewing.

In iOS, iPadOS, macOS, and tvOS, people often choose Dark Mode as their default and expect apps/games to respect it. The system applies the dark palette to screens, views, menus, and controls, sometimes with greater perceptual contrast.

## Best Practices

- Avoid an app-specific appearance setting; it makes people manage two settings and may appear broken when it ignores the system choice.
- Ensure the app works in both appearances and with **Auto**, which can switch between them while the app runs.
- Test legibility in both modes with Increase Contrast and Reduce Transparency separately and together. In Dark Mode, Increased Contrast can reduce contrast between dark text and dark backgrounds; low-contrast text may be illegible.
- In rare cases, consider a dark-only interface for immersive media viewing, where a receding UI helps focus on media.

## Dark Mode Colors

Dark Mode uses dimmer backgrounds and brighter foregrounds; colors are not necessarily light-mode inversions.

- Use semantic colors that adapt automatically (`labelColor`/`controlColor` in macOS; `separator` in iOS/iPadOS).
- For custom colors, add an Xcode Color Set with bright and dim variants. Avoid hard-coded or non-adaptive values.
- Keep foreground/background contrast at least **4.5:1**; for custom colors, strive for **7:1**, especially for small text.
- Consider slightly darkening a content image with a white background so it doesn’t glow in the surrounding dark context.

### Icons and Images

- Use SF Symbols where possible; dynamic colors or vibrancy let them work in both modes.
- If needed, design separate light/dark interface-icon variants. A full-moon icon may need a subtle dark outline on a light background but none on a dark background; an oil-drop icon may need a slight border on a dark background.
- Ensure full-color images/icons work in both modes. Reuse one asset when it does; otherwise modify it or create light/dark assets and combine them in one named asset-catalog image.

### Text

- Use system primary, secondary, tertiary, and quaternary label colors; they adapt automatically.
- Use system views for text fields/text views so vibrancy and background adaptation preserve legibility.

## Platform Considerations

No additional tvOS considerations. Dark Mode isn’t supported in visionOS or watchOS.

### iOS, iPadOS

Dark interfaces use base and elevated background sets to convey depth. Base is dimmer and recedes; elevated is brighter and advances. Prefer system background colors: the system changes base to elevated when a foreground interface (such as a popover or modal sheet) appears, and uses elevated backgrounds to separate apps in multitasking and windows in multiple-window contexts. Custom backgrounds can obscure these distinctions.

### macOS

With the graphite accent color, window backgrounds pick up color from the desktop picture (“desktop tinting”). For custom components with a visible background or bezel, include transparency **when appropriate** and only in a neutral state so the component harmonizes as the desktop changes. Transparency in a colored state can make its color fluctuate as the desktop/window background changes.

## References

[Color](https://developer.apple.com/design/human-interface-guidelines/color), [Materials](https://developer.apple.com/design/human-interface-guidelines/materials), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols), and [Typography](https://developer.apple.com/design/human-interface-guidelines/typography). APIs: [AppKit `labelColor`](https://developer.apple.com/documentation/appkit/nscolor/labelcolor), [AppKit `controlColor`](https://developer.apple.com/documentation/appkit/nscolor/controlcolor), and [UIKit `separator`](https://developer.apple.com/documentation/uikit/uicolor/separator).

Source: [Apple Human Interface Guidelines — Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode/), captured 2026-09-12.
