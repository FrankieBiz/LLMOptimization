---
tags: [prompt]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Prompt: Feature Planning

**Use this prompt to have an AI agent plan out a new feature for the app.**

## Prompt Template
```
I want to plan a new feature for the workout tracking and scheduling app.

Feature idea: [describe the feature in 1-2 sentences]

Our tech context:
- TypeScript strict mode, React Native (or Flutter — TBD)
- Offline-first: local DB (WatermelonDB) writes first, background sync to server
- Existing data models: Exercise, Set, WorkoutSession, Program, Schedule, PersonalRecord
- See architecture/data-models.md and architecture/api-design.md for current conventions

Please produce a feature spec following this structure:
1. **User story** — As a [user], I want to [action] so that [benefit]
2. **Acceptance criteria** — Bulleted checklist, testable
3. **Data model changes** — New fields, types, or tables needed (if any)
4. **API changes** — New or modified endpoints (if any)
5. **UI/UX notes** — Key screens or interactions
6. **Technical notes** — Implementation approach, edge cases, risks
7. **Effort estimate** — Small / Medium / Large

Then ask me any clarifying questions you need before finalizing the spec.
```

## Related
- [[AGENTS.md]]
- [[features/_template-feature]]
- [[architecture/data-models]]
- [[architecture/api-design]]
