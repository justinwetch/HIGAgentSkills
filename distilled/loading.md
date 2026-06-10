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

> The best loading experience completes before people notice it.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Best Practices

- **Show something immediately** — display placeholder text, graphics, or animations while content loads; replace them as content arrives. A blank screen signals a broken app.
- **Let people do other things while waiting** — load content in the background and keep the rest of the app interactive. A game can load a level while players read hints or navigate menus.
- **For unavoidably long loads, show something interesting** — gameplay hints, tips, feature introductions. Gauge remaining time accurately to prevent too-brief or repeated filler content.
- **Use BackgroundAssets framework** to schedule large asset downloads (level packs, 3D models, textures) after installation, during updates, or at other non-disruptive times — improves install-to-play time.

## Showing Progress

- Use progress indicators when loading takes more than a moment. Use **determinate** when duration is known, **indeterminate** when it isn't.
- For games, consider **custom loading views** — standard progress indicators can feel out of place in a game context; match the visual style of the game.

## Platform Considerations

### watchOS

Avoid loading indicators as much as possible — people expect immediate interactions. For the rare cases where content takes a second or two, show a brief loading indicator rather than a blank screen.
