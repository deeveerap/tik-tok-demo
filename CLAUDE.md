# Tic-Tok-Demo

A simple web-based Tic-Tac-Toe game built with Flask.

## Overview

Two players take turns placing X and O on a 3x3 grid. The first to get three in a row wins. If all nine cells fill without a winner, the game is a draw.

## Stack

- **Backend:** Python 3, Flask 3
- **Frontend:** Vanilla HTML, CSS, JavaScript
- **State:** Flask session (per-browser)

## Project layout

```
tic-tok-demo/
├── app.py                  # Flask app: routes, game logic, session state
├── requirements.txt
├── .gitignore
├── templates/
│   └── index.html          # Board markup
└── static/
    ├── style.css           # Styling
    └── app.js              # Click handlers, fetch calls, board rendering
```

## Running locally

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000.

## API

| Method | Path     | Body                  | Returns the updated game state. |
|--------|----------|-----------------------|----------------------------------|
| GET    | `/`      | —                     | Renders the board.               |
| POST   | `/move`  | `{"index": 0..8}`     | Plays into a cell.               |
| POST   | `/reset` | —                     | Starts a new game.               |

Game state shape: `{"board": [..9 cells..], "turn": "X"|"O", "winner": "X"|"O"|null, "draw": bool}`.

## Game rules implemented

- X always moves first.
- Cannot play into an occupied cell.
- Cannot play after a win or draw.
- Win = three of the same mark in a row, column, or diagonal.
- Draw = board full with no winner.
