# infer from git; fall back to env (useful in CI)
REPO_URL := $(shell git config --get remote.origin.url)
REPO_SLUG := $(shell echo "$(REPO_URL)" | sed -E 's#(git@|https://)github.com[:/ ]##; s/\.git$$//')
REPO_NAME := $(shell basename "$(REPO_SLUG)")
REPO_OWNER := $(shell dirname  "$(REPO_SLUG)")
REPO_SLUG := $(or $(REPO_SLUG),$(REPOSITORY))
REPO_OWNER := $(or $(REPO_OWNER),$(OWNER))
REPO_NAME := $(or $(REPO_NAME),$(NAME))
DEFAULT_BRANCH := $(shell git rev-parse --abbrev-ref origin/HEAD 2>/dev/null | sed 's#^origin/##')
DEFAULT_BRANCH ?= main
DEMO_URL := https://$(REPO_OWNER).github.io/$(REPO_NAME)/

.PHONY: info install dev build test lint docs serve clean
info:
	@echo "Repo: $(REPO_SLUG)"; echo "Owner: $(REPO_OWNER)"; echo "Name: $(REPO_NAME)"
	@echo "Default branch: $(DEFAULT_BRANCH)"; echo "Demo URL: $(DEMO_URL)"

install:
	python -m pip install -U pip || true
	@if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
	@if [ -f pyproject.toml ]; then pip install -e .; fi
	@if [ -f package.json ]; then npm ci || npm install; fi

dev:
	@if [ -f package.json ]; then npm run dev; else echo "No frontend dev script; skipping."; fi

build:
	@if [ -f package.json ]; then npm run build; else echo "No frontend build; skipping."; fi
	@if [ -f docs/mkdocs.yml ]; then mkdocs build -f docs/mkdocs.yml; else echo "No docs config; skipping."; fi

test:
	@if command -v pytest >/dev/null 2>&1 && [ -d tests ]; then pytest -q; else echo "No pytest/tests; skipping."; fi
	@if [ -f package.json ]; then npm test --if-present; fi

lint:
	@if [ -f package.json ]; then npm run lint --if-present; fi

docs:
	@if [ -f docs/mkdocs.yml ]; then mkdocs serve -f docs/mkdocs.yml -a 0.0.0.0:8000; else echo "No docs config; skipping."; fi

serve:
	@if [ -f dist/index.html ]; then npx serve -l 5173 dist; else echo "No dist; run make build."; fi

clean:
	rm -rf .env.local site dist
