---
topic: activity-rings
tier: 3
platforms: [ios, ipados, tvos]
category: components/watchos
triggers:
  - "activity ring"
  - "Move ring"
  - "Exercise ring"
  - "Stand ring"
  - "HKActivityRingView"
related:
  - healthkit
  - workouts
---
# Activity Rings

> Activity rings show daily progress toward Move, Exercise, and Stand goals. Colors and meanings are system-defined and must never change.

**Platforms:** iOS, iPadOS, watchOS *(not macOS, tvOS, visionOS)*

**watchOS**: Always shows all three rings.
**iOS with Apple Watch paired**: Shows all three rings.
**iOS without Apple Watch**: Shows Move ring only (step + workout approximation).

## When to Display

Show Activity rings in health/fitness apps when relevant — e.g., on a live workout metrics screen, or on a post-workout summary screen.

## Rules

- **Only for Move, Exercise, and Stand** — never repurpose for other data or in ring-like elements.
- **One person only** — clearly label whose progress (name, photo, avatar). Never aggregate multiple people.
- **Black background required** — always. Preferably enclosed in a circle (adjust corner radius, don't apply circular mask).
- **Ensure black background remains visible** around the outermost ring. If needed, add a thin black stroke around it. No gradients or shadows.
- **Never alter colors** — no filters, hue shifts, or opacity changes.
- **Scale appropriately** — don't let rings appear disconnected or oversized.
- **Design surrounding interface to blend with rings**, not the other way around.
- **Minimum outer margin**: no less than the distance between rings. Never crop, obstruct, or encroach on rings.
- **Separate from other ring-like elements** with padding, lines, labels, color, or scale.
- **Matching label colors**: when labeling ring values, use ring-specific colors:
  - Move = red
  - Exercise = green
  - Stand = blue
- **Not decorative** — never use in backgrounds or labels.
- **Not for branding** — never use in app icon or marketing materials.
- **Don't send redundant notifications** — system already delivers Move/Exercise/Stand updates. Don't include Activity ring visuals in notifications.
