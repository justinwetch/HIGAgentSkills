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

> Live Photos capture audio and extra frames before and after a still photo. People press to see it animate.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

visionOS can view Live Photos but can't capture them. Don't claim capture support unless the current platform source explicitly supports it.

## Best Practices

- **Apply edits/effects to all frames** - not just the still frame. If your app can't apply effects to all frames, give people the option to convert to a still photo first.
- **Keep the Live Photo intact** - don't disassemble into separate frames or audio. Consistent visual treatment and interaction across apps is essential.
- **Great sharing experience** - let people preview the full contents before sharing. Always offer the option to share as a traditional still photo.
- **Clearly indicate download progress** - show a progress indicator during download; signal when the photo is ready to play.
- **Unsupported environments**: display as a traditional still photo; don't try to replicate the Live Photo experience.
- **Make Live Photos distinguishable from stills**:
  - Best: subtle motion hint (custom motion effect you implement).
  - Fallback: use a system-provided badge in a consistent corner. Never use a playback button; it will be mistaken for video.
  - Keep badge placement consistent across all photos.
