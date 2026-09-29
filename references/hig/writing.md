---
topic: writing
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "copy"
  - "tone"
  - "voice"
  - "writing style"
  - "label"
  - "placeholder"
  - "alert text"
related:
  - inclusion
  - accessibility
  - voiceover
  - notifications
  - alerts
  - action-sheets
  - settings
  - text-fields
---

# Writing

Word choice is part of your app's user experience.

## Getting started

- **Determine your app's voice** from your audience. Keep and reference a list of common terms for consistency.
- **Match your tone to the context**: what people are doing, physically and in the app. It affects both wording and how text is displayed.
- **Be clear.** Use easily understood words, as few as you can. When in doubt, read it aloud.
- **Write for everyone** in simple, plain language, with accessibility and localization in mind; avoid jargon and gendered terminology. See [Writing inclusively](https://help.apple.com/applestyleguide/#/apdcb2a65d68).

## Best practices

- **Consider each screen's purpose.** Put the most important information first and format text for readability. For more than one idea, consider splitting it across screens.
- **Be action oriented**, with active voice. Button and link labels are almost always best as verbs; avoid being too cute or clever ("Send" often works better than "Let's do it!"). For links, avoid "Click here" in favor of descriptive text, especially for screen readers.
- **Build language patterns** and reuse them.
- **Choose a capitalization style per UI element type and apply it consistently**: title case (generally considered formal) or sentence case (more casual). Some components, like button labels, have specific guidelines.
- **Label multistep flows consistently.** Begin with language like "Get Started", consistently use next-step hints or "Continue"/"Next", and end with language like "Done".
- **Use possessive pronouns sparingly** ("Favorites", not "Your Favorites"). If you use them, use them consistently and try not to switch perspectives. Avoid *we* altogether; who it means can be unclear.
- **Write for how people use each device.** Keep language consistent, adjusting where helpful, and make sure you describe gestures correctly ("tap", not "click", on iPhone or iPad). iPhone and Apple Watch allow personalization, but their small screens require brevity. Several people likely see a TV, so consider who you're addressing. Bigger screens also require brevity, since text must be large enough to read from a distance.
- **Provide clear next steps on any blank screens**, with a button or link if possible. Make sure empty-state content is useful and fits the context. Don't show crucial information there; empty states are usually temporary.
- **Write clear error messages.** It's always best to help people avoid errors. Show errors as close to the problem as possible, avoid blame, and say how to fix it ("Choose a password with at least 8 characters"). Interjections like "oops!" are typically unnecessary and can sound insincere. If wording alone can't fix an error likely to affect many people, rethink the interaction.
- **Choose the delivery method and tone** by urgency, importance, context, whether action is needed now, and how much detail is needed.
- **Keep settings labels clear, simple and practical.** If a label isn't enough, explain what the setting does when on; people infer the opposite. To direct people to a setting, provide a direct link or button, not directions.
- **Show hints in text fields.** Label all fields clearly; use hint or placeholder text to show the format, by example ("name@example.com") or description ("Your name"). Show errors next to the field and say how to enter information correctly, without scolding ("Use only letters for your name", not "Don't use numbers or symbols"). Avoid unhelpful robotic messages like "Invalid name".

## Platform considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS or watchOS.

## Resources

Source: [Writing](https://developer.apple.com/design/human-interface-guidelines/writing), captured 2026-09-12.
