---
topic: camera-control
tier: 3
platforms: [ios]
category: technologies
triggers:
  - "Camera Control"
  - "iPhone camera button"
  - "hardware camera button"
  - "AVCaptureControl"
  - "AVCaptureSlider.localizedValueFormat"
  - "AVCaptureSlider.prominentValues"
  - "LockedCameraCapture"
related:
  - sf-symbols
  - controls
---
# Camera Control

Camera Control provides direct access to an app’s camera experience. On iPhone 16 and iPhone 16 Pro models, it quickly opens that experience. A light press displays an overlay extending from the bezel; a light double-press shows available controls, and sliding a finger adjusts the selected value.

## Anatomy

- **Slider:** selects a value within a range, such as contrast.
- **Picker:** chooses discrete options, such as viewfinder grid on/off.

You can add custom controls, and optionally include system controls for zoom and exposure.

## Best practices

- **Use SF Symbols for control functionality.** Custom symbols aren’t supported. Choose a symbol that clearly denotes behavior; control symbols don’t represent current state. For example, use `bolt.fill` for flash and `camera.filters` for filters. See the Camera & Photos section of the [SF Symbols app](https://developer.apple.com/sf-symbols/).
- **Keep control names short.** Labels use Dynamic Type and longer names may obscure the viewfinder.
- **Give slider values context with units or symbols** such as EV, %, or a custom string. [`AVCaptureSlider.localizedValueFormat`](https://developer.apple.com/documentation/avfoundation/avcaptureslider/localizedvalueformat) is a `String?` that defines localized slider-value presentation.
- **Define prominent slider values** — frequently chosen or evenly spaced values such as major zoom increments — so sliding lands on them more easily. [`AVCaptureSlider.prominentValues`](https://developer.apple.com/documentation/avfoundation/avcaptureslider/prominentvalues-199dz) is `[Float]`; its members may receive unique visuals or behaviors.
- **Reserve space for the overlay.** Its labels occupy the area beside Camera Control in portrait and landscape. Put capture UI outside those areas, maximize viewfinder height and width, and let the overlay appear over it. Avoid duplicating sliders or toggles when the overlay is visible; people benefit from a large, distraction-free preview.
- **Enable or disable controls by camera mode** (for example, disable video controls while taking photos). The overlay supports multiple controls, but controls can’t be added or removed at runtime.
- **Arrange controls by frequency.** Put common controls toward the middle and less-used controls to either side. When people lightly press to reopen the overlay, the system remembers the last control used in your app.
- **Support launch from anywhere.** Create a locked camera capture extension so people can configure Camera Control to launch the camera experience from the locked device, Home Screen, or another app; see [Camera experiences on a locked device](https://developer.apple.com/design/human-interface-guidelines/controls#Camera-experiences-on-a-locked-device).

Not supported in iPadOS, macOS, watchOS, tvOS, or visionOS.

## Resources

[SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) · [Controls](https://developer.apple.com/design/human-interface-guidelines/controls) · [Enhancing your app experience with the Camera Control](https://developer.apple.com/documentation/avfoundation/enhancing-your-app-experience-with-the-camera-control) — AVFoundation · [AVCaptureControl](https://developer.apple.com/documentation/avfoundation/avcapturecontrol) — AVFoundation abstract camera-control base class · [LockedCameraCapture](https://developer.apple.com/documentation/lockedcameracapture)

Source: [Apple HIG — Camera Control](https://developer.apple.com/design/human-interface-guidelines/camera-control), captured 2026-09-12.
