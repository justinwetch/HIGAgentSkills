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

> Thousands of consistent, configurable symbols that integrate seamlessly with San Francisco system font, auto-aligning with text at all weights and sizes.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Use symbols in toolbars, tab bars, context menus, and within text. Symbol availability varies by OS version — symbols introduced in a given year aren't available on earlier systems.

Don't use SF Symbols (or confusingly similar images) in app icons, logos, or any trademarked use.

## Rendering Modes

Symbols organize paths into primary, secondary, and tertiary **layers**. Four rendering modes:

| Mode | Behavior |
|---|---|
| **Monochrome** | One color applied to all layers. Paths render in specified color or transparent within color-filled paths. |
| **Hierarchical** | One color, varying opacity per layer — creates visual depth. |
| **Palette** | Two or more colors, one per layer. If only two colors specified for a three-layer symbol, secondary and tertiary share the second color. |
| **Multicolor** | Intrinsic colors for symbols where color carries meaning (e.g., `leaf` = green, `trash.slash` = red). Some layers can receive additional colors. |

Use system-provided colors in any rendering mode for automatic adaptation to accessibility and Dark Mode. Use the `automatic` setting to get a symbol's preferred mode; still verify legibility in all contexts.

## Gradients (SF Symbols 7+)

Gradient rendering applies a smooth linear gradient from a single source color. Works in all rendering modes, for system and custom colors, and custom symbols. Best at larger sizes.

## Variable Color

Represents a changing characteristic (capacity, signal strength) by applying color to layers as a value crosses defined thresholds between 0–100%.

- Use to communicate **change over time**, not to convey depth — use Hierarchical mode for depth.
- Layers can opt out of variable color (e.g., the speaker body in `speaker.wave.3` doesn't change with volume).
- Closed-loop symbols (circular paths, like a progress ring) feature seamless continuous variable color playback. Open-loop symbols (linear start/end points that don't meet) do not.

## Weights and Scales

- **9 weights** — ultralight to black — matching SF font weights for precise text/symbol weight pairing.
- **3 scales** — small, medium (default), large — defined relative to SF cap height. Adjusting scale changes symbol emphasis without disrupting weight matching.

## Design Variants

| Variant | Best used in |
|---|---|
| Outline | Toolbars, lists, alongside text |
| Fill | Tab bars (iOS), swipe actions, selection states with accent color |
| Enclosed (circle, square, rectangle) | Improves legibility at small sizes |
| Slash | Unavailable state |

Outline + fill, enclosed + slash combinations are supported. Many views automatically choose outline vs. fill (e.g., iOS tab bars prefer fill; toolbars take outline) — no manual specification needed.

Language-specific variants (Arabic, Hebrew, Hindi, Thai, CJK, Cyrillic, Devanagari, Indic numerals) auto-apply when device language changes.

## Animations

Apply animations judiciously — too many overwhelm the interface. Each animation communicates a specific type of action; verify the meaning matches the intent.

| Animation | Behavior / Use |
|---|---|
| **Appear** | Symbol gradually emerges into view |
| **Disappear** | Symbol gradually recedes out of view |
| **Bounce** | Elastic scale movement returning to initial state. Communicates that an action occurred or needs to. Default: plays once. |
| **Scale** | Persistent size change (doesn't return to original). Use for selection emphasis or tap feedback. |
| **Pulse** | Opacity variation over time. Pulses annotated layers (optionally all). Use for ongoing activity. |
| **Variable color** | Incrementally varies opacity of layers. Cumulative: changes persist per layer through cycle. Iterative: one layer at a time. Use for progress, connecting, broadcasting. Supports autoreverse and hiding inactive layers. |
| **Replace** | Swaps one symbol for another across weights/modes. Configs: Down-up (state change), Up-up (forward progression), Off-up (emphasize next state). |
| **Magic Replace** | Smart transition between related symbols (slashes draw on/off, badges appear/disappear). Falls back to down-up for unrelated symbols. |
| **Wiggle** | Back-and-forth on a directional axis. Use to highlight change, call to action, or directional meaning. |
| **Breathe** | Smooth opacity + size variation for a living quality. Use for status changes or ongoing activity (e.g., recording). Differs from Pulse: changes both opacity and size. |
| **Rotate** | Full or partial rotation. Use for in-progress indicators or real-world rotation behavior (e.g., fan blades via By Layer). |
| **Draw On / Draw Off** (SF Symbols 7+) | Draws symbol along a path — all at once, staggered, or one layer at a time. Use for progress or to reinforce directionality. |

## Custom Symbols

Export a similar symbol's template → modify in a vector editor → annotate layers for rendering modes/color.

- Match system symbols in detail level, optical weight, alignment, position, and perspective.
- Custom symbols must be: simple, recognizable, inclusive, and directly related to the concept.
- Copyright restriction: Apple product/feature symbols cannot be customized.
- Use **negative side margins** when a badge or element increases symbol width (naming pattern: e.g., `left-margin-Regular-M`).
- **Annotate layers** for variable color and animation support. Use whole shapes (not cutouts) for best animation behavior — use erase layers for negative space.
- Use the SF Symbols **component library** for common variants (enclosures, badges) — maintains design consistency.
- Provide **alternative text labels** for VoiceOver accessibility.
- Don't replicate Apple product designs.

## Platform Considerations

*No additional considerations for any platform.*
