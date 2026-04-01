"""Minimal end-to-end demo of the Nightingale conversion pipeline.

Run from the repo root:

    python examples/quick_demo.py
"""

from pathlib import Path

from nightingale.converter import musicxml_to_midi


def main() -> None:
    src = Path(__file__).resolve().parent / "sample_score.musicxml"
    dst = Path("output.mid")

    print(f"Parsing {src.name} ...")

    result = musicxml_to_midi(str(src), str(dst), tempo=92)

    stat = dst.stat()
    print(f"Writing {dst.name} ({stat.st_size:,} bytes)")
    print(f"Done -- rendered {result}")


if __name__ == "__main__":
    main()
