---
topic: steppers
tier: 4
platforms: [ios, ipados, macos, visionos]
category: components/controls
triggers:
  - "stepper"
  - "NSStepper"
  - "UIStepper"
  - "increment decrement control"
related:
  - text-fields
  - pickers
---

# Steppers

A stepper is a two-segment control for increasing or decreasing an incremental value. It doesn’t display the value, so place it next to a field that displays the current value and make the affected value obvious.

## Best practices

Steppers suit small changes requiring a few taps or clicks. Consider pairing one with a text field when large changes are likely or values vary widely, so people can enter a specific value; a printing screen, for example, can use both to set the number of copies.

## Platform considerations

No additional considerations for iOS, iPadOS, or visionOS. Steppers aren’t supported in watchOS or tvOS.

### macOS

For a large value range, consider Shift-click to change the value by more than the default increment (10 times the default is an example).

## Resources

Related: [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers), [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields)

Developer documentation: [`UIStepper`](https://developer.apple.com/documentation/uikit/uistepper) (UIKit; increments or decrements a value); [`NSStepper`](https://developer.apple.com/documentation/appkit/nsstepper) (AppKit; up/down arrow buttons increment or decrement a value).

Source: [Apple Human Interface Guidelines — Steppers](https://developer.apple.com/design/human-interface-guidelines/steppers) (captured 2026-09-12).
