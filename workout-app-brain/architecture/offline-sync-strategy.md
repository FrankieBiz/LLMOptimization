---
tags: [architecture, decision]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Offline Sync Strategy

**How the app handles data when offline and reconciles with the server when reconnected.**

## Core Principle
The app must be fully functional with zero internet connectivity. The network is an enhancement, not a requirement.

## Write Path (Local First)
1. User action triggers a mutation (e.g., log a set)
2. Write to local DB immediately → UI updates instantly
3. Mutation is added to the **sync queue** with a UUID and timestamp
4. Background sync worker picks up the queue and replays to server
5. Server acknowledges → queue entry marked complete
6. If server rejects → entry marked `error`, user notified

## Read Path
- All reads come from local DB
- Background sync pulls server changes periodically (configurable, default: 5min)
- Pull sync downloads only changes since `lastSyncedAt` timestamp

## Conflict Resolution
| Scenario | Resolution |
|----------|-----------|
| Same field updated locally + remotely | Last-write-wins (by timestamp) |
| Session sets | Append-only — no conflicts |
| Soft-delete vs edit | Soft-delete wins |
| Program/schedule edits | Server wins (manual conflicts flagged) |

## Sync Queue Schema
```typescript
interface SyncQueueEntry {
  id: string;             // UUID
  operation: 'CREATE' | 'UPDATE' | 'DELETE';
  entityType: 'session' | 'set' | 'exercise' | 'schedule';
  entityId: string;
  payload: Record<string, unknown>;
  createdAt: string;      // ISO 8601
  attempts: number;
  status: 'pending' | 'syncing' | 'complete' | 'error';
  lastError?: string;
}
```

## Connectivity Detection
- Use `@react-native-community/netinfo`
- On reconnect: trigger immediate sync queue flush
- Show sync status indicator in UI (syncing spinner, last synced time)

## Related
- [[api-design]] — `/sync/push` and `/sync/pull` endpoints
- [[data-models]]
- [[state-management]]
