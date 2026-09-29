---
topic: shareplay
tier: 3
platforms: [ios, ipados, macos, tvos, visionos]
category: technologies
triggers:
  - "SharePlay"
  - "Group Activities"
  - "GroupActivities"
  - "SystemCoordinator"
  - "SpatialTemplatePreference"
  - "shared experience"
  - "FaceTime activity"
related:
  - collaboration-and-sharing
---

# SharePlay

SharePlay lets people do your app's activities together in real time from their own devices, synced by the system alongside FaceTime or Messages.

Activities start from an in-app control, a FaceTime call or a shared link. The system asks participants to open your app, invites those without it to download it, and prompts anyone lacking purchased or subscription content to get their own.

## Best practices

- **Use SharePlay for real-time experiences.** For asynchronous collaboration too, let people share or save the activity afterward.
- **Fit the experience to the activity**: one shared view for watching or browsing; per-role views where richer, as in games.
- **Design activities that work across Apple platforms**, devices and communication methods.
- **Make it easy to start a shared activity** with a recognizable control, like a button with the SharePlay symbol. People can also use the share sheet.
- **Let people join without friction.** Go straight to shared content, without unrelated views. Handle required sign-in, download or subscription in a self-dismissing view; offer nonsubscribers provisional access or support Family Sharing. Defer nonessential steps like profile setup.
- **Describe activities clearly and concisely** in invitations (movie: title, summary, poster) to avoid truncation.
- **Keep people oriented as an activity changes**: when one person's action affects everyone, show why. The system can sync media playback (one pause pauses all); otherwise show who's doing what with in-app cues.
- **Use the term *SharePlay* correctly**: as a noun ("Join SharePlay") or a verb in an action ("SharePlay Movie"). Don't add adjectives (like *virtual* or *spatial* in visionOS) or variations (*SharePlayed*, *SharePlays*, *SharePlaying*).

## Platform considerations

No additional considerations for tvOS. Not supported in watchOS.

### iOS, iPadOS, macOS

**Support Picture in Picture for shared video**: a PiP window on iPhone and iPad; on Mac, a window people bring forward.

### visionOS

The Share button beside the window bar mirrors standard windows by default; adopt SharePlay to share volumetric windows and immersive content. The system's *shared context* puts content in the same relative location for everyone. Align windows and volumes across devices; position 3D objects, sounds and interactions to reinforce togetherness.

- **Prefer starting your experience from a window**; one starting in an immersive space needs custom start UI.
- **Resolve conflicts naturally.** If only one person can use something at a time, avoid UI for taking control; let people speak or gesture for a turn. Consider a simple rule like last change wins.
- **Reserve unique views for moments that call for them.** In general, sync views and immersion levels. When someone enters a personal immersive view, show a contact photo instead of their spatial Persona and keep FaceTime Audio going.
- **Let people opt in to immersion changes mid-task.** Your app can bring everyone along when one person changes immersion, but if that would interrupt someone, such as a person busy in another window, prompt them to join when ready; others transition right away.
- **Let participants customize for comfort and accessibility**; keep settings like volume and subtitles per participant.
- **Make it easy to leave and rejoin** with a clear rejoin control. A windowed version lets people multitask while staying connected.

#### Personas

Remote Vision Pro users appear as spatial Personas, which can make eye contact, gesture and move, or contact photos without one; iPhone, iPad, Mac and Apple TV users, in a 2D video window. Vision Pro users in one room see each other through passthrough, with content in the same physical spot. **Support people without a spatial Persona** (other devices, Persona off, windowed FaceTime): if your experience relies on facial expressions or gestures, offer UI alternatives.

#### Spatial templates

A *spatial template* automatically seats participants, setting where each appears and faces. Adopt the best-fitting system template, or a custom one if none fits.

|Template|Layout|Suits|
|---|---|---|
|Side-by-side|Curve facing content; less nonverbal interaction|Watching together|
|Surround|Circle around content, facing each other; more verbal and nonverbal interaction|Tabletop games, centralized or 3D or per-person content|
|Conversational|Circle, content on its edge; not all can easily interact|Consider for togetherness while the app works in the background, like music|

- **Divide a complex activity into stages**, each with a suitable template (teams, then play); a system and custom mix is preferable to one complex custom template.
- **Let people initiate template transitions** through an explicit action, like choosing a team.
- **Keep template transitions smooth and infrequent**, without excessive movement. When moving someone's seat or role, fade out and in, then give reorienting cues.

#### Custom templates

Seats apply only to visionOS spatial Personas; others join seatless.

- **Account for people who are physically together**: templates can seat remote Personas but can't move people in the room. If positions matter, use cues like position markers.
- **Orient seats for your content**: they face its center by default; set direction with `SpatialTemplateSeatElement`.
- **Support the maximum number of seats**: include five (the spatial Persona limit) whenever your activity allows. Define every seat up front and keep seats after people leave. With a participant limit, consider spectator seats.
- **Place seats at least a meter apart**; a Persona too close to another becomes a contact photo.
- **Define the order in which people take seats.** Seats fill in join order; keep partial arrangements balanced (left to right may not be).
- **Keep roles (player, spectator, team member) independent of seats**; they must work for seatless and same-room people (`isSpatial`, `isNearbyWithLocalParticipant`). Let people take any open seat; reserve a spot only for a role that truly requires it, like a host at a table's head.

## Resources

Developer: `GroupActivities`, `spatialTemplatePreference`.

Source: [SharePlay](https://developer.apple.com/design/human-interface-guidelines/shareplay), captured 2026-09-12.
