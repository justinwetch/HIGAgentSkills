---
topic: healthkit
tier: 3
platforms: [ios, ipados, watchos]
category: technologies
triggers:
  - "HealthKit"
  - "health data"
  - "activity ring"
  - "workout data"
  - "HKHealthStore"
  - "requestAuthorization(toShare:read:completion:)"
  - "HKActivityRingView"
related:
  - activity-rings
  - workouts
---
# HealthKit

> HealthKit is the central health and fitness data repository for iOS, iPadOS, and watchOS. Only integrate if your app provides health or fitness functionality.

**Platforms:** iOS, iPadOS, watchOS *(not macOS, tvOS, visionOS)*

> **IMPORTANT**: Don't request access to health data if your app isn't health/fitness-focused.

## Privacy

- **Request permissions in context** — when people perform the relevant action, not on launch.
- **Add descriptive messages to the system permission screen** — explain why you need the data and how it benefits the person. Don't build custom permission screens.
- **Manage health data sharing via Settings → Privacy only.** Don't build additional data-flow controls in your app.
- **Provide a coherent privacy policy** (required at App Store submission).
- Re-request access every time you need it — permissions can change.

## Activity Rings

The Activity ring element shows Move, Exercise, and Stand progress. Colors and ring positions are system-defined and must never change.

**Rules:**
- **Only for Move, Exercise, and Stand** — don't repurpose for other data or use other ring-like elements for those three.
- **One person at a time** — clearly label whose progress is shown (name, photo, avatar).
- **Not decorative** — don't use in backgrounds or labels.
- **Not for branding** — don't use in app icon or marketing.
- **Preserve colors and appearance exactly** — no filters, color changes, opacity changes.
- **Minimum outer margin**: no less than the distance between the rings. Never clip, obscure, or encroach on the rings. To display within a circle, adjust corner radius of the containing view — don't apply a circular mask.
- **Separate from other ring elements** using padding, lines, labels, color, or scale.
- **Don't include Activity rings in notifications** — don't replicate the system's own progress updates.

## Apple Health Icon

- Don't display Health app images or screenshots.
- Use only Apple-provided artwork — no custom icons.
- **Display "Apple Health" text near the icon** for clarity.
- Match size with other health-related app icons in the same view.
- **Not a button** — use only to indicate compatibility.
- **No appearance changes**: no corner radius masking, no circular cropping, no borders, overlays, gradients, or shadows.
- Minimum clear space: 1/10 of icon height.
- Don't use inline in text.

## Editorial Guidelines

- Refer to the app as **"Apple Health"** or **"the Apple Health app"** (not "HealthKit" in user-facing text).
- **"HealthKit"** is a developer framework name — don't use in user-facing copy.
- **"Apple Health"** — two words, capital A and H.
- Use system-provided localized translation of "Health" on device.
