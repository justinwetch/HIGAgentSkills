---
topic: watch-faces
tier: 3
platforms: [watchos]
category: components/watchos
triggers:
  - "watch face"
  - "shareable watch face"
  - "face configuration"
  - "ClockKit"
  - "Sharing an Apple Watch face"
  - "watchOS 7"
related:
  - complications
  - designing-for-watchos
---
# Watch Faces

> People choose a watch face as their primary watchOS view and add complications to customize it. You can create and share pre-configured watch faces featuring your complications.

**Platforms:** watchOS only

## Shareable Watch Faces

- **Share watch faces with your complications** to drive app discovery — if someone adds your face without your app installed, the system prompts them to install it.
- **Display a preview** of each watch face you share. Preview images include an illustrated device bezel. Optionally composite onto a high-fidelity hardware bezel (downloadable from Apple's design resources).
- **Offer faces for all Apple Watch devices.** Watch faces available only on Series 4+ (California, Chronograph Pro, Gradient, Infograph, Infograph Modular, Meridian, Modular Compact, Solar Dial) and Explorer (Series 3+ with cellular). Offer a compatible alternative for Series 3 and earlier. Label each face with its device requirements.
- **Handle incompatible face errors gracefully** — immediately offer an alternative configuration rather than displaying an error.
