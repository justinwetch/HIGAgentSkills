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

Apple's social gaming network, which surfaces your game across the system. Adopt it with `GameKit`, using its system UI or your own custom UI.

## Accessing Game Center

At launch, determine whether the player is signed in to Game Center; if not, initialize the player then, to maximize discovery.

### Access point

An Apple-designed control that opens the player's Game Center profile and information in-game: the *Game Overlay* in iOS, iPadOS and macOS (progress and activities; full screen on iPhone, trailing edge on iPad), or the full-screen *dashboard* in visionOS and tvOS.

- **Display the access point in menu screens.** Consider the main menu or settings area. Avoid it during active gameplay and in temporary splash screens, cinematics or tutorials before the main menu.
- **Avoid placing controls near the access point.** You can fix it in any of the four corners; check whether its collapsed or expanded version overlaps important UI and controls, and adjust your layout. In visionOS, its locations vary by game type, such as immersive or volume-based.
- **Consider pausing your game while the Game Overlay or dashboard is present.**

### Custom UI

Custom UI can deep-link into Game Overlay or dashboard areas, such as leaderboards or a player's profile.

- **In custom links, use the official Game Center artwork** from Apple Design Resources. Don't alter its appearance, dimensions or visual effects.
- **Use correct terminology in custom links:**

|Term|Not|Localization|
|---|---|---|
|Game Center|GameKit, GameCenter, game center|System-provided translation|
|Game Center Profile|Profile, Account, Player Info|System translation of *Game Center*; localize *Profile*|
|Achievements|Awards, Trophies, Medals||
|Leaderboards|Rankings, Scores, Leaders||
|Challenges|Competitions||
|Add Friends|Add, Add Profiles, Include Friends||

## Achievements

- **Align with the four achievement states:** locked, in-progress, hidden, completed. The system groups completed achievements under Completed and all others under Locked.
- **Determine a display order before uploading.** Achievements appear in upload order.
- **Be succinct.** The title and the description each truncate beyond two lines. Use title-style capitalization for titles, sentence-style for descriptions.
- **Give players a sense of progress.** For progressive achievements, the system shows progress and encouraging messages.
- **Design rich, high-quality images.** Avoid reusing an asset for more than one achievement. Without one, the card shows a placeholder.
- The system applies a circular mask to achievement images, so be sure to keep content centered.

## Leaderboards

Players get notified when friends challenge them or pass their score.

- **Choose a leaderboard type:**
  - *Classic*: tracks a player's best all-time score; always active, no end.
  - *Recurring*: resets on an interval you define, such as daily or weekly.
- **Take advantage of leaderboard sets** to organize multiple leaderboards. Consider grouping by theme or gameplay experience, such as difficulty or genre.
- **Add leaderboard images.** Aim for a unique image per leaderboard that reflects its gameplay. iOS, iPadOS, macOS: a single image. tvOS: a set of images that animate in focus (template in Apple Design Resources).
- **Be mindful of cropping.** In iOS, iPadOS and macOS, the system crops artwork for leaderboards in a set; in tvOS, the focus effect may crop the edges of some layers. Make sure primary content stays comfortably visible.

## Challenges

Time-limited competitions with friends, built on leaderboards.

- **Create engaging challenges.** Challenges suit short, skill-based activities with a clear measure of accomplishment. Create challenges that take 1-5 minutes, which players can complete individually.
- **Avoid challenges that track overall progress or personal best scores**; they can give regular players an unfair advantage. Instead, track the most recent score after each attempt.
- **Make it easy to jump in.** Players arrive via invitation links, the Game Overlay, or the Games app in iOS, iPadOS and macOS. Always deep-link to the exact mode or level where the challenge begins; help first-time players through any initial onboarding first, telling them the game then jumps into the challenge automatically.
- **Create high-quality challenge artwork.** It appears in the Game Overlay, the Games app and invitation-link previews. The card overlays the title and player count, with a system gradient at the bottom. Avoid placing primary content where the title and description might cover it. Provide localized versions of any image text through App Store Connect or Xcode.

## Multiplayer activities

Game Center supports real-time and turn-based multiplayer, reached through party codes, the Game Overlay, the dashboard or the Games app.

- **Use party codes to invite players.** For real-time sessions, with or without Game Center matchmaking and networking. Game Center generates alphanumeric codes, typically eight characters, such as "2MP4-9CMF". Consider:
  - Allowing players to join late, leave early and return later.
  - Showing the current party code in your game.
  - Allowing manual code entry.
- **Support multiplayer through in-game UI.** The Game Overlay and dashboard's default multiplayer interface lets players invite nearby or recent players, Game Center friends and contacts without leaving your game. You can also present multiplayer in custom UI.
- **Provide engaging activity artwork.** The preview image appears system-wide on a card like a challenge card.

## Artwork specifications

|Artwork|Platforms|Format|Size (pt)|Other (pt)|
|---|---|---|---|---|
|Achievement|iOS, iPadOS, macOS, visionOS|PNG, TIF, JPG|512x512|Mask diameter 512|
|Achievement|tvOS|PNG, TIF, JPG|320x320|Mask diameter 200|
|Leaderboard|iOS, iPadOS, macOS|JPEG, JPG, PNG|512x512|Cropped area 512x312|
|Leaderboard|tvOS|PNG, TIF, JPG|659x371|Focused 618x348; unfocused 548x309|
|Challenge, multiplayer activity||JPEG, JPG, PNG|1920x1080|Cropped area 1465x767|
|Dashboard image|tvOS|PNG, TIF, JPG|600x180||

All: sRGB or P3, 72 DPI minimum; @2x px = 2x pt.

## Platform considerations

No additional considerations for iOS, iPadOS, macOS or visionOS.

### tvOS

**You can add an optional image at the top of the dashboard.** Use a simple, easily recognizable image that looks great at a distance. Consider your logo or wordmark; don't use your app icon.

### watchOS

GameKit is available, but there's no system-supported Game Center UI you can invoke; Game Center content for watchOS games appears on a connected iPhone.

## Resources

Source: [Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center), captured 2026-09-12.
