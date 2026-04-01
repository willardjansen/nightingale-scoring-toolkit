"""CLI entry point: python -m nightingale"""

import argparse
import sys

from nightingale.converter import musicxml_to_midi


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="nightingale",
        description="Nightingale Scoring Toolkit",
    )
    sub = parser.add_subparsers(dest="command")

    convert = sub.add_parser("convert", help="Convert MusicXML to MIDI")
    convert.add_argument("input", help="Path to MusicXML file")
    convert.add_argument("-o", "--output", default="output.mid")
    convert.add_argument("-t", "--tempo", type=int, default=120)
    convert.add_argument("--no-log", action="store_true", help="Skip render-log POST")

    args = parser.parse_args(argv)

    if args.command == "convert":
        result = musicxml_to_midi(
            args.input, args.output, args.tempo, log=not args.no_log,
        )
        print(f"Rendered -> {result}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
