---
name: git-commit-formatter
description: Analyzes staged changes and writes Conventional Commits messages
triggers: [commit my changes, commit this, write a commit message, stage and commit]
---

# Git Commit Formatter

Analyzes staged changes and produces a well-structured Conventional Commits message.

## Conventional Commits Format
```
<type>(<scope>): <short summary>

[optional body]

[optional footer(s)]
```

## Types
| Type | When to use |
|------|------------|
| `feat` | New feature or capability |
| `fix` | Bug fix |
| `refactor` | Code change that isn't a fix or feature |
| `test` | Adding or updating tests |
| `docs` | Documentation only |
| `chore` | Build, config, dependency updates |
| `perf` | Performance improvement |
| `style` | Formatting, whitespace (no logic change) |

## Process
1. Run `git diff --staged` to see what's staged
2. Identify the primary change type and scope
3. Write a summary line: imperative mood, max 72 chars, no period
4. Add a body if the change needs context (why, not what)
5. Add breaking change footer if applicable: `BREAKING CHANGE: ...`

## Examples
```
feat(workout-tracking): add rest timer auto-start after set logging

fix(scheduling): correct timezone offset in next occurrence calculation

refactor(api-client): extract auth interceptor into separate module

test(useRestTimer): add coverage for pause/resume state transitions

BREAKING CHANGE: WorkoutSession.weight field renamed to weightKg
```

## Output Format
Provide the commit message in a code block, ready to copy-paste:
```
git commit -m "feat(scope): description"
```
Or for multi-line:
```
git commit -m "$(cat <<'EOF'
feat(scope): summary line

Body explaining context or why.

EOF
)"
```
