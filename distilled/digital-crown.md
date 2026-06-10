---
topic: digital-crown
tier: 3
platforms: [visionos, watchos]
category: components/watchos
triggers:
  - "Digital Crown"
  - "crown"
  - "haptic detent"
  - "crown input"
  - "WKCrownDelegate"
related:
  - designing-for-watchos
  - gestures
  - feedback
  - action-button
  - immersive-experiences
---
# Digital Crown

> The Digital Crown is a hardware input on Apple Watch and Apple Vision Pro for navigation, control, and adjustment.

**Platforms:** visionOS, watchOS *(not iOS, iPadOS, macOS, tvOS)*

## Apple Vision Pro

Used for:
- Adjusting volume
- Adjusting immersion level (portal, Environment, Full Space)
- Recentering content
- Opening Accessibility settings
- Exiting an app to the Home View

Your app does not need to handle these — all are system-reserved.

## Apple Watch

**watchOS 10+**: Digital Crown is the primary navigation input.
- **Watch face**: turn to view Smart Stack widgets.
- **Home Screen**: turn to scroll through apps.
- **Within apps**: turn to switch between vertically paginated tabs, scroll list views and variable-height pages.

System provides linear haptic *detents* (taps) as the Crown is turned. Some controls (like table views) provide row-based detents.

> **Note**: Apps don't respond to Digital Crown *presses* — those are reserved for system actions (e.g., revealing the Home Screen).

### Design Rules

- **Anchor navigation to the Digital Crown** — vertically orient list, tab, and scroll views so the Crown can navigate them naturally. Back up all Crown interactions with touch equivalents.
- **Use Crown for data inspection** where navigation isn't needed — e.g., drag-through time in World Clock.
- **Always provide visual feedback** in response to Crown input — update the interface to reflect changes. No feedback = people assume the Crown does nothing.
- **Match interface update speed to Crown rotation speed** — give people precise, proportional control. Avoid rates that make value selection difficult.
- **Match haptic feedback to your content** — if default detents don't fit (e.g., mismatched animation), disable them. Tables can switch to linear detents for unequal row heights.
