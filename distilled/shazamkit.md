---
topic: shazamkit
tier: 4
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "ShazamKit"
  - "audio recognition"
  - "Shazam"
  - "frequency matching"
related:
  []
---
# ShazamKit

> ShazamKit matches audio samples against the ShazamKit catalog or a custom audio catalog for recognition features.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

**Use cases:** Sync graphics to music genre; provide captions/sign language synced to audio; synchronize in-app experiences with broadcast content.

**Requires microphone permission** if sampling live audio — always explain why you need access.

## Best Practices

- **Stop recording as soon as possible.** Users don't expect the microphone to stay on after the recognition sample is captured. Record only as long as needed.
- **Let people opt in to storing recognized songs to their iCloud library.** Don't store automatically — always get explicit approval first.
