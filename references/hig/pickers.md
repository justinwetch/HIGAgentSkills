---
topic: pickers
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/controls
triggers:
  - "picker"
  - "DatePicker"
  - "date picker"
  - "UIDatePicker"
  - "UIPickerView"
  - "NSDatePicker"
  - "wheel picker"
  - "navigationLink"
related:
  - pop-up-buttons
  - pull-down-buttons
  - lists-and-tables
---

# Pickers

A picker displays one or more scrollable lists of distinct values for choosing single or multipart values. System styles differ in selectable values and appearance; values and order depend on device language. Date pickers also support calendar-day selection and date/time entry with a numeric keypad.

## Best practices

- Consider a picker for medium-to-long lists. For a fairly short list, consider a [pull-down button](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), because picker visual weight may be excessive. For a very large set, consider a [list or table](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables); lists and tables adjust in height, and tables can include an index for faster section targeting.
- Use predictable, logically ordered values. Many values are hidden before interaction; an alphabetized country list, for example, lets people predict and move through items quickly.
- Avoid switching views to show a picker. Keep it in context, below or near the field being edited; it typically appears at the bottom of a window or in a popover.
- Consider less minute granularity in a date picker. The default list has 60 values (0–59); an optional interval must divide evenly into 60, such as 15-minute values (0, 15, 30, 45).

## Platform considerations

No additional considerations for visionOS.

### iOS and iPadOS

A date picker selects a date, time, or both through touch, keyboard, or pointing device.

| Style | Behavior |
| --- | --- |
| Compact | Use when space is constrained. A button shows the current value in the app’s accent color; tapping opens a modal calendar/time editor for multiple edits, confirmed by tapping outside. In a compact layout, it opens as a popover over the content. |
| Inline | For time only, a button displaying value wheels; for dates and times, an inline calendar. |
| Wheels | Scrolling wheels supporting data entry through built-in or external keyboards. |
| Automatic | System-determined from the current platform and date-picker mode. |

| Mode | Values and limits |
| --- | --- |
| Date | Months, days of the month, and years. |
| Time | Hours, minutes, and optionally AM/PM. |
| Date and time | Dates, hours, minutes, and optionally AM/PM. |
| Countdown timer | Hours and minutes, up to 23 hours 59 minutes; unavailable in Inline and Compact styles. |

Date-picker values and order depend on device location.

### macOS

Choose between textual and graphical date pickers. Textual suits limited space and specific date/time selections. Graphical suits browsing calendar days, selecting a date range, or using a clock-face appearance.

### tvOS

Pickers are available with SwiftUI.

### watchOS

Pickers display lists navigated with the Digital Crown. The wheels style supports item lists and date/time pickers. A picker can have an outline, caption, and scrolling indicator.

For longer lists, `navigationLink` displays the picker as a button. Tapping shows the options list, while people can scrub through options with the Digital Crown without tapping. The button displays the selected item.

## Resources

Related: [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)

Developer documentation: [`Picker`](https://developer.apple.com/documentation/swiftui/picker) (SwiftUI; selects mutually exclusive values), [`DatePicker`](https://developer.apple.com/documentation/swiftui/datepicker) (SwiftUI; selects an absolute date), and [`PickerStyle/navigationLink`](https://developer.apple.com/documentation/swiftui/pickerstyle/navigationlink) (SwiftUI; pushes a List-style picker view); [`UIDatePicker`](https://developer.apple.com/documentation/uikit/uidatepicker) and [`UIPickerView`](https://developer.apple.com/documentation/uikit/uipickerview) (UIKit); [`NSDatePicker`](https://developer.apple.com/documentation/appkit/nsdatepicker) (AppKit).

Source: [Apple Human Interface Guidelines — Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) (captured 2026-09-12).
