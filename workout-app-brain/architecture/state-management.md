---
tags: [architecture, decision]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# State Management

**Client-side state strategy for the workout app.**

## Approach
Separate concerns into three layers:

1. **Server/Persisted State** — Data that lives in the local DB (WatermelonDB/SQLite)
   - Workout sessions, exercises, programs, schedules, PRs
   - Source of truth for all app data
   - Synced to backend when online

2. **UI State** — Ephemeral state that doesn't need to persist
   - Active workout timer state
   - Modal visibility
   - Form inputs in progress
   - Managed with React `useState` / `useReducer` locally in components

3. **Global App State** — Lightweight cross-component state
   - Current user, auth token, sync status, user preferences
   - Managed with **Zustand** store (or TBD — confirm before implementation)

## Zustand Store Structure (Draft)
```typescript
interface AppStore {
  // Auth
  user: User | null;
  authToken: string | null;
  setUser: (user: User, token: string) => void;
  logout: () => void;

  // Sync
  syncStatus: 'idle' | 'syncing' | 'error';
  lastSyncedAt: string | null;
  setSyncStatus: (status: SyncStatus) => void;

  // Preferences
  weightUnit: 'kg' | 'lbs';
  restTimerEnabled: boolean;
  defaultRestSeconds: number;
  setPreferences: (prefs: Partial<Preferences>) => void;
}
```

## Patterns
- Never store derived data in state — compute from source of truth
- WatermelonDB reactive queries handle data subscriptions automatically
- Use custom hooks to abstract data access: `useWorkoutSession(id)`, `useExercises()`
- All hooks live in `src/hooks/`

## Related
- [[tech-stack]]
- [[data-models]]
- [[offline-sync-strategy]]
