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
# iMessage Apps and Stickers

> iMessage apps and sticker packs live inside Messages conversations (and FaceTime effects). Can be standalone or embedded extensions within an iOS/iPadOS app.

**Platforms:** iOS, iPadOS *(not macOS, tvOS, visionOS, watchOS)*

## Best Practices

- **One primary experience** — people are mid-conversation; no complex flows. If you need multiple types of content, make separate iMessage apps.
- **Surface iOS/iPadOS app content** people would want to share (shopping lists, trip itineraries, group decisions).
- **Compact view = essential features.** Expanded view = additional content. Compact is roughly keyboard-height.
- **Keyboard interactions in expanded view only** — keeps content visible when keyboard is up.
- **Stickers**: expressive, inclusive, legible against varied backgrounds, works when rotated or scaled. Use transparency to blend with text/photos. Provide localized accessibility descriptions for VoiceOver.

## Icon Sizes

System auto-applies corner radius mask — supply square-cornered icons:

| Usage | @2x (px) | @3x (px) |
|---|---|---|
| Messages/notifications | 148×110 | — |
| Messages/notifications | 143×100 | — |
| Messages/notifications | 120×90 | 180×135 |
| Messages/notifications | 64×48 | 96×72 |
| Messages/notifications | 54×40 | 81×60 |
| Settings | 58×58 | 87×87 |
| App Store | 1024×1024 | 1024×1024 |

## Sticker Sizes

Pick **one size** — don't mix within a pack. Supply at @3x; system generates @2x and @1x.

| Size | @3x dimensions (px) |
|---|---|
| Small | 300×300 |
| Regular | 408×408 |
| Large | 618×618 |

Max file size: **500 KB per sticker.**

| Format | Transparency | Animation |
|---|---|---|
| PNG | 8-bit | No |
| APNG | 8-bit | Yes |
| GIF | Single-color | Yes |
| JPEG | No | No |
