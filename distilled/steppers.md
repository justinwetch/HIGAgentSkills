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

> A stepper is a two-segment control (− and +) for incrementally increasing or decreasing a value.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS or watchOS)*

Steppers don't display the current value — they sit next to a field that shows it.

## Best Practices

- **Make the affected value obvious** — the stepper gives no self-labeling; adjacent text makes the connection clear.
- **Pair with a text field for wide value ranges** — steppers are efficient for small, predictable increments. For broadly varying values (e.g., number of print copies), provide both a stepper and a text field.

## Platform Considerations

### macOS

- **Consider Shift-click for large jumps** — Shift-click can increase/decrease value by a larger increment (e.g., 10× the default), useful when the value range is large.
