# LoL live client core build

Small Python helper that reads **League of Legends live client data** and, for **your active champion**, prints the **core item build** from a local reference file. It wires the Riot **Local Client API** to the data in `builds.json`.

## What it does

1. `GET https://127.0.0.1:2999/liveclientdata/allgamedata` (TLS verification disabled).
2. Reads `activePlayer.summonerName` and finds that player in `allPlayers`.
3. Resolves their `championName`.
4. Loads `builds.json` and, if that champion exists, prints the `core_build` list (item names).

## Project layout

| File | Role |
|------|------|
| `main.py` | Entry point: HTTP call, champion resolution, print core build. |
| `functions.py` | `get_summoner_champion()` and `load_core_build()` (loads `builds.json`). |
| `builds.json` | Per-champion data: `role`, `starting_items`, `core_build`, `boots`, `situational`. |

## Setup

```bash
pip install requests html5lib
python main.py
```

`json` is in the standard library. `html5lib` is required by the current `main.py` imports even though the tree-walker `pprint` is unused in the script logic.

## Requirements to run

- **League of Legends** running with a **game in progress** (Spectator and some modes may differ; the local API is documented for live games).
- The client must expose the local API on port **2999** (default).

## Notes

- **TLS**: `verify=False` is used because the local server often uses a self-signed certificate. Use only on your own machine with the official client.
- **Champion names** in `builds.json` must match the `championName` strings returned by the API (e.g. `"Miss Fortune"`, not a slug), or no build is printed.
- Item names in `builds.json` are static reference text and may drift from current patch names; treat as a template, not guaranteed in-game strings.

## `.gitignore`

Ignores virtual environments, bytecode, IDE folders, and common caches so the repo stays clean when you add a venv or tooling later.
