---
topic: pickers
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/controls
triggers:
  - "picker"
  - "date picker"
  - "UIDatePicker"
  - "UIPickerView"
  - "wheel picker"
related:
  - segmented-controls
  - pop-up-buttons
---
# Pickers

> A picker displays one or more scrollable lists of distinct values for people to choose from.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Value display order depends on device language/locale (dates) or device location (date pickers).

## Best Practices

- **Medium-to-long lists** — for short lists, use a pull-down button; for very large sets, use a list or table (supports an index for fast section navigation).
- **Predictable, logically ordered values** — e.g., alphabetized country list. People often can't see hidden values and must predict what's there.
- **In-context display** — show the picker below or near the field being edited, not in a separate view. Typically appears at the bottom of a window or in a popover.
- **Date pickers: consider coarser minute intervals** — default is 60 values (0–59). You can increase the interval as long as it divides evenly into 60 (e.g., 15 for quarter-hour intervals).

## Date Picker Styles and Modes (iOS, iPadOS)

**Styles:**
| Style | Appearance |
|---|---|
| Compact | Button showing current value in accent color; tapping opens a modal calendar/time editor |
| Inline | Time only: scrolling wheels. Dates: inline calendar view |
| Wheels | Scrolling wheels; supports keyboard and external keyboard data entry |
| Automatic | System-determined style based on platform and mode |

**Modes:**
| Mode | Contents |
|---|---|
| Date | Months, days of month, years |
| Time | Hours, minutes; optional AM/PM |
| Date and time | Dates, hours, minutes; optional AM/PM |
| Countdown timer | Hours and minutes (max 23h 59m); not available in Inline or Compact styles |

**Use Compact** when space is constrained — shows the current value as a button; tapping reveals full editing in a modal.

## Platform Considerations

### macOS

Two styles: **Textual** (space-efficient, precise selection) and **Graphical** (calendar browse or date-range selection, or clock-face appearance).

### tvOS

Available via SwiftUI.

### watchOS

- **Wheels style** for lists. Navigate with Digital Crown for precise, engaging selection.
- Configure with outline, caption, and scrolling indicator.
- **Navigation link** for longer lists — shows picker as a button; tapping reveals options. People can also scrub with Digital Crown without tapping.
