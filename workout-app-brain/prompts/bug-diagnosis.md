---
tags: [prompt]
created: 2026-04-08
updated: 2026-04-08
status: active
---

# Prompt: Bug Diagnosis

**Use this prompt when reporting a bug to an AI agent for diagnosis.**

## Prompt Template
```
I have a bug in the workout tracking app. Please help diagnose and fix it.

**Error / Symptom:**
[Paste the error message, stack trace, or describe the unexpected behavior]

**Steps to reproduce:**
1.
2.
3.

**Expected behavior:**
[What should happen]

**Actual behavior:**
[What actually happens]

**Affected code (paste relevant files or sections):**
[paste code]

**Context:**
- Feature area: [workout tracking / scheduling / exercise library / etc]
- Environment: [iOS / Android / both]
- Does this happen offline too? [yes / no / unknown]

Before suggesting a fix:
1. Check bugs/ in this vault — has this been seen before?
2. Check snippets/ for any patterns that might apply
3. Explain the root cause in plain terms
4. Propose the minimal fix
5. Suggest any guard to prevent this class of bug in future

After fixing, I'll create a note in bugs/ to document the solution.
```

## Related
- [[AGENTS.md]]
- [[bugs/_template-bug]]
