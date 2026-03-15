---
topic: combo-boxes
tier: 4
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/controls
triggers:
  - "combo box"
  - "NSComboBox"
  - "editable dropdown"
related:
  - pop-up-buttons
  - text-fields
---
# Combo Boxes

> A combo box combines a text field with a pull-down button, letting people enter a custom value or choose from a list of predefined values.

**Platforms:** macOS only

Custom values are not added to the predefined list. See also text-fields and pull-down-buttons.

## Best Practices

- **Meaningful default value from the list** — even if not the first item; empty default misses the opportunity to convey what the list contains.
- **Introductory label** — title-style capitalization, ends with a colon. Tells people what type of items to expect.
- **Provide relevant predefined choices** — the list should cover the most common values; people should rarely need to type.
- **List items no wider than the text field** — truncation in the dropdown is hard to read.
