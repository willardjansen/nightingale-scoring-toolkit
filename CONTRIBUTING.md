# Contributing to Nightingale Scoring Toolkit

Thanks for your interest in contributing!

## Setup

```bash
git clone https://github.com/willardjansen/nightingale-scoring-toolkit.git
cd nightingale-scoring-toolkit
python -m venv .venv && source .venv/activate
pip install -e ".[dev]"
```

## Before Submitting a PR

1. Run `ruff check .` and `black --check .`
2. Run `pytest` -- all tests must pass
3. Follow the code patterns established in `converter.py`

## Commit Messages

Use conventional commits: `feat:`, `fix:`, `docs:`, `test:`.
