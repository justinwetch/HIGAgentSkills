---
topic: offering-help
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/ux
triggers:
  - "help"
  - "coach mark"
  - "hint"
  - "tooltip"
  - "tips"
  - "help documentation"
related:
  - onboarding
  - feedback
  - writing
  - the-menu-bar
---
# Offering Help

> Design help that's contextual, concise, and easy to dismiss — always directly related to what people are doing right now.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Best Practices

- **Match help type to task complexity** — inline views for simple 1–2 step tasks; tutorials for complex multistep tasks.
- **Context-match language and images** — don't show game controller images when someone is using a Siri Remote; don't say "click" on iPhone or "tap" on Mac.
- **Make help inclusive** (see inclusion guidelines).
- **Don't explain standard components** — describe what the standard element does *in your specific app or game*. For novel controls or nonstandard input usage, orient people quickly with animation or graphics, not lengthy text.

## Tips (TipKit)

Tips are small, transient views that teach features or faster paths.

- **Use the right tip type:** popover tip (preserves content flow) or inline tip (keeps surrounding info visible; annotation-style for pointing at UI, hint-style when not tied to a specific element).
- **Only for simple features** — if a feature requires more than ~3 actions, it's too complex for a tip.
- **Short, actionable, action-oriented** — 1–2 sentences max. Start with what it does, then how to use it. No promotional content, no unrelated flows.
- **Use eligibility rules** — parameter-based or event-based. Don't show a tip for a feature the person has already used. Space tips at a reasonable cadence (for example, once every 24 hours).
- **Include a related image or symbol if one exists** — prefer the filled variant (e.g., a star for favorites). Don't repeat an image that's already visible in the adjacent UI.
- **Add buttons for actions** — link to settings the tip refers to, or to additional learning resources.

## Platform Considerations

### macOS, visionOS — Tooltips

A tooltip (called a "help tag" in documentation) is a small transient view triggered by hovering (Mac) or looking at / hovering (visionOS).

- **Describe only the indicated control** — not adjacent controls or larger tasks.
- **Explain the action the control initiates** — begin with a verb: "Restore default settings", "Add or remove a language from the list."
- **Don't repeat the control's name** — wastes space and rarely adds value.
- **Keep to 60–75 characters max** — use sentence fragments; omit articles. More text signals the UI needs simplification.
- **Use sentence case** — casual and approachable. Omit ending punctuation unless required by style consistency.
- **Provide context-sensitive tooltips** — different text for different states of the same control.
