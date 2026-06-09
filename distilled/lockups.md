---
topic: lockups
tier: 4
platforms: [tvos]
category: components/tvos
triggers:
  - "lockup"
  - "TVCardView"
  - "caption button"
  - "monogram"
  - "poster tvOS"
  - "TVLockupView"
  - "TVLockupHeaderFooterView"
  - "TVCaptionButtonView"
  - "TVMonogramContentView"
  - "TVPosterView"
related:
  - designing-for-tvos
  - focus-and-selection
---
# Lockups

> Lockups combine a content view, header, and footer into a single interactive unit in tvOS. All three sections expand and contract together on focus.

**Platforms:** tvOS only

Four lockup types: **cards**, **caption buttons**, **monograms**, **posters**.

## Best Practices

- **Leave adequate space between lockups** — focused lockups expand, so prevent overlap with neighbors.
- **Consistent sizes within a row or group** — matching widths and heights look better than varied sizes.

## Types

| Type | Structure | Notes |
|---|---|---|
| Card | Header + content + footer | Best for ratings/reviews of media items |
| Caption button | Button (image or text) + optional title + subtitle below | Tilts with swipe direction on focus: vertical alignment → tilt up/down; horizontal → tilt left/right; grid → both |
| Monogram | Circular photo + name | Identifies cast/crew. If no image available, shows initials. **Prefer image over initials.** |
| Poster | Image + optional title + subtitle | Title/subtitle hidden until focused. Size to suit content. |
