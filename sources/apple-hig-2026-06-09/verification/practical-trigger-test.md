# Practical Trigger Test

Date: 2026-06-09

Artifact under test: `apple-hig` runtime skill contents from the `ios27` branch.

## Method

Each case used the production-style wrapper:

> Use the apple-hig skill. First list "Loaded HIG files" as slugs only, then answer the question with exact HIG-backed guidance. If a needed file was not loaded, say which one.

Observed loaded files were computed by applying the installed `SKILL.md` protocol:

1. Load all tier-1 files.
2. Detect platform triggers.
3. Match tier-3 and tier-4 triggers as standalone words, phrases, or API symbols.
4. Expand one hop through `related:` frontmatter for tier-2 and tier-3 files.

## Pre-Fix Finding

An initial literal substring harness exposed false positives:

- `AR` matched inside "tab bar".
- `AI` matched inside "explain" and "detail".
- `graph` matched inside "typography".
- `pan` matched inside "panels".
- Broad triggers `guide` and `review` matched ordinary prose instead of HIG concepts.

Remediation:

- `SKILL.md` now requires standalone word/phrase/API-symbol matching, not arbitrary substring matching.
- `live-viewing-apps.md` changed `guide` to `program guide` and `channel guide`.
- `ratings-and-reviews.md` removed standalone `review`.
- `routing-index.md` was regenerated.

## Results

### 1. Design Principles Without Apple Mention

Prompt: "I'm designing a general productivity interface, not specifically for Apple. What design principles should guide the experience?"

Expected: tier-1 bundle only, especially `design-principles`, `accessibility`, `inclusion`, `privacy`, `writing`, `layout`.

Observed loaded files: `accessibility`, `branding`, `color`, `dark-mode`, `design-principles`, `icons`, `images`, `inclusion`, `layout`, `materials`, `motion`, `privacy`, `right-to-left`, `sf-symbols`, `typography`, `writing`.

Trigger result: pass.

Answer quality result: pass. `design-principles.md` provides the expected Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, and Delight guidance. Tier-1 support covers accessibility, privacy, layout, color, typography, and writing.

### 2. iOS Tab Bar / Liquid Glass

Prompt: "For an iOS app, review a bottom navigation design with four tabs, a Liquid Glass tab bar, customization, and minimize-on-scroll behavior."

Expected: tier-1 bundle, `designing-for-ios`, `tab-bars`, plus related files such as `sidebars`.

Observed loaded files: `accessibility`, `branding`, `color`, `dark-mode`, `design-principles`, `icons`, `images`, `inclusion`, `layout`, `materials`, `motion`, `privacy`, `right-to-left`, `sf-symbols`, `typography`, `writing`, `designing-for-ios`, `tab-bars`, `gestures`, `multitasking`, `sidebars`, `tab-views`, `toolbars`, `focus-and-selection`.

Trigger result: pass.

Answer quality result: pass. `tab-bars.md` covers navigation-only tab bars, no hidden/disabled tab buttons, Liquid Glass bottom floating tab bars, minimize-on-scroll accessory behavior, and customization guidance. `designing-for-ios.md` adds reachability guidance.

### 3. Wallet / Apple Pay / Tap to Pay

Prompt: "For an iPhone checkout and Wallet experience, explain when to use Apple Pay, a Wallet pass, pass fields and dates, change messages, and Tap to Pay on iPhone."

Expected: tier-1 bundle, `designing-for-ios`, `apple-pay`, `wallet`, `tap-to-pay-on-iphone`, plus related expansion.

Observed loaded files: `accessibility`, `branding`, `color`, `dark-mode`, `design-principles`, `icons`, `images`, `inclusion`, `layout`, `materials`, `motion`, `privacy`, `right-to-left`, `sf-symbols`, `typography`, `writing`, `designing-for-ios`, `apple-pay`, `gestures`, `tap-to-pay-on-iphone`, `wallet`, `multitasking`, `in-app-purchase`, `drag-and-drop`, `feedback`, `nfc`, `id-verifier`.

Trigger result: pass.

Answer quality result: pass. `apple-pay.md` distinguishes Apple Pay from In-App Purchase, requires Apple Pay to be at least as prominent as other payment options, and covers button usage. `wallet.md` includes expiration/relevant date/voided properties, time-critical-only change messages, and pass field roles. `tap-to-pay-on-iphone.md` covers setup, checkout option, finalizing amount first, and button labeling.

### 4. macOS Sidebar Navigation

Prompt: "Review a macOS document app that uses a sidebar, NavigationSplitView, toolbar actions, and a detail editor."

Expected: tier-1 bundle, `designing-for-macos`, `sidebars`, `split-views`, `toolbars`, possibly `the-menu-bar` or `controls` through related expansion.

Observed loaded files: `accessibility`, `branding`, `color`, `dark-mode`, `design-principles`, `icons`, `images`, `inclusion`, `layout`, `materials`, `motion`, `privacy`, `right-to-left`, `sf-symbols`, `typography`, `writing`, `designing-for-macos`, `file-management`, `sidebars`, `split-views`, `toolbars`, `the-menu-bar`, `windows`, `icloud`, `drag-and-drop`, `undo-and-redo`, `tab-bars`, `buttons`, `search-fields`.

Trigger result: pass. `file-management` is an acceptable direct trigger from "document app"; other extras are related expansions.

Answer quality result: pass. `sidebars.md` covers leading-side navigation, customization, hiding, max two hierarchy levels, macOS sidebar size, and auto-collapse. `split-views.md` covers sidebar/list/detail pane relationships and current-selection highlighting. `toolbars.md` distinguishes toolbar actions from tab-bar navigation and covers customization/overflow.

### 5. visionOS Spatial Layout

Prompt: "In visionOS, where should a floating video player, controls, and secondary panels live in a shared spatial experience?"

Expected: tier-1 bundle, `designing-for-visionos`, `spatial-layout`, `windows`, `playing-video`, `immersive-experiences` if triggered or related.

Observed loaded files: `accessibility`, `branding`, `color`, `dark-mode`, `design-principles`, `icons`, `images`, `inclusion`, `layout`, `materials`, `motion`, `privacy`, `right-to-left`, `sf-symbols`, `typography`, `writing`, `designing-for-visionos`, `playing-video`, `windows`, `spatial-layout`, `immersive-experiences`, `digital-crown`, `shareplay`, `gestures`, `eyes`, `playing-audio`, `live-viewing-apps`, `going-full-screen`.

Trigger result: pass. `spatial-layout`, `windows`, and `immersive-experiences` arrive through `designing-for-visionos` related expansion, which is expected.

Answer quality result: pass. `designing-for-visionos.md` covers Shared Space vs. Full Space and standard windows for UI-centric tasks. `spatial-layout.md` covers depth, dynamic scale, avoiding too many windows, Digital Crown recentering, and avoiding control overlap. `windows.md` covers default windows, volumes, and ornaments.

### 6. Widget Accessibility / Rendering

Prompt: "Audit a WidgetKit widget that uses rasterized text, custom typography, configurable content, Dynamic Type, and light/dark full-color rendering."

Expected: tier-1 bundle, `widgets`, with tier-1 support from `typography`, `accessibility`, `dark-mode`, `color`, and `writing`.

Observed loaded files: `accessibility`, `branding`, `color`, `dark-mode`, `design-principles`, `icons`, `images`, `inclusion`, `layout`, `materials`, `motion`, `privacy`, `right-to-left`, `sf-symbols`, `typography`, `writing`, `labels`, `widgets`, `text-views`, `live-activities`, `complications`.

Trigger result: pass. `labels` is acceptable from the standalone `text` trigger and expands to `text-views`; `widgets` provides the target guidance.

Answer quality result: pass. `widgets.md` covers avoiding rasterized text, Dynamic Type support from Large through AX5 on iOS/iPadOS/visionOS, choosing automatic vs. configurable content intentionally, and supporting light/dark appearances for full-color rendering.

## Summary

Post-remediation practical trigger results: 6 pass, 0 partial, 0 fail.

Answer quality results: 6 pass, 0 partial, 0 fail.

Release implication: the runtime skill works as expected for these six production-style probes after tightening trigger matching and broad trigger terms.
