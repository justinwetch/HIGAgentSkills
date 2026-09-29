---
topic: shazamkit
tier: 4
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "ShazamKit"
  - "audio recognition"
  - "Shazam"
related:
  []
---
# ShazamKit

ShazamKit recognizes audio by matching a sample against the ShazamKit catalog or a custom audio catalog. Possible uses include graphics matching the genre of currently playing music, closed captions or sign language synchronized to audio for people with hearing disabilities, and in-app experiences synchronized with virtual content in education or retail.

If the device microphone is needed to capture a sample, request microphone access and explain the feature’s benefit in context.

After permission:

- **Stop recording as soon as possible.** Record only as long as needed to obtain the recognition sample; people don’t expect the microphone to remain on.
- **Let people opt in before storing recognized songs in their iCloud library.** Even though Music Recognition and the Shazam app show your app as the source, people should control which apps store content in their library.

Platform considerations: no additional guidance for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

Resources: [ShazamKit](https://developer.apple.com/documentation/shazamkit) and [Explore ShazamKit](https://developer.apple.com/videos/play/wwdc2021/10044).

Source: [Apple Human Interface Guidelines — ShazamKit](https://developer.apple.com/design/Human-Interface-Guidelines/shazamkit), captured 2026-09-12.
