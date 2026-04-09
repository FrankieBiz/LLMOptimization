---
tags: [prompt]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Prompt: Code Review

**Use this prompt when asking an AI agent to review code in this project.**

## Prompt Template
```
Review the following code from the workout tracking app.

Context:
- Language: TypeScript (strict mode)
- Framework: [React Native / Flutter — confirm]
- This code handles: [brief description]

Please review for:
1. **Bugs** — Logic errors, edge cases, null safety, off-by-one errors
2. **TypeScript** — Type safety, proper use of strict mode, any `any` types to eliminate
3. **Performance** — Unnecessary re-renders, N+1 queries, memory leaks, expensive operations in render
4. **Offline-first** — Is local DB written before any network call? Are failures handled gracefully?
5. **Data integrity** — Is soft-delete respected? Are timestamps in ISO 8601 with timezone?
6. **Code quality** — Is it readable? Is there dead code? Are magic numbers extracted to constants?

Format your response as:
- **Critical** (must fix before shipping): ...
- **High** (should fix): ...
- **Medium** (nice to fix): ...
- **Low** (suggestions): ...

Code to review:
[paste code here]
```

## Related
- [[AGENTS.md]]
- [[architecture/tech-stack]]
