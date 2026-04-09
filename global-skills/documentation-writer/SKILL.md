---
name: documentation-writer
description: Generates JSDoc/TSDoc comments for functions, classes, and modules
triggers: [document this, add docs, add jsdoc, write documentation, add comments]
---

# Documentation Writer

Generates TSDoc comments for TypeScript functions, hooks, classes, and modules.

## TSDoc Format (TypeScript Standard)

### Function / Method
```typescript
/**
 * Calculates the estimated 1-rep max using the Epley formula.
 *
 * @param weightKg - The weight lifted in kilograms
 * @param reps - The number of reps performed
 * @returns The estimated 1RM in kilograms, or `null` if inputs are invalid
 *
 * @example
 * ```typescript
 * const estimated1RM = calculateEpley1RM(100, 5);
 * // → 116.67
 * ```
 */
export function calculateEpley1RM(weightKg: number, reps: number): number | null {
  if (weightKg <= 0 || reps <= 0) return null;
  return weightKg * (1 + reps / 30);
}
```

### Interface / Type
```typescript
/**
 * Represents a single training set within a workout session.
 *
 * @remarks
 * Weight is always stored in kilograms. Convert to the user's preferred
 * unit at render time using `convertWeight()`.
 */
export interface Set {
  /** Unique identifier (UUID) */
  id: string;
  /** ID of the exercise performed */
  exerciseId: string;
  /** Weight lifted, in kilograms */
  weightKg: number;
  /** Number of repetitions */
  reps: number;
  /** Rate of Perceived Exertion (1–10), optional */
  rpe?: number;
}
```

### React Component
```typescript
/**
 * Displays a summary card for a completed workout session.
 *
 * @param session - The workout session to display
 * @param onPress - Callback invoked with the session ID when the card is tapped
 */
export function WorkoutCard({ session, onPress }: WorkoutCardProps) { ... }
```

### Custom Hook
```typescript
/**
 * Manages rest timer state between sets.
 *
 * @returns Timer state, remaining seconds, and control functions (start, pause, resume, reset)
 *
 * @example
 * ```typescript
 * const { state, remaining, start } = useRestTimer();
 * // After logging a set:
 * start(90); // 90-second rest
 * ```
 */
export function useRestTimer(): UseRestTimerReturn { ... }
```

## Rules
- Every exported function, type, interface, and component gets a JSDoc comment
- Internal/private helpers: comment only if non-obvious
- `@param` for every parameter that isn't self-explanatory
- `@returns` always present for non-void functions
- `@example` for utility functions and hooks
- `@remarks` for important gotchas or constraints
- Keep comments accurate — outdated docs are worse than no docs
