---
topic: ratings-and-reviews
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/ux
triggers:
  - "rating"
  - "star rating"
  - "app review"
  - "RequestReviewAction"
  - "rate prompt"
related: []
---
# Ratings and Reviews

People often inspect an app’s ratings and reviews before downloading it, and can always rate it in the App Store. A good overall experience is the strongest basis for positive feedback; timing matters too.

Ask only after demonstrated engagement, such as completing a game level, meaningful task, or feature exploration. Avoid asking on first launch or during onboarding: people have not yet formed an opinion and may react negatively. Useful timing signals can include launch count/frequency, features explored, and tasks completed. Avoid interrupting an active task or game; choose a natural break. Avoid pestering: consider at least 1–2 weeks between requests and ask again only after additional engagement.

Prefer the system prompt on iOS, iPadOS, and macOS. The system checks for prior feedback and, if there isn’t any, shows a nonintrusive in-app request for a rating and optional written review; `RequestReviewAction` itself asks StoreKit to request feedback “if appropriate.” People can submit or dismiss with one tap/click and can opt out of prompts for all installed apps. It automatically limits prompts to **3 occurrences per app within 365 days**. Developer reference: [`RequestReviewAction`](https://developer.apple.com/documentation/storekit/requestreviewaction).

Before resetting the summary of individual ratings received since the previous reset after a new release, weigh the benefit of reflecting the current version against the likely disadvantage of having fewer total ratings, which can discourage downloads. See [Reset app summary rating](https://help.apple.com/app-store-connect/#/devfb7e87af8) and [Ratings, reviews, and responses](https://developer.apple.com/app-store/ratings-and-reviews/).

Source: [Apple Human Interface Guidelines — Ratings and Reviews](https://developer.apple.com/design/Human-Interface-Guidelines/ratings-and-reviews), captured 2026-09-12.
