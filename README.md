# LoL Win Predictor

Work-in-progress project to fetch live game data from the League of Legends local client API.

## What it does (so far)
- Calls the local endpoint `https://127.0.0.1:2999/liveclientdata/allgamedata`
- Prints basic data from the returned JSON payload

## Setup
```bash
pip install requests html5lib
python main.py
```

## Notes
- The local client API is only available while a game is running.
- TLS verification is disabled in the current prototype.

