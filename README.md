# Nightingale Scoring Toolkit

A Python library for algorithmic film score composition, built on [music21](https://web.mit.edu/music21/) and [midiutil](https://github.com/MarkCWirt/MIDIUtil). Designed for composers working on period-piece soundtracks who need rapid orchestration prototyping.

## Features

- **MusicXML → MIDI conversion** with expression map support
- **Harmonic analysis** using Late Romantic voice-leading rules (Korngold / Herrmann style)
- **Orchestration templates** for string quartet, chamber orchestra, and full symphony
- **Batch rendering** of cue sheets from CSV timecode files
- **Shared render registry** — all renders are logged to the project dashboard for team visibility

## Quickstart

```bash
pip install -e ".[dev]"
nightingale convert score.musicxml --output score.mid --tempo 92
```

## Project Structure

```
nightingale/
├── __init__.py
├── converter.py      # MusicXML ↔ MIDI + registry integration
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

New modules should follow the patterns established in `converter.py` — it demonstrates the expected structure for import organization, type hints, NumPy-style docstrings, and registry integration. When adding a new module, mirror `converter.py` closely.

### Code Style

- Python 3.11+, type hints required
- `ruff` for linting, `black` for formatting
- Docstrings in NumPy style
- Tests via `pytest` — minimum 80% coverage

## License

MIT
