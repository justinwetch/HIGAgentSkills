---
topic: right-to-left
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "RTL"
  - "right to left"
  - "Arabic"
  - "Hebrew"
  - "localization"
  - "mirroring"
related:
  - layout
  - inclusion
---
# Right to left

Support Arabic, Hebrew, and other RTL languages by reversing the interface as needed to match their reading direction. System UI frameworks and standard layouts flip automatically in RTL, so custom work is mainly for fine-tuning layout and locale-specific currencies, numerals, symbols, and typography. See [Localization](https://developer.apple.com/localization/).

## Text

- If the system doesn’t align text automatically, mirror alignment with the interface: left-aligned LTR content becomes right-aligned in RTL.
- Align paragraphs (three or more lines) by the paragraph’s language, not the surrounding context: Arabic right, English left, even in an RTL interface. One- and two-line blocks follow the current reading direction. Keep every item in a list consistently aligned, including items in a different script.

## Numbers, controls, and text balance

- RTL locales differ: Hebrew uses Western Arabic numerals; Arabic may use Western or Eastern Arabic numerals, varying by country, region, and even areas within one region. Number-centric apps should identify the appropriate representation per locale; other apps can generally rely on system representations.
- Never reverse digits within a specific number (for example **541**, a phone number, or credit-card number). Reverse the order of numerals when they show progress, counting direction, or a meaningful sequence; never flip the numeral glyphs. Thus a five-star rating/progress control reverses the numeral sequence with the stars in RTL while retaining each numeral’s shape.
- Flip progress controls (sliders, progress indicators) and reverse the positions of beginning/ending glyphs. Flip navigation controls that access a fixed order: a back button points right in RTL; next and previous buttons each flip to match RTL reading order. Preserve controls that mean an actual direction or point to a fixed onscreen area.
- Arabic and Hebrew can look smaller beside all-uppercase Latin because they have no uppercase letters. To balance adjacent scripts, increasing RTL text by about **2 points** often works well.

## Images

Avoid flipping photographs, illustrations, and general artwork: it can change meaning and may violate copyright. If an image’s content is strongly tied to reading direction, consider creating a new version instead. Reverse the positions of images when their order is meaningful (chronological, alphabetical, favorite, and similar); preserve the images themselves.

## Interface icons

- SF Symbols supplies RTL and localized Arabic/Hebrew variants; custom symbols can specify directionality. For text/reading-direction icons, flip represented alignment (for example left-aligned bars become right-aligned). For icons that display actual letters or words, consider localized variants (SF Symbols has localized signature, rich-text, and I-beam symbols); if text conveys an unrelated concept, consider an alternative without text.
- Flip icons that depict forward/backward motion because people tend to read movement in the reading direction (for example, speaker waves emanate right in LTR and left in RTL).
- Never flip logos or universal signs/marks such as a checkmark: flipping can confuse people and create legal issues. Generally don’t flip icons depicting real-world objects (a clock or right-handed pencil/tool), unless the object itself conveys direction. Most people are right-handed, so flipping a right-handed tool can confuse rather than help.
- Before flipping a complex custom icon, assess each component and overall balance. A slash may retain the same visual direction in both locales (as in SF Symbols). A badge representing UI should flip with that UI; for a badge that modifies meaning, consider whether flipping it preserves both the modified meaning and overall balance (a cart’s plus badge moves from top-right to top-left in RTL). Consider preserving a handed tool’s orientation while flipping its base if necessary.

### Platform considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

Developer references: [Preparing views for localization](https://developer.apple.com/documentation/swiftui/preparing-views-for-localization), [Creating custom symbol images for your app](https://developer.apple.com/documentation/uikit/creating-custom-symbol-images-for-your-app), and [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols). Videos: [Enhance your app’s multilingual experience](https://developer.apple.com/videos/play/wwdc2025/222), [Design for Arabic](https://developer.apple.com/videos/play/wwdc2022/10034).

Source: [Apple HIG — Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left), captured 2026-09-12.
