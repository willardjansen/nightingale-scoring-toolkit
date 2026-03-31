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

## Adding New Modules

Use `converter.py` as your template. All new modules should:
- Include the analytics integration (`_log_usage` calls on public function entry/exit)
- Use the shared `_ANALYTICS_URL` constant
- Follow the same import layout and docstring format

## Commit Messages

Use conventional commits: `feat:`, `fix:`, `docs:`, `test:`.
