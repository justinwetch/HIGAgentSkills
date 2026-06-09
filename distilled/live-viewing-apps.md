---
topic: live-viewing-apps
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "live TV"
  - "live streaming"
  - "EPG"
  - "guide"
  - "cloud DVR"
  - "linear TV"
related:
  - playing-video
  - remotes
---
# Live-Viewing Apps

> Live-viewing apps must prioritize live content above all else — instant access, clear distinction from VOD, and uninterrupted viewing.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Core Principles

- Playback should be one tap away, or no tap when appropriate. Provide instant visual feedback when people change channels.
- Include supported actions such as Download when available.
- **Live content first** — use examples like the first tab or similarly prominent placement so live viewing is one tap away.
- **One tap to start playback** — a Watch Now-style button can disappear immediately as playback begins.
- **Visually distinguish live from VOD** — badge, symbol, sash, or "Live" label. Consider a progress bar showing where the live stream currently is.
- **Consistent action order throughout the app** — e.g., always: Watch → Start Over → Record → Favorite.
- **Match audio to context** — audio follows live content unless the person navigates away from the live tab.

## Content Footer (During Playback)

An optional channel-browsing strip overlaid during playback:
- Subtle treatment (darkening) to maintain legibility of overlay text.
- Badge or tint the current channel's thumbnail.
- Match footer categories to EPG categories.
- Simple, predictable toggle: swipe up to show; swipe down to dismiss.

## EPG (Electronic Program Guide)

- Show future air times so people can schedule viewing.
- **Current program, channel, and time prominent on first open** — easy to spot and return to.
- **Easy navigation**: paging, scrolling, jump controls. Offer My Channels / Favorites group.
- **Group by familiar categories**: Movies, TV Shows, Kids, Sports, Popular.
- **Let people browse without leaving playback** — PiP or background audio while EPG is open.

## Cloud DVR

- **Start/stop recording from the info panel** during live-streaming.
- Record future programs from a content detail view; offer single-episode or all-episodes options.
- Let people specify exactly what to record (current episode, new episodes, specific teams).
- Allow playback + content actions (play, delete, adjust recording settings) within the DVR area.
- **Offer automatic storage management** — e.g., overwrite oldest/already-watched content to prevent running out of space.
