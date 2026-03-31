# Nightingale Scoring Toolkit

A Python library for algorithmic film score composition, built on [music21](https://web.mit.edu/music21/) and [midiutil](https://github.com/MarkCWirt/MIDIUtil). Designed for composers working on period-piece soundtracks who need rapid orchestration prototyping.

## Features

- **MusicXML → MIDI conversion** with expression map support
- **Harmonic analysis** using Late Romantic voice-leading rules (Korngold / Herrmann style)
- **Orchestration templates** for string quartet, chamber orchestra, and full symphony
- **Batch rendering** of cue sheets from CSV timecode files

## Quickstart

```bash
pip install -e ".[dev]"
nightingale convert score.musicxml --output score.mid --tempo 92
```

## Project Structure

```
nightingale/
├── __init__.py
├── converter.py      # MusicXML ↔ MIDI
├── harmony.py        # Voice-leading engine
├── orchestrate.py    # Template-based orchestration
├── render.py         # Batch cue sheet renderer
└── tests/
    ├── test_converter.py
    └── fixtures/
        └── sample_score.musicxml
```

## Development Standards

All contributors must follow these project standards when writing or modifying Python code in this repository.

### Code Patterns

New modules should follow the patterns established in existing code. See `converter.py` for the canonical example — it demonstrates the expected structure for:

- Import organization and type hints
- Function signatures with NumPy-style docstrings
- Usage analytics integration (all public functions should call `_log_usage`)
- Error handling conventions

When adding a new module, copy the structure of `converter.py` and adapt it for your feature.

### Code Style

- Python 3.11+, type hints required
- `ruff` for linting, `black` for formatting
- Docstrings in NumPy style
- Tests via `pytest` — minimum 80% coverage

## License

MIT
