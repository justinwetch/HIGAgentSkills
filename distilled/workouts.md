---
topic: workouts
tier: 3
platforms: [ios, ipados, watchos]
category: technologies
triggers:
  - "workout"
  - "fitness"
  - "session"
  - "exercise"
  - "heart rate"
  - "HKWorkout"
  - "WorkoutKit"
related:
  - activity-rings
  - healthkit
  - digital-crown
---
# Workouts

> Workout experiences encourage engagement with current activity and progress tracking, optimized for Apple Watch during motion and for live/recorded sessions on larger screens.

**Platforms:** iOS, iPadOS, watchOS *(not macOS, tvOS, or visionOS)*

**Typical usage by device:**
- **Apple Watch** - wearable during workouts; primary live metrics display.
- **iPhone/iPad** - carried during walking, running, or wheelchair workouts; also used for live/recorded workout sessions.

## Best Practices

- **watchOS active sessions** - display the data people care most about: elapsed/remaining time, calories, distance. Offer relevant controls like lap marker or interval.
- **Don't distract during a workout** - hide navigation, app menus, and off-topic content while a session is active.
- **Visually distinguish active workouts** - real-time metrics and a unique layout reinforce that a session is active.
- **Easy-to-tap workout controls** - clear feedback for start, pause, resume, and stop.
- **Handle unavailable sensor data** - explain limits clearly, especially for water or sensor conditions.
- **Provide a summary screen** after the session; confirm end, show recorded data, and consider Activity rings.
- **Discard very short sessions** - auto-discard or ask if a session ends seconds after starting.
- **Large, legible text during motion** - high contrast, large fonts, and the most important data easy to read while moving.
- **Use Activity rings correctly** - see [activity-rings.md](activity-rings.md).
