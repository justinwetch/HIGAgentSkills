---
topic: windows
tier: 3
platforms: [ipados, macos, visionos]
category: components/navigation
triggers:
  - "window"
  - "WindowGroup"
  - "UIScene"
  - "NSWindow"
  - "resizable window"
  - "OpenWindowAction"
  - "DefaultWindowStyle"
  - "PlainWindowStyle"
  - "VolumetricWindowStyle"
  - "volume"
  - "volumetric window"
related:
  - split-views
  - multitasking
  - layout
---
# Windows

> A window presents UI views and components within visual boundaries that define app content and separate it from the system.

**Platforms:** iPadOS, macOS, visionOS *(not iOS, tvOS, or watchOS)*

Two conceptual types:
- **Primary window** — main navigation, content, and associated actions.
- **Auxiliary window** — a specific task/area; no navigation to other parts of the app; includes a close button.

## Best Practices

- **Fluid adaptation to different sizes** — supports multitasking and multi-window workflows.
- **Choose the right moment to open a new window** — new windows help multitask or preserve context (e.g., Mail opens a compose window alongside the inbox). Don't open new windows excessively; avoid as default behavior.
- **Offer "Open in New Window" as an option** (context menu or File menu) — flexibility without forcing it.
- **No custom window UI** — system windows look and behave as people expect. Custom frames or controls that imperfectly match system look/behavior make the app feel broken.
- **Use "window" in user-facing text** — not "scene" (an implementation term) or any other variant.

## Platform Considerations

### iPadOS

Two presentation modes (user-controlled in Multitasking & Gestures settings):
- **Full screen** — one window fills the screen; app switcher to switch.
- **Windowed** — freely resizable, multiple windows on screen simultaneously; system remembers size/position between sessions.

- **Prevent window controls from overlapping toolbar items** — in windowed mode, window controls appear at the leading edge of the toolbar. Move leading-edge toolbar buttons inward when window controls appear to avoid being hidden.
- **Support pinch to open content in a new window** (optional) — e.g., pinch a Notes item to expand into a new window.

### macOS

**Window states:**
| State | Description |
|---|---|
| Main | Frontmost window; one per app |
| Key (active) | Accepts input; one across all apps at once; usually same as main |
| Inactive | Not in the foreground; appears subdued, no vibrancy |

- Key window: title bar controls use color. Inactive/non-key main windows: controls use gray.
- **Custom windows must update appearance automatically for all three states** — system components do this automatically; custom implementations must handle it manually.
- **No critical information or actions in a bottom bar** — window repositioning often hides the bottom edge. Bottom bars (status bars) should display only a small amount of content-related info. Use an inspector for more data.

### visionOS

**Two window styles:**

**Default windows:**
- Upright plane with unmodifiable *glass* background. Includes close button, window bar, resize controls. Can also include a Share button, tab bar, toolbar, and ornaments.
- `PlainWindowStyle` is similar to the default style but omits the glass background.
- Default size: **1280×720 pt** (placed ~2m in front, giving ~3m apparent width).
- Uses dynamic scale by default (content stays consistently legible regardless of distance).
- **Retain the glass background** — glass adapts dynamically to lighting, uses specular reflections and shadows for depth cues. Removing it makes UI elements less legible and unrelated-looking; an opaque background obscures surroundings and feels heavy.
- **Minimize empty areas** — choose an initial size that suits the content shape (wide for slides, tall for webpages).
- **Set min/max size** — prevents people from making windows unusably small or large.
- **Minimize 3D content depth** — deep 3D content is clipped by the window boundary; use a volume for greater 3D depth.

**Volumes (volumetric windows):**
- Displays 2D or 3D content viewable from any angle. Window controls exist but shift to face the viewer as they move around.
- **Use volumes for rich 3D content** (e.g., game boards); use a window for familiar 2D UI-centric interfaces.
- **2D content in volumes: pin to 3D content using attachments** — perspective shifting as people move can make standalone 2D content appear to change position unexpectedly.
- **Dynamic scaling recommended** (keeps content legible at distance). Exception: fixed scaling for real-world-representative objects.
- **Baseplate glow** (visionOS 2+) — system auto-shows a gentle glow around horizontal "floor" edges when people look at the volume, helping them discern edges and find resize controls. Suppress if content is full-bleed or you use a custom baseplate.
- **Ornaments in volumes** — visionOS 2+: volumes can include an ornament. Use anchor positions like `topBack` or `bottomFront`; avoid same edge as toolbar/tab bar; prefer one additional ornament max.
- **Choose alignment for interaction style** — baseplate parallel to floor for passive content; tilted to match viewer gaze for interactive content (comfortable when reclining).
