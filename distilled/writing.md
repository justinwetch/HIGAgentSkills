---
topic: writing
tier: 1
platforms: [ios, ipados, macos, tvos, visionos, watchos]
category: foundations
triggers:
  - "copy"
  - "tone"
  - "voice"
  - "writing style"
  - "label"
  - "placeholder"
  - "alert text"
related:
  - inclusion
  - accessibility
  - voiceover
  - notifications
  - alerts
  - action-sheets
  - settings
  - text-fields
---
# Writing

> The words in your app are an essential part of the user experience — design through the lens of language.

**Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

## Getting Started

- **Define your app's voice.** Determine vocabulary and tone that aligns with your app's values and resonates with your audience. Create a reference list of common terms for consistency.
- **Match tone to context.** Vary tone based on what the person is doing (exercising and hit a goal vs. facing a payment error). Situational context affects both the words and how they're displayed.
- **Be clear.** Every word should earn its place. If you can use fewer words, do so. Read your writing aloud.
- **Write for everyone.** Use plain, simple language. Write with accessibility and localization in mind — avoid jargon and gendered terminology.

## Best Practices

**Screen structure:**
- Put the most important information first.
- Format text for easy reading.
- If conveying multiple ideas, consider splitting across screens. Think about information flow across the whole sequence.

**Labels and actions:**
- Use active voice and verb-based button/link labels ("Send" over "Let's do it!").
- For links, use descriptive text over "Click here" ("Learn more about X") — critical for screen readers.

**Consistency:**
- Build reusable language patterns. Consistency creates familiarity and coherence.
- Choose capitalization style per UI element type (title case = formal; sentence case = casual) and apply it everywhere.

**Multi-step flows:**
- Use "Get Started" to open a flow, "Continue" or "Next" between steps (pick one and be consistent), and "Done" to close it.

**Pronouns:**
- Prefer "Favorites" over "Your Favorites" — possessives are often unnecessary.
- Avoid "we" in error messages ("We're having trouble loading" → "Unable to load content").
- If using "my"/"your", be consistent and don't switch perspective.

**Device-specific language:**
- Use "tap" for touch devices (iPhone, iPad, Apple Watch), not "click."
- Small screens (iPhone, Watch): maximize brevity. Large screens (TV): also requires brevity — text must be large to read from a distance. TV is often a shared screen — consider who you're addressing.

**Empty states:**
- Provide clear next steps and an action (button or link). Empty states are temporary — don't put crucial info there.

**Error messages:**
- Help people avoid errors first.
- Display errors close to the problem. Avoid blame. Be specific about the fix.
- "Choose a password with at least 8 characters" > "That password is too short."
- Avoid interjections ("oops!", "uh-oh") — unnecessary and can seem insincere.

**Settings labels:**
- Be as practical as possible. Add a description only if the label isn't sufficient.
- Describe what the setting does when ON — people infer the OFF state.
- Provide a direct link/button to navigate to settings rather than describing the location.

**Text fields:**
- Label all fields clearly.
- Use hint/placeholder text to show format ("name@example.com" or "Your name").
- Show errors next to the field. Frame positively: "Use only letters for your name" > "Don't use numbers or symbols." Avoid robotic messages like "Invalid name."

**Delivery method:**
- Match urgency, importance, and context to the right delivery mechanism. See: notifications, alerts, action-sheets.

## Platform Considerations

*No additional considerations for any platform.*
