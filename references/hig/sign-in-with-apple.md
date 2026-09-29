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

Sign in with Apple provides fast, private sign-in to apps and websites using an existing Apple Account. It supports Face ID, Touch ID, or Optic ID, includes two-factor authentication, and avoids profiling people or their activity in apps. It can be offered across all app platforms, including non-Apple platforms. People can skip forms, email verification, and password creation; if you request name or email, they may share a unique private relay address that forwards to their personal email. Developer starting point: [Authentication Services](https://developer.apple.com/documentation/authenticationservices).

## Offering it

Ask for sign-in only in exchange for clear value, such as personalization, additional features, or data synchronization. Delay the request until people have experienced useful content. If an account is required, explain the reason and set up the account before offering Sign in with Apple alongside other supported methods.

Consider linking Sign in with Apple to an existing account before or after the person signs in. If the shared email matches an existing account, you can suggest linking; if a person signs in with an existing user name and password, you can suggest linking in account settings or another logical place. In commerce, wait until after purchase to ask for account creation; if supporting guest checkout, provide a quick creation path after the transaction. For Apple Pay, offer account setup on the order-confirmation page; do not ask again for name or email already supplied in the payment flow. Welcome people immediately after authorization and do not delay with unnecessary questions. Show the current method in settings or an account view, such as “Using Sign in with Apple.”

## Data and privacy

Minimize setup data. Mark each additional item as required or optional: legally/contractually required terms acceptance, region, birth date, or real-identity data must be supplied; optional data needs an explanation of its benefit and must not block account access or features. Never ask for a password unless the person has stopped using Sign in with Apple with the app or site.

Respect a private relay address; do not override it by requesting a personal email. Let people view the relay address in the app/site, direct them to **Settings > Apple Account > Password & Security > Apps using Apple Account**, or use another identifier collected in context, such as an order number or phone number. Let people engage before asking for optional data (for example, a phone number for text updates or social information for multiplayer), and do not gate the account if they decline. Explain why additional data is needed and clearly display the data received. Greeting people by the name or email they shared is one transparent example; it shows how the data is used and, for a relay address, where it can be found.

## Buttons

Display the button prominently, at least as large as other sign-in buttons and without requiring scrolling. Prefer the system API: it supplies Apple-approved appearance and proportions, localized titles, configurable corner radius on iOS/macOS/web, and VoiceOver alternative text. Use [`ASAuthorizationAppleIDButton`](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidbutton) for iOS/macOS/tvOS and [`WKInterfaceAuthorizationAppleIDButton`](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton) for watchOS; set corner radius on iOS/macOS with `ASAuthorizationAppleIDButton.cornerRadius` (in points). [Web guidance](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web) covers CSS appearance configuration; the [live button page](https://appleid.apple.com/signinwithapple/button) provides adjustable previews and code.

Choose one title variant consistently for the terminology of the experience:

| Platform | Titles |
|---|---|
| iOS, macOS, tvOS, web | **Sign in with Apple**, **Sign up with Apple**, **Continue with Apple** |
| watchOS | ** Sign in** (the sole system title) |

Choose appearance for contrast:

| Appearance | Availability and use |
|---|---|
| White | All platforms and web; use on a dark background with sufficient contrast. |
| White with outline | iOS, macOS, web; use on white/light backgrounds where white fill lacks contrast. Avoid on dark or saturated backgrounds, where the outline adds clutter. |
| Black | All platforms and web; use on white/light backgrounds with sufficient contrast; never on black/dark backgrounds. |

The watchOS black variant is system dark gray rather than pure black so it contrasts with the watch’s black background. Adjust corner radius to match other app buttons; system buttons support square through capsule shapes on iOS, macOS, and web. In iOS, macOS, and web, keep the minimums below because localized titles vary:

| Minimum width | Minimum height | Margin around button |
|---|---|---|
| 140 pt (140 px @1x; 280 px @2x) | 30 pt (30 px @1x; 60 px @2x) | At least 1/10 of button height |

## Custom buttons

For iOS, macOS, or the web, create a custom button only if the interface requires it—for example, to align authentication logos, use a logo-only control, or coordinate font, bezel, or background. App Review evaluates it. Keep the button instantly recognizable as Sign in with Apple. Use only artwork downloaded from [Apple Design Resources](https://developer.apple.com/design/resources/); never draw an Apple logo or use the logo itself as the button. Match artwork height to button height, do not crop or add vertical padding, and retain the supplied padding. Logo+text buttons remain rectangular; logo-only buttons may be rectangular or circular. Keep logo and title both black or both white. Allowed titles are exactly *Sign in with Apple*, *Sign up with Apple*, and *Continue with Apple*.

You may change title font (including weight/size), capitalize all letters when the interface is all caps, and use a subtle texture/gradient while the overall color remains black or white; corner radius, bezel, and shadow may also change. For logo+text buttons, SVG/PDF work at any height; PNG is only for 44 pt-high buttons, the default/recommended iOS height, with small/medium/large artwork available to match the buttons you display. Prefer the system font for the title. Regardless of the selected font, preserve system proportions: title size is 43% of button height (button height about 233% of title size, rounded): a 44 pt button takes a 19 pt title, a 56 pt button a 24 pt title. By default, capitalize the first word (*Sign* or *Continue*) and *Apple*; change this only when the interface uses all capitals. Vertically center title and logo, with logo artwork height equal to the button; inset the logo only when needed to align it with other authentication logos. Keep at least 8% of the button width between the title and the right edge. Use the same minimum size and 1/10-height outer margin as system buttons.

For logo-only buttons, keep a 1:1 aspect ratio and add no horizontal padding; supplied artwork already includes correct padding. Use SVG/PDF at any size, but PNG only for a 44x44 pt button. Apply a mask to change the square shape to circular or rounded rectangular. Do not crop artwork, remove its built-in padding, or add more padding; keep at least 1/10 button-height margin.

## Resources

[Sign in with Apple button](https://appleid.apple.com/signinwithapple/button) · [Authentication Services](https://developer.apple.com/documentation/authenticationservices) · [Apple Design Resources](https://developer.apple.com/design/resources/)

Source: [Apple Human Interface Guidelines — Sign in with Apple](https://developer.apple.com/design/Human-Interface-Guidelines/sign-in-with-apple), captured 2026-09-12.
