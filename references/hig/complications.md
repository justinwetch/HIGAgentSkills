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

A complication shows timely, relevant information on the watch face, visible whenever people raise their wrist. Most faces can show at least one; some four or more.

Since watchOS 9, complications (*accessories*) belong to families (circular, corner, inline, rectangular) with recommended layouts; each face slot specifies its supported family. Complications for earlier watchOS can use legacy templates: nongraphic styles that don't take the wearer's selected color. Prefer WidgetKit for watchOS 9 and later; for earlier versions, keep implementing `CLKComplicationDataSource`.

## Best practices

- **Identify essential, dynamic content that people want to view at a glance.** A static complication without meaningful data may lose its prominent spot.
- **Support all complication families when possible** (more families, more faces). If a family can't show useful information, provide an image representing your app (like its icon) that still launches it.
- **Consider creating multiple complications for each family**, enabling shareable faces centered on your app (e.g., swim, bike and run complications, each deep-linking to its segment, preconfigured on one face).
- **Define a different deep link for each complication you support**, opening the most relevant area.
- **Keep privacy in mind.** Always-On may expose the face to others; help people keep sensitive information from being visible.
- **Carefully consider when to update data.** Each timeline entry specifies when it displays (a meeting 1 hour before it starts; a forecast when the conditions are expected). Daily timeline updates and stored entries per app are limited; choose times that maximize usefulness.

## Visual design

- **Choose a ring or gauge style based on the data you need to display:**
  - Closed: a percentage of a whole (battery).
  - Open: arbitrary min/max, not a percentage (speed).
  - Segmented: an app-defined range; can convey rapid changes (Noise).
- **Make sure images look good in tinted mode.** The system applies a solid color to text, gauges and images, and desaturates full-color images unless you provide tinted versions (`WidgetRenderingMode`). With legacy templates, it applies only to graphic complications.
  - Avoid using color as the only way to communicate important information.
  - When necessary, provide a tinted-mode version of a full-color image that looks bad desaturated.
- **Recognize that people might prefer tinted mode to full color.** The system then converts the complication to grayscale and tints it with one color based on the wearer's selected color.
- **Generally use line widths of 2 pt or greater**; thinner lines are hard to see at a glance, especially in motion. Suit line weight to image size and complexity.
- **Provide a set of static placeholder images for each complication you support** (`placeholder(in:)`). The system shows them when there's no other content (e.g., after install while checking for a localized placeholder) and in the selection carousel. Sizes vary per layout and legacy template; a placeholder may not match the actual image's size.

Sizes below are in pt; @2x px = 2x pt unless shown.

## Circular

Text, gauges and full-color images in circular areas on Infograph and Infograph Modular. Layouts (regular and extra-large): closed gauge image/text, open gauge image/text/range, image, stack image/text.

Text can accompany a regular-size circular image, curving along the bezel on some faces (Infograph); it can fill nearly 180 degrees before truncating.

Regular size (system applies a circular mask to each image):

|Image|40mm|41mm|44mm|45mm/49mm|
|---|---|---|---|---|
|Image|42x42|44.5x44.5|47x47|50x50|
|Closed gauge|27x27|28.5x28.5|31x31|32x32|
|Open gauge|11x11|11.5x11.5|12x12|13x13|
|Stack (not text)|28x14|29.5x15|31x16|33.5x16.5|

Default SwiftUI text: Rounded, Medium; 12 pt (40mm), 12.5 (41mm), 13 (44mm), 14.5 (45mm/49mm).

Use extra-large layouts for an oversized treatment of important information (e.g., Contacts' photo), filling most of the X-Large face; some text fields support multicolor. The system masks image, open-gauge and closed-gauge images circularly.

|Extra-large|40mm|41mm|44mm|45mm/49mm|
|---|---|---|---|---|
|Image|120x120|127x127|132x132|143x143|
|Open gauge|31x31|33x33|33x33|37x37|
|Closed gauge|77x77|81.5x81.5|87x87|91.5x91.5|
|Stack|80x40|85x42|87x44|95x48|

Default SwiftUI text: Rounded, Medium; 34.5 pt (40mm), 36.5 (41mm), 36.5 (44mm), 41 (45mm/49mm).

No-content placeholders: Circular and Bezel use the regular Image sizes, Extra Large the extra-large Image sizes (40mm values also for 42mm; none for 38mm).

## Corner

Full-color images, text and gauges in face corners (Infograph); some templates support multicolor text. Layouts: circular image, gauge image/text, stack text, text image. System applies a circular mask to each image.

|Image|40mm|41mm|44mm|45mm/49mm|
|---|---|---|---|---|
|Circular|32x32|34x34|36x36|38x38|
|Gauge|20x20|21x21|22x22|24x24|
|Text|20x20|21x21|22x22|24x24|

No-content placeholder: Gauge sizes (40mm value also for 42mm; none for 38mm).

Default SwiftUI text: Rounded, Semibold; 10 pt (40mm), 10.5 (41mm), 11 (44mm), 12 (45mm/49mm).

## Inline

**Utilitarian small** occupies a rectangular corner area (Chronograph, Simple): an image, interface icon or circular graph. Layouts: flat, ring image/text, square.

|Content|38mm|40mm/42mm|41mm|44mm|45mm/49mm|
|---|---|---|---|---|---|
|Flat|9-21x9|10-22x10|10.5-23.5x21 pt (21-47x21 @2x; px and Utilitarian large imply 10.5 pt height)|N/A|12-26x12|
|Ring|14x14|14x14|15x15|16x16|16.5x16.5|
|Square|20x20|22x22|23.5x23.5|25x25|26x26|

**Utilitarian large** is primarily text, optionally with a leading interface icon, spanning the face bottom (Utility, Motion). Layout: large flat.

|Content|38mm|40mm/42mm|41mm|44mm|45mm/49mm|
|---|---|---|---|---|---|
|Flat|9-21x9|10-22x10|10.5-23.5x10.5|N/A|12-26x12|

## Rectangular

Full-color images, text, a gauge and an optional title in a large region; some text fields support multicolor. Suits charts, graphs and diagrams of values changing over time (Heart Rate: high-contrast white and red primary content, lower-contrast gray graph lines and labels). Layouts: standard body, text gauge, large image.

Since watchOS 10, the system may show rectangular layouts in the Smart Stack (`WidgetFamily.accessoryRectangular`). Optimize by supplying background color or content that informs or aids recognition, using intents to specify relevance, and creating a Smart Stack-optimized custom layout.

|Content|40mm|41mm|44mm|45mm/49mm|
|---|---|---|---|---|
|Large image with title|150x47|159x50|171x54|178.5x56|
|Large image without title|162x69|171.5x73|184x78|193x82|
|Standard body|12x12|12.5x12.5|13.5x13.5|14.5x14.5|
|Text gauge|12x12|12.5x12.5|13.5x13.5|14.5x14.5|

Both large-image layouts automatically get a 4 pt corner radius.

Default SwiftUI text: Rounded, Medium; 16.5 pt (40mm), 17.5 (41mm), 18 (44mm), 19.5 (45mm/49mm).

## Legacy templates

In each stack measurement, width is the maximum. Placeholder images use the Simple size (Circular small, Modular small, Extra large).

### Circular small

A small image or a few characters in a face corner (Color). Layouts: ring, simple and stack, each image or text.

|Image|38mm|40mm/42mm|41mm|44mm|45mm/49mm|
|---|---|---|---|---|---|
|Ring|20x20|22x22|23.5x23.5|24x24|26x26|
|Simple|16x16|18x18|19x19|20x20|21.5x21.5|
|Stack|16x7|17x8|18x8.5|19x9|19x9.5|

### Modular small

Two stacked rows of icon and content, a circular graph, or one larger item (Modular face bottom row). Layouts: columns text; ring, simple and stack, each image or text.

|Image|38mm|40mm/42mm|41mm|44mm|45mm/49mm|
|---|---|---|---|---|---|
|Ring|18x18|19x19|20x20|21x21|22.5x22.5|
|Simple|26x26|29x29|30.5x30.5|32x32|34.5x34.5|
|Stack|26x14|29x15|30.5x16|32x17|34.5x18|

### Modular large

Up to three rows of content (Modular face center). Layouts: columns, standard body, table, tall body.

|Content|38mm|40mm/42mm|41mm|44mm|45mm/49mm|
|---|---|---|---|---|---|
|Columns, Standard body, Table|11-32x11|12-37x12|12.5-39x12.5|14-42x14|14.5-44x14.5|

### Extra large

Larger text and images (X-Large faces). Layouts: ring, simple and stack, each image or text.

|Image|38mm|40mm/42mm|41mm|44mm|45mm/49mm|
|---|---|---|---|---|---|
|Ring|63x63|66.5x66.5|70.5x70.5|73x73|79x79|
|Simple|91x91|101.5x101.5|107.5x107.5|112x112|121x121|
|Stack|78x42|87x45|92x47.5|96x51|103.5x53.5|

## Platform considerations

Not supported in iOS, iPadOS, macOS, tvOS or visionOS.

## Resources

Developer: `WidgetKit`, `WidgetRenderingMode`, `WidgetFamily.accessoryRectangular`, `placeholder(in:)`, `CLKComplicationDataSource` (earlier watchOS).

Source: [Complications](https://developer.apple.com/design/human-interface-guidelines/complications), captured 2026-09-12.
