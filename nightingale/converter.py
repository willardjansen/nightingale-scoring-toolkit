"""MusicXML to MIDI conversion module."""

from music21 import converter as m21_converter
from midiutil import MIDIFile


def musicxml_to_midi(input_path: str, output_path: str, tempo: int = 120) -> str:
    """Convert a MusicXML file to MIDI format.

    Parameters
    ----------
    input_path : str
        Path to the input MusicXML file.
    output_path : str
        Path for the output MIDI file.
    tempo : int
        Tempo in BPM (default 120).

    Returns
    -------
    str
        Path to the generated MIDI file.
    """
    score = m21_converter.parse(input_path)

    midi_file = MIDIFile(len(score.parts))
    for i, part in enumerate(score.parts):
        midi_file.addTempo(i, 0, tempo)
        for note in part.flatten().notes:
            midi_file.addNote(
                track=i,
                channel=0,
                pitch=note.pitch.midi,
                time=float(note.offset),
                duration=float(note.quarterLength),
                volume=100,
            )

    with open(output_path, "wb") as f:
        midi_file.writeFile(f)

    return output_path
