---
topic: sliders
tier: 3
platforms: [ios, ipados, macos, visionos, watchos]
category: components/controls
triggers:
  - "slider"
  - "UISlider"
  - "NSSlider"
  - "continuous value"
  - "range control"
related:
  - pickers
  - steppers
---

# Sliders

A slider is a horizontal track with a thumb people adjust between a minimum and maximum; the track fills with color up to the thumb. Optional left and right icons can illustrate the extremes.

## Best practices

- **Customize appearance if it adds value**: track color, thumb image and tint, end icons.
- **Use familiar directions**: minimum leading, maximum trailing (horizontal); minimum bottom, maximum top (vertical).
- **Consider adding a text field and stepper**, especially for wide ranges: the field shows and accepts exact values; the stepper increments whole values.

## Platform considerations

Not supported in tvOS.

### iOS, iPadOS

**Don't use a slider to adjust audio volume.** Use a customizable volume view instead (it includes a volume slider and output-device control).

### macOS

Linear thumbs are narrow lozenges, and linear sliders often include min/max icons; circular thumbs are small circles, with any tick marks as evenly spaced dots around the circumference.

- **Consider live feedback as the value changes.**
- **Match style to expectations**: horizontal between fixed endpoints; circular when values repeat or continue indefinitely (rotation 0-360 degrees; four spins = 1440 degrees).
- **Consider introducing a slider with a label**, generally sentence-case, ending with a colon.
- **Use tick marks to increase clarity and accuracy.**
- **Consider labeling tick marks** with numbers or words. Labeling every mark is unnecessary unless it reduces confusion; often min and max suffice. For nonlinear values, periodic labels provide context. A thumb-value tooltip on pointer hover is also a good idea.

### visionOS

**Prefer horizontal sliders**; side-to-side gestures are generally easier.

### watchOS

Discrete steps or a continuous bar over a finite range. People can tap the buttons at either end of the slider to change the value by a predefined amount. **If necessary, create custom glyphs** for the slider's purpose; the default is plus and minus signs.

## Resources

Developer: `Slider` (SwiftUI), `UISlider`, `NSSlider`.

Source: [Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders), captured 2026-09-12.
