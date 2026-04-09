---
tags: [architecture, decision]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Data Models

**Core TypeScript interfaces and database schema for the workout app.**

## Core Types

```typescript
// An individual movement pattern (e.g. "Bench Press", "Back Squat")
interface Exercise {
  id: string;
  name: string;
  category: 'strength' | 'cardio' | 'mobility' | 'plyometric';
  muscleGroups: string[];
  equipment: string[];
  instructions?: string;
  createdAt: string;      // ISO 8601
  deletedAt?: string;     // soft-delete
}

// One group of reps within a workout
interface Set {
  id: string;
  exerciseId: string;
  weightKg: number;       // Always store in kg; convert for display
  reps: number;
  rpe?: number;           // Rate of Perceived Exertion (1-10)
  restSeconds?: number;
  completedAt: string;    // ISO 8601 with timezone offset
  notes?: string;
}

// A single training session
interface WorkoutSession {
  id: string;
  name?: string;
  sets: Set[];
  startedAt: string;      // ISO 8601
  completedAt?: string;   // null if in-progress
  notes?: string;
  programId?: string;     // null if ad-hoc
  scheduledSessionId?: string;
  deletedAt?: string;     // soft-delete
}

// A multi-week training plan
interface Program {
  id: string;
  name: string;
  description?: string;
  durationWeeks: number;
  sessions: ProgramSession[];
  createdAt: string;
  deletedAt?: string;
}

// A planned session within a program (template)
interface ProgramSession {
  id: string;
  programId: string;
  dayOfWeek: 0 | 1 | 2 | 3 | 4 | 5 | 6;  // 0 = Sunday
  name: string;
  plannedExercises: PlannedExercise[];
}

// A recurring calendar entry
interface Schedule {
  id: string;
  programSessionId?: string;
  name: string;
  recurrenceRule: string;   // iCal RRULE format
  nextOccurrence: string;   // ISO 8601
  timezone: string;         // IANA timezone (e.g. "America/New_York")
  active: boolean;
}

// Personal records per exercise
interface PersonalRecord {
  id: string;
  exerciseId: string;
  metric: 'max_weight' | 'max_reps' | 'estimated_1rm' | 'max_volume';
  value: number;
  setId: string;
  achievedAt: string;
}
```

## Data Integrity Rules
- Never hard-delete workout data — always use `deletedAt` timestamp
- Store weight as kg internally; derive display unit (kg/lbs) at render time
- All timestamps include timezone info for travel-aware tracking
- PRs are recalculated whenever a new set is logged

## Related
- [[api-design]]
- [[state-management]]
- [[offline-sync-strategy]]
