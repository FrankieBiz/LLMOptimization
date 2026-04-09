---
tags: [feature, v1]
created: 2026-04-08
updated: 2026-04-08
status: active
priority: P2
---

# Scheduling Engine

**Summary:** Allows users to schedule recurring workout sessions on a calendar with support for programs and custom recurrence rules.

## User Story
As a user, I want to schedule my workouts on specific days of the week so that I follow my training program consistently.

## Acceptance Criteria
- [ ] User can assign workouts to days of the week
- [ ] Supports simple recurrence (weekly, every N weeks)
- [ ] Scheduled sessions appear on a calendar view
- [ ] Missed sessions (not completed within 24h) are marked as missed
- [ ] User can skip a single occurrence without deleting the schedule
- [ ] Upcoming sessions display the planned exercises

## Data Model Changes
Uses [[data-models]] `Schedule` and `Program` types. RRULE format for recurrence.

## API Changes
- `GET/POST/PATCH/DELETE /schedules`
- `GET /programs` + `POST /programs`
- See [[api-design]]

## UI/UX Notes
- Weekly calendar strip on home screen showing upcoming sessions
- Tap a session to preview exercises or start it early
- Missed session shown in red; tapping allows logging it retroactively

## Technical Notes
- Recurrence calculated using `rrule.js` library
- Next occurrence stored in DB for efficient querying (updated after each occurrence)
- Timezone stored per-schedule using IANA format (e.g., "America/New_York")
- See [[snippets/schedule-recurrence]] for recurrence calculation patterns
- Background job checks for missed sessions daily at midnight local time

## Related
- [[workout-tracking]]
- [[notifications]]
- [[offline-sync-strategy]]
