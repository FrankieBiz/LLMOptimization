---
name: obsidian-sync
description: Reads from and writes to the Obsidian project vault
triggers: [update the vault, log this decision, create a bug note, update obsidian, add to vault, sync to obsidian]
---

# Obsidian Sync

Reads from and writes to the workout app Obsidian knowledge base.

## Vault Location
`C:\Users\frank.DESKTOP-8VOID7R\Documents\workout-app-brain`

## Always Read First
Before writing any vault note, read `AGENTS.md` and `SCHEMA.md` to confirm conventions.

## Common Operations

### Log a Decision (`log.md`)
Add an entry at the top of the log, newest-first:
```markdown
## 2026-04-08
- [Decision]: Chose Zustand over Redux for global state — simpler API, smaller bundle
```

### Create a Bug Note (`bugs/`)
Use `bugs/_template-bug.md` as the template.
File naming: `bugs/{YYYY-MM-DD}-{short-description}.md`
After creating: add to `index.md` under the Bugs section.

### Create a Feature Spec (`features/`)
Use `features/_template-feature.md` as the template.
File naming: `features/{feature-name}.md`
After creating: add to `index.md` under Features.

### Add a Snippet (`snippets/`)
File naming: `snippets/{pattern-name}.md`
Include: frontmatter, a bold summary line, code block, usage notes, related links.

### Update an Architecture Note (`architecture/`)
Locate the relevant file (tech-stack, data-models, api-design, etc.)
Add new content under an appropriate heading.
Update the `updated` date in frontmatter.
Add a log entry in `log.md`.

### Update `index.md`
When creating any new note, add it to `index.md` under the appropriate section:
```markdown
- [[new-note-name]] — One-line description
```

## Frontmatter Rules
Every note must have:
```yaml
---
tags: [feature|bug|architecture|snippet|prompt|sprint]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active|completed|archived
---
```

## After Any Write
1. Update `log.md` with a one-line entry
2. Update `index.md` if a new page was created
3. Update `updated` date in frontmatter of modified notes
