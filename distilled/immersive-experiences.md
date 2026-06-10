---
topic: immersive-experiences
tier: 3
platforms: [visionos]
category: patterns/visionos
triggers:
  - "immersive"
  - "Full Space"
  - "passthrough"
  - "environment"
  - "mixed immersion"
  - "ImmersionStyle.automatic"
  - "ImmersionStyle.mixed"
  - "ImmersionStyle.progressive"
  - "ImmersionStyle.full"
  - "SurroundingsEffect"
  - "SceneReconstructionProvider"
  - "CoordinateSpaceProtocol"
related:
  - spatial-layout
  - motion
  - accessibility
  - playing-audio
---
# Immersive Experiences

> In visionOS, apps can expand beyond windows into Full Space immersive experiences, partially or fully replacing passthrough.

**Platforms:** visionOS only

## Shared Space vs. Full Space

- **Shared Space**: app runs alongside others, like a Mac desktop. People can switch between apps naturally.
- **Full Space**: your app runs alone, hiding other experiences. Required for full-immersion styles.
- Apps can transition between Shared Space and Full Space fluidly at any time.

## Immersion Styles

Progressive immersion supports portrait and landscape orientations.

| Style | API | Where | Passthrough | Boundary |
|---|---|---|---|---|
| Dimmed/tinted passthrough | — | Shared Space or Full Space | Dimmed/tinted but visible | None |
| Mixed | `.mixed` | Full Space | Visible; nearby objects auto-dim content | None (system auto-dims near physical objects) |
| Progressive | `.progressive` | Full Space | Partial replacement by custom environment; Digital Crown adjustable (120°–360° or custom range) | ~1.5 m from head |
| Full | `.full` | Full Space | Completely replaced by 360° custom environment | ~1.5 m from head |

- **Tint color**: available in visionOS 2+. Prefer subtle colors — avoid bright/dramatic tints.
- **Boundary behavior** (progressive/full): as head approaches boundary, experience fades; beyond boundary, replaced by app icon; restored on return or Digital Crown recenter.

## Best Practices

Digital Crown: press and hold to recenter; double-click to briefly hide all content and show passthrough.

- **Offer multiple ways to use the experience** — support accessibility features and interaction alternatives; immersion must not require a single movement or input style.
- **Prefer launching in Shared Space or `.mixed`** — gives people more control; they choose when to deepen immersion.
- **Reserve immersion for meaningful moments** — not every task needs full immersion. Let people immerse in specific content, not the entire app.
- **Use subtle cues** (dimming, tinting, motion, scale, Spatial Audio) to draw attention, whether in a window or fully immersive.
- **Avoid `.progressive` or `.full` if people might need to move** beyond the 1.5m boundary.
- **Let people bring content to them** — don't require physical movement (important for accessibility and space constraints).
- **Don't obscure too much passthrough in `.mixed`** — if your content would substantially block someone's view, use `.full` or `.progressive` instead.
- **Adopt ARKit for blending with surroundings** (surface detection, hand positions) — requires user permission.

## Transitioning Between Styles

- **Smooth, predictable transitions** — gentle, not jarring or disorienting.
- **Let people choose when to enter/exit** — don't auto-enter a more immersive style unexpectedly.
- **Clear exit controls** — indicate whether they return to less immersive context or quit entirely. Offer pause/save if exiting also quits.

## Virtual Hands

When your Full Space app hides real hands and shows virtual hands:
- **Match familiar characteristics** — same positions and gestures as real hands.
- **Avoid oversized hands** — blocking content and awkward interaction.
- **On tracking interruption**: fade out virtual hands, reveal real hands. Fade back in when tracking resumes.

## Creating a Custom Environment

- **Minimize distracting content** — avoid high-contrast details or movement when people need to focus.
- **Distinguish interactive objects** by proximity — objects far away feel non-interactive; closer = more interactive.
- **Keep animation subtle** — small gentle movements. Avoid lots of motion near the field-of-view's edges.
- **Make the space expansive** — small restrictive environments cause discomfort/claustrophobia.
- **Spatial Audio for atmosphere** — avoid repetition or excessive looping. Lower/stop soundscape when people play their own audio.
- **Avoid flat 360° images** — prefer 3D meshes with lighting/shaders for realism and scale.
- **Always provide a ground plane mesh** — prevents floating sensation.
- **Minimize asset repetition** — reusing the same models frequently reduces realism.
