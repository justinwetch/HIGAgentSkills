---
topic: camera-control
tier: 3
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: technologies
triggers:
  - "Camera Control"
  - "iPhone camera button"
  - "hardware camera button"
related:
  - gestures
  - app-shortcuts
---
# Camera Control

> The Camera Control provides direct hardware access to your app's camera experience on iPhone 16 models.

**Platforms:** iOS only (iPhone 16 and iPhone 16 Pro)

Light press → shows an overlay extending from the device bezel. Light double-press → shows available controls. Slide finger on the Camera Control → adjusts the selected control's value.

## Anatomy

Two control types in the overlay:
- **Slider** — range of values (e.g., contrast level)
- **Picker** — discrete options (e.g., toggle viewfinder grid on/off)

System provides standard controls for zoom and exposure; you can include these in addition to custom controls.

## Best Practices

- **SF Symbols only** — no custom symbols supported. Use symbols from SF Symbols that clearly represent the control's behavior. Symbols do not show current state. Browse the Camera & Photos section of the SF Symbols app.
- **Short control names** — labels follow Dynamic Type and long names obscure the viewfinder.
- **Include units/symbols with slider values** — e.g., EV, %, or a custom string for context.
- **Define prominent values for sliders** — values people choose most frequently or evenly-spaced major increments (e.g., zoom factor stops). The system snaps more easily to prominent values during sliding.
- **Reserve overlay space in the viewfinder** — overlay appears adjacent to the Camera Control in both orientations. Place your camera UI outside the overlay area. Allow the overlay to appear/disappear over the viewfinder without conflicts.
- **Minimize viewfinder distractions** — large preview area with few visual interruptions is preferred. Don't duplicate controls that already appear in the overlay.
- **Enable/disable controls by camera mode** — e.g., disable video controls in photo mode. Controls cannot be added or removed at runtime.
- **Control order** — commonly used controls near the middle; less-used on either side. The system remembers the last-used control per app when reopening the overlay.
- **Locked capture extension** — create a locked camera capture extension so people can configure Camera Control to launch your camera from the lock screen, Home Screen, or inside other apps.
