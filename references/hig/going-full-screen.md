---
topic: going-full-screen
tier: 3
platforms: [ios, ipados, macos]
category: patterns/system
triggers:
  - "full screen"
  - "fullscreen"
  - "Enter Full Screen"
  - "expanded view"
  - "preferredScreenEdgesDeferringSystemGestures"
  - "NSWindow.toggleFullScreen(_:)"
  - "NSApplication.PresentationOptions.hideDock"
related:
  - the-menu-bar
  - playing-video
  - status-bars
  - immersive-experiences
  - windows
  - layout
  - multitasking
---

# Going full screen

Full-screen mode expands a window to fill the screen, hiding system controls.

## Best practices

- **Support full screen when it makes sense**, like for games, videos, slideshows or in-depth focused tasks.
- **If necessary, adjust layout, but don't programmatically resize the window.** Keep essential content prominent, use the extra space, and be sure changes are subtle (e.g., proportions rather than which items appear) to avoid jarring transitions between modes.
- **Keep essential controls available without exiting**, like persistent or easily revealed playback controls.
- **Except in games, let people reveal the Dock in iPadOS and macOS.** Games can have iPadOS ignore the first bottom-edge swipe up (`preferredScreenEdgesDeferringSystemGestures`) or hide the macOS Dock (`hideDock`).
- **Help people resume after switching away**; games and slideshows need to pause automatically.
- **Let people choose when to exit**; don't end it automatically when they switch away or finish an activity like a game or movie.
- **Prioritize content by temporarily hiding toolbars and navigation controls** when content is the focus, like photos or documents; if you do, let a familiar gesture or action restore them (tap, swipe down, pointer to screen top), and be sure to keep controls essential for navigation or tasks visible.

## Platform considerations

Not supported in tvOS, visionOS or watchOS. A visionOS window can hide toolbars, but people generally expect different immersive experiences (see immersive-experiences).

### iOS, iPadOS

**Consider deferring system gestures to prevent accidental exits.** By default, the Home Screen indicator auto-hides shortly after people switch to your app and reappears on interaction near the bottom; one swipe exits. Whenever possible, keep this; if it causes unexpected exits, you can require two swipes (`preferredScreenEdgesDeferringSystemGestures`).

### macOS

- **Use the system full-screen experience** (`toggleFullScreen(_:)`); it accommodates the camera housing on some Macs.
- **In a game, don't change the display mode on entering full screen**; it doesn't improve performance (see *Managing your game window for Metal in macOS*).
- **Always let people choose when to enter.** Prefer the window's Enter Full Screen button, View menu item or Control-Command-F; avoid a custom window-mode menu. Games might also offer a custom toggle.

## Resources

Developer: `fullScreenCover(item:onDismiss:content:)`, `NSScreen`, `NSWindow.CollectionBehavior`.

Source: [Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen), captured 2026-09-12.
