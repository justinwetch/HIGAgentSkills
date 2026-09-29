---
topic: siri
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "Siri"
  - "Siri AI"
  - "Apple Intelligence and Siri AI"
  - "App Intents"
  - "AppEntity"
  - "App schema domains"
  - "Spotlight"
  - "intent donation"
  - "App Shortcut"
  - "Snippets"
related:
  - app-shortcuts
  - snippets
---

# Siri

Siri is a personal assistant; on supported devices, Siri AI (powered by Apple Intelligence) can start an integrated app's actions from anywhere, act on onscreen content and reach deep features.

## Getting your app to work with Siri

To work with Siri, an app has to expose actions (*intents*) and content (*entities*) to Apple Intelligence with `AppIntents`, so the system can surface them where it makes sense, like in Siri, Spotlight and Shortcuts. To get the most out of Siri, an app can also adopt app *schemas*, preset templates for functionality the system already understands; apps in common domains like email, music or photos get built-in, more conversational handling.

### Sharing contextual information

An app can annotate its views and other onscreen content with app entities so Siri understands references to it, donate entities to the on-device Spotlight index for Spotlight and Siri search, and donate people's actions (like recent activity) as intents so Siri can anticipate them and surface them at appropriate times.

## Best practices

- **Identify your most popular actions and when and where they occur** (like hands-free or on a particular device) to prioritize what to expose.
- **Use familiar terms for content and actions.**
- **Offer relevant content.** Consider giving Spotlight what's personally relevant (like recent searches, favorites or a wishlist), not everything; categories like email or messaging may warrant full-catalog access.
- **Don't include ads, marketing or in-app purchase pitches** in content Siri delivers.
- **Only provide a custom response if built-in responses don't meet your needs.**

## Customizing your app's experience with Siri

Schema domains need no extra work; outside them, App Shortcuts can expose custom actions. For schema-associated actions or content, an app can define optional intent or entity properties, like a playback control snippet, to enhance Siri's response. Responses aren't always visual, so these may not always appear. When you provide them, consider:

- **Write clear, descriptive dialogue** that conveys what the action does. If you ask follow-up questions, be sure to customize the default dialogue ("Which soup?", not "Which one?").
- **Keep responses as succinct as possible**, using conversation context to remove as many details as possible. Avoid unnecessary words or attempts at humor.
- **Provide responses Siri can deliver audibly and visually.** Make sure the voice response can stand alone.
- **Avoid specific pronouns when not necessary** ("Who should I send it to?").
- **Ask an open-ended question when the full list of options is too long** for Siri to read in a timely way.
- **Keep responses device-independent whenever possible.** If you must reference a device, make sure it's accurate and makes sense in context.
- **Omit your app name**; the system already attributes your app.
- **Don't include offensive language; respect parental controls.** Siri may respond aloud, where others can hear.
- **Help people understand errors.** The system has default error descriptions, but it's best to make your error responses situation-specific ("Sorry, we're out of chicken noodle soup").

## Editorial guidelines

- **Refer to Siri by name**, ideally just *Siri*; don't use pronouns like *she*, *him* or *her* (see [trademark guidelines](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)).
- **Never impersonate Siri, attempt to reproduce its functionality or appear to respond as Apple.** Don't use reserved phrases like "Call 911" or "Hey Siri."
- **In a localized context, translate only *Hey* in "Hey Siri"**; *Siri*, an Apple trademark, is never translated. Acceptable translations:

|Translation|Locales|
|---|---|
|Hey Siri|de_AT, de_CH, de_DE, en_AU, en_CA, en_GB, en_IE, en_IN, en_NZ, en_SG, en_US, en_ZA, ja_JP, tr_TR|
|يا Siri|ar_AE, ar_SA|
|Hej Siri|da_DK, sv_SE|
|Oye Siri|es_CL, es_ES, es_MX, es_US|
|Hei Siri|fi_FI, nb_NO, no_NO|
|Dis Siri|fr_BE, fr_CA, fr_CH, fr_FR|
|Ehi Siri|it_CH, it_IT|
|Siri야|ko_KR|
|Hai Siri|ms_MY|
|Hé, Siri|nl_BE|
|Hé Siri|nl_NL|
|E aí Siri|pt_BR|
|привет Siri|ru_RU|
|หวัดดี Siri|th_TH|
|嘿Siri|zh_CN|
|喂 Siri|zh_HK|
|嘿 Siri|zh_TW|

## Resources

Source: [Siri](https://developer.apple.com/design/human-interface-guidelines/siri), captured 2026-09-12.
