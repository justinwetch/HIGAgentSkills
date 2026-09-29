---
topic: toggles
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/controls
triggers:
  - "toggle"
  - "switch"
  - "checkbox"
  - "radio button"
  - "UISwitch"
  - "NSSwitch"
  - "NSButton.ButtonType.toggle"
  - "ToggleStyle"
  - "allowsMixedState"
  - "on/off control"
  - "boolean control"
related:
  - buttons
  - segmented-controls
  - pop-up-buttons
  - layout
---

# Toggles

A toggle lets people choose between two opposing states, like on and off, with a distinct appearance for each. Styles (switch, checkbox) vary by platform. All platforms also support buttons that behave like toggles (`ToggleStyle`).

## Best practices

- **Use a toggle for two opposing values that affect the state of content or a view.** For other actions, like choosing from a list, use another component, such as a pop-up button.
- **Clearly identify what the toggle affects.** Context generally suffices; in some cases, often in macOS, you can add a state label. A toggle-like button generally uses a purpose-conveying icon and changes appearance, typically its background, with state.
- **Make state differences obvious**, for example by adding or removing a fill or background shape, or changing inner details like a checkmark or dot. Avoid relying solely on color.

## Platform considerations

No additional considerations for tvOS, visionOS, or watchOS.

### iOS, iPadOS

- **Use the switch style only in a list row**, where the row gives context and no label is needed.
- **Change a switch's default green only if necessary**, for example to your accent color; be sure it contrasts perceptibly with the uncolored appearance.
- **Outside a list, use a toggle-like button, not a switch.**
- **Avoid a label explaining the button's purpose**; the icon and alternate backgrounds convey it (`changesSelectionAsPrimaryAction`).

### macOS

**Use switches, checkboxes, and radio buttons in the window body, not the window frame**; in particular, avoid toolbars and status bars.

#### Switches

- **Prefer a switch for settings you want to emphasize**, like a group of settings rather than one (`switch`).
- **In a grouped form, consider a mini switch for a single-row setting**, matching other controls' height. For a hierarchy, you can use a regular switch for the primary setting and mini switches for subordinates (`GroupedFormStyle`, `ControlSize`).
- **In general, don't replace a checkbox with a switch.**

#### Checkboxes

A checkbox is a small square, typically titled on its trailing side; in an editable checklist, it can appear without a title.

- **Use checkboxes instead of switches for a hierarchy of settings**, showing dependencies with alignment (generally along the leading edge) and indentation.
- **Consider a label describing a checkbox group whose relationship isn't clear**, baseline-aligned with the first checkbox.
- **Accurately reflect state**: off (empty), on (checkmark), or mixed (dash). When a checkbox globally controls subordinates whose states differ, show mixed, as for a text style over bold and italic (`allowsMixedState`).

#### Radio buttons

A radio button is a small circle followed by a label; filled when selected, empty when deselected. A mixed state (dash) is possible but rarely useful; for mixed state, consider a checkbox instead.

- **Prefer radio buttons for mutually exclusive options** (consider them when there are more than two); for multiple choices, use checkboxes.
- **Avoid too many radio buttons in a set** (typically two to five); for more than about five options, consider a component like a pop-up button.
- **For a single on/off setting, prefer a checkbox.** In rare cases where one checkbox doesn't clearly convey the opposing states, you can use two radio buttons, each labeled with the state it controls.
- **Space horizontal radio buttons consistently**, sized to the longest label.

## Resources

Developer: `Toggle` (SwiftUI), `UISwitch`, `NSButton.ButtonType.toggle`, `NSSwitch`.

Source: [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), captured 2026-09-12.
