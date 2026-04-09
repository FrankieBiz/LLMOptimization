# SCHEMA.md — Vault Conventions

## Note Frontmatter Template
Every note should have YAML frontmatter:
```yaml
---
tags: [feature, v1]
created: 2026-04-08
updated: 2026-04-08
status: active | completed | archived
---
```

## Status Definitions
- `active` — Currently being worked on or referenced
- `completed` — Done, kept for reference
- `archived` — No longer relevant, kept for history

## Linking Rules
- Architecture notes link to features they support
- Bug notes link to the feature and the code file affected
- Sprint notes link to all features included in that sprint

## AI Maintenance Tasks
When asked to "maintain the vault" or "clean up":
1. Check all notes for missing frontmatter — add it
2. Check for broken [[wiki links]] — fix or flag them
3. Update `index.md` with any new notes
4. Flag notes with `updated` older than 30 days for review
