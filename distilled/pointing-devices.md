---
topic: pointing-devices
tier: 3
platforms: [ios, ipados, macos]
category: patterns/interaction
triggers:
  - "pointer"
  - "mouse"
  - "trackpad"
  - "cursor"
  - "hover"
  - "pointer interaction"
  - "iPadOS pointer"
related:
  - gestures
  - focus-and-selection
  - drag-and-drop
---
# Pointing Devices

> Pointing devices (trackpad, mouse) offer precision navigation and interaction, complementing touch, eyes, and gestures.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS, watchOS)*

On Mac: primary alongside keyboard. On iPad and visionOS: additional input, not a replacement for touch/eyes/gestures.

## Best Practices

- **Consistent gesture behavior** — gestures should work the same across apps (e.g., "swipe between pages" always navigates pages).
- **Don't redefine systemwide trackpad gestures** — even in games. People expect Dock/Mission Control gestures to work everywhere; they can also customize those gestures.
- **Consistent cross-input experience** — pointer, touch, eyes, and keyboard should all work fluently; people switch between them without needing to re-learn.
- **Hover to reveal/hide auto-minimized controls** — e.g., Safari's minimized toolbar reappears on pointer hover.
- **Consistent modifier key behavior** — Option + drag = duplicate, Shift + drag-resize = constrain aspect ratio — these should work the same whether touching or using the pointer.

## Platform Considerations

### iPadOS — Pointer System

The iPadOS pointer adapts automatically to context and provides rich visual feedback. Default shape: circle. Over text: I-beam. Doesn't replace touch.

**Content effects** (pointer-triggered visual responses):

| Effect | What it does | System default targets |
|---|---|---|
| Highlight | Translucent rounded-rect background + gentle parallax | Bar buttons, tab bars, segmented controls, edit menus |
| Lift | Scales up + shadow below + specular highlight; pointer fades beneath element | App icons, Control Center buttons |
| Hover | Custom scale/tint/shadow; pointer shape unchanged | Large elements (custom) |

**Usage rules:**
- Highlight → small elements with transparent background
- Lift → small elements with opaque background
- Hover → large elements; customize scale, tint, shadow

**Magnetism** — iPadOS pulls the pointer toward interactive elements as it approaches or flicks toward them. Applied by default to lift and highlight elements, not hover (hover doesn't transform pointer shape; adding magnetism would feel jarring).

**Padding for hit regions:**
- Elements with a bezel: ~12pt padding.
- Elements without a bezel: ~24pt padding around visible edges.
- Create contiguous hit regions for adjacent bar buttons — gaps cause jarring pointer resets.

**Custom pointer guidance:**
- Specify corner radius if a non-standard element receives the lift effect (so the pointer animates to the correct shape).
- Consistent effects within your app — all drawing areas should share the same pointer behavior.
- No decorative/gratuitous effects — people notice changes; they expect them to be useful.
- Custom pointer shapes: simple and contextually meaningful; people should understand them instantly.
- Consider custom annotations (e.g., X/Y coordinates on hover in a graphing area).
- No instructional text attached to the pointer — it makes apps feel complicated.
- Hover with scale: only for elements with space around them. Scale does not work for table rows (can't expand without overlapping). No shadow without scale (shadow implies elevation, which looks wrong on an unscaled element).

**Pointer accessories** — secondary visual indicators (e.g., small arrows near a resizable edge). Should be simple images. Use transitions to signal state changes (e.g., `plus` → `circle.slash` when an add action becomes unavailable).

### macOS — Gestures & Mouse/Trackpad

People can customize mouse and trackpad interactions. Key gestures:

| Gesture | Mouse | Trackpad |
|---|---|---|
| Primary click | ✓ | ✓ |
| Secondary click | ✓ | ✓ |
| Scrolling | ✓ | ✓ |
| Smart zoom | ✓ | ✓ |
| Swipe between pages | ✓ | ✓ |
| Swipe between full-screen apps | ✓ | ✓ |
| Mission Control | ✓ | ✓ |
| Lookup/data detectors | — | ✓ |
| Force click | — | ✓ |
| Zoom (pinch) | — | ✓ |
| Rotate | — | ✓ |
| Notification Center | — | ✓ |
| App Exposé | — | ✓ |
| Launchpad | — | ✓ |
| Show Desktop | — | ✓ |

**macOS Pointer Styles (AppKit):**

| Pointer | Name | AppKit API |
|---|---|---|
| → | Arrow | `arrow` |
| ✊ | Closed hand (dragging content) | `closedHand` |
| ☞ | Contextual menu | `contextualMenu` |
| + | Crosshair | `crosshair` |
| ✕ disappear | Disappearing item | `disappearingItem` |
| + badge | Drag copy | `dragCopy` |
| ↗ badge | Drag link | `dragLink` |
| I | Horizontal I-beam | `iBeam` |
| ☜ | Open hand | `openHand` |
| ⊘ | Operation not allowed | `operationNotAllowed` |
| 👆 | Pointing hand | `pointingHand` |
| Resize arrows (×6) | Resize down/left/left-right/right/up/up-down | `resizeDown` etc. |
| I (vertical) | Vertical I-beam | `iBeamCursorForVerticalLayout` |

### visionOS

External pointing device or keyboard can be attached alongside eyes/hands. System handles focus integration automatically:
- Eyes target → then pointer moves → system brings focus to the element under the pointer. No app code needed.
- Eye gaze determines pointer context: when eyes shift windows, pointer context transitions immediately.
- Pointer hides while gesturing (e.g., trackpad gesture); reappears at the location the person is looking at when they move it.
