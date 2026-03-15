# apple-hig-skill

A Claude skill containing 150 distilled Apple Human Interface Guidelines reference files, structured for accurate, context-efficient design guidance across all Apple platforms.

## What This Is

The Apple HIG is authoritative and comprehensive, but its full text is too large and too prose-heavy to load directly into an agent's context. This skill addresses that by distilling each HIG topic into a compact, information-dense reference file that preserves every specific rule, measurement, API name, and platform distinction while stripping pedagogical scaffolding and redundant prose.

The result is a corpus that fits within a practical context budget and gives Claude precise, citable answers rather than paraphrased recollections.

## Coverage

| Tier | Role | Count |
|------|------|-------|
| 1 | Foundations (always loaded) | 14 files |
| 2 | Platform overviews | 7 files |
| 3 | Components, patterns, technologies | 100 files |
| 4 | Niche and platform-specific controls | 29 files |

**Total:** 150 files, 751 trigger keywords, ~130k tokens in the full corpus.

Platforms covered: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## How It Works

`SKILL.md` defines a 7-step loading protocol:

1. Parse the request for platform(s), component names, and framework references
2. Load all 14 tier-1 foundation files (always, every invocation)
3. Load the matching `designing-for-[platform]` file based on detected platform
4. Keyword-scan the request against `routing-index.md` and load all tier-3 matches
5. Expand one hop through each loaded file's `related:` frontmatter
6. Load tier-4 files only on direct keyword match
7. Answer citing exact values from loaded files

The `routing-index.md` file maps 751 trigger keywords to their corresponding reference files across all four tiers.

## File Structure

```
SKILL.md               Claude's entry point and loading protocol
routing-index.md       Keyword-to-file routing map (auto-generated)
distilled/             150 reference files, one per HIG topic
  *.md
```

Each `distilled/*.md` file includes YAML frontmatter with `topic`, `tier`, `platforms`, `category`, `triggers`, and `related` fields. Claude reads these fields to navigate the corpus without loading every file.

## Token Budget

The floor cost per invocation is approximately 21,400 tokens (tier-1 files plus the routing index). Typical queries load 20 to 30 files and land between 22,000 and 37,000 tokens, well within a 40,000-token practical budget on a 200k context window.

## Distillation Method

Each reference file was distilled from the corresponding Apple HIG source page, targeting a 75% reduction in word count. The compression preserved:

- Specific measurements, sizes, and spacing values
- API names, class names, and framework identifiers
- Platform distinctions and per-platform behavioral rules
- Do/do not rules stated as direct directives

Removed: introductory framing, change history, repetitive examples, and prose that restated rules already expressed concisely elsewhere.

Each compression pass was followed by an evaluation step to confirm that no substantive rules or specifications were lost, only extraneous prose. Files were only accepted when the distilled version could answer the same design questions as the source.

## Installation

Drop this directory into your Claude skills path. The skill triggers when a request involves Apple platform design, HIG components, specific measurements, or Apple framework integration.

## Attribution

Content distilled from the Apple Human Interface Guidelines, available at [developer.apple.com/design/human-interface-guidelines](https://developer.apple.com/design/human-interface-guidelines). This repository is an independent reference tool and is not affiliated with or endorsed by Apple Inc.
