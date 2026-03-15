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
  - motion
  - loading
---
# Feedback

> Feedback helps people know what's happening, discover next steps, understand action results, and avoid mistakes.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Match delivery method to significance: passive status info shown inline when needed; critical warnings must interrupt.

## Best Practices

- **Make all feedback multimodal** — combine color, text, sound, and haptics so it reaches people regardless of whether they mute their device, look away, or use VoiceOver.
- **Integrate status feedback into the interface** — show it near the items it describes, without requiring action or context switches (e.g., Mail shows last-update time and unread count in the mailbox toolbar).
- **Use alerts only for critical, actionable information** — alerts disrupt flow; overuse or low-priority use dilutes their impact.
- **Warn before unexpected, irreversible data loss** — don't warn for expected data loss (e.g., Finder doesn't warn when trashing a file because deletion is the intent).
- **Confirm successful completion** only for sufficiently important actions (e.g., Apple Pay transaction) — people expect tasks to succeed; only call out when it matters.
- **Explain when a command fails** — show what went wrong and why (e.g., Maps: "Can't provide directions to and from the same location").

## Platform Considerations

### watchOS

Don't show indeterminate progress indicators (loading spinners) in watchOS — animated indicators make people feel they must keep watching the display. Instead, reassure them that a notification will arrive when the process completes.
