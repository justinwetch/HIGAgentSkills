---
topic: feedback
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/system
triggers:
  - "feedback"
  - "haptic"
  - "vibration"
  - "sound cue"
  - "visual feedback"
  - "system feedback"
related:
  - playing-haptics
  - playing-audio
  - motion
---
# Feedback

Feedback tells people what’s happening, what they can do next, the result of an action, and how to avoid mistakes. Match delivery to significance: status is usually passive and available in context; a possible data-loss warning should interrupt so people can act.

## Best practices

- Make feedback accessible through multiple channels. Combining color, text, sound, and haptics reaches people who silence the device, look away, or use VoiceOver; see [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics).
- Consider integrating status feedback near the item it describes (for example, Mail’s update status and unread count in the iOS/iPadOS mailbox toolbar).
- Use [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) for critical, ideally actionable information, and match interruption to importance; overuse makes alerts lose impact. Warn before unexpected, irreversible data loss, but not when loss is the expected result (Finder deleting a file).
- Confirm significant completed tasks when useful (such as a successful Apple Pay transaction); people generally expect success, so reserve confirmation for sufficiently important actions. If a command can’t be carried out, say so and explain why (for example, Maps rejecting directions without a destination).

**watchOS:** Avoid indeterminate progress indicators. They can imply that people must keep watching; reassure them that a notification will arrive when the process completes.

Developer reference: [Animation and haptics](https://developer.apple.com/documentation/uikit/animation-and-haptics).

Source: [Apple HIG — Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), captured 2026-09-12.
