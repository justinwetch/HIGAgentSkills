---
topic: playing-video
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: patterns/system
triggers:
  - "video"
  - "AVPlayer"
  - "AVPlayerViewController"
  - "VideoPlayer"
  - "RealityKit"
  - "HLS Trick Play"
  - "playback"
  - "video controls"
  - "PiP"
related:
  - playing-audio
  - live-viewing-apps
  - going-full-screen
---

# Playing video

Prefer the system video player for familiar behavior in apps and games on iOS, iPadOS, macOS, tvOS, and visionOS, or offer content through the TV app. Build a custom player only when necessary, and follow the system player’s interactions closely.

## Display and playback

System players support aspect-ratio modes and, on most platforms, Picture in Picture (PiP). People can switch modes; defaults are:

|Mode|Default aspect ratios|Result|
|---|---|---|
|Full-screen / `aspect-fill`|Wide, 2:1 through 2.40:1|Fills the display; edges may crop ([`AVLayerVideoGravity.resizeAspectFill`](https://developer.apple.com/documentation/avfoundation/avlayervideogravity/resizeaspectfill); Objective-C `AVLayerVideoGravityResizeAspectFill`)|
|Fit-to-screen / `aspect`|Standard (4:3, 16:9, and anything up to 2:1) or ultrawide (above 2.40:1)|Shows the whole video with letterboxing/pillarboxing as needed ([`AVLayerVideoGravity.resizeAspect`](https://developer.apple.com/documentation/avfoundation/avlayervideogravity/resizeaspect); Objective-C `AVLayerVideoGravityResizeAspect`)|

Apple’s guidance places exactly 2:1 in both default ranges without saying which mode applies.

Always supply video at its original aspect ratio. Embedded letterbox/pillarbox padding can make both modes smaller and breaks edge-to-edge contexts such as iPad PiP.

In iOS, iPadOS, tvOS, and visionOS, provide additional metadata (image, title, description, and other useful information) only when it adds value and keep it from obscuring playback. Use [`AVPlayerItem.externalMetadata`](https://developer.apple.com/documentation/avfoundation/avplayeritem/externalmetadata). Support expected input across devices: Space toggles play/pause on Apple Vision Pro, Mac, iPhone, iPad, and Apple TV; Apple TV viewers also expect familiar Siri Remote gestures.

In tvOS, consider a transport control for playback actions (such as favoriting) or a custom content tab for succinct supplementary information/recommendations. Keep actions to one or two steps. tvOS and visionOS built-in players provide transport controls for subtitles, audio language, library/favorite actions, and content tabs below the controls, such as Info, Episodes, or Chapters; in visionOS the controls are an [ornament](https://developer.apple.com/design/human-interface-guidelines/ornaments).

Don’t mix audio sources as viewers switch modes. For example, PiP may mute a full-screen video; if a game started meanwhile fails to handle secondary audio and the video is unmuted, both sounds mix. Handle the secondary-audio hint ([Swift `AVAudioSession.silenceSecondaryAudioHintNotification`](https://developer.apple.com/documentation/avfaudio/avaudiosession/silencesecondaryaudiohintnotification); Objective-C `AVAudioSessionSilenceSecondaryAudioHintNotification`).

## TV app integration

When the TV app opens your app for playback, immediately show black because the TV app fades to black and skips your launch screen. Start the selected or resumed content as soon as the transition completes: avoid splash/detail screens and intro animations. If an interstitial is unavoidable, Select steps through it and Play skips it. Resume automatically without asking. Space on a connected Bluetooth keyboard plays/pauses.

For multiple profiles, switch to the profile specified by the TV app before playback; if none is specified, ask the viewer to choose one and retain that information. Resume long clips at their previous end time. Viewers remain in your app after exiting rather than returning to the TV app, so prepare an exit view as soon as a playback notification arrives: show the just-watched content’s detail view with Resume, or a menu containing it/main menu.

Avoid a loading screen when content loads quickly. If loading takes more than two seconds, consider a black screen with a centered activity spinner and no surrounding content; begin playback as soon as enough data is ready and load the rest in the background. Keep branding/images minimal and retain the black background.

## Platform considerations

No additional iOS, iPadOS, or macOS guidance.

- **tvOS:** Keep logos/countdowns small and unobtrusive. Avoid large overlays; image-retention-prone devices favor short, translucent SDR graphics over bright opaque ones. For interactive quizzes, surveys, or progress checks, delay pausing by at least 0.5 seconds, show a dismissible overlay, and let people resume afterward.
- **visionOS:** Let people choose when playback starts, use a small resizable window, and keep surroundings visible. In full immersion, use the system’s predictable player location and keep virtual content from obscuring playback controls or the bottom ornament; don’t auto-start a fully immersive video. For scrubbing, provide an HLS Trick Play thumbnail track with thumbnails 160 px wide ([specification](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices#Trick-Play)). Keep inline video 2D and leave surrounding window content visible; controls share its plane rather than floating in an ornament. Use a RealityKit player for splash/transitional views or surface effects when playback controls and system integration (such as dimming and view anchoring) aren’t needed; it handles 2D/3D aspect ratio and closed captions ([`RealityKit`](https://developer.apple.com/documentation/realitykit)).
- **watchOS:** The system manages playback. Active foreground apps can embed a movie element for inline clips or play one separately; prefer clips ≤30 seconds because long clips consume disk and keep the wrist raised. Don’t scale assets. Recommended values:

  |Attribute|Value|
  |---|---|
  |Video codec|H.264 High Profile|
  |Video bit rate|160 kbps, up to 30 fps|
  |Full-screen resolution|208×260 px, portrait|
  |16:9 resolution|320×180 px, landscape|
  |Audio|64 kbps HE-AAC (movies and audio-only assets)|

  Don’t make a poster image resemble a system control. A poster that represents the clip can help people decide; tapping it replaces it with video and starts inline playback.

## Resources and provenance

- [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio), [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
- [`AVPlayerViewController`](https://developer.apple.com/documentation/avkit/avplayerviewcontroller), [`VideoPlayer`](https://developer.apple.com/documentation/avkit/videoplayer), [AVFoundation media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback), [AVKit](https://developer.apple.com/documentation/avkit), and [HTTP Live Streaming](https://developer.apple.com/streaming/)
- [*Create a great video playback experience*](https://developer.apple.com/videos/play/wwdc2022/10147), [*Explore video experiences for visionOS*](https://developer.apple.com/videos/play/wwdc2025/304), [*Deliver a great playback experience on tvOS*](https://developer.apple.com/videos/play/wwdc2021/10191)

Source: [Playing video](https://developer.apple.com/design/human-interface-guidelines/playing-video) (captured 2026-09-12).
