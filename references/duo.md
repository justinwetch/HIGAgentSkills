# Duo mode: guided iPhone Duo redesign

Use this for `/duo [scope]`, `Use apple-hig in Duo mode …`, or an explicit request to adapt an existing app for iPhone Duo. Asking about the command, or ordinary Duo design questions, is ordinary guidance.

Duo mode moves one app through five fixed stages. Don't skip a stage, reorder them or merge them:

**0 Resume → 1 Assess → 2 Match → 3 Decide → 4 Build → 5 Verify**

Work in the user's app project and in its own stack. Stop only at the points marked **Stop**.

## Hard rules

- **Native only.** Never make HTML, SVG, CSS, canvas, web pages, browser prototypes or image mockups to show a design. That applies even as a fallback, and even to "illustrate" a direction.
  - Previews are the app's own UI, meaning SwiftUI previews, UIKit views, or a simulator run of real code.
  - If you can't make a native preview, describe the change in words and show the code diff.
- **Change the app itself.** Don't build a parallel demo app or a mock data layer. Keep existing features, state, content and visual identity unless the user asks to change them.
- **Cite, don't invent.** Every Apple rule comes from the loaded HIG files or [duo-checklist.md](duo-checklist.md), with its tag. Label your own product judgment as a recommendation.
- **Observed ≠ verified.** Code presence doesn't prove runtime behavior. A simulator doesn't prove on-device behavior, such as camera quality or real hinge angles. Say which checks you actually ran.
- **Stack scope.** This workflow targets native iOS apps (SwiftUI, UIKit, or both).
  - For a web or cross-platform app, say that vertical bars, reserved regions and arrangements are native iOS behaviors.
  - Then offer only the parts that map onto the app's framework: size-class-driven layout, safe areas, and keeping the fold clear.
  - Still no mockups.

## Load guidance

1. Follow SKILL.md Steps 1–6 for the user's request.
2. Add `designing-for-iphone-duo` and `designing-for-ios` to the initial set even if the request doesn't name the device, so Step 5 expands both files' `related:` lists once.
3. Read [duo-checklist.md](duo-checklist.md).
4. Load any other specific HIG topic only when the app's journey needs it, such as `sheets`, `search-fields` or `camera-control`. Don't expand its related list.

## Stage 0: Resume

Look for `duo-notes.md` in the app project root.

- **If it exists:** read it. Check whether the code named in its decisions has changed since, e.g. with `git log`/`git diff` for those files. Continue at its recorded stage from its **Next** line; completed stages aren't repeated unless that code changed.
- **If it doesn't exist:** fix the scope. Use the journey named in the arguments. Otherwise, pick the app's main journey (its first tab or root flow) and say which one you picked.
  - One journey per pass: typically 2–5 screens.
  - Create the notes file at the end of Stage 1.

Keep the notes file plain Markdown and under 50 lines, and update it at the end of every stage. It records outcomes, not the full inventory:

```markdown
# iPhone Duo redesign notes
Journey: <screens, in order>
Stack: <SwiftUI/UIKit, deployment target, SDK/Xcode seen>
Stage: <0–5>  Next: <one concrete action>

## Findings
- <screen/component>: Change|Decision — <one line> [source]
- Ready: <n>; N/A: <sections>

## Decisions
- <decision>: recommended <option>; chosen <option|pending> (<user|agent>, <date>) — <why in one line>

## Done / verified
- <change or check> — <how verified, or "not run">
```

Don't add hashes, JSON or extra files.

## Stage 1: Assess the current design

Read-only. Establish the facts before judging anything.

1. **Stack and build.** SwiftUI, UIKit or mixed; deployment target; whether the project already builds with Xcode/iOS 27.1 SDK. Whether Xcode and a simulator are available in this environment.
2. **Journey map.** For each screen, record:
   - its container (`NavigationStack`, `NavigationSplitView`, `TabView`, `UINavigationController`, `UISplitViewController`, `UITabBarController`, or custom);
   - how you get there;
   - which state must survive a display change (selection, draft text, scroll position, playback).
3. **Bars and items.** For each screen, record:
   - every toolbar, navigation-bar and tab-bar item, in order;
   - whether each has a title and a symbol (`Label`, or a `UIBarButtonItem` with title + image), or is text-only;
   - custom views in bars;
   - fixed spacers;
   - app-made "more" menus and their symbol;
   - custom bars (a hand-built `HStack` toolbar, a floating button, a `UIToolbar` the app manages itself);
   - sheets and their bar items.
4. **Layout risks.** Search the code for these, and note what each one controls:
   - fixed widths and frames;
   - `UIScreen.main` / `mainScreen`;
   - `userInterfaceIdiom` and orientation checks;
   - width breakpoints;
   - `ignoresSafeArea` on interactive content;
   - symmetric hard-coded padding;
   - centered fixed-size content;
   - custom side-by-side, stacked or layered splits (`HStack`/`VStack`/`ZStack` or custom container views);
   - locked orientations or `UIRequiresFullScreen`;
   - camera capture code;
   - multiwindow and scene support.
5. **Look at it if you can.** Use existing screenshots, SwiftUI previews or a simulator run. If you can't, say that the assessment is code-only.

Report to the user as a short screen-by-screen summary (under 15 lines) of what the journey is and what you found. Write the notes file, then continue. This isn't a stop.

## Stage 2: Match against Apple guidance

Walk every section of [duo-checklist.md](duo-checklist.md) in order against the Stage 1 inventory. Give each item one status:

- **Ready**: already meets the guidance. Say why in a few words.
- **Change**: the guidance is clear and the app doesn't meet it. Name the fix.
- **Decision**: Apple gives options, or the choice depends on the product.
- **N/A**: doesn't apply to this app (e.g., no camera). Say this once per section, not per item.

Each Ready, Change and Decision needs a source tag from the checklist. Where a listed tension applies, mark the item Decision and state both sides. Record the findings in the notes file.

## Stage 3: Decide and recommend

Present one compact table with every Decision item and the major Change items: **Item · Options · Recommendation · Why (source)**. The usual decisions are:

- **Inner display:** split view, width reflow, or tab bar as sidebar.
- **Outer layout for immersive screens:** inset, full-display, or mixed.
- **Compression per view:** toolbar first or tab bar first.
- **Visibility priorities:** which items stay last to overflow.
- **Vertical-bar opt-outs:** Calculator-like pages, single-button sheets.
- **Fold handling for custom layouts:** an arrangement or a displacement, and its destination.
- **Optional table-pose layout.**
- **Extras:** multiwindow, hinge effects, scene accessories, cameras.

Recommend one option per row. Keep product judgment separate from Apple's wording, and keep Apple's strength (consider/prefer/avoid). Group the clear Change items in one line each under the table as "will do unless you object".

Then offer native previews: "I can make SwiftUI previews of [screen] at compact and regular width before building, or go straight to the change." If previews can't render in this environment, say so in the offer.

Record each recommendation in the notes file as a pending decision, then **Stop** and wait for the user's choices. If the user said up front to use your judgment, record that and continue with your recommendations.

## Stage 4: Build natively

Implement in Apple's order. Do each step only if Stages 2–3 call for it, and keep changes minimal and in the app's existing style:

1. Build settings/SDK (report it; don't upgrade Xcode for the user).
2. Resizability fixes.
3. Move custom bars into managed bars.
4. Bar audit fixes.
5. Outer layout, inner display and sheets.
6. Fold handling.
7. Optional table-pose layout.
8. Chosen extras.

For each step:

- make the edit;
- build it if you can;
- update a SwiftUI `#Preview` where one exists or was requested (e.g., with `.environment(\.horizontalSizeClass, .compact)` and `.regular` variants);
- tick it in the notes file.

If a step turns out to need a new product decision, **Stop** and ask only that question.

Established SwiftUI and UIKit APIs are fine. For the iPhone Duo APIs new in iOS 27.1, use only those named in the loaded references or the checklist; it gives names, not signatures. Confirm each signature in the installed SDK or Apple's documentation, then guard it with `if #available(iOS 27.1, *)` / `@available` if the project targets earlier iOS. If you can't confirm it, don't guess: leave a clearly marked TODO naming the API and its intended effect. Say which changes are unbuilt.

Don't commit unless the user asks.

## Stage 5: Verify

Run what the environment allows, and report each check as **run: result** or **not run: why**:

- Build succeeds.
- The previews render.
- In the Device Hub iPhone Duo simulator (Xcode 27.1):
  - open, close, rotate and fold;
  - Split View on one side, then the other;
  - overflow in outer landscape, with the keyboard up, and with PiP;
  - Reduce Transparency;
  - right-to-left.
- The checklist's **Continuity checks** for each journey screen.
- The App Resizability skill in Xcode, if available.
- Camera preview and mirroring on a physical iPhone Duo. The simulator can't settle this.

Fix what fails and rerun that check.

Finish with a short summary to the user:
- what changed (files);
- what was decided;
- what was verified, and what wasn't;
- the next journey worth doing.

Set **Next** in the notes file.
