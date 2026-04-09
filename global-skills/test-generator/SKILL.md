---
name: test-generator
description: Generates unit tests for functions, hooks, and components
triggers: [write tests for, test this, add tests, generate tests, what should I test]
---

# Test Generator

Generates unit tests for TypeScript functions, React hooks, and React Native components.

## Framework Detection
Check the project for:
- `jest.config.*` → Jest
- `vitest.config.*` → Vitest
- `pytest.ini` / `pyproject.toml` → pytest (Python)
- Default assumption: **Jest + React Native Testing Library**

## What to Generate for Each Type

### Pure Functions
- Happy path (expected input → expected output)
- Edge cases (empty input, zero, null, max values)
- Error cases (should throw, should return null)

### Custom Hooks
- Initial state
- State transitions (e.g., idle → running → complete)
- Side effects triggered correctly
- Cleanup on unmount

### React Native Components
- Renders without crashing
- Displays expected content
- User interactions (press, input) trigger correct callbacks
- Conditional rendering branches

### Services / API Calls
- Mock `apiClient`
- Test successful response handling
- Test error response handling
- Test that correct endpoint + payload is sent

## Output Pattern
Generate tests in this structure:
```typescript
describe('{Subject}', () => {
  describe('{method or scenario}', () => {
    it('{specific behavior}', () => {
      // Arrange
      // Act
      // Assert
    });
  });
});
```

Always use descriptive `it()` strings that read like requirements:
- ✅ `it('returns null when session has no sets')`
- ❌ `it('test 1')`

## After Generating
Remind the user to run:
```bash
npx jest {filename}.test.ts --coverage
```
