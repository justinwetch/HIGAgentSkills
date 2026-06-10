---
topic: icons
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "icon"
  - "glyph"
  - "interface icon"
  - "document icon"
  - "toolbar icon"
related:
  - sf-symbols
  - app-icons
  - inclusion
  - right-to-left
  - voiceover
---
# Icons

> Interface icons (glyphs) use streamlined shapes and colors to represent actions and concepts. Use SF Symbols wherever possible; design custom icons as vectors.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Best Practices

- **Recognizable, simplified design** — familiar visual metaphors, not detailed. Details become confusing or unreadable at small sizes.
- **Visual consistency across all icons** — same size, detail level, stroke weight, and perspective throughout your app. Adjust dimensions for visual balance (not pixel-perfect equality).
- **Match icon weight to adjacent text weight** unless you intend to visually emphasize one.
- **Optical alignment** — asymmetric icons may need position adjustment to look centered. Add asymmetric padding to the asset rather than adjusting at runtime.
- **Selected-state icons**: system components (toolbars, tab bars, buttons) auto-provide them. Only supply manually when using custom components.
- **Inclusive images** — gender-neutral human figures; globally recognizable concepts.
- **Text in icons**: only when essential. Localize any characters. For abstract "text" imagery, use an abstracted representation; provide an RTL flipped version.
- **Use vector format** (PDF or SVG) for custom icons — auto-scales for Retina. PNG doesn't scale; requires multiple sizes.
- **Provide alt-text labels** for all custom icons for VoiceOver.
- **Don't replicate Apple hardware** — hardware designs change. Use only Apple-provided images or SF Symbols for Apple products.

## Standard SF Symbol Names

### Editing
| Action | Symbol |
|---|---|
| Cut | `scissors` |
| Copy | `document.on.document` |
| Paste | `document.on.clipboard` |
| Done | `checkmark` |
| Cancel | `xmark` |
| Delete | `trash` |
| Undo | `arrow.uturn.backward` |
| Redo | `arrow.uturn.forward` |
| Compose | `square.and.pencil` |
| Duplicate | `plus.square.on.square` |
| Rename | `pencil` |
| Move to | `folder` |
| Attach | `paperclip` |
| Add | `plus` |
| More | `ellipsis` |

### Selection
| Action | Symbol |
|---|---|
| Select | `checkmark.circle` |
| Deselect | `xmark` |
| Delete | `trash` |

### Text Formatting
| Action | Symbol |
|---|---|
| Superscript | `textformat.superscript` |
| Subscript | `textformat.subscript` |
| Bold | `bold` |
| Italic | `italic` |
| Underline | `underline` |
| Align Left | `text.alignleft` |
| Center | `text.aligncenter` |
| Justified | `text.justify` |
| Align Right | `text.alignright` |

### Search
| Action | Symbol |
|---|---|
| Search | `magnifyingglass` |
| Find | `text.page.badge.magnifyingglass` |
| Filter | `line.3.horizontal.decrease` |

### Sharing & Exporting
| Action | Symbol |
|---|---|
| Share | `square.and.arrow.up` |
| Print | `printer` |

### Users & Accounts
| Action | Symbol |
|---|---|
| Account | `person.crop.circle` |

### Ratings
| Action | Symbol |
|---|---|
| Dislike | `hand.thumbsdown` |
| Like | `hand.thumbsup` |

### Layer Ordering
| Action | Symbol |
|---|---|
| Bring to Front | `square.3.layers.3d.top.filled` |
| Send to Back | `square.3.layers.3d.bottom.filled` |
| Bring Forward | `square.2.layers.3d.top.filled` |
| Send Backward | `square.2.layers.3d.bottom.filled` |

### Other
| Action | Symbol |
|---|---|
| Alarm | `alarm` |
| Archive | `archivebox` |
| Calendar | `calendar` |

## macOS: Document Icons

Custom document types can have a document icon (paper with top-right corner folded). If not provided, macOS auto-generates one from your app icon + file extension.

**Composition**: background fill + center image + extension text, composited onto folded-corner shape.

**Rules:**
- Simple shapes, limited palette — must be recognizable at 16×16 px.
- Avoid important content in the **top-right corner** — system draws the folded corner there.
- **Center image** = half the overall document icon canvas size. Margin = ~10% of canvas; keep primary content within the remaining ~80%.
- Extension text: supply a short, friendly term if the extension is unfamiliar (e.g., "scene" instead of "scn"). System auto-capitalizes.

**Background fill sizes:**
- 512×512 @1x / 1024×1024 @2x
- 256×256 @1x / 512×512 @2x
- 128×128 @1x / 256×256 @2x
- 32×32 @1x / 64×64 @2x
- 16×16 @1x / 32×32 @2x

**Center image sizes:**
- 256×256 @1x / 512×512 @2x
- 128×128 @1x / 256×256 @2x
- 32×32 @1x / 64×64 @2x
- 16×16 @1x / 32×32 @2x
