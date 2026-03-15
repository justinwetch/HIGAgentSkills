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
# Right to Left

> Support RTL languages (Arabic, Hebrew) by reversing your interface to match their reading direction.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

System UI frameworks flip automatically in RTL context. Apps using system components and standard layouts may need no changes. Fine-tune using the guidelines below.

## Text Alignment

- If the system doesn't auto-adjust: left-align in LTR → right-align in RTL.
- **Paragraphs (3+ lines):** align to the paragraph's own language direction, not the UI direction. (Right-aligning an LTR paragraph makes line starts hard to find.)
- **Lists:** reverse alignment for all items, including items in a different script.

## Numbers and Characters

- Different RTL locales use different numeral sets: Hebrew uses Western Arabic; Arabic may use Western or Eastern Arabic (varies by country/region).
- **Never reverse digits within a specific number** (phone numbers, credit card numbers, quantities always read left-to-right regardless of context).
- **Reverse numeral ordering in progress/counting controls** (sliders, rating indicators) — flip the sequence, not the individual digits.

## Controls

- **Flip controls showing progress** (sliders, progress bars, rating controls). Also reverse the positions of the start/end glyphs.
- **Flip navigation controls** (back button must point right in RTL; next/previous buttons must flip to match reading order).
- **Preserve controls referring to actual directions** ("to the right" must always point right regardless of locale).
- **Balance mixed Latin + RTL text** — Arabic/Hebrew lacks uppercase, so next to all-caps Latin text it appears small. Increase RTL font size by ~2pt to visually balance.

## Images

- **Don't flip photos, illustrations, or general artwork** — it changes meaning and may violate copyright.
- **Reverse positions of ordered image sequences** (chronological, alphabetical) to preserve ordering meaning in RTL.

## Interface Icons

Use SF Symbols — provides automatic RTL variants and localized symbols for Arabic, Hebrew, and other scripts.

- **Flip icons representing text alignment or reading direction** (e.g., left-aligned text bars → right-aligned in RTL).
- **Create localized versions of icons that display actual text** — SF Symbols provides localized variants of signature, rich-text, and I-beam pointer symbols.
- **Flip icons showing forward/backward motion** — forward in LTR is rightward; forward in RTL is leftward. A speaker with sound waves moving right needs to flip so waves move left in RTL.
- **Never flip logos or universal signs** (checkmarks, brand marks) — confuses people and may have legal repercussions. Always use original orientation.
- **Don't flip real-world objects** unless they explicitly indicate directionality. Clocks, most tools, and familiar items appear the same regardless of locale.
- **For complex icons with badges/slashes:** evaluate each component individually. Badges depicting UI elements flip if the UI flips. Badges modifying icon meaning: check whether flipping preserves meaning and visual balance. Maintain backslash orientation for prohibition/negation symbols (SF Symbols does this consistently). If a tool implies handedness, consider preserving tool orientation while flipping the base image.

## Platform Considerations

*No additional considerations for any platform.*
