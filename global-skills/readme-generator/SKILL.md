---
name: readme-generator
description: Scans project structure and generates or updates README.md
triggers: [generate readme, update readme, write readme, create readme]
---

# README Generator

Scans the project and produces a well-structured README.md.

## Process
1. Read `package.json` (or equivalent) for project name, description, scripts
2. Scan folder structure to understand project layout
3. Check for existing README — update rather than overwrite if present
4. Generate README following the template below

## README Template

```markdown
# {Project Name}

> {One-line description from package.json}

## Prerequisites
- Node.js {version}
- {Other requirements}

## Installation
\`\`\`bash
git clone {repo-url}
cd {project-name}
npm install
\`\`\`

## Development
\`\`\`bash
npm start          # Start dev server / Expo
npm test           # Run tests
npm run lint       # Run linter
npm run build      # Production build
\`\`\`

## Project Structure
\`\`\`
src/
├── components/     # Reusable UI components
├── screens/        # Full screen views
├── services/       # API and data services
├── hooks/          # Custom React hooks
├── models/         # TypeScript interfaces and types
├── utils/          # Pure utility functions
├── constants/      # App-wide constants
└── store/          # State management
\`\`\`

## Environment Variables
Copy \`.env.example\` to \`.env\` and fill in:
| Variable | Description |
|----------|-------------|
| \`EXPO_PUBLIC_API_URL\` | Backend API base URL |

## Architecture
{Brief note on key decisions — link to Obsidian vault or ADRs}

## Contributing
1. Create a feature branch
2. Write tests alongside implementation
3. Follow Conventional Commits format for commit messages
4. Open a PR against \`main\`

## License
{License from package.json}
```

## Sections to Skip if Not Applicable
- Skip "Environment Variables" if no `.env.example` exists
- Skip "Contributing" if it's a personal project
- Skip "Deployment" if not yet relevant
