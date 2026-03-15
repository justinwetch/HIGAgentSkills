---
topic: designing-for-watchos
tier: 2
platforms: [ios, ipados, macos, tvos, visionos, watchos]
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
---
# Designing for watchOS

> Apple Watch delivers essential information and simple, timely task execution — glanceable, at a wrist raise.

**Platform:** watchOS

## Device Characteristics

| | |
|---|---|
| **Display** | Small, high-resolution, wrist-worn; Always On display shows watch face on wrist drop |
| **Ergonomics** | Worn on wrist; opposite hand interacts; viewing distance ≤1 ft on wrist raise |
| **Inputs** | Digital Crown (vertical scroll/data inspection), tap/swipe/drag gestures, Action button (essential action without looking), Siri shortcuts; GPS, blood oxygen, heart sensors, altimeter, accelerometer, gyroscope |
| **Usage pattern** | Many brief glances throughout the day; interactions often <1 min; complications, notifications, and Siri interactions used more than the app itself |

**Key system integrations:** Complications, notifications, Always On display, watch faces.

## Best Practices

- Design for **quick, glanceable, single-screen interactions** — deliver critical info succinctly and support actions with 1–2 gestures.
- Minimize navigation hierarchy depth. Use the Digital Crown for vertical navigation (scrolling, switching screens).
- Personalize proactively — use on-device data to surface relevant, actionable content in the moment.
- Use **complications** for relevant, potentially dynamic data directly on the watch face — tappable to deep-link into the app.
- Use **notifications** for timely, high-value information with actions people can take without opening the app.
- Use background color and materials to convey supporting info and establish hierarchy/sense of place.
- Design the app to function **independently**, extending (not duplicating) functionality from complications and notifications.
