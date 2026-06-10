---
topic: app-clips
tier: 3
platforms: [ios, ipados]
category: technologies
triggers:
  - "App Clip"
  - "mini app"
  - "NFC clip"
  - "QR clip"
  - "lightweight experience"
related:
  - launching
  - onboarding
  - nfc
---
# App Clips

> An App Clip is a lightweight version of your app that provides an instant, focused on‑the‑go or demo experience without a full install.

**Platforms:** iOS, iPadOS only

Discovered via: App Clip Code, NFC tag, QR code, Siri Suggestions, Maps, Smart App Banners, Safari App Clip cards, Messages links (and other apps' in-app links since iOS 17).

## Designing Your App Clip

- **Complete the task — don't require the full app** — people shouldn't need to install anything to finish a task or demo.
- **Essential features only** — no tab bars, complex navigation, or settings. Minimum screens and forms. Remove all extraneous UI.
- **Avoid web views** — use native components. If only web components are available, link to the website instead.
- **No ads or marketing content** — App Clips must provide real value.
- **Launch immediately to context** — no splash screens, no waiting. Skip unnecessary steps. All assets must be bundled; don't download additional data on launch.
- **Keep it small** — the smaller, the faster the launch, especially on limited bandwidth.
- **Shareable** — let people share links to specific points within the App Clip.
- **Easy payment** — support Apple Pay for express checkout; avoid requiring account creation. If an account is needed, offer Sign in with Apple; collect minimal info.
- **Privacy**: no background operations. Don't rely on previously stored data (may be deleted between launches). Store login info securely off-device.

### Notifications (App Clips)

- Default: can schedule and receive notifications for up to 8 hours after launch.
- For activities spanning >1 day: explicitly request extended notification permission.
- Notifications must relate directly to completing the task (e.g., delivery update). No promotional notifications.

### Showcasing Your App

- When the full app is installed, it replaces App Clip invocations. Keep the experience familiar and focused, preserve continuity, and don't require people to log in again.
- Don't compromise the App Clip experience by aggressively asking people to install the full app.
- Show `SKOverlay` to recommend the full app at a **natural pause** or after task completion.
- Recommend politely — not repeatedly, not during a task, not via push notifications.

### Platform Providers (Multiple Businesses)

- Tone down your platform branding; show individual business branding front and center.
- Handle multi-business/multi-location scenarios — allow UI to update based on current business context.

## App Clip Card Content

| Attribute | Requirement |
|---|---|
| Image | 1800×1200 px, PNG or JPEG, no transparency |
| Title | ≤30 characters |
| Subtitle | ≤56 characters |
| Action button verb | View (media/educational), Play (games), Open (everything else) |

- Avoid text in the header image — not localizable, hard to read, aesthetically distracting.
- Use photography or graphics; no app screenshots.

## App Clip Codes

App Clip Codes use Apple-provided designs only. Two variants:
- **Scan-only** — camera icon at center. Use for posters, digital materials, inaccessible locations.
- **NFC-integrated** — iPhone icon at center. Use for physical/touchable locations (tables, registers, storefronts, signage, cards). People can also scan NFC-integrated codes with the camera.

**Size requirements:**

| Type | Minimum size |
|---|---|
| Printed | ≥3/4 inch (1.9 cm) diameter |
| Digital | ≥256×256 px (PNG or SVG) |
| NFC-integrated | NFC tag ≥35 mm diameter; for a 35 mm tag, printed App Clip Code at least 1.37 in / 3.48 cm |

- **Scanning distance ratio**: ≤20:1 distance:diameter. Prefer 10:1 (e.g., 40" away → at least 4" diameter).
- **Clear space**: at least equal to the gap between the center glyph and the circular code.
- **Surface**: flat or cylindrical only. On cylinders: width ≤1/6 of circumference.
- **Don't modify** the generated code — no filters, color adjustments, glows, shadows, gradients, reflections, rotation, or overlay content.
- **Color**: use the App Clip Code Generator or App Store Connect to choose colors. Three colors auto-generated (foreground, background, system-generated third). Both tools warn and reject combinations that would impair scanning.

**Printing:**
- Production color: convert to CMYK with relative colorimetric intent; use `Generic CMYK ICC profile` or `Gracol 2013 ICC profile`. Target `CIELab Delta E 2.5`, calibrate with printer sheets, and batch-verify scans.
- Use matte finish. No gloss, reflect, or holographic overlays.
- Outdoor: UV-resistant materials or coatings.
- Resolution: rasterize SVG at ≥600 ppi; print at ≥300 dpi.
- Grayscale printers: generate grayscale codes specifically (don't convert color codes to grayscale).
- NFC tags: Type 5 NFC tags ≥35 mm.

**Include App Clip logo** when space allows. Omit logo if:
- Clear space requirements can't be met.
- Placed on disposable or gambling/drinking items (playing cards, poker chips, bar coasters).

**Clear messaging**: always include a call to action if you omit the logo, or for digital placements where context is needed.

## Legal

- Only Apple-generated codes (App Store Connect or App Clip Code Generator tool) are approved.
- Don't use App Clip Code, App Clip mark, or App Clip designs in your company or product name.
- Don't copyright or trademark App Clip Codes.
- Remove App Clip Codes from display when the associated App Clip is no longer active.
- "App Clip" and "App Clip Code" must use title case. Apple trademarks remain in English.
