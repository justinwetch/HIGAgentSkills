---
topic: segmented-controls
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: components/controls
triggers:
  - "segmented control"
  - "UISegmentedControl"
  - "segmented"
  - "NSSegmentedControl"
  - "isMomentary"
  - "NSSegmentedControl.SwitchTracking.momentary"
  - "picker strip"
  - "option group"
related:
  - toggles
  - pickers
  - buttons
  - split-views
---
# Segmented Controls

> A segmented control is a linear set of two or more segments, each functioning as a button.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

All segments are usually equal width. Segments can contain text or images. Can represent:
- **Single-choice selection** (all platforms)
- **Multi-choice selection** (macOS only — e.g., Bold + Italic + Underline simultaneously)
- **Action buttons without selection state** (e.g., Reply / Reply All / Forward in macOS Mail)

## Best Practices

- **For closely related choices that affect an object, state, or view** — an inspector attribute selector or a toolbar action set.
- **When visible grouping and selection state matter** — segmented controls preserve grouping at all sizes and make current selection legible at a glance.
- **Keep control types consistent** — don't mix action segments with selection-state segments within the same control.
- **Max segments: ~5–7 in wide interfaces; ~5 on iPhone** — more is hard to parse.
- **Consistent segment width and content size** — equal-width segments feel balanced; uneven content within a uniform width looks awkward.

## Content

- **Prefer either text or images** within a single control for consistency.
- **Similar content sizes** across all segments — avoid some segments appearing full and others sparse.
- **Nouns or noun phrases** for text labels. Title-style capitalization. No introductory text needed.

## Platform Considerations

### iOS, iPadOS

- Use to switch between **closely related subviews** (e.g., Calendar event vs. reminder). For switching between fully separate app sections, use a tab bar.

### macOS

- **Introductory text** to clarify purpose when using symbols/icons. Add per-segment labels beneath icons if needed. Provide tooltips for each segment.
- **Use a tab view (not a segmented control) for view switching in the main window area.** Segmented controls are appropriate in toolbars or inspector panes.
- **Spring loading:** support for dragging items onto a segment + force-clicking to activate the segment without dropping the item (Magic Trackpad).

### tvOS

- **Consider a split view instead of a segmented control** for content filtering — easier to navigate between content and filter options.
- **Keep focusable elements away from segmented controls** — focus alone selects a segment (no explicit click). Adjacent elements that are too close cause accidental segment switches.

### visionOS

- System displays a tooltip with your descriptive text when people look at an icon-only segment.
