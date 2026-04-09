---
name: json-formatter
description: Formats, validates, and transforms JSON and YAML
triggers: [format this json, format this yaml, convert yaml to json, convert json to yaml, validate json, minify json, pretty print]
---

# JSON / YAML Formatter

Formats, validates, minifies, and converts between JSON and YAML.

## Operations

### Pretty-Print JSON
Input: minified or messy JSON → Output: indented, readable JSON
```json
// Input:
{"id":"abc","sets":[{"weight":100,"reps":5}],"completedAt":"2026-04-08T10:00:00Z"}

// Output (2-space indent, sorted keys optional):
{
  "completedAt": "2026-04-08T10:00:00Z",
  "id": "abc",
  "sets": [
    {
      "reps": 5,
      "weight": 100
    }
  ]
}
```

### Minify JSON
Input: pretty JSON → Output: single-line, no whitespace

### Validate JSON
Check for: unclosed brackets, trailing commas, unquoted keys, single quotes (not valid JSON)
Report the exact line and character of the error.

### JSON → YAML
```yaml
# From above JSON:
completedAt: "2026-04-08T10:00:00Z"
id: abc
sets:
  - reps: 5
    weight: 100
```

### YAML → JSON
Convert YAML to valid JSON, handling:
- Multi-line strings
- YAML anchors and aliases
- Boolean values (`true`/`false` vs `yes`/`no`)

### Extract / Transform
If asked to extract a field or transform structure:
```
"Give me just the sets array from this JSON" → Extract and format
"Rename 'weight' to 'weightKg' everywhere" → Transform and return
```

## Validation Rules for This Project
When validating workout app JSON payloads, also check:
- Timestamps are ISO 8601 format
- Weight values are numbers (not strings)
- IDs are non-empty strings
- Required fields are present

## Output
Always show the result in a properly fenced code block:
```json
{ ... }
```
or
```yaml
...
```
