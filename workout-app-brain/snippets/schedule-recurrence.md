---
tags: [snippet]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Schedule Recurrence Patterns

**Patterns for calculating recurring workout schedule dates using rrule.js.**

## Installation
```bash
npm install rrule
```

## Basic Weekly Recurrence
```typescript
import { RRule, RRuleSet } from 'rrule';

// Every Monday and Thursday at 7am
const rule = new RRule({
  freq: RRule.WEEKLY,
  byweekday: [RRule.MO, RRule.TH],
  dtstart: new Date(2026, 3, 8, 7, 0, 0),  // April 8 2026, 7:00am
  tzid: 'America/New_York',
});

// Get next 5 occurrences
const nextOccurrences = rule.all((date, i) => i < 5);

// Get next occurrence after now
const next = rule.after(new Date());
```

## Storing and Restoring Rules
```typescript
// Store as string in DB
const ruleString = rule.toString();
// e.g. "DTSTART;TZID=America/New_York:20260408T070000\nRRULE:FREQ=WEEKLY;BYDAY=MO,TH"

// Restore from string
const restored = RRule.fromString(ruleString);
const nextAfterNow = restored.after(new Date());
```

## Calculate Next Occurrence (Utility)
```typescript
// src/utils/scheduleUtils.ts
import { RRule } from 'rrule';

export function getNextOccurrence(rruleString: string): Date | null {
  try {
    const rule = RRule.fromString(rruleString);
    return rule.after(new Date()) ?? null;
  } catch {
    return null;
  }
}

export function getOccurrencesBetween(
  rruleString: string,
  start: Date,
  end: Date
): Date[] {
  const rule = RRule.fromString(rruleString);
  return rule.between(start, end, true);
}

export function isMissed(scheduledAt: Date, graceHours = 24): boolean {
  const now = new Date();
  const deadline = new Date(scheduledAt.getTime() + graceHours * 3600 * 1000);
  return now > deadline;
}
```

## Common RRULE Patterns
```typescript
// Every day
{ freq: RRule.DAILY }

// Every other week on Wednesday
{ freq: RRule.WEEKLY, interval: 2, byweekday: [RRule.WE] }

// Every Monday, Wednesday, Friday
{ freq: RRule.WEEKLY, byweekday: [RRule.MO, RRule.WE, RRule.FR] }

// First Monday of the month
{ freq: RRule.MONTHLY, byweekday: [RRule.MO.nth(1)] }
```

## Related
- [[scheduling-engine]]
- [[data-models]]
