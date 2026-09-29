---
name: apple-hig
description: >
  Apple Human Interface Guidelines reference, updated for iPhone Duo and
  OS 27. Provides authoritative platform-specific design rules, component
  specifications, exact measurements, and interaction patterns for iOS,
  iPadOS, macOS, tvOS, visionOS, and watchOS. Use when designing, reviewing,
  auditing, or fixing any Apple platform UI, or when asked about specific HIG
  components, sizing, system behaviors, frameworks (HealthKit, SiriKit, ARKit,
  etc.), or platform conventions. Also use when the user is designing any
  digital interface and could benefit from established design principles, even
  without an explicit Apple platform context. Includes a guided /duo workflow
  that adapts an existing iOS app to iPhone Duo, plus opt-in enforce mode with
  independent review.
---

# Apple HIG Skill

Use the distilled HIG references in `references/hig/` through `routing-index.md`. The source snapshot and verified release measurements are in README.md.

## Loading Protocol

Release **2026-09-27**; Apple source snapshot **2026-09-12**.
For help, installation, version or capability questions, read only this entry
point and the relevant README section. Do not load the HIG corpus for setup help.
Installing or upgrading this skill includes its `/duo` slash command. After the
skill folder is in place, check whether the host already offers `/duo`. If it
does not, copy `commands/duo.md` into the host's custom slash-command or custom
prompt directory (user-level unless the user asks for one project), confirm
`/duo` is available, and tell the user if a restart is needed.
Work directly in the conversation and the user's project; do not create a browser
intake form, onboarding site, dashboard, or browser setup step.

Ordinary guidance is the default. Only an explicit request to apply enforce mode
activates its procedure. Read `references/enforce.md` first in that case and check
reviewer, Python and observation capabilities before loading the design guidance.
A leading `/duo`, `Use apple-hig in Duo mode`, or an explicit request to adapt
an existing app for iPhone Duo starts Duo mode: read `references/duo.md` and
follow its stages. Questions about the command and ordinary Duo design questions
stay ordinary guidance. Duo mode works only in the app's native code; it never
produces HTML, SVG, or web mockups.
Use the available Python 3.10+ interpreter (`python3` or `python`); do not assume
the executable name. Ordinary guidance also works without Python.

When Python is available, use the standard-library routing helper to resolve
steps 2–6: save only the exact user request to a UTF-8 text file in a temporary
directory outside the user's project, then run `<python> "<skill-root>/scripts/hig_route.py" --request-file "<request.txt>"`.
Read every file in its `files` list in bounded sections, completing any truncated
read before continuing. Do not concatenate the entire set into one tool output;
the helper output is metadata, not the guidance itself. Do not add
your own instructions to the request text or promote inferred topics to
initial matches. If the user explicitly excludes a platform/device/topic, pass
the excluded topic IDs with `--exclude-topic` (repeat for each topic, including
platform aliases matched inside an excluded phrase); record the user's reason.
Keep a platform that is also positively requested elsewhere. Do not exclude
topics merely to reduce context. Exclusions apply
to direct and related selections, never to the 16 foundations. Without Python,
apply the same steps and explicit exclusions manually.

### Step 1 — Parse Task Context

From the user's request, identify:
- **Platform(s):** ios / ipados / macos / tvos / visionos / watchos
- **Device/form factor:** iPhone Duo when named or matched by its tier-2 triggers
- **Components or patterns** mentioned (buttons, tab bars, sheets, etc.)
- **Frameworks or SDKs** referenced (HealthKit, SiriKit, ARKit, etc.)
- **Task type:** design / review / spec / audit / guidance
- **Mode:** ordinary guidance by default. Activate enforce mode only when the user explicitly asks to apply it; mentioning the mode or asking what it means does not activate it. Duo mode starts only as described above.

### Step 2 — Load Tier 1 (every design or review task)

Read all 16 files listed in `routing-index.md` under `## tier-1`:

`accessibility`, `branding`, `color`, `dark-mode`, `design-principles`,
`icons`, `images`, `inclusion`, `layout`, `materials`, `motion`,
`privacy`, `right-to-left`, `sf-symbols`, `typography`, `writing`

These apply universally. Load them before answering.

### Step 3 — Load Platform File (Tier 2)

Read `routing-index.md` → `## tier-2 platform-map`.
For each detected platform, load its `designing-for-[platform]` file.
Also match the tier-2 map's device/form-factor and API triggers using
standalone word/phrase/API-symbol matching. A Duo match loads both
`designing-for-iphone-duo` and `designing-for-ios`; Duo is an iOS form factor.
If "game" or "gaming" is mentioned, also load `designing-for-games`.

### Step 4 — Keyword Scan (Tier 3)

Read `routing-index.md` → `## tier-3 trigger-map`.
Normalize the user request to lowercase. Match trigger strings as
standalone words, phrases, or API symbols; plural, hyphenated and bare-symbol
forms count (`tab bars`, `full-screen`, `keyboardType`). Never match a trigger
merely because it appears inside an unrelated word. For example, `AR` doesn't
match "tab bar," and `AI` doesn't match "explain." Load every matching
file. Load each file at most once.

### Step 5 — Related Expansion

Freeze the initial selection set as the tier-2 and tier-3 files selected in steps 3–4. Read only that set's `related:` frontmatter.
Load the listed files once. Do not expand related lists from those newly added files.

Bind each initial topic to the exact platform/device/trigger text matched in
the user's request. An inferred
component concept is not a literal trigger match.
A topic reached through `related:` stays related even when it is useful;
never promote it to initial and expand it again. If semantic relevance calls
for an additional reference, load that specific file without related expansion.

### Step 6 — Tier 4 On-Demand

Read `routing-index.md` → `## tier-4 trigger-map (on-demand)`.
Use the same standalone word/phrase/API-symbol matching rule. Load a
tier-4 file only on direct keyword match, or if named in the initial selection
set's `related:` list. Never expand from foundations, newly related files, or
directly matched tier-4 files. These are niche — avoid loading broadly.

### Step 7 — Answer or enforce

For explicitly requested enforcement, carry out `references/enforce.md` using
the loaded source guidance. Ordinary guidance never starts that procedure.

For an ordinary guidance answer, quote the short operative source clause verbatim
with all qualifiers intact, then give only the needed application. A compact
table works for multiple states. Keep the rule and application distinct;
do not paraphrase the quotation into a stronger, broader, or narrower rule.
Before sending, delete sentences that do not answer a requested part.
Check the actor, starting state, action and resulting state; do not substitute
a similar neighboring scenario. Mention an API as the implementation of a
rule only when the loaded source supports that relationship.

Do not add unrequested adjacent rules or measurements merely because they are
loaded. Preserve the source's full scope: do not invent narrower device/state
limits when applying a rule, and include every requested state it covers.

Apply the guidance for the named platform, device, orientation, and state.
An explicit scoped exception takes precedence over a broader rule within that scope;
apply that exception only to its stated platform, device and state.
Do not invent a reconciliation for unresolved source conflicts; identify the conflict.
Apply all other compatible loaded content. If a topic isn't covered by loaded files,
load the specific relevant reference before answering; keep unrelated expansion bounded.

---

## Non-Negotiables

- **Cite exact values.** State pt sizes, pixel densities, margins, and
  timing values as they appear in the distilled files. Preserve source
  ranges and approximation qualifiers; do not invent or round values.
- **Distinguish platforms.** When behavior differs across platforms,
  state each platform's rule explicitly. Never flatten to "generally."
- **Preserve recommendation strength.** Keep must, prefer, consider, examples, conditions, and exceptions distinct when answering; do not turn an optional recommendation into a requirement.
- **Preserve logical conditions.** Keep conjunctions and alternatives intact. A consequence stated for A and B does not establish the same consequence for either alone; an A-or-B option does not require both. Check the claim in the answer as well as its supporting clause.
- **No invention.** Every Apple rule, measurement, and API recommendation must
  trace to a loaded reference. Distinguish Apple guidance from your own design
  choices. If unsure, say so and name the source.
- **Terse and direct.** Keep ordinary guidance focused on the requested rule.

---

## File Locations

- Distilled reference files: `references/hig/[topic].md`
- Routing index: `routing-index.md`
- Opt-in enforcement procedure: `references/enforce.md`
- Guided iPhone Duo redesign: `references/duo.md`, `references/duo-checklist.md`;
  `/duo` slash command (install it with the skill): `commands/duo.md`
- Frontmatter schema: each distilled file contains `topic`, `tier`,
  `platforms`, `category`, `triggers`, and `related` fields.
