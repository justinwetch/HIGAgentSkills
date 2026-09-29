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

CareKit apps help people manage care plans for chronic illness (such as diabetes), recovery from injury or surgery, and health or wellness goals. CareKit 2.0 has two projects: CareKit UI supplies prebuilt, customizable views; CareKit Store defines an on-device database schema for patients, care plans, tasks, and contacts, with synchronization between the database and UI.

## Data, privacy, and integrations

Protect the extremely sensitive data people enter or the device/system supplies. Provide a clearly stated privacy-policy URL during App Store submission and obtain permission before accessing data through iOS features. HealthKit is the central iOS/watchOS repository; a CareKit app can request permission to access and share health/fitness data with designated caregivers. Request access in context (for example, weight when logged), not at launch; it’s a good idea to request whenever it’s needed because permissions can change. On the standard permission screen, write a few succinct sentences explaining why access is needed and how sharing benefits the person; manage sharing only through Settings > Privacy and don’t reproduce those system controls. Swift API: `HKHealthStore.requestAuthorization(toShare:read:completion:)`; Objective-C variant: `requestAuthorizationToShareTypes:readTypes:completion:`.

With permission and when useful for treatment, Core Motion can identify standing still, walking, running, cycling, or driving; for walking/running it can provide steps, pace, and flights of stairs ascended or descended. Physical-therapy data can include custom sensor measurements such as flexibility, range of motion, and ambulatory capability. Core Motion processes accelerometer, gyroscope, pedometer, and environment-related events. With permission, camera and photos can document treatment progress for a care team (for example, periodic injury photos for a physician); `UIImagePickerController` manages system interfaces for photos, movie recording, and media-library selection.

CareKit can incorporate ResearchKit surveys, tasks, and charts, plus its informed-consent module to request permission to collect and share data. See [HealthKit](https://developer.apple.com/design/Human-Interface-Guidelines/healthkit) and [ResearchKit](https://developer.apple.com/design/Human-Interface-Guidelines/researchkit) for related design guidance.

## Views

Use each CareKit UI view category for its intended content:

| Category | Purpose |
|---|---|
| Tasks | Present actions such as medication or physical therapy; log symptoms and other patient data. |
| Charts | Show graphical current or historical treatment progress. |
| Contacts | Show care-team contact information; support phone, message, email, and map links. |

Choose the view styles you need and supply CareKit Store data for display. Views have a header with optional text and symbol, an optional disclosure indicator, and an optional bottom separator; they may have a vertical content stack beneath it. CareKit UI manages layout constraints when subviews are added.

### Tasks

A task describes a prescribed action such as medication, food, exercise, or symptom reporting. Required information: **Title** (short introduction) and **Schedule**. Optional: **Instructions** (details, recommendations, warnings) and **Group ID** (an app-defined grouping identifier). In CareKit 2.0, choose one of five styles:

| Style | Use |
|---|---|
| Simple | One-step task; title, subtitle, and completion button. A supplied completion image is used; otherwise the button fills and shows a checkmark. No content stack by default. |
| Instructions | One-step task needing added text, such as “Take on an empty stomach” or “Take at bedtime.” |
| Log | Repeated event logging, such as tapping whenever nausea occurs; can timestamp each event. Header: title, time range, disclosure; below: instructions, Log button, completion time. |
| Checklist | Multistep task with separately completable scheduled steps (for example, medication at breakfast, lunch, and dinner), with optional instructions below. |
| Grid | Compact multistep button grid with succinct titles, with optional instructions below the grid and collection-view access for custom UI; consider checklist when each step needs more description. |

Consider using color to reinforce task categories (for example, medication vs. physical activity), never as the sole way to convey meaning. Describe tasks accurately but simply: use a medication’s marketing name rather than its chemical description and omit words that context already supplies. Consider video or images for complex steps so people avoid mistakes.

Example task data: **Title** *Ibuprofen*; **Schedule** *Four times a day*; optional **Instructions** *Take 1 tablet every 4–6 hours (not to exceed 4 tablets daily).*; optional **Group ID** such as *medication* or *exercise*.

### Charts

CareKit 2.0 provides bar, scatter, and line charts. Supply a descriptive title/subtitle, axis markers (such as days of the week), and the data set; charts update automatically with new data. Consider highlighting narratives and trends, such as the relationship between medication intake and pain, when this helps show progress or adherence. Keep labels short and nonrepeating (put *BPM* on an axis instead of every point); use distinct, sufficiently contrasting colors rather than similar shades; include a clear, succinct legend if colors aren’t immediately clear; state time units (seconds through years) on an axis or elsewhere; consolidate large data sets; and offset or restructure widely different values so small points remain readable.

### Contacts

CareKit UI offers simple and detailed contact views for care teams and trusted people. A simple contact shows a person glyph, name/practice, and disclosure for more information; a detailed contact repeats that identity header and adds doctor details with call, message, email, and directions actions in the subview. Consider color to categorize members at a glance.

## Notifications, symbols, and branding

Notifications can tell people when medication/tasks are due; badging the app icon can show an unread caregiver message, and Apple Watch can display a notification. Minimize interruptions because care plans differ; consider coalescing related items when possible. A notification detail view can show pending tasks and let people mark them complete without leaving the current context.

Most styles work best with CareKit’s built-in phone, message, envelope, and clock symbols. The grid task view can use custom UI; for unique groupings (such as a pill for medication or walking person for exercise), consider [SF Symbols](https://developer.apple.com/design/Human-Interface-Guidelines/sf-symbols), which coordinate with CareKit’s visual language and support custom symbols for unique app content. Any custom care symbol should relate to the app or health/wellness concept, never be purely decorative or a corporate logo. Use refined, unobtrusive branding through color and communication style; people using care apps don’t want advertising.

**Platforms:** iOS, iPadOS. No additional considerations; not supported in macOS, tvOS, visionOS, or watchOS.

Resources: [Research & Care > CareKit](https://www.researchandcare.org/carekit/) · [CareKit](https://carekit-apple.github.io/CareKit/documentation/carekit) · [CareKit > Chart Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/chart-interfaces) · [Research & Care > Developers](https://www.researchandcare.org/developers/) · [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit)

Source: [Apple Human Interface Guidelines — CareKit](https://developer.apple.com/design/Human-Interface-Guidelines/carekit), captured 2026-09-12.
