---
tags: [snippet]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Workout Timer Logic

**A state machine pattern for managing rest timers and active workout timing.**

## Rest Timer State Machine

```typescript
// src/hooks/useRestTimer.ts
import { useState, useEffect, useRef, useCallback } from 'react';

type TimerState = 'idle' | 'running' | 'paused' | 'complete';

interface UseRestTimerReturn {
  state: TimerState;
  remaining: number;        // seconds remaining
  elapsed: number;          // seconds elapsed
  start: (durationSeconds: number) => void;
  pause: () => void;
  resume: () => void;
  reset: () => void;
}

export function useRestTimer(): UseRestTimerReturn {
  const [state, setState] = useState<TimerState>('idle');
  const [remaining, setRemaining] = useState(0);
  const [elapsed, setElapsed] = useState(0);
  const durationRef = useRef(0);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const clear = () => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }
  };

  const start = useCallback((durationSeconds: number) => {
    clear();
    durationRef.current = durationSeconds;
    setRemaining(durationSeconds);
    setElapsed(0);
    setState('running');

    intervalRef.current = setInterval(() => {
      setElapsed((e) => {
        const newElapsed = e + 1;
        const newRemaining = durationSeconds - newElapsed;
        setRemaining(newRemaining);
        if (newRemaining <= 0) {
          clear();
          setState('complete');
        }
        return newElapsed;
      });
    }, 1000);
  }, []);

  const pause = useCallback(() => {
    clear();
    setState('paused');
  }, []);

  const resume = useCallback(() => {
    if (state !== 'paused') return;
    setState('running');
    const remainingAtPause = remaining;

    intervalRef.current = setInterval(() => {
      setRemaining((r) => {
        if (r <= 1) {
          clear();
          setState('complete');
          return 0;
        }
        return r - 1;
      });
      setElapsed((e) => e + 1);
    }, 1000);
  }, [state, remaining]);

  const reset = useCallback(() => {
    clear();
    setRemaining(0);
    setElapsed(0);
    setState('idle');
  }, []);

  useEffect(() => () => clear(), []);

  return { state, remaining, elapsed, start, pause, resume, reset };
}
```

## Usage
```typescript
const timer = useRestTimer();

// After logging a set:
timer.start(90); // 90 second rest

// In component:
<Text>{timer.remaining}s remaining</Text>
<Button onPress={timer.pause} title="Pause" />
```

## Notes
- Trigger `timer.start()` after every set log
- Show completion notification using `expo-notifications` when `state === 'complete'`
- Store `defaultRestSeconds` in user preferences (Zustand store)

## Related
- [[workout-tracking]]
- [[state-management]]
