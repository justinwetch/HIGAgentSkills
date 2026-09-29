# apple-hig

![Apple HIG reference library](https://raw.githubusercontent.com/justinwetch/HIGAgentSkills/main/docs/readme-graphics/2026-09-12/01-header-light.png)

**157 source-reviewed Apple Human Interface Guidelines references, updated for iPhone Duo and OS 27**, with a guided `/duo` workflow that adapts an existing iOS app to the folding iPhone. Covers iOS, iPadOS, macOS, tvOS, visionOS and watchOS.

Release **2026-09-27** · Apple source snapshot **2026-09-12**.

[![Watch the demo](https://img.youtube.com/vi/jnD82EqZ2VQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=jnD82EqZ2VQ)

## Copy-paste install prompt

Copy and paste this message to your agent to have it install the skill and its `/duo` command for you.

```text
Install the apple-hig skill for me from https://github.com/justinwetch/HIGAgentSkills.git
It includes a required /duo slash command in commands/duo.md. If /duo isn't
available after installing the skill, copy that file into your custom slash-command
or custom prompt directory, then confirm /duo works.
```

## 2026-09-27 release: iPhone Duo and OS 27

Apple's September guideline update added a whole new page for the folding iPhone Duo and brought the rest of the HIG up to OS 27. This release brings the skill up to that snapshot (captured September 12) and adds help for the job most iOS teams will actually have this fall: taking an app they already ship and making it work on a phone that opens.

- **Duo mode.** `/duo` takes an existing iOS app through assessing its screens, matching them to Apple's Duo guidance, recommending changes for you to approve, and building them in SwiftUI or UIKit. It works in your app's own code and never draws web mockups (see "Redesign for iPhone Duo" below).
- **Current guidance.** All 157 references follow Apple's September 12 pages, including the iPhone Duo page on displays, poses, reserved regions and side-mounted bars, and the OS 27 changes elsewhere.
- **Lighter references.** The references were rewritten to about a third of Apple's wording overall (261,621 down to 90,027 words) while keeping exact values, conditions and how strongly Apple phrases each rule, so a request loads less context for the same answer.

Ordinary questions work the way they did in June, just against newer and smaller files. There's also a new opt-in enforce mode for independent review and repair (see "Enforce mode" below). If you installed the June release, replace the whole skill folder rather than merging, since the references moved from `distilled/` to `references/hig/`. The release assessment and verification live in the repository under `docs/release-2026-09-27/`.

## Manual install

Extract the ZIP's complete `apple-hig/` folder into your agent's skills directory, either for one project or for all local projects. Your agent's documentation names that location. Agents without skill discovery need explicit access to the extracted `SKILL.md` and its sibling files.

Keep `SKILL.md`, README, routing index, references, the `commands/` folder and the two helper scripts together. When upgrading, replace the old skill folder rather than merging files; check for another installed copy with the same name.

Then install the `/duo` command. Some agents pick up `commands/duo.md` from the skill folder on their own; others need the file copied into their custom slash-command or custom prompt directory (your agent's documentation names it). If `/duo` doesn't appear after a restart, copy it there.

Confirm the installation in your agent:

```text
Find the installed apple-hig skill. Read its SKILL.md and report its absolute
location, release version and supported modes, and whether /duo is available
as a slash command. Do not load the HIG references or start a review for this
setup check.
```

Expect release **2026-09-27**, ordinary HIG guidance, Duo mode with `/duo` available, and opt-in enforce mode. If the skill or `/duo` is missing, or the version differs, check the installation location and refresh/restart the host before using it. Automatic discovery has not been tested in every host.

There is no onboarding website, browser intake, dashboard or setup server. The agent works in your conversation and project. Ordinary guidance needs file access only. Python **3.10+** enables the optional routing helper and is required for enforce scoring; use the available `python3` or `python` executable.

## Use

```text
Use apple-hig to review the navigation and accessibility of this iOS app.
```

The agent loads 16 foundations, relevant platform/device and component references, and one hop of related guidance. The [routing helper](scripts/hig_route.py) resolves literal matches; the agent passes any explicit topic exclusions separately. File-only hosts follow the same protocol manually. Setup/help questions do not load the corpus.

Answers quote the operative source clause before applying it, preserving conditions, recommendation strength and exact specifications. Ordinary guidance never starts enforcement.

## Redesign for iPhone Duo

![/duo redesigns your app for iPhone Duo: an open iPhone Duo on a table showing a record library in four columns](https://raw.githubusercontent.com/justinwetch/HIGAgentSkills/main/docs/readme-graphics/2026-09-27/01-duo-open.png)

```text
/duo the library and reading flow
```

Duo mode walks one journey of an existing iOS app through fixed stages:

1. **Assess** the current screens, bars and layouts in your code.
2. **Match** them against Apple's iPhone Duo guidance and tech talks, with sources.
3. **Decide:** it recommends options and stops for your choices, offering SwiftUI previews first.
4. **Build** the changes natively, in Apple's order.
5. **Verify** them in the Device Hub iPhone Duo simulator where available.

It keeps a short `duo-notes.md` in your project so a later `/duo continue` picks up where it left off. It never makes HTML or web mockups, and it reports which checks it could not run.

`/duo` comes from `commands/duo.md`, installed with the skill (see "Manual install"). If it's missing, `Use apple-hig in Duo mode for <journey>` starts the same workflow while you fix the install. The [workflow](references/duo.md) and [checklist](references/duo-checklist.md) load only in Duo mode.

## Enforce mode (optional)

Ask for it by name ("Use apple-hig in enforce mode to review and fix this interface") and two independent reviewers score the interface against the HIG; the agent repairs what they find and re-reviews, for up to three cycles. A pass needs 90/100 or better, complete evidence and no unresolved material finding; otherwise the result is `needs changes` or `blocked`. It needs subagents, Python 3.10+ and a way to observe the actual artifact. The [procedure](references/enforce.md) and [data format](references/enforce-format.md) load only when enforcement is requested.

## Coverage and context

The references cut Apple's source guidance from **261,621 to 90,027 words (65.6% shorter)**. That is short of the ~75% target: fidelity took priority, so exact values, conditions, recommendation strength, API names and scoped exceptions were kept, and short rule-dense topics stop around 57–68%. All 157 topics passed independent source review; each topic rewritten in the September 23–24 redistillation was re-reviewed against Apple's source.

Complete reference files total **163,033 o200k_base / 162,491 cl100k_base tokens**. The 16 foundations total **27,096 / 26,936 tokens**, about 17% below June. Routing, entry-point instructions and selected topics add context; Duo mode adds its workflow and checklist only when it runs. These are static file counts, not measured per-request loads. Source review does not establish runtime behavior or native-device certification.

## Repository and packaging

`SKILL.md` is the entry point; `routing-index.md` maps requests to `references/hig/*.md`. The repository's `distilled/` directory preserves the June baseline and is not loaded or packaged. Source captures, review logs, work files and maintenance documentation are also excluded from the runtime ZIP.

The maintainer's `scripts/package_runtime_zip.py` builds a deterministic ZIP from an approved manifest. Package checks verify membership, hashes and local links; they do not certify app behavior. Compact corpus measurements and dispositions are retained under `docs/corpus-2026-09-12/` outside the package.

## Attribution

Distilled from [Apple's Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines). The Duo checklist also paraphrases Apple's iPhone Duo developer tech talks, linked in it. This independent project is not affiliated with or endorsed by Apple Inc. The enforce diagnostic workflow is informed by [shadcn/ui lint](https://github.com/shadcn-ui/lint); it uses HIG review and artifact evidence rather than adopting Tailwind-specific rules.
