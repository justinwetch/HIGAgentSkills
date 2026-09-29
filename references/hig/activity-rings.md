---
topic: activity-rings
tier: 3
platforms: [ios, ipados, watchos]
category: components/watchos
triggers:
  - "activity ring"
  - "Move ring"
  - "Exercise ring"
  - "Stand ring"
  - "HKActivityRingView"
related:
  - healthkit
  - workouts
---

# Activity rings

Activity rings show daily progress toward Move, Exercise, and Stand goals. In watchOS the element always has three rings, with the Activity app's colors and meanings.

## Best practices

- **Display Activity rings where relevant to your app's purpose.** People generally expect them in health or fitness apps, especially HealthKit contributors. For sessions built around completing the rings, consider a workout metrics screen; you could also use an end-of-workout summary.
- **Use them only for Move, Exercise, and Stand.** Don't replicate or modify them for other purposes; never show other data in them, or this progress in another ring-like element.
- **Show a single person's progress.** Never represent more than one person; make it obvious whose progress it is with a label, photo, or avatar.
- **Always keep their appearance the same, wherever displayed.** Never change ring colors (such as with filters or opacity). Always use a black background. Prefer enclosing rings and background in a circle via the enclosing view's corner radius, not a circular mask. Ensure black stays visible around the outermost ring; if necessary, add a thin black stroke at its outer edge, avoiding gradients, shadows, or other visual effects. Always scale the rings so they don't seem disconnected or out of place. When necessary, adapt the surrounding interface to the rings; never the reverse.
- **Color the labels *Move*, *Exercise*, and *Stand*, and each ring's current and goal values, to match their ring:**

|Move (RGB)|Exercise (RGB)|Stand (RGB)|
|---|---|---|
|250, 17, 79|166, 255, 0|0, 255, 246|

- **Maintain margins.** The outer margin must be no less than the distance between rings. Never let other elements crop, obstruct, or encroach on it or the rings.
- **Differentiate other ring-like elements.** If you must include them, separate them from Activity rings with padding, lines, or labels; color and scale can also help.
- **Don't send notifications repeating the Activity app's** Move, Exercise, and Stand updates, and don't show the element in notifications. Referencing Activity progress in a way unique to your app is fine.
- **Don't use them for decoration or branding.** Never display them in labels, background graphics, your app icon, or marketing materials.

## Platform considerations

No additional considerations for iPadOS or watchOS. Not supported in macOS, tvOS, or visionOS.

### iOS

`HKActivityRingView` automatically shows all three rings when an Apple Watch is paired, otherwise only the Move ring, approximating activity from steps and other apps' workout information. Activity history can mix both styles.

## Resources

Source: [Activity rings](https://developer.apple.com/design/human-interface-guidelines/activity-rings), captured 2026-09-12.
