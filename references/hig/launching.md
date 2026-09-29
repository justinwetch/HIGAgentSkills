---
topic: launching
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/ux
triggers:
  - "launch"
  - "launch screen"
  - "splash screen"
  - "app startup"
  - "cold start"
  - "state restoration"
related:
  - onboarding
  - loading
---
# Launching

A launch runs from opening (including initial download) until the first screen is ready; onboarding may follow with a high-level view.

- **Launch instantly:** people may not wait more than a couple of seconds.
- **Provide a launch screen where required:** iOS/iPadOS/tvOS show it immediately, then replace it with the first screen; macOS/visionOS/watchOS don’t require one.
- **If needed, consider displaying** a succinct branding/required-information splash screen at onboarding’s beginning, or after launch without onboarding.
- **Restore as much granular prior state as possible on restart** so people continue where they left off, including the latest scroll position and each window’s prior state/location.

**Launch screens** *(not applicable to macOS, visionOS, or watchOS):* downplay them; they only make launch feel quick and ready, not onboarding, splash, or artistic/branding opportunities. Make one nearly identical to the first screen to avoid a flash; if it begins as a solid color, show only that color. Match orientation and appearance mode. Avoid text because static content can’t be localized. Don’t advertise or show logos/branding unless fixed on the first screen; avoid “About” or splash-like screens.

**Platform:** iOS/iPadOS: use the device’s orientation when both modes are supported; for one mode, launch in it and let people rotate. Landscape-only interfaces must work after rotation either way. tvOS launch screens are static despite layered app images; in live-viewing apps, consider starting new or recently viewed live content after a few seconds’ inactivity. visionOS: consider a Shared Space window first even for a fully immersive app; it provides context, loading time, and a Full Space control, letting people choose the transition while other apps run.

**Resources:** [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding), [Loading](https://developer.apple.com/design/human-interface-guidelines/loading). Xcode’s [Specifying your app’s launch screen](https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen) customizes an iOS launch screen; UIKit’s [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) covers initialization, preparation, and launch-time system requests.

Source: [Apple HIG — Launching](https://developer.apple.com/design/human-interface-guidelines/launching), captured 2026-09-12.
