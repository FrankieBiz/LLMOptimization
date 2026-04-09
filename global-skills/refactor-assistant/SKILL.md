---
name: refactor-assistant
description: Suggests and executes safe refactoring patterns
triggers: [refactor, clean up this code, simplify, extract function, split this file, reduce complexity]
---

# Refactor Assistant

Applies safe, targeted refactoring patterns. Always preserves behavior — no logic changes.

## Common Refactoring Patterns

### Extract Function
When a block of code is doing one clear thing — extract it:
```typescript
// Before
function processSession(session: WorkoutSession) {
  const totalVolume = session.sets.reduce((acc, set) => acc + set.weightKg * set.reps, 0);
  // ... more code
}

// After
function calculateSessionVolume(sets: Set[]): number {
  return sets.reduce((acc, set) => acc + set.weightKg * set.reps, 0);
}

function processSession(session: WorkoutSession) {
  const totalVolume = calculateSessionVolume(session.sets);
  // ... more code
}
```

### Reduce Complexity (Early Returns)
```typescript
// Before (arrow anti-pattern)
function getSessionStatus(session: WorkoutSession): string {
  if (session.completedAt) {
    return 'completed';
  } else {
    if (session.deletedAt) {
      return 'deleted';
    } else {
      return 'in-progress';
    }
  }
}

// After
function getSessionStatus(session: WorkoutSession): string {
  if (session.deletedAt) return 'deleted';
  if (session.completedAt) return 'completed';
  return 'in-progress';
}
```

### Split Large Files
If a file is doing too many things:
1. Identify distinct responsibilities
2. Create one file per responsibility
3. Export from an `index.ts` barrel
4. Update imports

### Magic Number Elimination
```typescript
// Before
if (now > scheduledAt + 86400000) { ... }

// After — in src/constants/scheduling.ts
export const MISSED_SESSION_GRACE_MS = 24 * 60 * 60 * 1000;

// In code
if (now > scheduledAt + MISSED_SESSION_GRACE_MS) { ... }
```

## Process
1. Identify the specific smell or complexity issue
2. Choose the appropriate pattern
3. Apply the refactoring
4. Confirm behavior is identical (run tests)
5. Update any affected imports

## Rules
- Never change behavior while refactoring
- One refactoring at a time
- Run tests before and after
- If no tests exist, write them first
