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
  - toggles
  - segmented-controls
---

# Buttons

A button initiates an instantaneous action. It communicates through **style** (size, color, shape), **content** (symbol, text or both) and **role** (semantic meaning that can affect appearance). Toggles, pop-up buttons and segmented controls are specialized button-like components.

## Best practices

- Leave enough space around a button to set it apart and make it easy to activate with any input. As a general rule, the hit region is at least 44x44 pt (60x60 pt in visionOS).
- **Always give a custom button a press state**, or it feels unresponsive.

## Style

- **In general, use a prominent style (accent-color background) for the most likely action.** Keep to one or two prominent buttons per view.
- **Distinguish the preferred choice by style, not size.** Same-size buttons read as a set; mixed sizes nearby look inconsistent.
- **Avoid label colors similar to the content layer.** Over bright, colorful content, prefer the default monochromatic labels.

## Content

- Make each button's purpose clear with a symbol, text or both, as the platform allows. In macOS and visionOS, hovering briefly shows a tooltip.
- **Try to use familiar icons for familiar actions** (`square.and.arrow.up` for sharing); consider an existing or customized SF Symbol.
- **Consider text when a short label is clearer.** Use a few words in title-style capitalization, and consider starting with a verb ("Add to Cart").

## Role

|Role|Meaning|Appearance (roles can affect it)|
|---|---|---|
|Normal|No specific meaning|—|
|Primary|Default; the most likely choice|Accent color|
|Cancel|Cancels the current action|—|
|Destructive|Can destroy data|System red|

- **Make the most likely choice primary.** When it responds to Return, people confirm quickly; in a sheet, editable view or alert, Return can also close the view.
- **Never make a destructive button primary**, even if most likely: people sometimes choose the prominent button without reading it.

## Platform considerations

No additional considerations for tvOS.

### iOS, iPadOS

**For actions that don't complete instantly, show an activity indicator in the button**, optionally with an alternative label ("Checkout" → "Checking out…"). The system shows it beside the label and hides any button image.

### macOS

**Push buttons** (the standard type) show text, a symbol, icon, image, or text plus image; they can be tinted and be a view's default button.
- Use a flexible-height push button ([`flexiblePush`](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/flexiblepush)) only for tall or variable-height content, such as two text lines or a tall icon. It keeps the standard corner radius and padding.
- **Append a trailing ellipsis when the button opens another window, view or app**, signaling that more input follows.
- Consider spring loading: on a Magic Trackpad, people drag items over the button and force click to activate it without dropping them.

**Square (gradient) buttons** ([`smallSquare`](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/smallsquare)) act on a view, like adding or removing table rows. Place them near the view, usually within or beneath it. They contain symbols or icons, never text (prefer SF Symbols); they can behave as push buttons, toggles or pop-up buttons. Avoid an introducing label.

**Help buttons** are circular question-mark buttons that open app help. Use the system one, at most one per window, without introductory text. Open the help topic for the current context when possible, otherwise the top level.

|View|Help button location|
|---|---|
|Dialog with dismissal buttons|Lower corner opposite them, vertically aligned|
|Dialog without dismissal buttons|Lower-left or lower-right|
|Settings window or pane|Lower-left or lower-right|

**Image buttons** show an image, symbol or icon and can behave as push buttons, toggles or pop-up buttons. Leave about 10 px of padding between image and button edges, which define the clickable area. Generally avoid the system border ([`isBordered`](https://developer.apple.com/documentation/appkit/nsbutton/isbordered)). Put any label below.

Use square, help and image buttons within views, not in the window frame (toolbar, status bar); in a toolbar, use a toolbar item instead of a square or image button.

### visionOS

Buttons typically have a visible background and play sound on interaction. Icon-only buttons typically use `circle`; text-only, `roundedRectangle` or `capsule`; icon plus text, `capsule`. States: idle, hover, selected (white background, black content), unavailable. Custom hover effects aren't supported. A brief look can show a tooltip, which text buttons generally don't need.

|Shape|Mini 28 pt|Small 32 pt|Regular 44 pt|Large 52 pt|XL 64 pt|
|---|---|---|---|---|---|
|Circular|✓|✓|✓|✓|✓|
|Capsule, text||✓|✓|✓||
|Capsule, text and icon|||✓|✓||
|Rounded rectangle||✓|✓|✓||

- **Prefer a discernible background shape and fill**, except in toolbars, context menus, alerts and ornaments. On a glass window use the `thin` material; floating in space, use glass.
- **Avoid custom buttons with a white fill and black content**; that style means toggled.
- **In general, prefer circular or capsule shapes**; corners pull the eye away from the center. Prefer a capsule for a standalone button.
- **Aim to keep button centers at least 60 pt apart.** Add 4 pt padding around buttons 60 pt or larger so hover effects don't overlap. Usually avoid small or mini buttons in stacks or rows.
- For text buttons, prefer rounded rectangles in vertical stacks and capsules in horizontal rows.
- **Use standard controls for familiar audible feedback**; visionOS has no haptics.

### watchOS

Inline buttons are capsules with a contrasting material.
- **Use a toolbar for buttons in the corners**; the system moves the time and title and applies Liquid Glass. Toolbar buttons suit navigation to related areas or contextual actions.
- **Prefer full-width buttons for primary actions.** If two share a row, give them equal height and images or short titles.
- Keep vertically stacked one- and two-line text buttons the same height where possible.

## Resources

Developer: `Button` (SwiftUI), `UIButton`, `NSButton`. See also [Location button](https://developer.apple.com/design/human-interface-guidelines/privacy#Location-button).

Source: [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), captured 2026-09-12.
