"""Tests for the MusicXML → MIDI converter."""

import pytest
from nightingale.converter import musicxml_to_midi


def test_converter_raises_on_missing_file():
    with pytest.raises(Exception):
        musicxml_to_midi("nonexistent.xml", "out.mid")
