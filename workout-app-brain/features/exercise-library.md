---
tags: [feature, v1]
created: 2026-04-08
updated: 2026-04-08
status: active
priority: P1
---

# Exercise Library

**Summary:** A searchable database of exercises that users can browse, filter, and add to workouts or create custom entries.

## User Story
As a user, I want to search and browse exercises filtered by muscle group or equipment so that I can quickly find the right exercise during a workout.

## Acceptance Criteria
- [ ] Pre-seeded library of 100+ common exercises
- [ ] Search by name (fuzzy search)
- [ ] Filter by category (strength, cardio, mobility)
- [ ] Filter by muscle group (chest, back, legs, etc.)
- [ ] Filter by equipment (barbell, dumbbell, bodyweight, etc.)
- [ ] User can create custom exercises
- [ ] Custom exercises appear alongside built-in ones
- [ ] Exercises can be soft-deleted (built-in ones are read-only)

## Data Model Changes
Uses [[data-models]] `Exercise` type. Seed data shipped with app bundle.

## API Changes
- `GET /exercises` — filterable list
- `POST /exercises` — create custom
- `DELETE /exercises/:id` — soft-delete custom only

## UI/UX Notes
- Full-screen search modal triggered from active workout
- Recent exercises shown first
- Exercise detail view shows instructions and muscle diagram (future)

## Technical Notes
- Built-in exercises seeded into local DB on first launch
- Custom exercises get a `userId` field to distinguish them
- Search uses local DB full-text search (SQLite FTS5)

## Related
- [[workout-tracking]]
- [[data-models]]
