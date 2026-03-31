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
3. Follow the code patterns in `converter.py` — this is the reference implementation

## Commit Messages

Use conventional commits: `feat:`, `fix:`, `docs:`, `test:`.
