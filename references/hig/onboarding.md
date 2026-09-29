---
topic: onboarding
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/ux
triggers:
  - "onboarding"
  - "first launch"
  - "tutorial"
  - "welcome screen"
  - "permissions request"
related:
  - launching
  - feedback
  - offering-help
---
# Onboarding

People should understand an app or game by experiencing it. If needed, make onboarding fast, fun, and optional; it follows [launching](https://developer.apple.com/design/human-interface-guidelines/launching), rather than being part of launch.

- **Teach interactively:** let people safely perform the action, discover the feature, or try the mechanic.
- **Consider providing context-specific tips** instead of one large flow: focus on one current task/action and place instructions near its interface. [TipKit](https://developer.apple.com/documentation/tipkit) displays discovery tips.
- **Keep prerequisite onboarding brief and enjoyable;** avoid much memorization.
- **If it makes sense to offer a separate tutorial, consider making it optional.** If skipped initially, don’t show it on later launches; keep it easy to find in help, account, or settings.
- Keep onboarding about the app/game, not how to use the system or device.
- If needed, show a beautiful, succinct splash screen only long enough to absorb at a glance without delaying the experience.
- Don’t let large downloads block first interaction, whether people join or skip; consider including enough media/content in the package to start immediately.
- Keep licensing details out so the App Store can show agreements and disclaimers before download. If they must appear in onboarding, integrate them without disrupting balance.
- Postpone nonessential setup/customization and provide reasonable defaults.
- If private data/resources are required before the app functions, consider integrating the permission request into onboarding so you can explain why and the benefit of granting it; otherwise present it when the person first accesses the dependent feature. See [Requesting permission](https://developer.apple.com/design/human-interface-guidelines/privacy#requesting-permission).
- Prefer letting people experience the app/game before prompting for ratings or purchases; engagement can improve responses.

There are no additional platform considerations.

**Resources:** [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help), [Discoverable design](https://developer.apple.com/videos/play/wwdc2021/10126).

Source: [Apple HIG — Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding), captured 2026-09-12.
