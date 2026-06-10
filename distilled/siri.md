---
topic: siri
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "Siri"
  - "Siri AI"
  - "Apple Intelligence and Siri AI"
  - "App Intents"
  - "AppEntity"
  - "App schema domains"
  - "Spotlight"
  - "intent donation"
  - "App Shortcut"
  - "Snippets"
related:
  - app-shortcuts
  - snippets
---
# Siri

> Siri helps people find, know, and do things across the system. Siri AI uses Apple Intelligence so apps can expose actions, entities, and contextual content through App Intents.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Integration Model

- **Use App Intents** - expose app actions (*intents*) and content (*entities*) so Siri, Spotlight, and Shortcuts can understand them.
- **Prefer App schema domains when available** - common domains like email, music, and photos get built-in logic, natural conversation, and deeper contextual understanding.
- **Use App Shortcuts for custom actions** outside schema coverage.
- **Use snippets for richer responses** when a schema action/content item needs visual or interactive response content.

## Context And Discovery

- **Annotate onscreen content with app entities** - helps Siri understand references to visible content, controls, or graphics.
- **Donate relevant entities to Spotlight** - prefer recently used, favorited, bookmarked, wishlisted, or otherwise personally relevant items; don't dump everything unless the category justifies broad access.
- **Donate actions people actually take** - recent activity and expressed interest help Siri anticipate future actions.

## Best Practices

- **Prioritize popular, context-sensitive actions** - especially hands-free, cross-device, or deep-navigation tasks.
- **Use familiar terminology** for app content and actions.
- **Don't advertise** - no ads, marketing, or IAP pitches in Siri-delivered content.
- **Only customize responses when built-in responses fall short.**
- **Make responses work audibly and visually** - voice output must stand alone; snippets enhance but don't carry essential meaning alone.
- **Keep dialogue succinct** - repeated Siri interactions make filler, humor, and excess detail irritating.
- **Use open-ended follow-up questions for huge option lists.**
- **Keep wording device-independent** unless the specific device is known and relevant.
- **Omit your app name from responses** - the system provides attribution.
- **Use specific, helpful error text** - "We're out of chicken noodle soup" beats generic failure.
- **Respect parental controls and appropriate language** in anything Siri might speak aloud.

## Editorial Guidelines

- Refer to **Siri** by name, not pronouns.
- Don't impersonate Siri, reproduce Siri functionality, imply Apple authorship, or use reserved phrases like "Call 911" or "Hey Siri" as custom commands.
- In localized text, translate only **Hey** in "Hey Siri"; never translate **Siri**.
- **Shortcuts** is capitalized for the app/feature; individual shortcuts are lowercase unless part of a title.
