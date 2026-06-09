---
topic: gyro-and-accelerometer
tier: 4
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "gyroscope"
  - "accelerometer"
  - "motion sensor"
  - "CMMotionManager"
  - "Core Motion"
  - "Getting processed device-motion data"
  - "device tilt"
related:
  - gestures
---
# Gyroscope and Accelerometer

> On-device gyroscopes and accelerometers provide motion data for real-time, motion-based experiences.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

- iOS, iPadOS, macOS, tvOS, visionOS, watchOS: use Core Motion when motion data provides tangible user benefit.
- tvOS: motion data can come from the Siri Remote.

## Best Practices

- **Only use motion data for tangible user benefit** — e.g., fitness activity tracking, enhanced gameplay. Don't collect data speculatively.
- **Permissions required** — must provide copy explaining why you need motion data. The system includes this copy in a permission request the first time you access it.
- **Outside gameplay, don't use motion for direct interface manipulation** — motion-based gestures are imprecise, may be physically challenging, and increase battery usage. Reserve for active gameplay.
