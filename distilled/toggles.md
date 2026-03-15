---
topic: toggles
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/controls
triggers:
  - "toggle"
  - "switch"
  - "UISwitch"
  - "on/off control"
  - "boolean control"
related:
  - buttons
  - segmented-controls
---
# Toggles

> A toggle lets people choose between two opposing states (on/off) with distinct appearances for each state.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

All platforms also support buttons that behave like toggles (distinct appearance per state).

## Best Practices

- **For two opposing values that affect content or view state** — not for choosing from a list (use pop-up button for that).
- **Clearly identify what's being toggled** — surrounding context usually suffices. macOS apps may supply an explicit label.
- **Make state visually obvious** — add/remove color fill, show/hide background shape, show/hide checkmark or dot. Don't rely solely on color to communicate state.

## Platform Considerations

### iOS, iPadOS

- **Switch style: only in list rows** — the row content provides context; no label needed.
- **Default switch color: green** — change only if necessary, using a color with sufficient contrast against the uncolored state. App accent color is acceptable.
- **Outside of lists: use a toggle button, not a switch** — e.g., Phone app's Recent Calls filter button uses a blue highlight to show active state.
- **Toggle buttons: no explanatory label** — the icon + alternative background appearances communicate the purpose.

### macOS

macOS supports switches, checkboxes, and radio buttons. All three belong in the **window body**, not the toolbar or status bar.

**Switches:**
- Prefer for settings you want to emphasize — more visual weight than checkboxes, appropriate for controlling a group of settings rather than just one.
- **Mini switch** in grouped forms — similar height to buttons/other controls for consistent row heights. Use regular switch for primary setting, mini switches for subordinate settings.
- **Don't replace existing checkboxes with switches** — maintain consistency.

**Checkboxes:**
- A small square button: empty (off), checkmark (on), dash (mixed/indeterminate).
- Usually includes a trailing title. Can appear without title in editable checklists.
- **Use checkboxes (not switches) for hierarchical settings** — alignment and indentation express dependencies (child checkboxes governed by a parent).
- **Checkboxes for multi-select; radio buttons for mutually exclusive choices** greater than two.
- **Introduce a group of checkboxes with a label** when their relationship isn't obvious — align label baseline with the first checkbox.
- **Accurately reflect mixed state** — if a parent checkbox controls multiple child checkboxes with different states, show the dash (mixed) state.

**Radio buttons:**
- Small circular button + label. Typically 2–5 in a group. Mutually exclusive choices.
- States: selected (filled circle), deselected (empty circle). Mixed state (dash) exists but is rarely useful.
- **Use checkboxes for multi-select; radio buttons for mutually exclusive choices.**
- **Avoid long radio button lists** — more than ~5 options → consider a pop-up button.
- **Single on/off preference: prefer a checkbox.** Use a radio button pair only when the checkbox doesn't clearly communicate the two opposing states.
- **Consistent horizontal spacing** — measure the longest label and apply that spacing consistently across all buttons.
