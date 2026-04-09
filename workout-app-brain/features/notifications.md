---
tags: [feature, v2]
created: 2026-04-08
updated: 2026-04-08
status: active
priority: P3
---

# Notifications

**Summary:** Push notifications for scheduled workout reminders, rest timer completion, and personal record celebrations.

## User Story
As a user, I want to receive a reminder 30 minutes before my scheduled workout so that I don't forget to train.

## Acceptance Criteria
- [ ] Scheduled workout reminder (configurable lead time: 15min, 30min, 1hr)
- [ ] Rest timer completion notification (local)
- [ ] PR celebration notification
- [ ] All notifications can be individually enabled/disabled in settings
- [ ] Notification tapping deep-links to the relevant screen

## Data Model Changes
No new models. Notification preferences stored in user preferences in Zustand + persisted locally.

## API Changes
- `POST /users/push-token` — register device push token with server

## UI/UX Notes
- Notification settings screen under Profile
- Each notification type has a toggle
- Preview notification button to test

## Technical Notes
- Use `expo-notifications` for cross-platform local + push
- Local notifications (rest timer, PR) never require server
- Push notifications (workout reminders) scheduled server-side via push token
- On iOS: request notification permission at first scheduled workout creation

## Related
- [[scheduling-engine]]
- [[progress-analytics]]
- [[workout-tracking]]
