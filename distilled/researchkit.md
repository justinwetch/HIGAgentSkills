---
topic: researchkit
tier: 4
platforms: [ios, ipados]
category: technologies
triggers:
  - "ResearchKit"
  - "clinical study"
  - "research app"
  - "consent"
  - "survey"
  - "active task"
related:
  - healthkit
  - carekit
---
# ResearchKit

> ResearchKit provides predesigned screens and transitions for building medical research apps. People can join, consent, contribute data, and track their participation on iOS and iPadOS.

**Platforms:** iOS, iPadOS *(not macOS, tvOS, visionOS, watchOS)*

> These guidelines are informational only — not legal advice. Consult an attorney for regulatory requirements.

## Onboarding (fixed order)

1. **Introduction** — Clearly describe the study's subject and purpose. Let existing participants log in and resume.
2. **Eligibility** — Determine eligibility as early as possible. Simple language, easy inputs. Don't ask for criteria unnecessary to your study.
3. **Informed Consent** — Break long consent forms into digestible sections (data gathering, benefits, risks, time commitment, withdrawal process). Use Learn More buttons for detail. Consider a quiz to test understanding. Collect signature and contact info; most research apps email a PDF copy.
4. **Permission Requests** — Ask for only the data critical to the study (location, Health, notifications). Explain clearly why each type of data is needed.

## Surveys

- Tell participants how many questions there are and how long the survey will take.
- **One screen per question.**
- Show progress through the survey.
- **Keep surveys short** — multiple short surveys > one long survey.
- For questions needing explanation: standard font for the question, slightly smaller font for explanatory text.
- Tell participants when the survey is complete.

## Active Tasks

- **Clear, simple instructions**: describe how to perform the task and any constraints (timing, environment).
- Make completion obvious.

## Dashboard and Profile

- **Profile screen**: lets participants change evolving data (weight, sleep habits), view upcoming activities, withdraw from the study, and access the consent document / privacy policy. Ideally accessible at all times.
- **Dashboard**: motivates participation with daily progress, weekly assessments, activity results, and (if appropriate) aggregated comparison results. Ideally accessible at all times.
