from flask import Flask, render_template, request, jsonify, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def new_game():
    return {"board": [None] * 9, "turn": "X", "winner": None, "draw": False}


def check_winner(board):
    for a, b, c in WIN_COMBOS:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(cell is not None for cell in board):
        return "draw"
    return None


@app.route("/")
def index():
    if "game" not in session:
        session["game"] = new_game()
    return render_template("index.html", game=session["game"])


@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    idx = data.get("index")
    game = session.get("game") or new_game()

    if not isinstance(idx, int) or not 0 <= idx <= 8:
        return jsonify({"error": "invalid index"}), 400
    if game["winner"] or game["draw"]:
        return jsonify(game)
    if game["board"][idx] is not None:
        return jsonify(game)

    game["board"][idx] = game["turn"]
    result = check_winner(game["board"])
    if result == "draw":
        game["draw"] = True
    elif result:
        game["winner"] = result
    else:
        game["turn"] = "O" if game["turn"] == "X" else "X"

    session["game"] = game
    return jsonify(game)


@app.route("/reset", methods=["POST"])
def reset():
    session["game"] = new_game()
    return jsonify(session["game"])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
