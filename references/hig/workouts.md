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

A workout experience uses device activity data and familiar components to display fitness metrics.

## Best practices

- **In a watchOS fitness app, use workout sessions for useful data and relevant controls.** During an active session, watchOS keeps the app onscreen between wrist raises; show key data like elapsed or remaining time, calories or distance, and controls like lap or interval markers.
- **Avoid irrelevant information during a workout**, like your workout list or other app areas. Many watchOS workout apps, including Workout, place large session controls (such as End, Resume, New) leftmost, glanceable metrics in the middle and media playback (if supported) rightmost.
- **Use a distinct appearance so people recognize an active workout at a glance.** Real-time metric values can signal it; you can add a unique metrics-screen layout.
- **Make workout controls easy to find and tap** (pause, resume, stop), and give clear feedback when a session starts or stops.
- **When sensor data is unavailable, help people understand what your app can still record.** For *Swimming* or *Other* types, use language similar to Workout's, e.g., for a Pool Swim, "GPS is not used ... water may prevent a heart-rate measurement, but Apple Watch will still track your calories, laps, and distance using the built-in accelerometer," or "you earn the calorie equivalent of a brisk walk anytime sensor readings are unavailable."
- **Provide an end-of-session summary** confirming completion with recorded data. Consider including Activity rings for current progress.
- **Discard extremely brief sessions.** If one ends within seconds of starting, either discard the data automatically or ask whether to record it as a workout.
- **Make sure text is legible in motion.** When a session requires movement, use large fonts and high-contrast colors, and arrange text so the most important information is easy to read.
- **Use Activity rings only for their documented purpose**; they're an Apple-designed element whose colors and meanings match the Activity app.

## Platform considerations

No additional considerations for iOS, iPadOS or watchOS. Not supported in macOS, tvOS or visionOS.

## Resources

Developer: `WorkoutKit`, HealthKit.

Source: [Workouts](https://developer.apple.com/design/human-interface-guidelines/workouts), captured 2026-09-12.
