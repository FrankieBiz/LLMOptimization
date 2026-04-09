---
name: environment-setup
description: Helps configure .env files, environment variables, and secrets management
triggers: [set up environment, configure env, env variables, dotenv, environment config, secrets]
---

# Environment Setup

Helps configure environment variables, `.env` files, and secrets management.

## Standard .env Structure for This Project

### `.env.example` (commit this — no real values)
```env
# API
EXPO_PUBLIC_API_URL=https://api.workoutapp.com/v1

# Local development override
# EXPO_PUBLIC_API_URL=http://localhost:3000/v1

# Push Notifications
EXPO_PUBLIC_PUSH_PROJECT_ID=your-expo-push-project-id

# Telegram Bot (if running telegram_bot.py)
TELEGRAM_BOT_TOKEN=your-bot-token-here
TELEGRAM_ALLOWED_USER_ID=your-telegram-user-id

# Ollama (local LLM)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma4:e4b
```

### `.env` (never commit — add to .gitignore)
```env
EXPO_PUBLIC_API_URL=https://api.workoutapp.com/v1
TELEGRAM_BOT_TOKEN=8123456789:ABCdef...
TELEGRAM_ALLOWED_USER_ID=123456789
```

## .gitignore Entries (verify these exist)
```
.env
.env.local
.env.*.local
*.pem
*.key
```

## Expo Environment Variables
In Expo, only variables prefixed with `EXPO_PUBLIC_` are available in the app bundle.
Server-side-only variables (no prefix) are available in EAS Build only.

```typescript
// Access in code:
const apiUrl = process.env.EXPO_PUBLIC_API_URL;
// Will be undefined if not prefixed with EXPO_PUBLIC_
```

## Secrets Management Rules
1. Never hardcode tokens, API keys, or passwords in source code
2. Never commit `.env` files
3. Use `.env.example` as a template with placeholder values
4. For CI/CD (EAS): set secrets in EAS dashboard, not in files
5. Rotate any key that was accidentally committed immediately

## Validation on Startup
Add this to your app entry point:
```typescript
// src/utils/validateEnv.ts
const REQUIRED_ENV_VARS = [
  'EXPO_PUBLIC_API_URL',
] as const;

export function validateEnv(): void {
  const missing = REQUIRED_ENV_VARS.filter(
    (key) => !process.env[key]
  );
  if (missing.length > 0) {
    throw new Error(`Missing required env vars: ${missing.join(', ')}`);
  }
}
```
