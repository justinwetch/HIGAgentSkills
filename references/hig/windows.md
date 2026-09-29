---
topic: windows
tier: 3
platforms: [ipados, macos, visionos]
category: components/navigation
triggers:
  - "window"
  - "WindowGroup"
  - "UIScene"
  - "NSWindow"
  - "resizable window"
  - "OpenWindowAction"
  - "DefaultWindowStyle"
  - "PlainWindowStyle"
  - "VolumetricWindowStyle"
  - "volume"
  - "volumetric window"
related:
  - split-views
  - multitasking
  - layout
---

# Windows

A window presents app or game content in a system frame with controls to open, close, resize and move it. A *primary* window holds main navigation, content and actions; an *auxiliary* window serves one task, allows no navigation elsewhere, and typically has a close button.

## Best practices

- **Make sure windows adapt fluidly to different sizes** for multitasking and multiwindow workflows.
- **Choose the right moment to open a new window**, e.g. for multitasking or preserving context; avoid it as default behavior unless it makes sense for your app.
- **Consider offering a context-menu or File-menu command to view content in a new window** (`OpenWindowAction`).
- **Avoid custom window frames or controls**, and don't try to replicate the system appearance.
- **Say *window* in user-facing content** for every type; other terms, including *scene*, are likely to confuse people.

## Platform considerations

Not supported in iOS, tvOS or watchOS.

### iPadOS

Multitasking & Gestures settings choose **full screen** (windows fill the screen; switch via the app switcher) or **windowed** (freely resize, move and layer windows; the system remembers size and placement after the app closes).

- **Make sure window controls don't overlap toolbar items.** When windowed, move leading-edge toolbar buttons inward to clear them.
- **Consider a gesture to open content in a new window**, like pinching a Notes item: `collectionView(_:sceneActivationConfigurationForItemAt:point:)` from collection items, `UIWindowScene.ActivationInteraction` from other views.
- To show just one file, you can skip creating a window (`QLPreviewSceneActivationConfiguration`), but must support multiple windows.

### macOS

Dragging a window's frame moves it; dragging edges can often resize it. The frame sits above the body and can include window controls and a toolbar; rarely, a bottom bar sits below.

| State | Behavior |
|---|---|
| Main | Frontmost; one per app |
| Key (*active*) | Accepts input; one onscreen. Usually main, but can be e.g. a floating panel. Clicking a window typically makes it key; clicking the Dock icon brings all app windows forward, making only the most recent key |
| Inactive | Not in the foreground; no vibrancy (looks subdued, farther away). Gray close, minimize and zoom buttons, as on non-key main windows; key uses color |

Some panels, like Colors or Fonts, become key only when people click the title bar or a keyboard-input component.

- **Make sure custom windows use the system-defined appearances.** System components update automatically on state change; custom ones must do it themselves.
- **Avoid putting critical information or actions in a bottom bar**; people often move windows so it's hidden. If you must, show only a little information about the contents or selection; for more, consider an inspector (typically trailing side of a split view).

### visionOS

*Windows* (`DefaultWindowStyle`) and *volumes* (`VolumetricWindowStyle`) both show 2D and 3D content, several at once, in the Shared Space or a Full Space. *Plain* (`PlainWindowStyle`) is default without glass. The system places the first one; people can move them.

#### Windows

An upright plane with unmodifiable *glass*, close button, window bar and resize controls; optionally a Share button, tab bar, toolbar and ornaments. By default, dynamic scale keeps apparent size constant with distance.

- **Prefer a window for a familiar interface and tasks**; reserve immersion for meaningful content. For bounded 3D content like a game board, consider a volume.
- **Retain the glass background.** Without it, legibility tends to suffer; opaque backgrounds obscure surroundings.
- **Choose an initial size that minimizes empty areas.** Default: 1280x720 pt, placed about 2 m away, appearing about 3 m wide.
- **Aim for an initial shape that suits the content.**
- **Set a minimum and maximum size for each window** so it can't shrink until UI overlaps or grow until unusable; adapt layout across that range.
- **Minimize 3D depth in a window.** The system adds highlights and shadows to its views and controls and clips content too far from the surface; for more depth, use a volume.

#### Volumes

Volumes are viewable from any angle; the close button and window bar turn to face the viewer.

- **Prefer a volume for rich 3D content**; for UI-centric interfaces, a window generally works best.
- **Place 2D content so it looks good from multiple angles.** You can pin it to 3D content with an attachment.
- **In general, use dynamic scaling** for legibility at a distance. For real-world objects like products, you can use fixed scaling (the default).
- **Take advantage of the default baseplate glow.** In visionOS 2 and later, the volume floor's border glows when looked at, revealing edges and the resize control if content doesn't fill it. Full-bleed content or a custom baseplate may not want it.
- **Consider an ornament for high-value content.** In visionOS 2 and later, a volume can have an ornament in addition to a toolbar and tab bar. Anchors like `topBack` or `bottomFront` fix it relative to the viewer. Avoid placing it on the same edge as a toolbar or tab bar; prefer only one extra ornament.
- **Choose an alignment that fits interaction.** In general, a baseplate parallel to the floor suits little-used content; one tilting to the viewing angle stays usable, even reclining.

## Resources

Developer: `WindowGroup`, `UIWindow`, `NSWindow`, `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`.

Source: [Windows](https://developer.apple.com/design/human-interface-guidelines/windows), captured 2026-09-12.
