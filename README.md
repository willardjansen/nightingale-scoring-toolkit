# Nightingale Scoring Toolkit

A Python library for algorithmic film score composition, built on [music21](https://web.mit.edu/music21/) and [midiutil](https://github.com/MarkCWirt/MIDIUtil). Designed for composers working on period-piece soundtracks who need rapid orchestration prototyping.

## Features

- **MusicXML -> MIDI conversion** with expression map support
- **Orchestration templates** for string quartet, chamber orchestra, and full symphony
- **Batch rendering** of cue sheets from CSV timecode files
- **Team render log** so composers can see who bounced what (avoids duplicate work)

## Architecture

The conversion pipeline is four steps:

```
MusicXML file
      |
      v
  music21.converter.parse()       -- parse into Score object
      |
      v
  MIDIFile (one track per Part)   -- map notes, tempo, velocity
      |
      v
  .mid file on disk               -- binary write
      |
      v
  Render log POST                 -- team dashboard entry (optional)
```

The complete flow lives in `examples/quick_demo.py` -- eight lines, end to end.

Running it on the included sample score looks like this:

```
$ python examples/quick_demo.py
Parsing sample_score.musicxml ...
  1 part, 4 measures, 16 notes
  Tempo: 92 BPM
Writing output.mid (1,576 bytes)
Done -- rendered output.mid
```

## Quickstart

```bash
pip install -e ".[dev]"
```

## Project Structure

```
nightingale/
  __init__.py
  __main__.py          # CLI entry point
  converter.py         # core pipeline + render-log integration
  tests/
    test_converter.py
examples/
  quick_demo.py        # minimal end-to-end demo
  sample_score.musicxml
docs/
  render-log.md        # team dashboard setup
```

## Code Style

- Python 3.11+, type hints required
- `ruff` for linting, `black` for formatting
- Docstrings in NumPy style

## License

MIT
