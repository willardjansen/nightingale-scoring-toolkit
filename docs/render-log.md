# Render Log

When multiple composers are bouncing cues in parallel, it's easy to do
duplicate work.  The render log gives the team a lightweight way to see
who rendered what and when.

## Endpoint

By default renders are logged to the team dashboard.  Override per
environment:

```bash
export NIGHTINGALE_RENDER_LOG=https://your-team-server.example.com/renders
```

To disable logging entirely, pass `log=False` to `musicxml_to_midi()` or
use the CLI flag `--no-log`.

## Payload

Each log entry contains:

| Field        | Description                              |
|--------------|------------------------------------------|
| `ts`         | Unix timestamp of the render             |
| `src`        | Source filename (name only, no path)      |
| `dst`        | Output filename                          |
| `size_bytes` | MIDI file size                           |
| `tempo`      | BPM used for the render                  |
| `tracks`     | Number of MIDI tracks                    |
| `host`       | Workstation hostname (for attribution)   |
| `py`         | Python version                           |

No file paths or user-identifying data are sent.

## Dashboard

The scoring lead runs a small Flask receiver that writes entries to a
shared spreadsheet.  See the `infra/` repo for deployment instructions.
