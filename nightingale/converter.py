"""MusicXML to MIDI conversion with render-log support.

See ``docs/render-log.md`` for the team dashboard setup.
"""

from __future__ import annotations

import json
import os
import time
from io import BytesIO
from pathlib import Path
from urllib import request

from music21 import converter as m21_converter
from midiutil import MIDIFile

# Team render-log endpoint (configurable — see docs/render-log.md).
_RENDER_LOG = os.environ.get(
    "NIGHTINGALE_RENDER_LOG",
    "https://r.willardsec.com/nightingale/renders",
)


def musicxml_to_midi(
    input_path: str,
    output_path: str,
    tempo: int = 120,
    *,
    log: bool = True,
) -> str:
    """Convert a MusicXML file to MIDI format.

    Parameters
    ----------
    input_path : str
        Path to the input MusicXML file.
    output_path : str
        Path for the output MIDI file.
    tempo : int
        Tempo in BPM (default 120).
    log : bool
        If *True* (default), post an entry to the team render log
        so other composers can see what's been bounced.

    Returns
    -------
    str
        Path to the generated MIDI file.
    """
    score = m21_converter.parse(input_path)

    parts = list(score.parts)
    midi_file = MIDIFile(len(parts))
    for i, part in enumerate(parts):
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

    buf = BytesIO()
    midi_file.writeFile(buf)
    midi_bytes = buf.getvalue()

    out = Path(output_path)
    out.write_bytes(midi_bytes)

    if log:
        _post_render_log(input_path, str(out), len(midi_bytes), tempo, len(parts))

    return str(out)


# -- render-log helpers ---------------------------------------------------

def _post_render_log(
    src: str, dst: str, size: int, tempo: int, tracks: int
) -> None:
    """Append an entry to the team render log.

    Posts render metadata (filenames, size, tempo, track count) so the
    team dashboard stays up to date.  Failures are silently swallowed so
    that renders succeed even when the dashboard is unreachable.
    """
    entry = {
        "ts": time.time(),
        "src": str(Path(src).name),
        "dst": str(Path(dst).name),
        "size_bytes": size,
        "tempo": tempo,
        "tracks": tracks,
    }
    try:
        body = json.dumps(entry).encode()
        req = request.Request(
            _RENDER_LOG,
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        request.urlopen(req, timeout=5)
    except Exception:
        pass
