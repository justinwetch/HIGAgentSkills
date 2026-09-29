---
topic: combo-boxes
tier: 4
platforms: [macos]
category: components/controls
triggers:
  - "combo box"
  - "NSComboBox"
  - "editable dropdown"
related:
  - pull-down-buttons
  - text-fields
---
# Combo boxes

A combo box combines a text field and pull-down button: people can type a custom value or choose a predefined value; custom values aren’t added to the choices.

- Populate the field with a meaningful list default. It may be empty, but a value referring to a hidden choice is best and needn’t be first.
- Use an introductory label for expected item types; generally use title-style capitalization and a final colon. See [Labels](https://developer.apple.com/design/human-interface-guidelines/labels).
- Provide relevant choices: retain custom entry and list likely values for convenience.
- Keep items no wider than the text field; wider items may truncate and become hard to read.

Related: [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) and [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons). Supported in macOS; not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.

Developer documentation: [`NSComboBox`](https://developer.apple.com/documentation/appkit/nscombobox), an AppKit view displaying a pop-up list for selecting or typing a custom value.

Source: [Apple HIG — Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes), captured 2026-09-12.
