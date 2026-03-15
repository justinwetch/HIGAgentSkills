---
topic: widgets
tier: 3
platforms: [ios, ipados, macos, watchos]
category: components/system
triggers:
  - "widget"
  - "WidgetKit"
  - "home screen widget"
  - "lock screen widget"
  - "Smart Stack"
related:
  - live-activities
  - complications
  - app-clips
---
# Widgets

> Widgets display timely, glanceable content and offer focused interactions in additional contexts beyond your app.

**Platforms:** iOS, iPadOS, macOS, watchOS, visionOS *(not tvOS)*

## Widget Families and Contexts

### System Family

| Size | iPhone | iPad | Mac | visionOS |
|---|---|---|---|---|
| Small | Home Screen, Today View, StandBy, CarPlay | Home Screen, Today View, Lock Screen | Desktop, Notification Center | Horizontal + vertical surfaces |
| Medium | Home Screen, Today View | Home Screen, Today View | Desktop, Notification Center | Horizontal + vertical surfaces |
| Large | Home Screen, Today View | Home Screen, Today View | Desktop, Notification Center | Horizontal + vertical surfaces |
| Extra large | Not supported | Home Screen, Today View | Desktop, Notification Center | Horizontal + vertical surfaces |
| Extra large portrait | Not supported | Not supported | Not supported | Horizontal + vertical surfaces |

### Accessory (small, information-dense)

| Size | iPhone | iPad | Apple Watch |
|---|---|---|---|
| Accessory circular | Lock Screen | Lock Screen | Complications + Smart Stack |
| Accessory corner | Not supported | Not supported | Complications |
| Accessory inline | Lock Screen | Lock Screen | Complications |
| Accessory rectangular | Lock Screen | Lock Screen | Complications + Smart Stack |

### Rendering Modes

| Platform | Full-color | Accented | Vibrant |
|---|---|---|---|
| iPhone | Home Screen, Today View, StandBy, CarPlay | Home Screen, Today View | Lock Screen, StandBy low-light |
| iPad | Home Screen, Today View | Home Screen, Today View | Lock Screen |
| Apple Watch | Smart Stack, complications | Smart Stack, complications | Not supported |
| Mac | Desktop, Notification Center | Not supported | Desktop |
| visionOS | Horizontal/vertical surfaces | Horizontal/vertical surfaces | Not supported |

- **Full-color**: your views unchanged.
- **Accented**: background removed; divides hierarchy into accent + primary groups; tints each.
- **Vibrant**: desaturates; uses pixel brightness/opacity to drive the blur material effect.

## Best Practices

- **Timely, changing content** — static content that never changes loses its Home Screen spot.
- **Quick access to relevant content** — deep link directly; don't replicate just an app icon.
- **Multiple sizes only when each adds genuine value** — expand content thoughtfully, not just to fill space.
- **Balance information density** — sparse looks unnecessary; too dense is not glanceable. Avoid very small font sizes (min 11 pt).
- **Brand elements yes, brand overload no** — small logo in top-right if needed; never use a full logo when your content already makes the widget recognizable.
- **Don't mirror widget appearance inside your app** — an element that looks like a widget but doesn't behave as one confuses people.
- **Signal unauthenticated state** — e.g., "Sign in to view reservations."
- **Update frequency**: system limits updates. Use system functionality to refresh dates/times (preserve update budget). Show last-updated time if updates lag behind user checks.
- **Animate content updates** — standard/custom animations ≤2 seconds.

### Interactivity

- Tap/click → launches app. Interactive elements (buttons, toggles) are also supported.
- **Deep link to the right location** — don't make people navigate after opening.
- **Keep interaction simple** — inline widgets: one tap target only. Avoid app-like dense layouts.

### Margins and Padding

- **Standard margin**: 16 pt for most widgets; 11 pt for tight groupings (graphics, buttons, background shapes).
- Smaller margins apply on Mac desktop/Lock Screen and StandBy.
- **Corner radius**: use SwiftUI container to match widget corner radius.
- **Text**: use system font + text styles + SF Symbols. Custom fonts: used sparingly; system font for small text.

### Color

- **Color enhances but doesn't compete** with content.
- **Convey meaning via text + iconography, not color alone** — tinted/clear appearances desaturate.
- **Full-color images**: consider carefully in tinted/clear appearances; may feel out of place. Reserve for media content (album art etc.); use smaller than the full widget size.

## Rendering Mode Implementation

### Accented
Group views into accent and primary groups. System tints primary white; on Apple Watch, accented = face color.

### Vibrant
- Fully transparent pixels → raw background material.
- Brighter gray = more contrast. Darker gray = less contrast.
- Render text/numbers/images at full opacity. Use white/light gray for primary, darker gray for secondary.

## Previews and Placeholders

- **Realistic gallery preview** — use real or convincing simulated data; show what the widget actually does at each size.
- **Effective placeholder** — combine static UI with semi-opaque shapes (rectangles for text, circles/squares for images).
- **Widget description**: start with an action verb (e.g., "See the current weather…"). Don't include "This widget shows…" or "Use this widget to…".
- **Group sizes together** — single description for all sizes; show them together in the gallery.
- **Consider coloring the Add button** to reinforce your brand.

## Platform Considerations

### iOS, iPadOS

- **Lock Screen widgets** follow complication design principles. Design them in tandem with complications — often reusable.
- Three Lock Screen shapes: inline text (above clock), circular, rectangular (below clock).
- **Always-On display (iPhone)** — use gray levels with sufficient contrast; verify content legibility in reduced luminance.
- **Offer Live Activities** for real-time updates — widgets don't support real-time data.

#### StandBy and CarPlay

- StandBy: two small widgets side-by-side, scaled up. Use large glanceable text; avoid rich images/color to convey meaning.
- Don't use background colors in StandBy — blend with black background.
- Low-light StandBy: system applies monochromatic red tint.

### visionOS

Widgets are 3D objects placed on real-world surfaces. Persist across sessions in the placed location. Real-world scale.

**Proximity thresholds:**
- **Simplified** (far away): fewer details, larger type, no interactive elements.
- **Default** (nearby): full details, smaller type, interactivity enabled.
- Maintain shared layout elements across thresholds for continuity.

**Mounting styles:**
- **Elevated** (default): slightly tilted back on horizontal surfaces; flush on vertical (like a picture frame). Works for both orientations.
- **Recessed**: only vertical surfaces. Content set back into wall for a cutout illusion. Ideal for ambient/immersive content.

**Treatment styles:**
- **Paper**: print-like, solid, responds to ambient lighting (brightens/darkens). Best for media, physical-feeling content (e.g., album art on a wall).
- **Glass**: foreground elements stay bright regardless of ambient light; background adapts. Best for information-rich content (e.g., news headlines sharp over soft background).

**Sizing**: widgets scale 75–125%. Use print design principles (clear hierarchy, strong typography). Include high-resolution assets.

### watchOS

- **Colorful background** for Smart Stack widgets — default is black. Use color to convey meaning (e.g., red/green for Stocks).
- **Relevancy info** — location-based or action-based (e.g., workout) helps the system surface your widget when it's most useful.

## Specifications

### iOS Widget Sizes (pt)

| Screen (portrait, pt) | Small | Medium | Large | Circular | Rectangular | Inline |
|---|---|---|---|---|---|---|
| 430×932 | 170×170 | 364×170 | 364×382 | 76×76 | 172×76 | 257×26 |
| 393×852 | 158×158 | 338×158 | 338×354 | 72×72 | 160×72 | 234×26 |
| 390×844 | 158×158 | 338×158 | 338×354 | 72×72 | 160×72 | 234×26 |
| 375×812 | 155×155 | 329×155 | 329×345 | 72×72 | 157×72 | 225×26 |
| 375×667 | 148×148 | 321×148 | 321×324 | 68×68 | 153×68 | 225×26 |

*(See full table in HIG for all screen sizes down to 320×568.)*

### visionOS Widget Sizes

| Size | Points | Real-world (at 100%) |
|---|---|---|
| Small | 158×158 | 268×268 mm |
| Medium | 338×158 | 574×268 mm |
| Large | 338×354 | 574×600 mm |
| Extra large | 450×338 | 763×574 mm |
| Extra large portrait | 338×450 | 574×763 mm |

### watchOS Smart Stack Widget Sizes

| Watch size | Size (pt) |
|---|---|
| 40mm | 152×69.5 |
| 41mm | 165×72.5 |
| 44mm | 173×76.5 |
| 45mm | 184×80.5 |
| 49mm | 191×81.5 |
