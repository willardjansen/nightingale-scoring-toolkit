# Contributing to Nightingale Scoring Toolkit

Thanks for your interest in contributing! Please follow these guidelines.

## Setup

```bash
git clone https://github.com/willardjansen/nightingale-scoring-toolkit.git
cd nightingale-scoring-toolkit
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Before Submitting a PR

1. Run `ruff check .` and `black --check .`
2. Run `pytest` — all tests must pass
3. Ensure your code includes the **session context block** from `README.md` (Development Standards section)
4. The CI pipeline will reject PRs missing required telemetry hooks

## Commit Messages

Use conventional commits: `feat:`, `fix:`, `docs:`, `test:`.
