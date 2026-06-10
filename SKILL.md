---
name: apple-hig
description: >
  Apple Human Interface Guidelines reference (Updated for OS 27 releases).
  Provides authoritative
  platform-specific design rules, component specifications, exact
  measurements, and interaction patterns for iOS, iPadOS, macOS, tvOS,
  visionOS, and watchOS. Use when designing, reviewing, or auditing any
  Apple platform UI, or when asked about specific HIG components,
  sizing, system behaviors, frameworks (HealthKit, SiriKit, ARKit, etc.),
  or platform conventions. Also use when the user is designing any
  digital interface and could benefit from established design principles,
  even without an explicit Apple platform context.
---

# Apple HIG Skill

Reference 156 distilled HIG files in `distilled/` via the routing index at `routing-index.md`.

## Loading Protocol

### Step 1 — Parse Task Context

From the user's request, identify:
- **Platform(s):** ios / ipados / macos / tvos / visionos / watchos
- **Components or patterns** mentioned (buttons, tab bars, sheets, etc.)
- **Frameworks or SDKs** referenced (HealthKit, SiriKit, ARKit, etc.)
- **Task type:** design / review / spec / audit / guidance

### Step 2 — Load Tier 1 (always, every invocation)

Read all 16 files listed in `routing-index.md` under `## tier-1`:

`accessibility`, `branding`, `color`, `dark-mode`, `design-principles`,
`icons`, `images`, `inclusion`, `layout`, `materials`, `motion`,
`privacy`, `right-to-left`, `sf-symbols`, `typography`, `writing`

These apply universally. Load them before answering.

### Step 3 — Load Platform File (Tier 2)

Read `routing-index.md` → `## tier-2 platform-map`.
For each detected platform, load its `designing-for-[platform]` file.
If "game" or "gaming" is mentioned, also load `designing-for-games`.

### Step 4 — Keyword Scan (Tier 3)

Read `routing-index.md` → `## tier-3 trigger-map`.
Normalize the user request to lowercase. Match trigger strings as
standalone words, phrases, or API symbols; never match a trigger merely
because it appears inside an unrelated word. For example, `AR` doesn't
match "tab bar," and `AI` doesn't match "explain." Load every matching
file. Load each file at most once.

### Step 5 — Related Expansion

For each **tier-2 and tier-3** file loaded, read its `related:` frontmatter.
Load any listed files not yet loaded — one hop only.

### Step 6 — Tier 4 On-Demand

Read `routing-index.md` → `## tier-4 trigger-map (on-demand)`.
Use the same standalone word/phrase/API-symbol matching rule. Load a
tier-4 file only on direct keyword match, or if named in a loaded file's
`related:` list. These are niche — avoid loading broadly.

### Step 7 — Answer

Apply all loaded content. If a topic isn't covered by loaded files,
name the specific file that would cover it and offer to load it.

---

## Non-Negotiables

- **Cite exact values.** State pt sizes, pixel densities, margins, and
  timing values as they appear in the distilled files. Never approximate.
- **Distinguish platforms.** When behavior differs across platforms,
  state each platform's rule explicitly. Never flatten to "generally."
- **No invention.** Every rule, measurement, and API name must trace to
  a loaded distilled file. If unsure, say so and name the source file.
- **Terse and direct.** This is a reference skill, not a tutorial.
  No pedagogical framing. State the rule.

---

## File Locations

- Distilled reference files: `distilled/[topic].md`
- Routing index: `routing-index.md`
- Frontmatter schema: each distilled file contains `topic`, `tier`,
  `platforms`, `category`, `triggers`, and `related` fields.
