---
topic: popovers
tier: 3
platforms: [ios, ipados, macos, visionos]
category: components/presentation
triggers:
  - "popover"
  - "UIPopoverPresentationController"
  - "popover(isPresented:attachmentAnchor:arrowEdge:content:)"
  - "NSPopover"
  - "floating panel"
related:
  - action-sheets
  - alerts
  - sheets
  - menus
  - modality
---

# Popovers

A transient view over other content, opened by clicking or tapping a control or interactive area.

## Best practices

- **Limit a popover to a little information or functionality**: a few related tasks.
- **Consider popovers for temporary content** instead of a sidebar or panel.
- **Point the arrow as directly as possible at the revealing element**, ideally covering neither it nor essential content.
- **Use a Close, Cancel or Done button only for confirmation and guidance**, like save-or-discard exits. Otherwise they generally close on an outside click/tap or a selection; if multiple selections are possible, make sure one stays open until people explicitly dismiss it or click or tap outside.
- **Always save work when a nonmodal popover closes automatically**; discard it only on an explicit Cancel.
- **Show one popover at a time**, never a cascade, and **nothing over a popover except an alert**.
- **When possible, switch popovers with one click or tap**, especially between bar buttons.
- **Avoid oversized popovers**: fit the contents and arrow. The system can resize one if necessary.
- **Animate size changes** so the popover doesn't look replaced.
- **Avoid "popover" in help documentation**; name the task or selection.
- **Avoid popovers for warnings**; use an alert.

## Platform considerations

No additional considerations for visionOS. Not supported in tvOS or watchOS.

### iOS, iPadOS

**Avoid popovers in compact views.** Adapt layout to the content area's size class: reserve popovers for wide size classes; in compact ones use a full-screen modal like a sheet.

### macOS

**Consider making popovers detachable**: dragging turns one into a panel that stays visible alongside other content. **Minimally change the panel's appearance.**

## Resources

Developer: `popover(isPresented:attachmentAnchor:arrowEdge:content:)`, `UIPopoverPresentationController`, `NSPopover`.

Source: [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers), captured 2026-09-12.
