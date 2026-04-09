# AGENTS.md — Instructions for AI Agents

## Project Overview
This vault is the knowledge base for a workout tracking and scheduling mobile app.
The app lets users plan workouts, log exercises with sets/reps/weight, schedule
recurring sessions, and track progress over time.

## Vault Structure
- `architecture/` — System design decisions. READ THESE FIRST before making code changes.
- `features/` — Feature specifications. Each file is one feature with acceptance criteria.
- `bugs/` — Known bugs and their solutions. CHECK HERE before debugging to avoid re-solving.
- `research/` — External references. Articles, competitor analysis, API docs.
- `sprints/` — Sprint plans with priorities and deadlines.
- `snippets/` — Tested code patterns specific to this project. REUSE these.
- `prompts/` — Proven prompts for common tasks. Use these as starting points.

## Conventions
- All dates use ISO 8601 format (2026-04-08T14:30:00Z)
- Note titles use kebab-case: `workout-timer-logic.md`
- Every note starts with a one-line summary in bold
- Tags use format: #feature, #bug, #decision, #research, #snippet
- Link related notes with [[wiki links]]
- When you create or modify a note, update `log.md` with a one-line entry
- When you create a new wiki page, add it to `index.md`

## For Code Generation
- Language: TypeScript (strict mode)
- Confirm framework choice before generating UI code
- Reference `architecture/data-models.md` for all type definitions
- Reference `architecture/api-design.md` for endpoint patterns
- Check `snippets/` for existing patterns before writing new ones
- When solving a bug, create a note in `bugs/` with the solution

## For Feature Planning
- Use the template in `features/_template-feature.md`
- Include: user story, acceptance criteria, data model changes, API changes
- Link to relevant architecture notes

## Priority Stack (what matters most)
1. Offline-first — the app must work without internet
2. Performance — workout logging must feel instant
3. Data integrity — never lose a user's workout data
4. Clean code — maintainable, tested, typed
