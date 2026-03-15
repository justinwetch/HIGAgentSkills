---
topic: focus-and-selection
tier: 3
platforms: [ipados, macos, tvos]
category: patterns/interaction
triggers:
  - "focus"
  - "focus ring"
  - "selection"
  - "keyboard navigation"
  - "directional focus"
related:
  - remotes
  - keyboards
  - designing-for-tvos
---
# Focus and Selection

> Focus lets people using remotes, game controllers, or keyboards navigate to and select interface elements without touching the screen.

**Platforms:** iPadOS, macOS, tvOS, visionOS *(not iOS, watchOS)*

In many cases, bringing focus to an item also selects it — except when auto-selection would cause a distracting context shift (e.g., opening a new view). In tvOS, selection requires an explicit separate gesture from focus.

## Best Practices

- **Use system-provided focus effects** — precisely tuned, fluid, lifelike. Custom focus effects only when absolutely necessary.
- **Don't change focus without user interaction** — unprompted focus changes force people to hunt for the new focused item. Exception: if a focused item disappears while navigating with discrete directional input (keyboard/remote), move focus to the nearest remaining item. If not navigating this way, simply hide the focus indicator.
- **Be consistent with platform focus conventions** (see per-platform guidance below).
- **Visual focus appearance**:
  - **Focus ring** (halo): best for text fields, search fields, images within cells.
  - **Highlighted row**: best for lists and collections.
- In lists/collections: focused = white text + accent-color background; unfocused = standard text + gray background.

## iPadOS

Uses **focus groups** (sidebar, grid, list, etc.), with two keyboard interactions:
- **Tab key**: moves focus between focus groups.
- **Arrow keys**: moves focus within a focus group (directional, like tvOS).

**Focus effects**:
- **Halo (focus ring)**: customizable outline around the component. Can refine shape (Bézier paths, rounded corners) and reposition if clipped/badged.
- **Highlighted appearance**: accent-colored text, indicates focus within collection cells.

**Custom view focus order**: by default, focus moves in reading order (leading→trailing, top→bottom). Override container as a single focus group if you need column-first navigation.

**Priority within focus groups**: set a *primary item* (higher priority) to auto-receive focus when the group is entered.

## tvOS

Uses **directional focus** — arrow keys, Siri Remote swipe, or game controller navigate all onscreen components.

- **Full-screen experiences**: gestures affect content directly, not focus. No focus indicator shown.
- **No pointer** — focus model only. Pointer only in very specific gameplay contexts (make it large and integrated).
- **5 focus states** — design for all of them; focused items often scale up, so provide larger assets:

| State | Description |
|---|---|
| Unfocused | Less prominent than focused items |
| Focused | Elevated to foreground with illumination + animation |
| Highlighted | Instant visual feedback on selection (e.g., button briefly inverts colors) |
| Selected | Action completed / toggle active (e.g., heart-button filled) |
| Unavailable | Item is inactive / disabled |

## visionOS

Uses same focus system as iPadOS and tvOS for connected input devices (keyboard, game controller).

> **Note**: Looking at an object uses the *hover effect*, not the focus system. Hover ≠ focus.

## macOS

Full Keyboard Access mode lets people reach every control via keyboard. Only need to support focus for content elements (listed/search fields, list items) — not for controls (buttons, sliders, toggles); the system handles those.
