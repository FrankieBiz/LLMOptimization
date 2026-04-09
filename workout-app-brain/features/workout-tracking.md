---
tags: [feature, v1]
created: 2026-04-08
updated: 2026-04-08
status: active
priority: P1
---

# Workout Tracking

**Summary:** Allows users to start a workout session and log sets (exercise, weight, reps) in real time.

## User Story
As a user, I want to log my exercises with sets, reps, and weight during a workout so that I have an accurate record of what I lifted.

## Acceptance Criteria
- [ ] User can start a new workout session from the home screen
- [ ] User can search and add exercises from the library
- [ ] User can log sets with weight (kg/lbs), reps, and optional RPE
- [ ] Rest timer starts automatically after logging a set (configurable)
- [ ] User can complete or abandon a session
- [ ] Session is persisted locally immediately — no data loss if app closes
- [ ] Completed sessions appear in history

## Data Model Changes
Uses [[data-models]] types: `WorkoutSession`, `Set`, `Exercise` (no schema changes needed for MVP)

## API Changes
- `POST /sessions` — create session
- `PATCH /sessions/:id` — add sets, mark complete
- See [[api-design]]

## UI/UX Notes
- Active workout screen stays persistent (bottom tab or persistent banner)
- Swipe to delete a set
- Weight input defaults to last used weight for that exercise
- Timer displayed prominently during rest period

## Technical Notes
- Session must persist to local DB before any network call
- Workout state machine: `idle → active → completed | abandoned`
- Auto-save on every set logged
- Rest timer runs in background (use `expo-background-fetch` or similar)
- See [[snippets/workout-timer-logic]] for timer implementation

## Related
- [[exercise-library]]
- [[progress-analytics]]
- [[offline-sync-strategy]]
