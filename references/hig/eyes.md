---
topic: eyes
tier: 3
platforms: [visionos]
category: patterns/visionos
triggers:
  - "visionOS eyes"
  - "look"
  - "gaze"
  - "hover effect"
  - "look to interact"
  - "eye input"
related:
  - gestures
  - immersive-experiences
  - spatial-layout
  - focus-and-selection
---

# Eyes

In visionOS, looking at an interactive element highlights it; this *hover effect* shows people they can use an indirect gesture like tap.

- In some cases, the system can automatically expand a component people look at, like a tab bar revealing labels (a tab highlights first and can be selected before labels appear) or a button showing a tooltip.
- For privacy, visionOS doesn't reveal where people look before they tap; for system-provided components, it automatically reports taps.
- *Focus effects* (keyboard or game controller navigation) are unrelated to hover.

## Best practices

- **Always give people multiple ways to interact**, supporting their accessibility features.
- **Design for visual comfort.** Make sure objects needed for the primary task are in the field of view. The system automatically places the first window or volume conveniently in front of people (Shared or Full Space); a Full Space can request head pose to place 3D content. In all cases, visual comfort improves when you avoid requiring multiple quick eye adjustments across a large area or multiple depths.
- **Aim to place content people read or engage with over time at least 1 m away**; in general, don't place content very close unless it's used only briefly.
- **Prefer standard UI components**; they respond consistently to looking, and custom feedback cues can be hard to learn.

## Making items easy to see

- **Minimize visual distractions**, especially peripheral movement. Content revealed near a button people are looking at can pull their eyes off it.
- **Space items so eyes don't jump between them**: you can use a margin of at least 16 pt around each interactive item's bounds, or keep centers always at least 60 pt apart.
- **Avoid a repeating pattern or texture that fills the field of view**; its elements can appear at different depths. Consider a smaller area.

## Encouraging interaction

- **Consider subtle cues to draw eyes to the most likely item**, like placing it near the center of the field of view, gentle motion, increased contrast, or color or scale variation. In general, prefer cues noticeable without being flashy or harsh.
- **In general, give interactive items a rounded shape**; corners pull eyes from the center.
- **For a multi-element interactive component, be sure to provide an overall containing shape visionOS can highlight**, like a custom region spanning an image and its label, so the entire region highlights when people look at either.

## Custom hover effects

When it makes sense, you can give a system or custom UI element or a RealityKit entity a custom animated hover effect that replaces or augments the standard one. You define two states, with and without it; the system applies it out of process, so you can't know when it shows or the element's state, or run code that depends on knowing when people look.

- **Prefer custom hover effects for special moments.** Too many, or using them when standard effects suffice, can dilute your design, distract people, and even cause visual discomfort.
- **Choose the right delay:** none (default) tends to be especially useful for subtle or interaction-inviting effects, like a slider knob appearing; consider a short delay so people can look and quickly interact without waiting for the effect, like tab bar expansion; a slightly longer delay can work well for additional information most people won't need every time, like a tooltip.
- **Aim to keep at least one primary view unchanged in both states**; changing all views can disorient people.
- **Thoroughly test custom hover effects**, aiming to test while wearing Apple Vision Pro.

## Platform considerations

Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.

## Resources

Source: [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes), captured 2026-09-12.
