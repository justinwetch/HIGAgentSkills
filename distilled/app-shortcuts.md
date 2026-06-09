---
topic: app-shortcuts
tier: 3
platforms: [ios, ipados, visionos, watchos]
category: technologies
triggers:
  - "App Shortcut"
  - "SiriKit"
  - "shortcut"
  - "AppIntents"
  - "action shortcut"
  - "Spotlight"
  - "App schema domains"
related:
  - siri
  - action-button
  - snippets
  - live-activities
---
# App Shortcuts

> App Shortcuts expose key app functions throughout the system — via Siri, Spotlight, the Shortcuts app, the Action button, and Apple Pencil squeeze.

**Platforms:** iOS, iPadOS, visionOS, watchOS *(not tvOS; macOS supports App Intents for custom Shortcuts only)*

Available immediately after app install — no first launch required. Up to **10 App Shortcuts** per app.

## Best Practices

- Use **App schema domains** for common domains so Apple Intelligence and Siri can surface actions and content contextually. Use App Shortcuts for unique app features or custom content not covered by schemas. See `Apple Intelligence and Siri AI` and `Making actions and content discoverable by Apple Intelligence`.
- **Only your app's most common and important tasks** — quick-completion tasks that don't need the full app UI. Opening the app is OK for complex multi-step tasks.
- **Single optional parameter for flexibility** — e.g., "Start [morning/daily/sleep] meditation." Use predictable, familiar values people won't need to look up.
- **Ask for clarification when optional info is missing** — suggest most recent or time-appropriate option; present a short list of alternatives.
- **Keep voice phrases short and memorable** — if it feels complicated to say aloud, simplify. Required parameters only; defer additional info to follow-up steps.
- **Make shortcuts discoverable** — show in-app tips when people do common actions to let them know a shortcut exists.

## Response Formats

When a shortcut runs, your app can respond via:
- **Snippets** — custom views for static info or dialog options (e.g., weather at location, order confirmation).
- **Live Activities** — ongoing timers/countdowns that update for a period of time.
- **Audio-only devices** — include all critical info in the full dialogue text (for AirPods, HomePod where people can't see the screen).

## Editorial Guidelines

- **Activation phrases**: brief, memorable, natural variants. Include your app name. Be creative — e.g., Keynote accepts "Create a Keynote" and "Add a new presentation in Keynote."
- **Capitalization**: *App Shortcuts* and *Shortcuts* (app name) are always title case and plural.
- **Individual shortcuts** (not App Shortcuts or the Shortcuts app): lowercase — e.g., "Run a shortcut by asking Siri."

## Platform Considerations

### iOS, iPadOS

- App Shortcuts appear in Spotlight (Top Hit area or Shortcuts section under your app).
- Each shortcut requires an **SF Symbols** icon (or a preview image for link-type shortcuts).
- **Order shortcuts by importance** — first determines initial display order in Spotlight and Shortcuts app. System re-prioritizes based on usage.

### macOS

App Shortcuts not supported. However, App Intents are — people can build custom Shortcuts from your app's actions in the Shortcuts app on Mac.
