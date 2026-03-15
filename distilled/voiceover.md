---
topic: voiceover
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/accessibility
triggers:
  - "VoiceOver"
  - "screen reader"
  - "accessibility label"
  - "rotor"
related:
  - accessibility
  - focus-and-selection
---
# VoiceOver

> VoiceOver is a screen reader that describes your app's interface audibly, enabling people who are blind or have low vision to use it without seeing the screen.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Descriptions (Alt Text)

- **Label all key interface elements** — system controls have generic labels by default; replace with descriptive ones that convey your app's functionality. Update labels when UI changes.
- **Describe meaningful images** — focus on what the image itself conveys, not surrounding captions (those are separate). Don't describe the surrounding context — VoiceOver handles that.
- **Make charts and infographics accessible** — provide a concise description of what each conveys. If it's interactive, make those interactions available to VoiceOver too.
- **Mark purely decorative images as decorative** — exclude them from VoiceOver to reduce cognitive noise.

## Navigation

- **Use unique, descriptive page/screen titles** — the title is the first thing VoiceOver reads on arrival.
- **Use accurate section headings** — help people build a mental model of the page hierarchy.
- **Describe visual relationships** — proximity, alignment, and grouping that sighted people see but VoiceOver doesn't know about. Explicitly specify grouping and ordering.
  - **Grouped**: VoiceOver reads image + its caption together.
  - **Ungrouped**: VoiceOver reads all images first, then all captions — confusing.
- VoiceOver reads in the active language's reading order (English: top→bottom, left→right).
- **Announce visible content and layout changes** — a content change without notification leaves people with a stale mental map.
- **Support the VoiceOver rotor** — include heading, link, and other content type identifiers so people can jump by content type.

## visionOS

- **Custom gestures are not accessible by default** when VoiceOver is on — VoiceOver intercepts hand input to support exploration. Users can enable *Direct Gesture mode* to bypass this, but don't assume they will. Design for VoiceOver exploration of your interface.
