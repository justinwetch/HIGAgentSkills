---
topic: eyes
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/visionos
triggers:
  - "eye tracking"
  - "look"
  - "gaze"
  - "hover effect"
  - "look to interact"
  - "eye input"
related:
  - designing-for-visionos
  - gestures
  - focus-and-selection
---
# Eyes

> In visionOS, eye gaze identifies the target for interaction — looking at an element highlights it and enables indirect gesture input.

**Platforms:** visionOS only

When people look at an interactive element, visionOS highlights it (hover effect), signaling that an indirect gesture (e.g., tap) can activate it. Some components auto-expand on gaze (e.g., tab bar reveals text labels; buttons reveal tooltips).

**Privacy**: visionOS does NOT provide apps with where people are looking before they tap. You're notified when someone taps a component — not that they looked at it.

## Best Practices

- **Multiple interaction methods** — always design for accessibility; not everyone can use eye input.
- **Visual comfort** — place primary task objects within the field of view. Avoid requiring rapid eye adjustments across large areas or multiple depth levels.
- **Comfortable viewing distance** — aim for at least 1 meter for content people will read or interact with over time.
- **Use standard UI components** — they respond consistently to gaze. Custom components with different visual cues can confuse people.

## Making Items Easy to See

- **Minimize visual distractions** — visual noise makes it hard to find targets. Movement is especially distracting in peripheral vision — it triggers involuntary gaze shifts.
- **Adequate spacing between interactive items**:
  - ≥16pt margin around each item's bounds, OR
  - ≥60pt between item centers.
  - Eyes make small constant adjustments — crowded items cause unintended target switches.
- **Avoid repeating patterns/textures filling the field of view** — can cause apparent depth variations. Use patterns in smaller areas only.

## Encouraging Interaction

- **Subtle visual cues toward the most likely target** — center placement, gentle motion, increased contrast, color/scale variations. Prefer noticeable but not flashy.
- **Rounded shapes for interactive items** — eyes are drawn to corners, making it harder to center gaze on sharp-cornered shapes. More rounded = easier to target.
- **Custom multi-element components: define a containing region** — e.g., image + label acting as one unit needs a custom highlight region encompassing both elements so visionOS highlights the whole thing when people look at either part.

## Custom Hover Effects

Custom hover effects animate when people look at an element. Run out-of-process (the system applies them without your app knowing when). Therefore: **custom hover effects cannot trigger code or actions**.

- **Use sparingly to emphasize special moments** — standard effects are well-understood; too many custom effects dilute impact and can cause visual discomfort.
- **Choose the right delay:**
  - No delay (default) — subtle effects or ones that invite immediate interaction (e.g., slider knob appearing).
  - Short delay — for elements people may look at briefly before interacting (e.g., tab bar expansion).
  - Long delay — for additional information (e.g., tooltips), since most people won't need them every time.
- **Keep at least one primary view unchanged in both states** — visual stability helps people follow the animation. If all views change simultaneously, it disorients people.
- **Test wearing Apple Vision Pro** — the only reliable way to validate comfort, timing, and visual feel.
