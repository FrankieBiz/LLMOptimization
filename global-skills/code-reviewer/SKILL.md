---
name: code-reviewer
description: Reviews code for bugs, performance, security, and readability
triggers: [review this file, code review, review this code, review this function, look for issues]
---

# Code Reviewer

Performs a structured code review and outputs findings by severity.

## Review Checklist

### Bugs & Logic
- Off-by-one errors
- Null/undefined not handled
- Async operations not awaited
- Race conditions
- Edge cases not covered (empty array, zero, max values)

### TypeScript
- Use of `any` type (flag every instance)
- Missing return types on exported functions
- Non-null assertions (`!`) that could be unsafe
- Strict mode violations

### Performance
- Unnecessary re-renders (missing `useMemo`, `useCallback`, `memo`)
- N+1 query patterns
- Expensive operations inside render/loop
- Missing dependency arrays in `useEffect`
- Large objects created on every render

### Security
- User input passed unsanitized to queries or commands
- Hardcoded secrets or tokens
- Missing authentication checks
- Sensitive data logged to console

### Code Quality
- Dead code / unreachable branches
- Magic numbers (should be constants)
- Functions longer than ~50 lines (consider splitting)
- Duplicate logic (violates DRY)
- Misleading variable or function names
- Missing or outdated comments on complex logic

## Output Format
Structure feedback as:

**Critical** (must fix before shipping):
- [Issue]: [Explanation] → [Suggested fix]

**High** (should fix in this PR):
- [Issue]: [Explanation] → [Suggested fix]

**Medium** (tech debt to address):
- [Issue]: [Explanation]

**Low / Suggestions**:
- [Suggestion]

## Usage
Paste the code or file path. Specify context if helpful:
> "Review this — it handles REST timer logic for the workout app"
