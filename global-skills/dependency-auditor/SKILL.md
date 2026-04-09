---
name: dependency-auditor
description: Checks package.json for outdated or vulnerable dependencies
triggers: [audit dependencies, check for updates, outdated packages, vulnerable dependencies, npm audit]
---

# Dependency Auditor

Checks project dependencies for outdated versions and known vulnerabilities.

## Process

### Step 1 — Security Vulnerabilities
```bash
npm audit
# or
yarn audit
```
Report all HIGH and CRITICAL findings. Suggest fixes with:
```bash
npm audit fix
# For breaking changes:
npm audit fix --force   # ⚠️ review carefully
```

### Step 2 — Outdated Packages
```bash
npm outdated
```

### Step 3 — Categorize Updates
For each outdated package, categorize the update type:

| Type | Version Change | Risk | Action |
|------|---------------|------|--------|
| Patch | `1.0.0 → 1.0.1` | Low | Update freely |
| Minor | `1.0.0 → 1.1.0` | Low-Medium | Update with test run |
| Major | `1.0.0 → 2.0.0` | High | Check changelog for breaking changes |

### Step 4 — Report Format
Output a prioritized list:

**Security (fix immediately):**
- `{package}@{version}` — {vulnerability} — Fix: `npm audit fix`

**Major updates (review changelog first):**
- `{package}`: `{current}` → `{latest}` — [Link to changelog/releases]

**Minor/patch updates (safe to update):**
- `{package}`: `{current}` → `{latest}`

**Dev dependencies:**
- {same format}

### Step 5 — Safe Update Command
For safe updates only (patch + minor):
```bash
npx npm-check-updates -u --target minor
npm install
npm test  # verify nothing broke
```

## Notes
- Never update major versions without reading the changelog
- Always run the test suite after updates
- Check `peerDependencies` when updating core libraries (React, React Native)
