---
topic: maps
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "map"
  - "MapKit"
  - "location"
  - "annotation"
  - "overlay"
  - "geocoding"
related:
  - layout
---
# Maps

> A MapKit map displays geographic data with zoom, pan, rotation, annotations, overlays, and routing.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Views: standard, satellite, hybrid. Can include custom annotations and overlays.

## Best Practices

- **Make maps interactive** — people expect to zoom, pan, and rotate. Noninteractive elements that obscure the map break expectations.
- **Map emphasis styles:**
  - **Default** — fully saturated colors; great for standard map apps; visually consistent with the Maps app.
  - **Muted** — desaturated; best when your custom content (pins, overlays) needs to stand out.
- **Search and filtering** — offer a search field with category filters (e.g., clothing, electronics for a mall map).
- **Selection styling** — clearly indicate selected areas/elements with distinct outline and color variation.
- **Cluster overlapping points of interest** — single pin for nearby group; expands as people zoom in.
- **Preserve the Apple logo and legal link**:
  - 7pt padding on sides, 10pt above/below.
  - Don't move them with your UI — they should appear fixed to the map.
  - If your UI moves (e.g., a pull-up card), place the logo/link 10pt above the lowest resting position of the card.
  - Maps smaller than 200×100px don't show the logo/legal link.

## Custom Information

- **Annotation styling** — default: red marker + white pin icon. Customize tint to match your app. Icons can be strings (2–3 chars max) or images. Selectable map features (Apple POIs, territories) can show custom appearance when selected.
- **Overlay levels:**
  - **Above roads** (default) — overlay above roads, below buildings/trees. People can see some map detail below.
  - **Above labels** — overlay above everything, hides all underneath. For fully abstracted areas or hiding irrelevant map sections.
- **Contrast for custom controls** — use a thin stroke or drop shadow to distinguish custom controls from the map underneath.

## Place Cards

Place cards show rich place info (hours, phone, address, etc.).

**Styles:**

| Style | Description |
|---|---|
| Automatic | System picks based on map view size |
| Full callout | Large, detailed popover (iPad/macOS) or sheet (iOS) |
| Compact callout | Space-saving; good for dense-annotation maps |
| Caption | "Open in Apple Maps" link only |
| Sheet | Place card in a sheet |

- **Choose style by context** — a small map with many annotations → compact callout. A single-feature map → full callout.
- **Ensure legibility across devices and window sizes** — for full callout, set a minimum width.
- **Don't duplicate info** — if your app already shows the place info, prefer compact or caption styles.
- **Maintain location visibility** — keep the selected place visible while the card is shown. Set an offset distance and direct the card arrow toward the location.
- **Outside map views**: displaying a place card without a map → must include a map in the place card. Use location cues (address, pin icon) in surrounding content to signal interaction.

## Indoor Maps

- **Progressive detail by zoom level** — show rooms/buildings at all levels; add store names, restrooms, etc. as people zoom in.
- **Distinctive styling** — color + icons to differentiate area types (stores, services, amenities).
- **Floor picker for multi-level venues** — list by floor number, not name; concise.
- **Include surrounding context** — adjacent streets and areas (dimmed, distinct color) to orient people.
- **Support transit routing** — offer connections to nearby bus stops, train stations, parking; quick switch to Apple Maps for broader navigation.
- **Limit scrolling outside venue** — prevent people from losing the indoor map. Keep part of the indoor map always visible; adjust allowed scroll range per zoom level.
- **Match your app's visual style** — don't replicate Apple Maps; make overlays/icons/text consistent with your design system.

## Platform Considerations

### watchOS
Maps on Apple Watch are **static snapshots** — not interactive. Tapping opens the Maps app.
- Max 5 annotations.
- Fit the map element to the full screen (no scrolling).
- Show the smallest region that encompasses all points of interest — all key content must be visible without scrolling.
