---
topic: game-controls
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: patterns/interaction
triggers:
  - "game controller"
  - "MFi controller"
  - "gamepad"
  - "thumbstick"
  - "GCController"
  - "GCRequiresControllerUserInteraction"
  - "GCControllerElement"
related:
  - designing-for-games
  - gestures
  - keyboards
  - playing-haptics
---
# Game Controls

> Games on Apple platforms support touch, physical controllers, keyboards, and platform-default input, and should ideally support all available input methods.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS *(not watchOS)*

Always support the platform's default input method — not every player has a physical controller.

## Touch Controls (iOS, iPadOS)

Use the TouchController framework for virtual controls overlaid on game content.

- **Use virtual controls when they make sense** — helpful for many-action games or movement control. For direct interaction games, prefer tapping objects directly instead of adding virtual buttons.
- **Placement**: below safe areas and Home indicator/Dynamic Island. Frequently used buttons near thumbs (avoid movement/camera thumb regions). Secondary controls (menus) at top.
- **Size**: Frequently used controls ≥ 44×44pt. Less important controls ≥ 28×28pt.
- **Always include visual press states** — even when finger covers the button. Combine with sound and haptics.
- **Symbols, not abstract shapes or controller button names (A, X, R1)** — artwork should communicate the action visually.
- **Show/hide controls dynamically** — hide when action is unavailable; reduce clutter.
- **Combine related actions** — use double tap and touch-and-hold for variations of an action; combine walk/sprint into one control.
- **Movement**: left side of screen (virtual thumbstick that follows thumb placement). **Camera**: right side, direct touch to pan. Make both control areas as large as possible.

## Physical Controllers

- **Always have a fallback** — not everyone has a controller. Every platform has a native default input method.
- **Requirement badge**: tvOS and visionOS can require a controller; App Store shows "Game Controller Required" badge. Gracefully prompt to connect if required.
- **Auto-detect connected controllers** — don't require manual setup. Use GameController framework.
- **Match onscreen UI to the connected controller's labels/colors** — the framework assigns generic names; use the actual connected controller's labeling.
- **Standard controller UI button mapping:**

| Button | Expected UI behavior |
|---|---|
| A | Activates a control |
| B | Cancels / returns to previous screen |
| X | — |
| Y | — |
| Left shoulder | Navigate left to a different screen/section |
| Right shoulder | Navigate right to a different screen/section |
| Left trigger | -- |
| Right trigger | -- |
| Left/right thumbstick | Move selection |
| Directional pad | Move selection |
| Home/logo | Reserved for system controls |
| Menu | Open game settings / pause gameplay |

- **Support multiple connected controllers** — use appropriate labels per player in multiplayer.
- **Use SF Symbols for controller elements** — Game Controller framework provides SF Symbols for most buttons; avoids text descriptions people may not know.

## Keyboards

- **Single-key commands preferred** — faster while simultaneously using mouse/trackpad. Use first letters (I = Inventory, M = Map), Space for main action.
- **Test on Apple keyboards** — remap Control ^ to Command ⌘ if needed (⌘ is next to Space; easier during WASD gameplay).
- **Physically proximate key bindings** — related actions on neighboring keys (WASD movement → nearby keys for common related actions; number keys for inventory categories).
- **Let players customize key bindings** — defaults should be reasonable, but customization is expected.

## Platform Considerations

### visionOS

- Support spatial controllers (e.g., PlayStation VR2 Sense). Match to hand input:
  - Look at object → left/right trigger = indirect interaction.
  - Reach out → left/right trigger = direct interaction.
