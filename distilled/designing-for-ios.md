---
topic: designing-for-ios
tier: 2
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: platforms
triggers:
  - "iOS"
  - "iPhone"
  - "SwiftUI iOS"
  - "UIKit"
related:
  - layout
  - gestures
  - multitasking
---
# Designing for iOS

> iPhone helps people stay connected, play games, view media, accomplish tasks, and track personal data — anywhere, on the go.

**Platform:** iOS

## Device Characteristics

| | |
|---|---|
| **Display** | Medium-size, high-resolution |
| **Ergonomics** | One or both hands; portrait or landscape; viewing distance ≤1–2 ft |
| **Inputs** | Multi-Touch gestures, virtual keyboard, Siri; gyro/accelerometer; spatial interactions |
| **Usage pattern** | Ranges from quick 1–2 min checks to 1+ hr sessions; multiple apps open simultaneously, frequent switching |

**Key system integrations:** widgets, home screen quick actions, Spotlight search, Siri shortcuts/suggestions, activity views.

## Best Practices

- Limit onscreen controls — let secondary details and actions be discoverable with minimal interaction.
- Adapt seamlessly to orientation changes, Dark Mode, and Dynamic Type.
- Place controls where they're reachable with typical one-hand grip — middle and bottom of display preferred. Support swipe-to-go-back and swipe actions in list rows.
- With permission, use platform capabilities (payments, biometric authentication, location) instead of asking people to enter data manually.
