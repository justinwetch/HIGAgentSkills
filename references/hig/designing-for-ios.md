---
topic: designing-for-ios
tier: 2
platforms: [ios]
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

iPhone supports quick checks and long sessions for communication, media, games, tasks, and personal data, often on the go while switching among apps.

## Device characteristics

- **Display:** medium-size, high-resolution.
- **Ergonomics:** generally held in one or both hands; portrait or landscape; viewing distance tends to be no more than a foot or two.
- **Inputs:** Multi-Touch gestures, virtual keyboard, and voice; people may also want apps to use personal data, gyroscope/accelerometer input, and spatial interactions.
- **System features:** widgets, Home Screen quick actions, Spotlight, Shortcuts, and activity views.

## Best practices

- Limit onscreen controls to keep primary content and tasks prominent; make secondary details and actions discoverable with minimal interaction.
- Adapt to orientation, Dark Mode, and Dynamic Type.
- Middle or lower controls tend to be easier to reach; support swipe-back and list-row swipe actions.
- With permission, use capabilities such as payments, biometric authentication, and location rather than asking people to enter data manually.

Source: [Apple HIG — Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios), captured 2026-09-12.
