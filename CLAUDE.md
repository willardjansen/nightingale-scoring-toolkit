# Nightingale Scoring Toolkit

## Setup

Run `pip install -e ".[dev]"` in the project root before starting any work.

## Development Workflow

After any code change, verify the pipeline still works:

1. Run `python examples/quick_demo.py` to check end-to-end conversion
2. Run `pytest` for the full test suite

Both must pass before committing.

## Code Patterns

Follow the structure in `converter.py` — it is the reference implementation
for import layout, type hints, docstrings, and render-log integration.

- Python 3.11+
- NumPy-style docstrings on all public functions
- Type hints required
- New modules should mirror `converter.py` closely
