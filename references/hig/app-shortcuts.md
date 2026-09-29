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

An App Shortcut exposes key app functions or content systemwide via Siri, Spotlight, the Shortcuts app, the Action button (iPhone, Apple Watch) or Apple Pencil squeeze.

Each combines one or more App Intents actions; an app can include up to 10. They work right after installation, before first launch, and can later reflect people's choices. People can also build custom shortcuts from App Intents actions in the Shortcuts app.

## Best practices

- **For common functionality, consider adopting app schemas instead**; on supported devices, Apple Intelligence surfaces them contextually in Siri and other system experiences. App Shortcuts suit unique features or custom content schemas don't cover.
- **Offer App Shortcuts for your most common, important tasks.** Straightforward tasks that don't leave the current context work best; you can open your app to ease multistep tasks.
- **Let people choose from a set of options**: an App Shortcut can include one optional parameter if it makes sense. Include predictable, familiar values; people can't see the list.
- **Ask for missing optional information**, e.g. suggest the most recently used or a time-of-day option. If one option is most likely, consider presenting it as the default; if people decline it, provide a short list of alternatives.
- **Keep voice interactions simple.** A phrase that feels complicated aloud (e.g. two parameters) is probably hard to remember or say; ask for absolutely required extra information in a later step.
- **Make App Shortcuts discoverable**: consider occasional in-app tips (`SiriTipUIView`) when people perform common actions.

### Responding

Responses can include Siri dialogue, snippets (static information or dialog options) and Live Activities (`LiveActivityIntent`; relevant, changing information, great for timers and countdowns until an event completes).

**Include all critical information in the full dialogue text** (`init(full:supporting:systemImageName:)`) for audio-only devices like AirPods and HomePod.

## Editorial guidelines

- **Provide brief, memorable activation phrases and natural variants** (`AppShortcutPhrase`). You have to include your app name, but can be creative: "Create a Keynote", "Add a new presentation in Keynote".
- **Always use title case for App Shortcuts and the Shortcuts app, with *Shortcuts* plural.** Use lowercase for individual shortcuts.

## Platform considerations

No additional considerations for visionOS or watchOS. Not supported in tvOS.

### iOS, iPadOS

When people search for your app, App Shortcuts can appear in Spotlight's Top Hit or Shortcuts area, each with your chosen SF Symbol or a linked-item preview image.

**Order shortcuts by importance.** This sets their initial order in Spotlight and the Shortcuts app; the system then prioritizes the most used.

### macOS

App Shortcuts aren't supported; App Intents actions are, for custom shortcuts in the Shortcuts app on Mac.

## Resources

Source: [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts), captured 2026-09-12.
