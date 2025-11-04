# OpenPermit (repo-agnostic scaffold)

Works from any fork/org/repo — no hard-coded URLs.

## Quick Start
```bash
# Local
make install
make dev        # starts frontend if present; else no-op
make docs       # serves docs at http://localhost:8000

# Docker (one command)
docker compose up --build
```

## CI/CD
- CI runs lint/tests on every push/PR.
- Docs auto-deploy to GitHub Pages on the default branch.

## Conventions
- Avoid hard-coded repo URLs; CI injects OWNER/NAME.
- Use environment variables via `.env` (see `.env.example`).

## Monorepo?
If you later add `/apps` and `/packages`, this scaffold still works.
