---
tags: [feature, v2]
created: 2026-04-08
updated: 2026-04-08
status: active
priority: P2
---

# Progress Analytics

**Summary:** Visualizes workout history with charts for volume, frequency, and personal records over time.

## User Story
As a user, I want to see charts of my strength progress over time so that I can understand whether my training is working.

## Acceptance Criteria
- [ ] Per-exercise progress chart (weight over time)
- [ ] Volume chart (total weight × reps per session)
- [ ] Workout frequency chart (sessions per week)
- [ ] Personal records list per exercise
- [ ] Date range filter (last 30 days, 90 days, 1 year, all time)
- [ ] PRs are automatically detected and celebrated when broken

## Data Model Changes
Uses existing `WorkoutSession`, `Set`, `PersonalRecord` from [[data-models]].
PRs stored in `personal_records` table — see data-models.md.

## API Changes
- `GET /progress` — aggregate stats
- `GET /progress/exercises/:id` — per-exercise history
- `GET /records` — all PRs
- See [[api-design]]

## UI/UX Notes
- Charts use Victory Native or Recharts (confirm)
- PR celebration: confetti animation + notification when a PR is broken
- Exercise selector to switch which exercise is being charted

## Technical Notes
- All calculations done locally from DB for offline support
- 1RM estimated using Epley formula: `weight × (1 + reps/30)`
- Volume = sum of (weight × reps) per session
- PRs recalculated on every set save — use a background job, not inline

## Related
- [[workout-tracking]]
- [[data-models]]
- [[notifications]]
