---
topic: sliders
tier: 3
platforms: [ios, ipados, macos, visionos]
category: components/controls
triggers:
  - "slider"
  - "UISlider"
  - "continuous value"
  - "range control"
  - "scrubber"
related:
  - steppers
  - gauges
  - digital-crown
---
# Sliders

> A slider is a horizontal track with a thumb that people drag between a minimum and maximum value.

**Platforms:** iOS, iPadOS, macOS, visionOS, watchOS *(not tvOS)*

Filled track between minimum and thumb shows current value. Optional left/right icons illustrate min/max meaning.

## Best Practices

- **Customize appearance when it adds value** — track color, thumb image/tint, left/right icons. Example: image-size slider with small→large image icons.
- **Consistent direction** — min on leading, max on trailing (horizontal); min at bottom, max at top (vertical). Always 0% (min) on the leading side.
- **Consider pairing with a text field and stepper** for wide value ranges — lets people both drag and type an exact value.

## Platform Considerations

### iOS, iPadOS

- **Don't use a slider for audio volume** — use `MPVolumeView` (volume view), which includes an output-device selector.

### macOS

Two types: **linear** (lozenge-shaped thumb, colored fill, optional tick marks) and **circular** (circular thumb, tick marks as evenly spaced dots).

- **Live feedback** — show results in real time as the value changes (e.g., Dock icon scaling).
- **Linear slider** for fixed start-to-end ranges (0–100% opacity). **Circular slider** for values that repeat or continue indefinitely (0–360° rotation, number of animation spins).
- **Label to introduce a slider** — sentence-style capitalization, ends with a colon.
- **Tick marks** — increase scale clarity and help locate specific values. Label min and max at minimum; add intermediate labels for nonlinear scales. Consider a tooltip showing the thumb value on hover.

### visionOS

- **Prefer horizontal sliders** — side-to-side gestures are easier than up-down.

### watchOS

A slider appears as discrete steps or a continuous bar. People tap +/− buttons on the sides to increment/decrement by a predefined amount.
- **Custom glyphs** if the default +/− don't communicate the slider's purpose.
