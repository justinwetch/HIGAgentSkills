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

# Watch faces

A watch face is the primary view people choose in watchOS.

## Best practices

- **Share faces (watchOS 7+) featuring your complications** via your app, website, Messages, Mail or social media. Ideally, support multiple complications to showcase. Some faces also take a system accent color, images, or styles. The system prompts people without your app to install it.
- **Preview each shared face.** Email the face to yourself from the iOS Watch app to get a preview with an illustrated bezel, for web and watchOS/iOS apps, or replace it with a high-fidelity hardware bezel from [Apple Design Resources](https://developer.apple.com/design/resources/#product-bezels), composited onto the preview.
- **Aim to offer shareable faces for all Apple Watch devices.** Faces such as California, Chronograph Pro, Gradient, Infograph, Infograph Modular, Meridian, Modular Compact, and Solar Dial need Series 4 or later; Explorer needs Series 3 (cellular) or later. If you use one, consider a similar configuration for Series 3 and earlier. You can clearly label each face with its supported devices.
- **Respond gracefully to incompatible faces.** On Series 3 or earlier, your app gets an error; consider immediately offering a compatible alternative instead of an error. With previews, help people understand they might get an alternative face.

## Platform considerations

watchOS only.

## Resources

Developer: [Sharing an Apple Watch face](https://developer.apple.com/documentation/ClockKit/sharing-an-apple-watch-face) (ClockKit)

Source: [Watch faces](https://developer.apple.com/design/human-interface-guidelines/watch-faces), captured 2026-09-12.
