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

HealthKit is the central repository for health and fitness data in iOS, iPadOS, and watchOS. Request private health-data access only when the app provides health or fitness functionality. For example, a nutrition app may read weight/activity for calorie goals and recommendations, and write logged calories to global progress metrics.

## Privacy and permission

- Request permission before accessing or updating private health data, protect it, and clearly explain how the app uses it after access is granted.
- Provide a clearly stated privacy-policy URL during App Store submission.
- Request each data type in context (for example, weight when someone logs it), not at launch. Permissions can change; request whenever access is needed. Swift: `HKHealthStore.requestAuthorization(toShare:read:completion:)`; Objective-C: `requestAuthorizationToShareTypes:readTypes:completion:`.
- Use the standard system permission screen with a few succinct sentences explaining why the data is needed and how sharing benefits the person. Don’t reproduce its behavior or content in a custom screen.
- Let people manage sharing globally through Settings > Privacy; don’t add app controls that alter the health-data flow.

## Activity rings

Activity rings communicate Move, Exercise, and Stand progress; the Activity app defines ring position/color. `HKActivityRingView` displays those rings from a HealthKit activity summary object. Use it for a single person only; never represent more than one person’s data, and identify whose progress is shown (label, photo, or avatar).

- Use rings only for Move, Exercise, and Stand. Don’t repurpose them for other data or show those goals in another ring-like element.
- Rings are informational, never ornamentation or branding: don’t put them in labels, backgrounds, the app icon, or marketing.
- Preserve ring and background appearance exactly: no filters, recoloring, or opacity changes. Blend the surrounding interface instead; scale appropriately.
- Keep an outer margin at least as large as the distance between rings. Don’t crop, obstruct, or encroach on it or the rings. To place rings in a circle, adjust the enclosing view’s corner radius rather than applying a circular mask.
- Separate any other ring styles with padding, lines, or labels; color and scale can provide additional separation.
- Don’t put Activity rings in notifications or repeat the system’s Move/Exercise/Stand updates. A notification may reference Activity progress only with app-specific information.

## Apple Health icon and language

Use only the Apple-provided icon from [Apple Design Resources](https://developer.apple.com/design/resources/#technologies). Place *Apple Health* near it and, in a view containing other app icons, size it at least as large as the others. It indicates compatibility only, never acts as a button, and must not be masked, circularly cropped, bordered, overlaid, given gradients or shadows, or otherwise altered. Keep clear space of at least 1/10 its height; don’t composite it, put it in text, or substitute it for *Health*, *Apple Health*, or *HealthKit*. Don’t display Health app images or screenshots in the app or marketing materials (copyrighted).

In user-facing copy, call the app *Apple Health* or *the Apple Health app*, not *HealthKit* (the latter is the developer-facing framework name). Capitalize *Apple Health* with uppercase A and H, except where an established all-caps style requires otherwise, and use the system-provided localized translation of “Health.”

**Platforms:** iOS, iPadOS, watchOS. No additional considerations; not supported in macOS, tvOS, or visionOS.

Resources: [Works with Apple Health](https://developer.apple.com/health-fitness/works-with-apple-health/) · [Apple Design Resources](https://developer.apple.com/design/resources/#technologies) · [App Information > App Store Connect Help](https://help.apple.com/app-store-connect/#/dev219b53a88)

Source: [Apple Human Interface Guidelines — HealthKit](https://developer.apple.com/design/Human-Interface-Guidelines/healthkit), captured 2026-09-12.
