---
topic: live-photos
tier: 4
platforms: [ios, ipados, macos, tvos, visionos]
category: components/content
triggers:
  - "Live Photo"
  - "LivePhotosKit JS"
  - "PHLivePhoto"
  - "animated photo"
  - "motion photo"
related:
  - images
---

# Live Photos

Camera captures audio and extra frames around a still; pressing it plays the sound- and motion-rich Live Photo.

## Best practices

- Apply effects or adjustments to every frame. If that isn’t supported, offer conversion to a still. Keep the Live Photo intact and consistent across apps; don’t split out frames or audio.
- For sharing, let people preview the complete Live Photo before deciding and always offer a traditional still. Show download progress and indicate when it is complete and playable.
- In unsupported environments, show a traditional still instead of recreating the Live Photo experience.
- Distinguish Live Photos from stills with movement; because the Photos full-screen swipe effect has no built-in equivalent, implement custom motion. Without movement, show the system badge above the image (with or without text), never a video-like playback button. Keep placement consistent, usually in a corner.

## Platform considerations

There are no additional iOS, iPadOS, macOS, or tvOS considerations. Live Photos aren’t supported in watchOS. visionOS can display Live Photos but can’t capture them.

## Resources

- [`PHLivePhoto`](https://developer.apple.com/documentation/photos/phlivephoto) — PhotoKit
- [`LivePhotosKit JS`](https://developer.apple.com/documentation/livephotoskitjs) — web playback
- [*What’s new in camera capture*](https://developer.apple.com/videos/play/wwdc2021/10047)

Source: [Live Photos](https://developer.apple.com/design/human-interface-guidelines/live-photos) (captured 2026-09-12).
