---
tags: [architecture, decision]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# API Design

**REST API conventions and endpoint patterns for the workout app.**

## Base URL
```
https://api.workoutapp.com/v1
```

## Conventions
- All requests/responses use JSON
- Auth via Bearer token in `Authorization` header
- Dates in ISO 8601 format in all payloads
- Soft-deleted records are excluded from list responses by default
- Pagination: `?page=1&limit=20` (cursor-based preferred for offline sync)
- Error format:
  ```json
  { "error": { "code": "WORKOUT_NOT_FOUND", "message": "..." } }
  ```

## Core Endpoints

### Exercises
```
GET    /exercises              List exercises (filterable by category, muscle group)
GET    /exercises/:id          Get single exercise
POST   /exercises              Create custom exercise
PATCH  /exercises/:id          Update exercise
DELETE /exercises/:id          Soft-delete exercise
```

### Workout Sessions
```
GET    /sessions               List sessions (filterable by date range)
GET    /sessions/:id           Get session with all sets
POST   /sessions               Start a new session
PATCH  /sessions/:id           Update session (add sets, mark complete)
DELETE /sessions/:id           Soft-delete session
```

### Programs & Schedules
```
GET    /programs               List programs
POST   /programs               Create program
GET    /programs/:id           Get program with sessions
PATCH  /programs/:id           Update program
DELETE /programs/:id           Archive program

GET    /schedules              List active schedules
POST   /schedules              Create schedule (links to program session)
PATCH  /schedules/:id          Update recurrence
DELETE /schedules/:id          Deactivate schedule
```

### Progress & PRs
```
GET    /progress               Aggregated progress stats (volume, frequency)
GET    /progress/exercises/:id History for one exercise
GET    /records                List all personal records
GET    /records/exercises/:id  PRs for one exercise
```

### Sync
```
POST   /sync/push              Push local changes to server (batch)
POST   /sync/pull              Pull server changes since timestamp
```

## Offline Sync Strategy
- Optimistic local writes first — always persist locally before network call
- Sync queue: all mutations are queued and replayed when connectivity returns
- Conflict resolution: last-write-wins on most fields; sets are append-only
- See [[offline-sync-strategy]] for full details

## Related
- [[data-models]]
- [[offline-sync-strategy]]
