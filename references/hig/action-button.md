---
topic: action-button
tier: 3
platforms: [ios, watchos]
category: components/controls
triggers:
  - "Action button"
  - "hardware button"
  - "quick action button"
  - "iPhone Action Button"
  - "Apple Watch Ultra"
related:
  - app-shortcuts
  - workouts
  - digital-crown
  - live-activities
---

# Action button

Hardware button on supported iPhone and Apple Watch models that runs App Shortcuts (as Siri or Spotlight would) or system functions like the flashlight; on Apple Watch Ultra, also activity actions including workouts and dives. Assigned at setup or in Settings.

## Best practices

- **Support your app's essential functions.** You needn't offer an app-opening shortcut; the system provides one.
- **Label each action briefly**: title-style capitalization, verb first, present tense, no articles or prepositions, as short as possible, 3 words max ("Start Race").
- **Prefer letting the system teach Action button use**, which it does automatically. Avoid repeating Settings guidance or other system usage tips.

## Platform considerations

Not supported in iPadOS, macOS, tvOS or visionOS.

### iOS

- **Let people act without leaving their current context.** When possible, use lightweight options like Live Activities and custom snippets instead of opening your app.

### watchOS

First press can drop a waypoint, start a dive or begin a workout; later presses can support secondary actions like marking a segment or advancing a multi-part workout.

- **Consider a secondary function that supports or advances the primary action.** A later press needs to follow logically from the first and suit the current context. For workouts or dives, consider a simple, easily learned one. Consider carefully before offering more than one.
- **Prefer later presses for added functionality, not stopping or concluding.** If people need to stop the main task (not pause), offer that in your interface.
- **Pause the current function on simultaneous Action and side button presses**, unless that causes a negative experience, as in dive apps, where pausing may be dangerous.

## Resources

Source: [Action button](https://developer.apple.com/design/human-interface-guidelines/action-button), captured 2026-09-12.
