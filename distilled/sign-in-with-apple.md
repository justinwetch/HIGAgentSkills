---
topic: sign-in-with-apple
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "sign in with apple"
  - "SIWA"
  - "ASAuthorizationAppleIDButton"
  - "authentication"
related:
  - onboarding
  - launching
---
# Sign in with Apple

> Sign in with Apple provides a fast, private way to authenticate with apps and websites using an existing Apple Account, with Face ID, Touch ID, or Optic ID. Supports all platforms including non-Apple.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Offering Sign in with Apple

- **Ask for sign-in only in exchange for value** — briefly explain the benefit (personalization, features, sync).
- **Delay sign-in as long as possible** — people abandon apps that require sign-in before anything useful.
- **If an account is required, explain why first** then offer all sign-in options.
- **Let people link an existing account** if a shared email address suggests one already exists.
- **Commerce apps: wait until after purchase to ask about account creation.** For Apple Pay flows, offer account setup on the order confirmation page — pre-fill from payment sheet data.
- **Welcome people immediately** after Sign in with Apple completes.
- **Indicate sign-in status** (e.g., "Using Sign in with Apple") in settings or account interfaces.
- **Display the Sign in with Apple button prominently** - make it no smaller than other sign-in buttons and don't require scrolling to see it.

## Collecting Data

- **Minimize data requests** during account setup.
- **Clearly indicate if additional data is required vs. optional.**
- **Don't ask for a password** — it defeats the purpose.
- **Don't ask for personal email if someone provides a private relay address.** Direct people to Settings > Apple Account > Password & Security > Apps using Apple Account to retrieve their relay address.
- **Support private relay identification** - let people view their relay address in your app/site, or use other purchase-provided identifiers like order number or phone number.
- **Give people time to engage before requesting optional data.** Don't block app access if optional data is withheld.
- **Be transparent** — display the name or email you received to show how you use it.

## System-Provided Buttons

Using system APIs gives you: guaranteed Apple-approved appearance, correct proportions, auto-localized title, configurable corner radius (iOS, macOS, web), VoiceOver support.

### Button Titles

Available on iOS, macOS, tvOS, and web: **Sign in with Apple**, **Sign up with Apple**, **Continue with Apple**.
Available on watchOS: **Sign in** only.

### Button Styles

| Style | Availability | Use on |
|---|---|---|
| Black | All platforms + web | White or light backgrounds with sufficient contrast |
| White | All platforms + web | Dark backgrounds with sufficient contrast |
| White with outline | iOS, macOS, web | White/light backgrounds without sufficient contrast; avoid on dark/saturated |

watchOS black button: uses system dark gray (not pure black) to contrast with the black watch background.

### Button Sizing

| | Value |
|---|---|
| Minimum width | 140 pt (140 px @1x, 280 px @2x) |
| Minimum height | 30 pt (30 px @1x, 60 px @2x) |
| Minimum margin | 1/10 of the button's height |

Adjust corner radius to match other buttons; default is rounded; can be square or capsule.

## Custom Sign in with Apple Buttons

App Review evaluates all custom buttons. Key rules:

**Must not change:**
- Titles: only *Sign in with Apple*, *Sign up with Apple*, or *Continue with Apple*
- General shape: logo+text = rectangular; logo-only = circular or rectangular
- Colors: both logo and text must be black or white (no custom colors)

**Can change:**
- Title font (weight, size)
- Title case (all caps if UI uses it)
- Background appearance (must remain black or white; subtle texture/gradient OK)
- Corner radius, bezel, shadow

**Logo file rules:**
- Match logo file height to button height; don't crop; don't add vertical padding.
- Never use the Apple logo as a button itself.
- Use only official Apple Design Resources artwork — never create a custom Apple logo.

### Logo+Text Buttons

- Use SVG/PDF for any button size; PNG only for 44 pt buttons.
- **Font size = 43% of button height** (button height ≈ 233% of font size, rounded).
- Keep title and logo vertically centered.
- Minimum margin between title and right edge: ≥8% of button width.
- Same minimum size as system buttons (140 pt wide, 30 pt tall, 1/10 margin).

### Logo-Only Buttons

- Always 1:1 aspect ratio. Don't add horizontal padding — artwork already has correct padding.
- Use a mask to change from square to circular or rounded-rectangular.
- Minimum margin: 1/10 of button height.
