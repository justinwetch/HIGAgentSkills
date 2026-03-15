---
topic: siri
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "Siri"
  - "SiriKit"
  - "voice"
  - "intent"
  - "shortcut"
  - "Hey Siri"
  - "App Shortcut"
related:
  - app-shortcuts
  - homekit
---
# Siri

> Siri lets people perform tasks by voice with your app — even when it's not running — via system intents and custom intents. Integrates with Shortcuts for suggestions and automation.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Intent Processing Phases

1. **Resolve** — Agree on what the request means. Ask for missing or ambiguous parameters. (e.g., "Which Amy?")
2. **Confirm** — Confirm before acting, especially for tasks with financial impact. Surface errors early.
3. **Handle** — Perform the task; provide visual + verbal response about what was done.

## System Intents

Siri handles natural language processing for system intents — your app just provides data.

| Domain | Intents |
|---|---|
| VoIP Calling | Initiate calls |
| Workouts | Start, pause, resume, end, cancel |
| Lists & Notes | Create/search notes; create reminders (date/time/location) |
| Media | Search and play (video, music, audiobooks, podcasts); like/dislike; add to library/playlist |
| Messaging | Send, search, read messages |
| Payments | Send and request payments |
| Car Commands | Hazard lights/horn; lock/unlock doors; fuel/power level |

**Design rules for system intents:**
- **Complete requests without leaving Siri.** If you must open the app, go directly to the destination.
- **Financial requests: default to safest / least expensive option.** Never surprise people with fees.
- **Offer alternative results for ambiguous media requests.**
- **Apple Watch: minimal interaction, intelligent defaults.** If you must show options, keep the list tiny.

**Enhance the voice experience:**
- Provide example request phrases for the Help menu.
- Define **custom vocabulary** specific to your app (account names, workout names, etc.) — never generic terms, other app names, inappropriate language, or "Hey Siri."
- Define **alternative app names** if people might refer to your app in multiple ways.

**Custom interface for system intents (iOS only, not watchOS):**
- No extraneous or redundant info. People must be able to complete the action without the custom UI (voice-only).
- **Margins**: 20 pt from each edge; center-align content under the app icon.
- **Max height**: ≤½ the screen height — no scrolling.
- Don't show your app name/icon — the system handles this.

## Custom Intents

Use custom intents for tasks not covered by any SiriKit domain.

### Custom Intent Categories

| Category | Default verb | Additional verbs |
|---|---|---|
| Generic | Do | Run, go |
| Information | View | Open |
| Order | Order | Book, buy |
| Start | Start | Navigate |
| Share | Share | Post, send |
| Create | Create | Add |
| Search | Search | Find, filter |
| Download | Download | Get |
| Other | Set | Request, toggle, check in |

Category affects Siri dialogue, button titles, and behavior (Order → requires authentication).

**Response types**: Confirmation, Success, Error. Default dialogue is category-defined; enhance with custom templates including placeholders for dynamic values. Custom confirmation dialogue prepends the default; success/error follow different orderings.

### Custom Intent Design Rules

- **Use a system intent if one fits** your action (e.g., INSendMessageIntent, INPlayMediaIntent).
- **Pick the most specific matching category.** For display/info tasks, use Information to avoid extra taps.
- **Keep intents simple, long-lived, and non-date-specific.** Avoid overly complex or temporary intents.
- **Don't ask permission for Siri** if you only support custom intents (no system intents).
- **Support background operation** — the best intents run without foregrounding your app.
- **Design for all surfaces**: lock screen suggestions, Siri watch face, search, voice-only, multistep shortcuts.

### Follow-up Questions (Parameters)

- **As few as possible** — aim for zero or one. Maximum two.
- **Sort options** by recency, frequency, or popularity.
- **Keep parameter names simple**: *soup*, *size*, *location* — not technical terms.
- **Ask for confirmation only when** there's financial impact. Never more than once.
- **Adapt offered options to context** (closest store locations, etc.).
- Dynamic option lists: narrow for runtime, comprehensive for Shortcuts setup.

### Voice Dialogue Rules

- **Write scripts; act them out** to find unnatural dialogue.
- **Specific error messages**: "Sorry, we're out of chicken noodle soup" > "Sorry, we can't complete your order."
- **Concise vocal responses** — clear what's happening, no filler, no humor (it becomes annoying).
- Provide **synonyms** for list options (e.g., "bowl" as synonym for "large").
- **Exclude your app name** from all voice responses — the system attributes it.
- **Don't mimic or impersonate Siri.** Never reproduce Siri's functionality or imply Apple authorship.
- **No offensive content, no advertising** in intent responses.
- **Avoid personal pronouns** for inclusivity.
- **Device-independent language** — or device-specific if you know the device.

## Shortcuts and Suggestions

- **Donate every time** an action occurs — improves suggestion accuracy.
- **Only donate actions people actually performed.** Don't donate browsing.
- **Remove donations** if associated data is deleted (e.g., deleted contact).
- Suggest shortcuts for actions people *haven't* done yet (relevant shortcut) to appear in Shortcuts Gallery.
- For Siri Watch Face: define a *relevant shortcut* with time/context metadata.

### Shortcut Titles

- **Start with a verb; sentence-style capitalization; no punctuation.**
- ✅ "Order my favorite coffee" | ❌ "Large latte", "Order My Favorite Coffee."
- **Lead with key info** — long titles truncate.
- **Exclude the app name.**
- **Localize titles and subtitles.**
- Optional shortcut image: 60×60 pt (180×180 px @3x) for iOS; 34×34 pt (68×68 px @2x) for Siri watch face on 44mm Apple Watch.

### Shortcut Invocation Phrases

- **Short and memorable.** 2–3 words ideal. Don't imply substitution ("Order a large clam chowder" → people may try varying it).
- **Accurate and specific**: "Reorder coffee" not "Reorder".
- **Never commandeer core Siri commands** (e.g., "Call 911") or include "Hey Siri."

### Parameter Summaries

- Provide a summary for every custom intent: *"Order [quantity] [coffee]"*.
- Include all required parameters and any that receive input from other apps. Optional parameters can go in Show More.
- **Start with a verb; sentence-case; no ending punctuation.** Match the intent title's opening verb.
- Provide multiple summaries for parent-child parameter relationships.
- Define **output parameters** if actions produce data useful in multistep shortcuts.
- Define an **input parameter** if the action accepts output from preceding actions.
- **Avoid multiple actions doing the same thing** — combine into one flexible action.

## Editorial Guidelines

- **"Hey Siri"** — two words, italicized or in quotes, uppercase H and S. No ellipsis after it.
  - ✅ *Say Hey Siri to activate Siri.* | ❌ *Say Hey Siri… to activate Siri.*
- **In localization, translate only "Hey"** — "Siri" is never translated.

**Selected "Hey Siri" locale translations:**

| Locale | Translation | Locale | Translation |
|---|---|---|---|
| ar | يا Siri | es | Oye Siri |
| da | Hej Siri | fi | Hei Siri |
| de | Hey Siri | fr | Dis Siri |
| en | Hey Siri | it | Ehi Siri |
| ja | Hey Siri | ko | Siri야 |
| nl | Hé Siri | pt_BR | E aí Siri |
| ru | привет Siri | sv | Hej Siri |
| tr | Hey Siri | zh_CN | 嘿Siri |

- **"Shortcuts"** (the app/feature) = capital S, plural.
- Individual shortcuts = lowercase.
- To describe voice use: "Run a shortcut by asking Siri" or "Add a shortcut to Siri to run with your voice." Never: "add voice shortcuts," "make a voice command," "create a voice prompt."
- For non-voice discovery: "For quick access, add to Shortcuts."
- **Never refer to Siri with pronouns** (she/him/her) — use "Siri."
- **Don't translate Siri, Apple, or other Apple trademarks.**
