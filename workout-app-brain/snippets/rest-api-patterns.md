---
tags: [snippet]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# REST API Patterns

**Standard patterns for all API calls in this project. Use these — don't reinvent.**

## Base API Client
```typescript
// src/services/api/client.ts
import axios, { AxiosInstance, AxiosError } from 'axios';
import { useAppStore } from '@/store/appStore';

const BASE_URL = process.env.EXPO_PUBLIC_API_URL ?? 'https://api.workoutapp.com/v1';

export const apiClient: AxiosInstance = axios.create({
  baseURL: BASE_URL,
  timeout: 10_000,
  headers: { 'Content-Type': 'application/json' },
});

// Inject auth token on every request
apiClient.interceptors.request.use((config) => {
  const token = useAppStore.getState().authToken;
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Normalize errors
apiClient.interceptors.response.use(
  (response) => response,
  (error: AxiosError) => {
    const message =
      (error.response?.data as any)?.error?.message ?? error.message;
    return Promise.reject(new Error(message));
  }
);
```

## Service Pattern
```typescript
// src/services/sessionsService.ts
import { apiClient } from './api/client';
import type { WorkoutSession } from '@/models/WorkoutSession';

export const sessionsService = {
  async getAll(params?: { from?: string; to?: string }): Promise<WorkoutSession[]> {
    const { data } = await apiClient.get('/sessions', { params });
    return data;
  },

  async getById(id: string): Promise<WorkoutSession> {
    const { data } = await apiClient.get(`/sessions/${id}`);
    return data;
  },

  async create(payload: Partial<WorkoutSession>): Promise<WorkoutSession> {
    const { data } = await apiClient.post('/sessions', payload);
    return data;
  },

  async update(id: string, patch: Partial<WorkoutSession>): Promise<WorkoutSession> {
    const { data } = await apiClient.patch(`/sessions/${id}`, patch);
    return data;
  },

  async delete(id: string): Promise<void> {
    await apiClient.delete(`/sessions/${id}`);
  },
};
```

## Custom Hook Pattern (Data Fetching)
```typescript
// src/hooks/useWorkoutSession.ts
import { useState, useEffect } from 'react';
import { sessionsService } from '@/services/sessionsService';
import type { WorkoutSession } from '@/models/WorkoutSession';

export function useWorkoutSession(id: string) {
  const [session, setSession] = useState<WorkoutSession | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    setLoading(true);
    sessionsService.getById(id)
      .then(setSession)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [id]);

  return { session, loading, error };
}
```

## Notes
- All services live in `src/services/`
- All hooks live in `src/hooks/`
- Never call `apiClient` directly from components — always go through a service
- Writes go local DB first, then sync queue — don't await the network call

## Related
- [[api-design]]
- [[offline-sync-strategy]]
- [[state-management]]
