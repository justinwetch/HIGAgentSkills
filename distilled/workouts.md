---
topic: workouts
tier: 3
platforms: [ios, ipados, tvos]
category: technologies
triggers:
  - "workout"
  - "fitness"
  - "session"
  - "exercise"
  - "heart rate"
  - "HKWorkout"
related:
  - activity-rings
  - healthkit
  - digital-crown
---
# Workouts

> Workout experiences encourage engagement with current activity and progress tracking, optimized for the display constraints of Apple Watch during motion.

**Platforms:** iOS, iPadOS, watchOS *(not macOS, tvOS, visionOS)*

**Typical usage by device:**
- **Apple Watch**: wearable during workouts — primary metrics display.
- **iPhone/iPad**: carried during walking, running, wheelchair. Also for consuming live/recorded workout sessions.

## Best Practices

- **watchOS active sessions**: display the data people care most about — elapsed/remaining time, calories, distance. Offer relevant controls (lap marker, interval).
- **Don't distract during a workout** — hide navigation, app menus, and off-topic content while a session is active.
- **Visually distinguish active workouts** — real-time updating metrics make a session feel active. Use a unique layout to further reinforce this.
- **Easy-to-tap workout controls** — clear feedback for session start, pause, resume, and stop.
- **Handle unavailable sensor data** — inform users when water/conditions prevent certain measurements (e.g., heart rate during swim) using language similar to the Workout app:
  - *"GPS is not used during a Pool Swim, and water may prevent a heart-rate measurement, but Apple Watch will still track your calories, laps, and distance using the built-in accelerometer."*
  - *"In this type of workout, you earn the calorie equivalent of a brisk walk anytime sensor readings are unavailable."*
- **Provide a summary screen** after the session — confirm end, show recorded data, consider including Activity rings.
- **Discard very short sessions** — if a session ends a few seconds after starting, auto-discard or ask the user.
- **Large, legible text during motion** — high-contrast colors, large font sizes, most important data easy to read while moving.
- **Use Activity rings correctly** — see [activity-rings.md](activity-rings.md) for all rules.
