---
topic: action-button
tier: 3
platforms: [ios, macos, tvos]
category: components/controls
triggers:
  - "Action button"
  - "hardware button"
  - "quick action button"
  - "iPhone Action Button"
related:
  - app-shortcuts
  - gestures
---
# Action Button

> The Action button gives people hardware-shortcut access to their favorite app function. Pressing it runs an App Shortcut, avoiding the need to open the app.

**Platforms:** iOS, watchOS *(not iPadOS, macOS, tvOS, visionOS)*

People choose an action in Settings; your app surfaces options. The system already provides "open app" — don't add that as an option.

## Best Practices

- **Support the Action button with essential app functions** — quick, repeatable actions that people use regularly (not onboarding or navigation tasks).
- **Short labels** — shown in Settings when people configure the button. Rules:
  - Start with a verb, present tense.
  - No articles or prepositions.
  - Max **3 words**.
  - ✅ "Start Race" | ❌ "Started Race", "Start the Race"
- **Don't explain how to configure the Action button** — the system already guides people through Settings.

## iOS

- **Don't open the app if you can avoid it.** Use Live Activities, custom snippets, or other lightweight multitasking. (e.g., "Set Timer" → prompts for duration → launches a Live Activity countdown; never opens the Clock app.)

## watchOS

The Action button supports:
- **First press**: drop a waypoint, start a dive, or begin a specific workout.
- **Secondary actions**: mark a segment, transition to the next modality in a multi-part workout.

**Secondary action design rules:**
- Flows logically from the first press — people often act without looking at the screen.
- Keep it simple and memorable; **avoid more than one secondary action** (increases cognitive load).
- **Prefer advancing a function** over stopping it — offer stop/end within the app UI, not via the button.
- **Action button + side button together = pause** current activity — always honor this, except diving (pausing dive = dangerous; loss of depth/time tracking). Don't implement pause via button combo if pausing would cause a harmful outcome.
