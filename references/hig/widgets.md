---
topic: widgets
tier: 3
platforms: [ios, ipados, macos, watchos, visionos]
category: components/system
triggers:
  - "widget"
  - "WidgetKit"
  - "home screen widget"
  - "lock screen widget"
  - "Smart Stack"
  - "CarPlay widget"
  - "StandBy"
  - "rendering mode"
  - "accented"
  - "vibrant"
  - "WidgetTexture"
  - "RelevanceKit"
related:
  - live-activities
  - complications
  - layout
---

# Widgets

A widget shows timely, glanceable content and focused interactions from an app or game in system contexts outside it.

## Anatomy

WidgetKit supplies defaults per size and context, but consider a custom design for each context.

### System family widgets

May include interactive elements.

|Size|iPhone|iPad|Mac|Apple Vision Pro (horizontal and vertical surfaces)|
|---|---|---|---|---|
|Small|Home Screen, Today View, StandBy, CarPlay|Home Screen, Today View, Lock Screen|Desktop, Notification Center|Yes|
|Medium, Large|Home Screen, Today View|Home Screen, Today View|Desktop, Notification Center|Yes|
|Extra large|Not supported|Home Screen, Today View|Desktop, Notification Center|Yes|
|Extra large portrait|Not supported|Not supported|Not supported|Yes|

### Accessory widgets

Very limited information.

|Size|iPhone, iPad|Apple Watch|
|---|---|---|
|Circular|Lock Screen|Complications, Smart Stack|
|Corner|Not supported|Complications|
|Inline|Lock Screen|Complications|
|Rectangular|Lock Screen|Complications, Smart Stack|

### Appearances

Per location, device and customization, the system may render a widget and its full-color images, symbols and glyphs tinted or clear.

- **Home Screen (iPhone, iPad):** light or dark (full-color), clear (desaturated, translucent, highlights, Liquid Glass) or tinted (desaturated, then the person's tint).
- **StandBy:** scaled up, background removed; red monochrome below an ambient-light threshold.

|Platform|Full-color|Accented|Vibrant|
|---|---|---|---|
|iPhone|Home Screen, Today view, StandBy and CarPlay (background removed)|Home Screen, Today view|Lock Screen, StandBy in low light|
|iPad|Home Screen, Today view|Home Screen, Today view|Lock Screen|
|Apple Watch|Smart Stack, complications|Smart Stack, complications|Not supported|
|Mac|Desktop, Notification Center|Not supported|Desktop|
|Apple Vision Pro|Surfaces|Surfaces|Not supported|

## Best practices

- **Choose simple ideas tied to your app's main purpose**, with timely content and relevant functionality.
- **Aim for quick access to wanted content**: meaningful content, useful actions, deep links. Replicating the app icon adds little value.
- **Prefer dynamic information that changes through the day.**
- **Look for chances to surprise and delight**, such as birthday or holiday treatments.
- **Offer multiple sizes when that adds value.** Small typically shows one piece of information; larger sizes add information and actions. Avoid expanding smaller content to fill space. One widget in the best size matters more than all sizes.
- **Balance density**: essentials at a glance, details on a longer look. If too dense, consider a larger size or graphics instead of text.
- **Show only information tied to the widget's main purpose.**
- **Use brand colors, typefaces and glyphs thoughtfully**, without overpowering information or looking out of place; people then seldom need your logo or app icon. If a logo helps (e.g., multi-source content), a small one top-right is sufficient.
- **Choose between automatic content and people customizing it.**
- **Avoid mirroring your widget's appearance in your app**; a widget-like element that doesn't behave like one confuses people.
- **Say when signing in adds value** ("Sign in to view reservations").

### Updating widget content

Widgets refresh periodically, not in real time; the system may adjust update limits.

- **Keep it up to date**, matching frequency to how often data changes and when people need it. If people check more often than you can update, consider showing the last-update time.
- **Let the system refresh dates and times**, preserving update opportunities. Show content quickly; don't hide stale data behind placeholders.
- **Animate data updates.** Many SwiftUI views do by default; use standard or custom animations up to 2 seconds long.

### Adding interactivity

Tapping or clicking a widget launches its app, except on buttons and toggles, which act in place.

- **Keep functionality simple and relevant; reserve complexity for your app.**
- **Open your app at the right location**, deep linking to related details and actions.
- **Stay glanceable and uncluttered.** Multiple targets (SwiftUI links, buttons, toggles) can make sense, but avoid app-like layouts. Size targets to prevent unintended interactions. Inline accessory widgets offer only one tap target.

### Choosing margins and padding

iOS resizes large-device designs for small devices; iPadOS renders widgets large, then scales down. Use the Specifications values; build in SwiftUI.

- **In general, use standard margins**: 16 pt for most widgets; 11 pt can work for tighter groupings of graphics, buttons or background shapes. Mac desktop and Lock Screen (including StandBy) widgets use smaller margins. See `padding(_:_:)`.
- **Match content corner radius to the widget's** with `ContainerRelativeShape`.

### Displaying text in widgets

- **Prefer the system font, text styles and SF Symbols.** Use custom fonts sparingly and keep them glanceable; a custom font for large text with SF Pro for smaller text often works well.
- **Avoid very small fonts.** In general, use 11 pt or larger.
- **Avoid rasterizing text.** Always use text elements and styles so text scales and VoiceOver can read it.

In iOS, iPadOS and visionOS, widgets support Dynamic Type Large to AX5 via `Font` (system) or `custom(_:size:)` (custom font).

### Using color

- **Use color without competing with content.** The asset catalog can set colors for the system-generated editing-mode interface.
- **Convey meaning with text and iconography, not color alone.** Widgets can be monochromatic, and watchOS may invert colors per watch face.
- **Use full-color images judiciously.** Tinted and clear appearances desaturate them by default; kept full-color, they draw attention and can look out of place. Consider reserving it for media such as album art, smaller than the widget.

## Rendering modes

`WidgetRenderingMode` values.

### Full-color

`fullColor`: view colors unchanged.

**Support light and dark appearances.** Prefer light backgrounds in light and dark in dark; consider semantic system colors or asset-catalog color variants.

### Accented

`accented`: system family widgets and Apple Watch accessory widgets. The system replaces the background with a tint effect (tinted) or Liquid Glass (clear) and gives each view group a solid color.

**Group components into accented and primary groups** with `widgetAccentable(_:)`. On iPhone, iPad and Mac (though Mac is also listed as not supporting accented), the system tints both white; on Apple Watch, primary white and accented the watch face color.

### Vibrant

`vibrant`: monochromatic, no widget tint (people may tint the Lock Screen). The system desaturates text, images and gauges and colors them for the Lock Screen background or a macOS desktop.

- **Offer enough contrast.** Pixel opacity sets blurred-material strength (fully transparent passes it through); brighter grays give more contrast.
- **Optimize assets for vibrancy.** Render images, numbers and text at full opacity: white or light gray for prominent content, darker grays for secondary. Check image contrast in grayscale; use opaque grays, not opacities of white.

## Previews and placeholders

- **Make the gallery preview realistic** for each type or size. If real data loads slowly, use realistic simulated data.
- **Design recognizable loading placeholders**: static components plus semi-opaque shapes (varying-width rectangles for text, circles or squares for glyphs and images).
- **Keep the description succinct.** Begin with an action verb ("See the current weather conditions and forecast for a location"); avoid "This widget shows…", "Use this widget to…" or "Add this widget". Use approachable language and sentence-style capitalization.
- **Group your sizes together under a single description.**
- **Consider coloring the gallery's Add button** with your brand color.

## Platform considerations

No additional considerations for macOS. Not supported in tvOS.

### iOS, iPadOS

Lock Screen widgets also follow Complications principles; consider designing both in tandem. Provide useful information, not just an app launcher. Inline widgets appear above the clock; circular and rectangular below.

- **Support the iPhone Always-On display.** Lock Screen widgets render at reduced luminance; use gray levels with enough contrast to stay legible.
- **Consider Live Activities (`ActivityKit`) for real-time updates** of a time-limited task or event; sharing frameworks and design, they can be developed in tandem with widgets.

#### StandBy and CarPlay

StandBy shows two small system family widgets side by side, scaled to fill the Lock Screen. CarPlay uses the same small widget, background removed, scaled to its Widgets grid, so supporting StandBy supports CarPlay. Glanceable information and large text matter especially in CarPlay.

- **Limit rich images or color to convey meaning in StandBy.** Scale up and rearrange text for distance viewing. Don't use background colors; blend with the black background.

### visionOS

Widgets are framed 3D objects at real-world scale that persist where placed, even across restarts. They're full-color by default, accented when people apply system palette tints. People can customize elevated widgets' frame width and widget-specific options. There's no systemwide light or dark appearance; a widget can offer its own.

- **Adapt design and content to people's rooms** from the start.
- **Test all system color palettes and lighting conditions** for consistent tone, contrast and legibility, including any elements you exclude from tinting.

#### Thresholds and sizes

Widgets can adapt to proximity at two thresholds (`LevelOfDetail`): `simplified` at a distance, `default` nearby.

- **Design a layout for each threshold.** At a distance, show fewer details in larger type, without buttons, toggles or other interactive elements; nearby, more detail in smaller type. Keep shared elements across both.
- **Offer sizes that fit people's surroundings** (small for a desk; extra large for artwork or photography).
- **Keep content legible across distances and at 75-125 percent scale** (people can resize): clear hierarchy, strong typography, high-resolution assets.

#### Mounting styles

- **Choose the mounting style that fits your content.** Elevated (`WidgetMountingStyle.elevated`; default, works on both surfaces; tilted back with a soft shadow on horizontal, flush on vertical) suits content that should stand out (reminders, media, glanceable data). Recessed (`recessed`; vertical only, set into the surface like a cutout) suits immersive or ambient content (weather, editorial). You can opt out of a style per widget.
- Declare supported styles with `supportedMountingStyles(_:)` on `WidgetConfiguration`; it applies to every widget in the configuration, so use separate configurations for differing support.
- **Test elevated designs at each system frame width.** You can't adapt layout to it; keep it balanced.

#### Treatment styles

Treatments (`WidgetTexture`):
- **Paper** (`paper`): the whole widget darkens or lightens with ambient light. **Choose it for a print-like, real-object look.**
- **Glass** (`glass`): foreground stays full-color regardless of ambient light; you decide which parts adapt. **Choose it for information-rich widgets.**

### watchOS

- **Consider a meaningful background color** instead of the default black in the Smart Stack (Stocks: red falling, green rising).
- **Provide relevance information** so the system shows or elevates your widget in the Smart Stack; it can be location-based or tied to system actions like a workout (`RelevanceKit`).

## Specifications

### iOS dimensions (pt)

|Screen (portrait)|Small|Medium|Large|Circular|Rectangular|Inline|
|---|---|---|---|---|---|---|
|430x932, 428x926|170x170|364x170|364x382|76x76|172x76|257x26|
|414x896|169x169|360x169|360x379|76x76|160x72|248x26|
|414x736|159x159|348x157|348x357|76x76|170x76|248x26|
|393x852, 390x844|158x158|338x158|338x354|72x72|160x72|234x26|
|375x812, 360x780|155x155|329x155|329x345|72x72|157x72|225x26|
|375x667|148x148|321x148|321x324|68x68|153x68|225x26|
|320x568|141x141|292x141|292x311|N/A|N/A|N/A|

### iPadOS dimensions (pt, canvas / device)

|Screen (portrait)|Small|Medium|Large|Extra large|
|---|---|---|---|---|
|768x1024, 744x1133|141x141 / 120x120|305.5x141 / 260x120|305.5x305.5 / 260x260|634.5x305.5 / 540x260|
|810x1080|146x146 / 124x124|320.5x146 / 272x124|320.5x320.5 / 272x272|669x320.5 / 568x272|
|820x1180, 834x1194|155x155 / 136x136|342x155 / 300x136|342x342 / 300x300|715.5x342 / 628x300|
|834x1112|150x150 / 132x132|327.5x150 / 288x132|327.5x327.5 / 288x288|682x327.5 / 600x288|
|1024x1366|170x170 / 160x160|378.5x170 / 356x160|378.5x378.5 / 356x356|795x378.5 / 748x356|
|954x1373*, 970x1389*|162x162|350x162|350x350|726x350|
|1192x1590*|188x188|412x188|412x412|860x412|

*Display Zoom set to More Space; canvas and device sizes are equal.

### visionOS dimensions

|Widget|pt|mm (at 100% scale)|
|---|---|---|
|Small|158x158|268x268|
|Medium|338x158|574x268|
|Large|338x354|574x600|
|Extra large|450x338|763x574|
|Extra large portrait|338x450|574x763|

### watchOS Smart Stack widget (pt)

|40mm|41mm|44mm|45mm|49mm|
|---|---|---|---|---|
|152x69.5|165x72.5|173x76.5|184x80.5|191x81.5|

## Resources

Developer: `WidgetKit`.

Source: [Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets), captured 2026-09-12.
