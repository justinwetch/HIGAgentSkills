---
topic: designing-for-watchos
tier: 2
platforms: [watchos]
category: platforms
triggers:
  - "watchOS"
  - "Apple Watch"
  - "wrist"
  - "complication"
  - "watch face"
related:
  - digital-crown
  - complications
  - watch-faces
  - always-on
  - action-button
  - app-shortcuts
  - siri
  - notifications
  - color
  - materials
---

# Designing for watchOS

Apple Watch offers essential information and simple, timely tasks at a glance on a small, high-resolution display.

- **Ergonomics:** usually viewed within a foot, wrist raised, operated with the other hand; Always On shows the watch face wrist-down.
- **Inputs:** the Digital Crown inspects data and behaves consistently on the watch face, Home Screen and in apps. Standard gestures like tap, swipe and drag work even in motion. The Action button starts an essential action without looking; shortcuts speed routine tasks. Device data comes from sensors such as GPS, blood oxygen, heart, altimeter, accelerometer and gyroscope.

## Best practices

- Support quick, glanceable, single-screen interactions (many glances a day, each can last under a minute): succinct critical information, targeted actions in a gesture or two.
- Minimize navigation depth; use the Digital Crown for vertical scrolling or switching screens.
- Personalize by proactively anticipating needs; use on-device data for actionable content relevant now or very soon.
- Related experiences like complications, notifications and Siri frequently get more use than the app.
- Use complications for relevant, potentially dynamic data and graphics seen on every wrist raise and tappable into your app.
- Use notifications for timely, high-value information and important actions without opening your app.
- Use background content such as color for supporting information; use materials to illustrate hierarchy and sense of place.
- Design your app to function independently, adding detail and functionality beyond notifications and complications.

Source: [Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos), captured 2026-09-12.
