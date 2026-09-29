---
topic: imessage-apps-and-stickers
tier: 3
platforms: [ios, ipados]
category: technologies
triggers:
  - "iMessage app"
  - "sticker"
  - "Messages extension"
  - "message bubble"
  - "MSStickerSize"
related:
  - collaboration-and-sharing
---

# iMessage apps and stickers

iMessage apps let people share content, collaborate or play games in a conversation; stickers are images that decorate it. Both also work in Messages and FaceTime effects; build as a standalone app or iOS/iPadOS app extension (`Messages`).

## Best practices

- **Prefer one primary experience per iMessage app**; for other functionality or content collections, consider a separate iMessage app each.
- **Consider surfacing content from your iOS or iPadOS app**, like a shareable shopping list or a simple collaborative task.
- **Make sure essential, most-used features are in the compact view** (below the transcript); reserve the rest for the expanded view.
- **In general, let people edit text only in the expanded view**; the compact view is roughly keyboard-sized, so this keeps your content visible.
- **Create expressive, inclusive, versatile stickers**; make sure each stays legible on a wide range of backgrounds and when rotated or scaled. Transparency can help them blend with text, photos and other stickers.
- **Provide a localized alternative description for each sticker**, for VoiceOver.

## Specifications

### Icon sizes

Supply a square-cornered icon for each extension; the system masks the corners round. After install, it also appears in the Messages app drawer.

|Usage|@2x (px)|@3x (px)|
|---|---|---|
|Messages, notifications|148x110|-|
||143x100|-|
||120x90|180x135|
||64x48|96x72|
||54x40|81x60|
|Settings|58x58|87x87|
|App Store|1024x1024|1024x1024|

### Sticker sizes

Pick the size that best fits your content; don't mix sizes within a pack. Messages arranges each size in a different grid. Supply @3x images; if necessary, the system downscales to @2x and @1x at runtime (`MSStickerSize`).

|Size|@3x (px)|
|---|---|
|Small|300x300|
|Regular|408x408|
|Large|618x618|

A sticker file must be 500 KB or smaller. Supported formats:

|Format|Transparency|Animation|
|---|---|---|
|PNG|8-bit|No|
|APNG|8-bit|Yes|
|GIF|Single-color|Yes|
|JPEG|No|No|

## Platform considerations

iOS and iPadOS only; no additional considerations.

## Resources

Source: [iMessage apps and stickers](https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers), captured 2026-09-12.
