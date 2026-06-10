---
topic: carekit
tier: 4
platforms: [ios, ipados]
category: technologies
triggers:
  - "CareKit"
  - "care plan"
  - "care management"
  - "patient care"
  - "OCKStore"
related:
  - healthkit
  - researchkit
---
# CareKit

> CareKit lets you build apps that help people manage care plans — chronic illness, post-surgery recovery, or wellness goals — with prebuilt UI components and on-device data storage.

**Platforms:** iOS, iPadOS *(not macOS, tvOS, visionOS, watchOS)*

CareKit 2.0 includes **CareKit UI** (prebuilt views) and **CareKit Store** (on-device database with automatic UI sync).

## Data and Privacy

- **Provide a coherent privacy policy** — required at App Store submission.
- Request data access (HealthKit, camera, motion) only in context, not at launch.
- Add descriptive messages to permission screens; don't build custom permission UIs.
- Manage health data sharing via Settings → Privacy only.
- See [HealthKit](healthkit.md) for HealthKit integration patterns. For surveys/tasks, see [ResearchKit](researchkit.md).

## CareKit Views

Three categories of prebuilt views:

| Category | Purpose |
|---|---|
| Tasks | Present prescribed actions; log symptoms and patient data |
| Charts | Display graphical progress data (bar, scatter, line) |
| Contacts | Show care team members; support phone/message/email/map |

Each view has a **header** (text, symbol, optional disclosure indicator) and an optional **content stack** (vertical subviews). CareKit UI handles all layout constraints.

### Task View Styles

| Style | Use when |
|---|---|
| Simple | Single-step task (button + checkmark). No content stack by default. |
| Instructions | Single-step task needing additional informative text (e.g., "Take on an empty stomach"). |
| Log | Logging events with timestamps (e.g., tap every time nausea occurs). |
| Checklist | Multi-step task with discrete completable steps (e.g., medication 3×/day with check times). Supports instructional text below. |
| Grid | Multi-step task in compact grid layout. Full collection view access for custom UI. Supports instructional text below. |

**Task content rules:**
- Required fields: **Title** and **Schedule**. Optional: **Instructions**, **Group ID**.
- Use marketing name, not chemical description.
- Use color to categorize tasks — but never as the only differentiator.
- Supplement complex tasks with images or video.

### Chart Design Rules

Chart styles: **bar**, **scatter**, **line**.

- **Highlight narratives and trends**, not raw data (e.g., correlation between medication adherence and pain level).
- **Short, non-repeating labels** — use "BPM" in axis, not in every data point label.
- **Distinct colors** — no similar shades for different data types. Ensure sufficient contrast.
- **Include a legend** if colors aren't immediately clear.
- **Denote time units** clearly (seconds, minutes, hours, days, etc.) in axis or elsewhere.
- **Consolidate large data sets** — too many points = unreadable.
- **Offset data** if large and small values coexist so small points remain readable.

### Contact Views

Two styles: **simple** and **detailed**. Support phone, message, email, and map. Use color to categorize care team members.

## Notifications

- **Minimize notifications** — coalesce multiple items when possible.
- **Include a detail view** to let people act immediately without launching the app (e.g., check off tasks from a notification).

## Symbols and Branding

- CareKit provides built-in symbols (phone, message, envelope, clock). Use them — most styles work best without customization.
- **Grid-style task views** support custom symbols. Prefer SF Symbols; create custom ones for unique content. Custom care symbols must be relevant to the app, health, or wellness task; don't use decorative symbols or corporate logos.
- **Subtle branding only** — convey brand through color and communication style, not prominent logos. Never show advertising.
