---
topic: live-activities
tier: 3
platforms: [ios, ipados, macos, watchos]
category: components/system
triggers:
  - "live activity"
  - "Dynamic Island"
  - "ActivityKit"
  - "realtime update"
  - "ActivityFamily.small"
  - "activitySystemActionForegroundColor(_:)"
  - "ContainerRelativeShape"
related:
  - notifications
  - widgets
---
# Live Activities

> Live Activities let people track an in-progress activity, event, or task at a glance across multiple system locations.

**Platforms:** iOS, iPadOS, macOS, watchOS. Not supported in tvOS or visionOS.

| Location | Appears on |
|---|---|
| iPhone, iPad | Lock Screen, Home Screen, Dynamic Island, StandBy |
| Mac | Menu bar |
| Apple Watch | Smart Stack |
| CarPlay | CarPlay Dashboard |

## Presentations

| Presentation | When used | Notes |
|---|---|---|
| **Compact** | One Live Activity active → Dynamic Island | Leading + trailing elements flanking TrueDepth camera |
| **Minimal** | Multiple Live Activities → Dynamic Island | One attached, one detached (circular or oval). Compact = basis for Apple Watch + CarPlay |
| **Expanded** | Touch and hold on compact or minimal | Enlarged version of compact/minimal |
| **Lock Screen** | Bottom of Lock Screen; banner on non-Dynamic Island devices | Similar layout to expanded |
| **StandBy** | Minimal presentation in StandBy; tap → Lock Screen 2×; if custom bg, system extends full-screen | Real-world scale |

## Best Practices

Required support: Compact, Minimal, Expanded, and Lock Screen. StandBy derives/scales from these presentations.

- **Defined beginning and end** — best for tasks ≤8 hours.
- **Only task-related information** — no ads or promotions.
- **Sensitive data**: show innocuous summary in the LA; let people tap into your app for details. Consider redacted views.
- **Match your app's visual style** in both light and dark appearances.
- **Logo marks without a container** — don't use the full app icon.
- **Don't draw attention to the Dynamic Island from within your app** — other items appear there when your app is open.
- **Large, heavier-weight text** (≥medium weight) — use small text sparingly.

## Layout Guidelines

- **Adapt to all screen sizes and presentations** — use spec values as a guide; content may scale or change dimensions.
- **Efficient use of space** — only use what's needed for content; adjust element size/placement to fit together well.
- **Standard margins; concentric placement** — match corner radii of inner rounded shapes to the outer LA shape by subtracting margin from outer radius (use SwiftUI container). Content snug with margin concentric to outer edge.
- **Don't draw content to the Dynamic Island edge** — use inset container shapes or thick lines to separate content blocks.
- **Dynamic height** on Lock Screen / expanded — reduce height when less data; expand when more becomes available.

### Colors

- **Compact, minimal, expanded**: no custom backgrounds — black opaque. Use bold, high-contrast colors for text/objects.
- **Lock Screen**: custom background color allowed. Ensure sufficient contrast especially for Always-On reduced luminance.
- **Key line color** (Dynamic Island border in dark mode) — match to your content colors.

### Animations

- Standard or custom animations, **max 2 seconds**. No animations on Always-On low-luminance display.
- **Reinforce the information** — use content-replace, scale, opacity, and movement transitions.
- **Animate layout changes** — animate existing elements to new positions; don't remove and re-add.
- **Avoid element overlaps** — fade out elements that would collide, then fade back at new positions.

## Interactivity

- **Tapping opens the app at the right location** — deep link directly. Both leading and trailing compact elements must link to the same screen.
- **Simple, direct actions only** — buttons/toggles for essential, directly related functions (music playback, workout pause, microphone record). Prefer ≤1 interactive element.

## Starting, Updating, and Ending

- **Start at expected times** — post food-order, rideshare request, match start. Unexpected LA starts feel intrusive. Provide in-app controls to turn off.
- **Offer an App Shortcut** to start your Live Activity (e.g., for Action button).
- **Update only when content changes** — don't push same-state updates.
- **Alert sparingly** — alerts play notification sound, light screen, show expanded. Don't duplicate alerts with push notifications for the same update.
- **Single LA for multiple events** — rotate through events dynamically rather than creating separate LAs.
- **End immediately when the task ends**:
  - Dynamic Island + CarPlay: immediately removed.
  - Lock Screen, Mac menu bar, watchOS Smart Stack: remain up to 4 hours.
  - Set a **custom dismissal time** proportional to the task (most cases: 15–30 min).

## Compact Presentation Design

- **Design leading + trailing as one visual unit** — consistent color/typography. Keep each element snug against the TrueDepth camera; balanced proportion between leading and trailing.
- **Minimal presentation**: show updated information (e.g., remaining time) not just a logo.
- **Expanded**: elements expand predictably from compact/minimal positions. Wrap content tightly around TrueDepth camera.

## Lock Screen Presentation Design

- **Don't replicate notification layouts** — unique Live Activity layout.
- **Standard margin**: 14 pt. Tighter OK for graphics/buttons; never crowd edges.
- Verify **dismiss button** auto-generated color looks right; adjust if needed.
- Support both dark and light appearances + Always-On luminance reduction.

## StandBy Design

- Make assets look great at 2× scale. Consider custom layout using extra space.
- Default background color blends with bezel; also allows slightly larger scale.
- **Standard margins** — content clips without them.
- **Night Mode** (red tint): verify contrast in this mode.

## CarPlay and watchOS Notes

- **macOS**: clicking a menu bar Live Activity launches the source app through iPhone Mirroring.

- **CarPlay**: system auto-combines compact leading + trailing. Interactive elements are deactivated. If beneficial, declare a `supplementalActivityFamily` for a custom layout with larger text.
- **watchOS**: compact leading + trailing are combined to form the Smart Stack view by default. Consider a custom watchOS layout for more info and interactivity. Custom layout also applies to CarPlay — so don't include buttons/toggles if people might use the Live Activity while driving.

## Specifications

### iOS Compact / Expanded Dimensions (pt)

| Screen | Compact leading | Compact trailing | Minimal width range | Expanded height range | Lock Screen height range |
|---|---|---|---|---|---|
| 430×932 | 62.33×36.67 | 62.33×36.67 | 36.67–45 | 408 × 84–160 | 408 × 84–160 |
| 393×852 | 52.33×36.67 | 52.33×36.67 | 36.67–45 | 371 × 84–160 | 371 × 84–160 |

Dynamic Island corner radius: **44 pt**.

### iPadOS Lock Screen Dimensions (pt)

| Screen dimensions (portrait) | Lock Screen height range |
|---|---|
| 1366x1024 | 500x84-160 |
| 1194x834 | 425x84-160 |
| 1012x834 | 425x84-160 |
| 1080x810 | 425x84-160 |
| 1024x768 | 425x84-160 |

### Dynamic Island Width (compact/minimal)

| Device | Width (pt) |
|---|---|
| iPhone 17 Pro Max / Air / 16 Plus / 15 Plus / 14 Pro Max | 250 |
| iPhone 17 Pro / 17 / 16 Pro / 16 / 15 Pro / 15 / 14 Pro | 230 |

### Expanded Width

| Device | Width (pt) |
|---|---|
| iPhone 17 Pro Max / Air / 16 Plus / 15 Plus / 14 Pro Max | 408 |
| iPhone 17 Pro / 17 / 16 Pro / 16 / 15 Pro / 15 / 14 Pro | 371 |

### CarPlay Dimensions (pt)

Smart Display Zoom configurations: Widescreen 1920x720, Portrait 900x1200, Standard 800x480.

| Live Activity size |
|---|
| 240×78 |
| 240×100 |
| 170×78 |

### watchOS (Smart Stack — same as widget)

| Watch | Smart Stack size (pt) |
|---|---|
| 40mm | 152×69.5 |
| 41mm | 165×72.5 |
| 44mm | 173×76.5 |
| 45mm | 184×80.5 |
| 49mm | 191×81.5 |
