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
  - dark-mode
---
# Materials

> Materials create depth, layering, and hierarchy between foreground and background elements by allowing color to pass through.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Apple provides two material types: **Liquid Glass** (controls/navigation layer) and **standard materials** (content layer differentiation).

## Liquid Glass

Liquid Glass forms the functional layer for controls and navigation (tab bars, sidebars). It floats above content, lets content scroll/peek through, and maintains control legibility.

- **Don't use Liquid Glass in the content layer.** It's for interactive elements only. Exception: transient interactive controls (sliders, toggles) briefly adopt Liquid Glass when activated.
- **Use sparingly on custom controls.** System components adopt it automatically. Overusing on custom controls distracts from content. Limit to most important functional elements.
- **Only use clear Liquid Glass over visually rich backgrounds** (photos, video). For text-heavy components (alerts, sidebars, popovers) use regular variant.

**Two Liquid Glass variants:**
- **Regular** — blurs and adjusts luminosity of background; used by most system components. Use when background may cause legibility issues or component has significant text.
- **Clear** — highly translucent; prioritizes background content visibility. Use over media backgrounds for an immersive feel.

**Dimming layer behind clear Liquid Glass:**
- Bright underlying content: add dark dimming layer at 35% opacity.
- Sufficiently dark content, or AVKit standard playback controls (which provide their own dimmer): no dimming layer needed.

## Standard Materials

Use standard materials within the content layer for visual structure and separation.

- Choose based on semantic meaning and purpose, not the color the material imparts (system settings alter appearance).
- Use vibrant (system-defined) colors on top of materials for automatic adaptation to accessibility and appearance contexts.
- Thicker (more opaque) materials = better contrast for text/fine details. Thinner (more translucent) = better context retention from background.

## Platform Considerations

### iOS, iPadOS

Four standard materials available for the content layer: `ultraThin`, `thin`, `regular` (default), `thick`.

Vibrancy values for **labels** (use on any material; avoid quaternary on thin/ultraThin):
- `label`, `secondaryLabel`, `tertiaryLabel`, `quaternaryLabel`

Vibrancy values for **fills** (all materials):
- `fill`, `secondaryFill`, `tertiaryFill`

One default vibrancy value for **separators** (works on all materials).

### macOS

Provides several standard materials with designated purposes, and vibrant versions of all system colors.

- Choose when to allow vibrancy in custom views/controls — test in varied contexts.
- Choose a background blending mode: **behind window** or **within window**.

### tvOS

Liquid Glass appears in navigation elements, Top Shelf, and Control Center. Image views and buttons adopt Liquid Glass when focused.

Standard materials for content layer:

| Material | Use for |
|---|---|
| `ultraThin` | Full-screen views requiring light color scheme |
| `thin` | Overlay views partially obscuring content; light color scheme |
| `regular` | Overlay views partially obscuring content |
| `thick` | Overlay views partially obscuring content; dark color scheme |

### visionOS

Windows use **glass** — a system-defined adaptive material letting physical surroundings, environments, and virtual content show through. Glass limits background color range to maintain contrast while adapting luminance to surroundings. No separate Dark Mode — glass adapts automatically.

- Prefer translucency over opacity in windows. Opaque areas block surroundings and feel confining.
- When creating custom components, choose system materials by purpose:
  - `thin` — interactive elements (buttons, selected items)
  - `regular` — visual section separation (sidebar, grouped table)
  - `thick` — dark elements that must remain distinct over a `regular` background

Vibrancy values for visionOS foreground content:
- `label` — standard text
- `secondaryLabel` — footnotes, subtitles
- `tertiaryLabel` — inactive elements where high legibility isn't required

### watchOS

Use materials to provide context in full-screen modal views. Don't remove or replace system-provided material backgrounds in modal sheets.
