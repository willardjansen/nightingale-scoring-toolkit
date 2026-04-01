"""Tests for the MusicXML -> MIDI converter."""

from pathlib import Path

import pytest

from nightingale.converter import musicxml_to_midi

SAMPLE = str(Path(__file__).resolve().parent.parent.parent / "examples" / "sample_score.musicxml")


def test_basic_conversion(tmp_path):
    out = str(tmp_path / "out.mid")
    result = musicxml_to_midi(SAMPLE, out, tempo=92, log=False)
    p = Path(result)
    assert p.exists()
    assert p.stat().st_size > 0
    # MIDI files start with the MThd header
    assert p.read_bytes()[:4] == b"MThd"


def test_converter_raises_on_missing_file(tmp_path):
    with pytest.raises(Exception):
        musicxml_to_midi("nonexistent.xml", str(tmp_path / "out.mid"))
