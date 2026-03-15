---
topic: buttons
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: components/controls
triggers:
  - "button"
  - "CTA"
  - "call to action"
  - "filled button"
  - "tinted button"
  - "BorderedButton"
related:
  - accessibility
  - icons
  - pull-down-buttons
  - pop-up-buttons
---
# Buttons

> A button initiates an instantaneous action.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

A button combines three attributes: **style** (size/color/shape), **content** (symbol, label, or both), and **role** (semantic meaning). Related components: toggles, pop-up buttons, segmented controls.

## Best Practices

- Minimum hit region: 44×44pt (60×60pt on visionOS).
- Always include a press state for custom buttons.

## Style

- Use a prominent style (accent-colored background) for the most likely action. Limit to 1–2 prominent buttons per view.
- Distinguish preferred actions by style, not size. Buttons of different sizes in proximity look inconsistent.
- If app has colorful content-layer backgrounds, prefer monochromatic button labels over colored ones.

## Content

- Use familiar icons for common actions (e.g. `square.and.arrow.up` for Share).
- Use short text labels when words communicate more clearly than an icon. Start labels with a verb (e.g. "Add to Cart").
- macOS/visionOS: system displays tooltips on hover for icon-only buttons.

## Role

| Role | Meaning | Appearance |
|---|---|---|
| Normal | No specific meaning | Default |
| Primary | Most likely choice; responds to Return key | Accent color |
| Cancel | Cancels current action | Default |
| Destructive | May cause data loss | System red |

- Assign primary to the most likely action. In sheets/alerts, primary + Return auto-dismisses.
- Never assign primary to destructive actions—users may click prominent buttons without reading.

## Platform Considerations

### iOS, iPadOS

- Use in-button activity indicator for non-instant actions. Can show alternate label (e.g. "Checkout" → "Checking out…").

### macOS

**Push buttons** — Standard type. Supports text, symbol, icon, image, or combinations. Can be tinted and act as default.
- Use flexible-height push buttons (`flexiblePush`) only for tall/variable-height content (same corner radius/padding as regular).
- Append trailing ellipsis (…) when button opens another window/view/app.
- Support spring loading on Magic Trackpad (force click to activate without dropping dragged items).

**Square buttons** (gradient buttons) — For view-level actions (add/remove rows). Contain symbols only, not text. Appear within or beneath their associated view.
- Use in views, not window frame/toolbars.
- Prefer SF Symbols. Avoid labels.

**Help buttons** — Circular, question mark. Opens app-specific help.
- Open context-specific help topic when possible, top-level otherwise.
- Max one per window.
- Position: lower corner, opposite dismissal buttons (if present), otherwise lower-left/right.
- Use in views, not window frame.

**Image buttons** — Display image/symbol/icon. Can behave as push, toggle, or pop-up.
- Use in views, not window frame. Include ~10px padding between image and button edges. Avoid system-provided border (`isBordered`).

### visionOS

Three standard shapes: circle (icon-only), roundedRectangle or capsule (text-only), capsule (icon+text).

Four interaction states: idle, hover, pressed, disabled. No custom hover effects supported.

| Shape | Mini (28pt) | Small (32pt) | Regular (44pt) | Large (52pt) | XL (64pt) |
|---|---|---|---|---|---|
| Circular | ✓ | ✓ | ✓ | ✓ | ✓ |
| Capsule (text) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Capsule (text+icon) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Rounded rect | ✓ | ✓ | ✓ | ✓ | ✓ |

- Prefer buttons with visible background shape/fill. On glass windows: thin material. Floating in space: glass material.
- Don't use white background + black text/icons — reserved for toggled state.
- Prefer circular/capsule shapes (corners draw eye away from center).
- Min 60pt center-to-center spacing. Add 4pt padding for buttons ≥60pt.
- Vertical stack: use rounded-rectangle. Horizontal row: use capsule.
- Avoid small/mini buttons in stacks or rows.

### watchOS

- All inline buttons use capsule shape with contrasting material.
- Use toolbar for corner buttons (system applies Liquid Glass).
- Prefer full-width buttons for primary actions.
- Two buttons sharing horizontal space: same height, use images or short text.
