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

> An interface icon (glyph) uses streamlined shapes and color to communicate one action or concept. You can design custom glyphs or choose SF Symbols, using them as-is or customizing them.

Interface icons and symbols define shapes with black and clear colors; the system can apply other colors to the black areas.

## Best Practices

- Create recognizable, highly simplified icons using familiar metaphors; detail can become confusing or unreadable.
- Keep all icons consistent in size, detail, stroke thickness/weight, and perspective. Adjust dimensions for visual weight so they look consistent, rather than forcing equal geometry. Match icon weight to adjacent text unless intentionally emphasizing one.
- Optically align asymmetric icons. If geometric centering looks unbalanced, slightly reposition the glyph and encode the adjustment as padding in the asset so the padded asset can be geometrically centered.
- Provide selected-state artwork only when necessary. Toolbars, tab bars, buttons, and other standard components update selected appearance automatically. A selected toolbar icon receives the app’s accent color; an unselected item retains the default toolbar appearance.
- Use inclusive imagery: prefer gender-neutral human figures and concepts understandable across cultures/languages.
- Include text only when essential. Localize individual characters. For abstract text, use an abstract passage representation and provide a flipped right-to-left version.
- For custom icons, use PDF or SVG. Vectors scale automatically. PNG does not support scaling, so PNG-based interface icons require multiple high-resolution versions; PNG is used for app icons and images with shading, texture, or highlighting. A custom SF Symbol can provide a matching scale/weight.
- Provide alternative text/accessibility descriptions so VoiceOver can describe custom icons.
- Avoid replicas of Apple hardware, which can date as designs change; use Apple Design Resources or relevant SF Symbols instead.

## Standard SF Symbols

These symbols can represent common actions in menus, toolbars, buttons, and other cross-platform interfaces.

| Group | Action | Symbol name |
|---|---|---|
| Editing | Cut | `scissors` |
| Editing | Copy | `document.on.document` |
| Editing | Paste | `document.on.clipboard` |
| Editing | Done; Save | `checkmark` |
| Editing | Cancel; Close | `xmark` |
| Editing | Delete | `trash` |
| Editing | Undo | `arrow.uturn.backward` |
| Editing | Redo | `arrow.uturn.forward` |
| Editing | Compose | `square.and.pencil` |
| Editing | Duplicate | `plus.square.on.square` |
| Editing | Rename | `pencil` |
| Editing | Move to; Folder | `folder` |
| Editing | Attach | `paperclip` |
| Editing | Add | `plus` |
| Editing | More | `ellipsis` |
| Selection | Select | `checkmark.circle` |
| Selection | Deselect; Close | `xmark` |
| Selection | Delete | `trash` |
| Text formatting | Superscript | `textformat.superscript` |
| Text formatting | Subscript | `textformat.subscript` |
| Text formatting | Bold | `bold` |
| Text formatting | Italic | `italic` |
| Text formatting | Underline | `underline` |
| Text formatting | Align Left | `text.alignleft` |
| Text formatting | Center | `text.aligncenter` |
| Text formatting | Justified | `text.justify` |
| Text formatting | Align Right | `text.alignright` |
| Search | Search | `magnifyingglass` |
| Search | Find; Find and Replace; Find Next; Find Previous; Use Selection for Find | `text.page.badge.magnifyingglass` |
| Search | Filter | `line.3.horizontal.decrease` |
| Sharing/exporting | Share; Export | `square.and.arrow.up` |
| Sharing/exporting | Print | `printer` |
| Users/accounts | Account; User; Profile | `person.crop.circle` |
| Ratings | Dislike | `hand.thumbsdown` |
| Ratings | Like | `hand.thumbsup` |
| Layer ordering | Bring to Front | `square.3.layers.3d.top.filled` |
| Layer ordering | Send to Back | `square.3.layers.3d.bottom.filled` |
| Layer ordering | Bring Forward | `square.2.layers.3d.top.filled` |
| Layer ordering | Send Backward | `square.2.layers.3d.bottom.filled` |
| Other | Alarm | `alarm` |
| Other | Archive | `archivebox` |
| Other | Calendar | `calendar` |

## Platform Considerations

No additional considerations for iOS, iPadOS, tvOS, visionOS, or watchOS.

### macOS: Document Icons

If a macOS app supports a custom document type, a folded top-right-corner paper icon distinguishes documents even at small sizes. Without one, macOS composites the app icon and file extension. If the app handles multiple file types, an icon set can distinguish them. A custom icon can combine any of a background fill, center image, and extension text; the system layers, positions, masks, and composites them.

- Use simple shapes and a reduced palette that remain recognizable at **16×16 px**. A single expressive background fill can be sufficient. Reduce detail and thicken lines for smaller sizes, aligning simplified lines to the reduced pixel grid. For example, a `32×32 px` version can use fewer grid lines and a thicker EKG; at `16×16 px @2x`, retain the EKG but remove the grid; at `16×16 px @1x`, remove both.
- Keep important background-fill content out of the **top-right corner**, which is masked and covered by the white folded corner. Supply:
- Background-fill assets:

  | @1x canvas (px) | @2x canvas (px) |
  |---:|---:|
  | 512×512 | 1024×1024 |
  | 256×256 | 512×512 |
  | 128×128 | 256×256 |
  | 32×32 | 64×64 |
  | 16×16 | 32×32 |

- Center-image assets:

  | @1x canvas (px) | @2x canvas (px) |
  |---:|---:|
  | 256×256 | 512×512 |
  | 128×128 | 256×256 |
  | 32×32 | 64×64 |
  | 16×16 | 32×32 |

- A center image is half the overall document-icon canvas (for a `32×32 px` icon, use a `16×16 px` center-image canvas). Leave a margin of about **10% per side** and keep most artwork within the remaining approximately **80%** area; content may extend into the margin for optical alignment. On a `256×256 px` canvas, most artwork fits an area of about `205×205 px`.
- If a familiar object can communicate the document type or its connection with the app, consider using it as the center image; keep it simple and recognizable at every size.
- If the extension is unfamiliar, supply a short descriptive term (for example, `scene` instead of `scn`). The system scales extension text to fit and capitalizes every letter by default.

## References

[SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols), [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons), [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion), [Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left), [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover), and [Apple Design Resources](https://developer.apple.com/design/resources/). For macOS document-icon assets, see [Apple Design Resources for macOS apps](https://developer.apple.com/design/resources/#macos-apps).

Source: [Apple Human Interface Guidelines — Icons](https://developer.apple.com/design/human-interface-guidelines/icons/)
