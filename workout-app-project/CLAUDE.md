# CLAUDE.md — Project Instructions for Claude Code

## Project
Workout tracking and scheduling mobile app.
Language: TypeScript (strict mode) | Framework: React Native (confirm before UI work)

## Knowledge Base
My Obsidian vault at `C:\Users\frank.DESKTOP-8VOID7R\Documents\workout-app-brain` contains:
- Architecture decisions in `architecture/`
- Feature specs in `features/`
- Known bugs and solutions in `bugs/`
- Reusable code patterns in `snippets/`
- Tested prompts in `prompts/`

**Before implementing any feature:** check `features/` for the spec.
**Before debugging:** check `bugs/` for known solutions.
**After solving a bug:** create a note in `bugs/` documenting the root cause and fix.
**After an architecture decision:** update the relevant note in `architecture/`.

## Code Standards
- TypeScript strict mode everywhere — no `any` types
- Functional components with hooks — no class components
- All services in `src/services/`, all types in `src/models/`
- All custom hooks in `src/hooks/`
- Test files colocated: `Component.tsx` → `Component.test.tsx`
- No magic numbers — constants go in `src/constants/`
- Commit messages follow Conventional Commits format (`feat:`, `fix:`, `refactor:`, etc.)

## Data Rules (Non-Negotiable)
- **Offline-first**: always write to local DB before any network call
- **Soft-delete only**: use `deletedAt` timestamp — never hard-delete workout data
- **Timestamps**: ISO 8601 with timezone offset (`2026-04-08T14:30:00-05:00`)
- **Weight**: stored in kg internally; convert to user-preferred unit at render time

## Workflow
1. Read the relevant feature spec from `workout-app-brain/features/`
2. Check `workout-app-brain/architecture/` for constraints
3. Check `workout-app-brain/snippets/` for existing patterns
4. Implement with tests
5. Update the Obsidian vault with any new decisions or patterns

## Model Selection (Antigravity)
| Task | Use |
|------|-----|
| Multi-file refactoring | Claude (cloud) |
| New feature scaffold | Claude (cloud) |
| Bug fix in a single file | Gemma 4 E4B (local) |
| Write unit tests | Gemma 4 E4B (local) |
| Code review | Claude (cloud) |
| Boilerplate / templates | Gemma 4 E4B (local) |
