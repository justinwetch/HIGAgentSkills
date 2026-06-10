---
topic: complications
tier: 3
platforms: [watchos]
category: components/watchos
triggers:
  - "complication"
  - "ClockKit"
  - "WidgetKit complication"
  - "watch face data"
  - "accessories"
  - "WidgetRenderingMode"
  - "WidgetFamily.accessoryRectangular"
  - "TimelineProvider.placeholder(in:)"
  - "CLKComplicationDataSource"
related:
  - watch-faces
  - widgets
  - designing-for-watchos
---
# Complications

> A complication displays timely, relevant information on the watch face for a quick wrist-raise glance.

**Platforms:** watchOS only

Use WidgetKit for watchOS 9+. Legacy ClockKit templates support earlier versions.
Most watch faces support ≥1 complication slot; some support 4 or more.

## Best Practices

- **Essential, dynamic content only** — static complications that show no useful data lose their spot. Deep-link each complication to the most relevant app section.
- **Support all complication families** — more families = available on more watch faces. If no useful data for a family, at minimum provide an app icon image (still lets people launch the app).
- **Multiple complications per family** — enables shareable, preconfigured watch faces centered on your app. Define a different deep link for each.
- **Privacy** — Always-On Retina display is visible to bystanders. Protect sensitive data; see always-on guidelines.
- **Timeline strategy** — you provide data as a timeline; entries specify display times. Limited updates/day and limited entries stored. Choose times that maximize usefulness.

## Visual Design

- **Ring/gauge style by data type:**
  - **Closed ring** — percentage of a whole (battery gauge).
  - **Open ring** — arbitrary min/max range (speed indicator).
  - **Segmented ring** — rapid value changes within a defined range (e.g., Noise complication).
- **Tinted mode** — system applies a solid color to text, gauges, images; desaturates full-color images unless you provide tinted alternatives. Never use color as the only differentiator.
- **Line widths** ≥2 pt — thinner lines are hard to read at a glance or in motion.
- **Static placeholder images** — required for each complication. Used while data loads and in the complication picker carousel. Size of placeholder may differ from live image size.

## Complication Families and Image Sizes

### Circular (regular size) — Infograph, Infograph Modular

| Image type | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Image | 42×42 pt | 44.5×44.5 pt | 47×47 pt | 50×50 pt |
| Closed gauge | 27×27 pt | 28.5×28.5 pt | 31×31 pt | 32×32 pt |
| Open gauge fill area | 11×11 pt | 11.5×11.5 pt | 12×12 pt | 13×13 pt |
| Stack (no text) | 28×14 pt | 29.5×15 pt | 31×16 pt | 33.5×16.5 pt |

Default text: Rounded, Medium, 12/12.5/13/14.5 pt per watch size.

### Circular (extra-large) — X-Large watch face

| Image type | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Image | 120×120 pt | 127×127 pt | 132×132 pt | 143×143 pt |
| Closed gauge | 77×77 pt | 81.5×81.5 pt | 87×87 pt | 91.5×91.5 pt |
| Open gauge fill | 31×31 pt | 33×33 pt | 33×33 pt | 37×37 pt |
| Stack | 80×40 pt | 85×42 pt | 87×44 pt | 95×48 pt |

Default text: Rounded, Medium, 34.5/36.5/36.5/41 pt per watch size.

### Corner — Infograph corners

| Image type | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Circular | 32×32 pt | 34×34 pt | 36×36 pt | 38×38 pt |
| Gauge | 20×20 pt | 21×21 pt | 22×22 pt | 24×24 pt |
| Text | 20×20 pt | 21×21 pt | 22×22 pt | 24×24 pt |

Default text: Rounded, Semibold, 10/10.5/11/12 pt per watch size.

### Rectangular — Infograph Modular center, Smart Stack

| Content | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Large image + title | 150×47 pt | 159×50 pt | 171×54 pt | 178.5×56 pt |
| Large image, no title | 162×69 pt | 171.5×73 pt | 184×78 pt | 193×82 pt |

Default text: Rounded, Medium, 16.5/17.5/18/19.5 pt per watch size. Note: large-image layouts include 4 pt corner radius automatically.

Smart Stack: supply background color/content, use AppIntents for relevancy, or create a custom Smart Stack layout. See widgets for additional guidance.

### Inline and Utilitarian Layouts

- **Small** (corner area): image, icon, or ring. Flat content: 9–21×9 pt (38mm) → 12–26×12 pt (45/49mm).
- **Large** (full-width bottom): text + optional leading icon. Same image sizes as small.

## Legacy Templates (watchOS 8 and earlier)

| Template | Sizes (image, simple) |
|---|---|
| Circular small | Ring: 20–26 pt; Simple: 16–21.5 pt; Stack: 16×7–19×9.5 pt |
| Modular small | Ring: 18–22.5 pt; Simple: 26–34.5 pt; Stack: 26×14–34.5×18 pt |
| Modular large | Content: 11–44 pt columns, standard body, or table |
| Extra large | Ring: 63–79 pt; Simple: 91–121 pt; Stack: 78×42–103.5×53.5 pt |

*(Legacy templates use nongraphic styles that don't adopt the wearer's color.)*
