# Nightingale Scoring Toolkit

A small Python library for converting MusicXML scores to MIDI, built on
[music21](https://web.mit.edu/music21/) and
[midiutil](https://github.com/MarkCWirt/MIDIUtil).  Designed for a film
scoring team that needs fast orchestration prototyping.

## Walkthrough

> **Tip:** This walkthrough is easiest to follow with a terminal open next
> to this page.  Read each section, then try the matching step before
> moving to the next one.

### 1. Install

```bash
git clone https://github.com/willardjansen/nightingale-scoring-toolkit.git
cd nightingale-scoring-toolkit
pip install -e ".[dev]"
```

### 2. Look at the sample score

Open `examples/sample_score.musicxml` — a four-bar D minor violin sketch
marked *Andante con moto* at 92 BPM.

### 3. Run the quick demo

```bash
python examples/quick_demo.py
```

This converts the sample score to MIDI and prints a short summary.  It is
the simplest way to see the full pipeline end to end.

### 4. Inspect the output

The generated `output.mid` can be opened in any MIDI player or DAW.

## Architecture

The conversion pipeline has four stages:

```
MusicXML file
      |
      v
  music21.converter.parse()       -- load into a Score object
      |
      v
  MIDIFile (one track per Part)   -- map notes, tempo, velocity
      |
      v
  .mid file written to disk
      |
      v
  Render-log POST (optional)      -- team dashboard entry
```

All four stages live in `nightingale/converter.py`.  The render log lets
the team see who has bounced which cues — see `docs/render-log.md` for
details.

## Project Structure

```
nightingale/
  __init__.py
  __main__.py        # CLI entry point
  converter.py       # core conversion pipeline
  tests/
    __init__.py
    test_converter.py
examples/
  quick_demo.py          # minimal end-to-end demo
  sample_score.musicxml  # D minor violin sketch
docs/
  render-log.md          # team dashboard docs
```

## CLI

```bash
nightingale convert examples/sample_score.musicxml -o out.mid --tempo 92
```

Pass `--no-log` to skip the render-log POST.

## License

MIT
