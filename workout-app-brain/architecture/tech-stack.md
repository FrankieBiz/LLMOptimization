---
tags: [architecture, decision]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Tech Stack

**The confirmed technology choices for the workout tracking and scheduling app.**

## Mobile Framework
- **TBD** — Confirm between React Native and Flutter before starting UI work
- React Native: TypeScript-native, larger ecosystem, easier web port
- Flutter: Better perf on low-end Android, single codebase, Dart language

## Language
- **TypeScript** (strict mode) — all application code
- Strict settings: `"strict": true`, `"noUncheckedIndexedAccess": true`

## State Management
- **TBD** — Confirm between Zustand, Redux Toolkit, or Jotai
- Leaning toward Zustand for simplicity + offline-first patterns

## Local Database
- **SQLite via expo-sqlite or Watermelon DB** — for offline-first data
- Watermelon preferred for reactive queries and lazy loading

## Backend / Sync
- **TBD** — Options: Supabase, Firebase, custom REST API
- Must support offline-first with conflict resolution

## API Client
- **Axios** or native fetch with a centralized service wrapper in `src/services/`

## Testing
- **Jest** + **React Native Testing Library** for unit/integration
- **Detox** for E2E (future)

## Build & Tooling
- **Expo** (managed or bare workflow) — simplifies cross-platform builds
- **EAS Build** for CI/CD

## Related
- [[data-models]]
- [[api-design]]
- [[state-management]]
- [[offline-sync-strategy]]
