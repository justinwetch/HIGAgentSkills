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
# Going Full Screen

> Full-screen mode expands a window to fill the screen, hiding system controls for a distraction-free environment.

**Platforms:** iOS, iPadOS, macOS

tvOS and watchOS: not applicable — apps fill the screen by default.
visionOS: not applicable — use window expansion or the Digital Crown to control passthrough/immersion (see immersive-experiences).

## Best Practices

- **Support full-screen when it makes sense** — games, video/photo viewing, slideshows, intensive tasks that benefit from a distraction-free environment.
- **Adjust layout if needed, but never programmatically resize the window** — use the extra space proportionally. Keep adjustments subtle to avoid jarring transitions between modes.
- **Keep essential controls accessible in full-screen** — people shouldn't have to exit to access necessary controls. Use auto-hiding controls that reappear on interaction (playback controls, etc.).
- **Preserve Dock access** in iPadOS and macOS full-screen apps (except games where accidental Dock reveal is likely — then you may defer the first swipe-up or hide the Dock entirely on macOS).
- **Pause and restore state** when people switch away from a full-screen experience (game, slideshow) and return.
- **Let people choose when to exit** — don't automatically end full-screen when they switch tasks or complete an activity.
- **Auto-hide toolbars and navigation controls** when content is primary (photos, reading). Restore them with a familiar gesture (tap, swipe down, or move cursor to top). Keep controls visible when they're essential.

## Platform Considerations

### iOS, iPadOS

- Home Screen indicator auto-hides shortly after app launch. It reappears when people touch the bottom edge. Preserve this default behavior. If it causes accidental exits, you can require two swipes instead of one.

### macOS

- **Use the system-provided full-screen experience** — ensures compatibility with all Mac models, including camera housing accommodation.
- **Don't change display mode** when players go full-screen in games — people expect control over their display mode.
- **Entry triggers:** let people use the window's Enter Full Screen button, View menu item, or Control-Command-F shortcut. Avoid custom window-mode menus. Games may additionally offer a custom toggle.
