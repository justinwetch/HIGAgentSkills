---
topic: popovers
tier: 3
platforms: [ios, ipados, macos]
category: components/presentation
triggers:
  - "popover"
  - "UIPopoverPresentationController"
  - "floating panel"
related:
  - sheets
  - menus
  - modality
---
# Popovers

> A popover is a transient view that appears above other content when people click or tap a control or interactive area.

**Platforms:** iOS, iPadOS, macOS, visionOS *(not tvOS or watchOS)*

Disappears when people interact with it or tap/click outside. Use for small amounts of information or functionality.

## Best Practices

- **Small amount of content or a few related tasks** — a calendar event popover changing date/time is appropriate; disappears after the change.
- **Use when space is limited and content is needed only temporarily** — sidebars and panels take persistent space; a popover is a lightweight alternative.
- **Arrow points directly at the element that revealed it** — ideally doesn't cover that element or essential visible context.
- **Close button only for confirmation-critical flows** (Cancel/Done for save-or-discard decisions). Otherwise, dismiss on outside tap/click. If multiple selections are possible, keep open until explicit dismiss.
- **Always save work on automatic dismissal of nonmodal popovers** — discard only on explicit Cancel.
- **One popover at a time** — no cascade or hierarchy of popovers. Close the open one before showing a new one.
- **Nothing appears over a popover** except an alert.
- **Single tap/click to switch between popovers** — when multiple bar buttons each reveal a popover, let tapping a new button close the open one and open the new one.
- **Don't make it too big** — size to fit content + pointer arrow; system can adjust for fit.
- **Animate size changes smoothly** — avoid the impression of a new popover replacing the old one.
- **Don't use "popover" in help text** — say "Select the Show button" not "Select Show at the bottom of the popover."
- **Don't use popovers for warnings** — people can miss or accidentally close them; use an alert.

## Platform Considerations

### iOS, iPadOS

- **Avoid popovers in compact views** — use a full-screen modal (sheet) instead. Reserve popovers for wide/regular views.

### macOS

- **Popovers can be made detachable** — people drag a popover to convert it into a floating panel that stays visible while they interact with other content.
- **Consider letting people detach** when they may want to view other content alongside the popover.
- **Minimal appearance changes on detach** — panel should look close to the original popover for context continuity.
