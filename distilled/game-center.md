---
topic: game-center
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "Game Center"
  - "GameKit"
  - "achievement"
  - "leaderboard"
  - "challenge"
  - "multiplayer"
related:
  - designing-for-games
  - game-controls
---
# Game Center

> Game Center is Apple's social gaming network — achievements, leaderboards, challenges, and multiplayer — with built-in GameKit UI or custom UI options.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

Initialize and sign in to Game Center at launch so players can access achievements, leaderboards, challenges, friends, and multiplayer without extra setup.

Discovery surfaces include **Top Played**, social recommendations, the Apple Games app, App Store, and notifications.

## Access Point

The **access point** lets players view their Game Center profile without leaving your game. On iOS/iPadOS/macOS it opens the **Game Overlay**; on visionOS/tvOS it opens the **in-game dashboard** (full-screen).

- **Place in menu screens** — not during active gameplay, splash screens, cinematic flows, or tutorials.
- **Don't place UI controls near it** — access point has collapsed and expanded states that can overlap layout.
- **Consider pausing the game** while the overlay/dashboard is visible.

### Correct Terminology

| ✅ Term | ❌ Incorrect |
|---|---|
| Game Center | GameKit, GameCenter, game center |
| Game Center Profile | Profile, Account, Player Info |
| Achievements | Awards, Trophies, Medals |
| Leaderboards | Rankings, Scores, Leaders |
| Challenges | Competitions |
| Add Friends | Add, Add Profiles, Include Friends |

- Use system-provided translations of "Game Center" in localized contexts.
- Use only Apple-provided Game Center artwork in custom UI — don't alter size or effects.

## Achievements

**Achievement image specs:** PNG/TIF/JPG, sRGB or P3, 72 DPI minimum. Keep primary content centered because the system applies a circular mask.

| Platform | Image | Mask |
|---|---|---|
| iOS, iPadOS, macOS, visionOS | 512x512 pt (1024x1024 px @2x) | 512 pt (1024 px @2x) circle |
| tvOS | 320x320 pt (640x640 px @2x) | 200 pt (400 px @2x) circle |

- **Map to Game Center states**: locked, in-progress, hidden, completed. System groups by completion (Completed vs. Locked).
- **Order before upload** — upload order = display order.
- **Title**: ≤2 lines, title-style caps. **Description**: ≤2 lines, sentence-style caps.
- **Progressive achievements**: system shows progress + encouraging messages.
- **Achievement image**: applied circular mask — keep content centered. High quality, unique per achievement.

## Leaderboards

**Leaderboard image specs:** sRGB or P3, 72 DPI minimum.

| Platform | Format | Source | Display/crop |
|---|---|---|---|
| iOS, iPadOS, macOS | JPEG/JPG/PNG | 512x512 pt (1024x1024 px @2x) | 512x312 pt (1024x624 px @2x) crop |
| tvOS | PNG/TIF/JPG | 659x371 pt (1318x742 px @2x) | 618x348 pt focused; 548x309 pt unfocused |

**Types:**
- **Classic** — tracks best all-time score, always active.
- **Recurring** — resets on a defined interval (daily, weekly). Increases engagement.

**Leaderboard sets**: group leaderboards by difficulty, activity type, or theme for easy navigation.

**Leaderboard artwork**:
- iOS/iPadOS/macOS: single image.
- tvOS: set of images that animate on focus.
- Note: iOS/iPadOS/macOS crops artwork for leaderboards in a set; tvOS focus effect may crop edges.

## Challenges

- **1–5 minutes** of skill-based gameplay with a clear metric.
- **Track most recent score, not personal best** — prevents unfair advantages for regular players.
- **Deep-link directly** to the challenge mode/level. Route first-time players through onboarding, then auto-enter challenge.
- **Challenge artwork specs:**

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI minimum |
| Image size | 1920×1080 pt (3840×2160 px @2x) |
| Cropped area | 1465×767 pt (2930×1534 px @2x) |

## Multiplayer

- Default invite sources: nearby players, recent players, Game Center friends, and contacts.
- **Party codes**: typically 8-character alphanumeric (e.g., "2MP4-9CMF"). Let players join late, leave early, return later. Show code in-game; let players enter codes manually.
- **Multiplayer activity artwork** (same spec as challenge artwork):

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI minimum |
| Image size | 1920×1080 pt (3840×2160 px @2x) |
| Cropped area | 1465×767 pt (2930×1534 px @2x) |

## Platform Notes

- **tvOS dashboard**: optional top image (simple logo/wordmark, not app icon): 600×180 pt (1200×360 px @2x), PNG/TIF/JPG, sRGB or P3, 72 DPI.
- **watchOS**: no system Game Center UI on watch — Game Center content for watchOS games appears on the connected iPhone.
