---
name: error-explainer
description: Takes an error message or stack trace and explains root cause and fix
triggers: [what does this error mean, explain this error, stack trace, error message, why is this failing]
---

# Error Explainer

Takes an error message or stack trace and provides a plain-language explanation plus a fix.

## Process

1. **Parse the error** — Identify the error type and the relevant stack frame (usually the first line in your own code, not library internals)
2. **Explain in plain terms** — What went wrong, not just what the error says
3. **Identify root cause** — Why it happened
4. **Provide the fix** — Minimal change to resolve it
5. **Suggest prevention** — Pattern or guard to prevent this class of error

## Common React Native / TypeScript Errors

### `TypeError: Cannot read properties of undefined (reading 'X')`
Root cause: Trying to access a property on something that is `undefined`.
Fix: Add null check or optional chaining: `obj?.property`

### `Cannot update a component while rendering a different component`
Root cause: State update called during render of another component.
Fix: Wrap the state update in `useEffect` or move it to an event handler.

### `Warning: Each child in a list should have a unique "key" prop`
Root cause: Missing `key` prop on list items.
Fix: Add `key={uniqueId}` to each item — use a stable ID, not array index.

### `Rendered more hooks than during the previous render`
Root cause: Hooks called conditionally or inside loops.
Fix: Move all hooks to the top of the component, unconditionally.

### `Network request failed` (offline)
Root cause: API call made while device is offline.
Fix: Check connectivity before network calls; write to local DB first.

### TypeScript `Type 'X' is not assignable to type 'Y'`
Root cause: Type mismatch — passing wrong type to a function or variable.
Fix: Check the expected type, cast carefully, or update the interface.

## Output Format

**What happened:** Plain English explanation.

**Root cause:** Why this occurred in this specific code.

**Fix:**
```typescript
// Before (broken)
...

// After (fixed)
...
```

**Prevention:** Pattern to avoid this in the future.
