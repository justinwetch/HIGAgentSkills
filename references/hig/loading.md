---
topic: loading
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/status
triggers:
  - "loading"
  - "skeleton"
  - "placeholder"
  - "shimmer"
  - "content loading state"
related:
  - progress-indicators
  - feedback
  - launching
---
# Loading

Best loading ends before people notice; avoid disruption.

- **Show something quickly:** otherwise people may think the app is broken; use placeholder text, graphics, or animations until content arrives.
- **Keep it usable while loading:** load in the background so people can act elsewhere (a game loads the next level while players read about it or open a menu).
- **For unavoidable long waits,** show hints, tips, or feature introductions; estimate remaining time accurately so people have time to enjoy the filler without repetition.
- **Move large downloads to nondisruptive times:** consider [Background Assets](https://developer.apple.com/documentation/backgroundassets) for level packs, 3D models, textures, and similar assets immediately after installation, during updates, or otherwise in background. [GameKit guidance](https://developer.apple.com/documentation/gamekit/improving-the-player-experience-for-games-with-large-downloads) recommends ample base-install content, then on-demand resources and the Background Assets API.

**Progress:** Communicate loading and duration. Show content instantly when possible; for waits beyond a moment or two, you can use system [progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators): determinate when duration is known, indeterminate otherwise. Standard indicators suit most apps; games may use a custom matching-style view. (iOS/iPadOS/macOS/tvOS/visionOS: no additional guidance.) On watchOS, avoid indicators when possible; for a one- or two-second wait, one beats a blank screen.


Source: [Apple HIG — Loading](https://developer.apple.com/design/human-interface-guidelines/loading), captured 2026-09-12.
