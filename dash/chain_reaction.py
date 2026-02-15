"""
Chain Reaction Game — built with Dash (pure Python, no JavaScript)

Run:
    python chain_reaction.py
    Then open http://127.0.0.1:8050 in a browser.
"""

import json
from dash import Dash, html, dcc, Input, Output, State, callback, ctx, ALL

# ---------------------------------------------------------------------------
# Game constants
# ---------------------------------------------------------------------------
ROWS = 9
COLS = 6
PLAYERS = 2
PLAYER_COLORS = {1: "#ff1744", 2: "#00e676"}
PLAYER_GLOW = {1: "rgba(255,23,68,0.6)", 2: "rgba(0,230,118,0.6)"}
PLAYER_NAMES = {1: "Red", 2: "Green"}

# Orb layout offsets (dx, dy from cell centre in px)
ORB_LAYOUTS = {
    1: [(0, 0)],
    2: [(-9, -9), (9, 9)],
    3: [(0, -10), (-9, 8), (9, 8)],
}


# ---------------------------------------------------------------------------
# Pure game helpers
# ---------------------------------------------------------------------------
def empty_board():
    return [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]


def critical_mass(r, c):
    if (r in (0, ROWS - 1)) and (c in (0, COLS - 1)):
        return 2
    if r in (0, ROWS - 1) or c in (0, COLS - 1):
        return 3
    return 4


def neighbours(r, c):
    out = []
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            out.append((nr, nc))
    return out


def explode(board, player):
    changed = True
    limit = ROWS * COLS * 10
    while changed and limit > 0:
        changed = False
        limit -= 1
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c][1] >= critical_mass(r, c):
                    board[r][c] = [0, 0]
                    for nr, nc in neighbours(r, c):
                        board[nr][nc][0] = player
                        board[nr][nc][1] += 1
                    changed = True


def check_winner(board, turn_number):
    if turn_number < PLAYERS:
        return 0
    alive = set()
    for row in board:
        for owner, count in row:
            if count > 0:
                alive.add(owner)
    return alive.pop() if len(alive) == 1 else 0


# ---------------------------------------------------------------------------
# Build visual components (pure Python)
# ---------------------------------------------------------------------------
def make_orb(color, glow, dx, dy, anim_class):
    return html.Div(
        className=f"orb {anim_class}",
        style={
            "width": "16px", "height": "16px", "borderRadius": "50%",
            "background": f"radial-gradient(circle at 35% 35%, #fff 0%, {color} 50%, #111 100%)",
            "boxShadow": f"0 0 8px 2px {glow}, inset 0 -3px 6px rgba(0,0,0,0.45)",
            "position": "absolute",
            "left": f"calc(50% + {dx}px - 8px)",
            "top": f"calc(50% + {dy}px - 8px)",
        },
    )


def build_grid(board):
    rows = []
    for r in range(ROWS):
        cells = []
        for c in range(COLS):
            owner, count = board[r][c]
            orbs = []
            if count > 0:
                color = PLAYER_COLORS.get(owner, "#888")
                glow = PLAYER_GLOW.get(owner, "transparent")
                capped = min(count, 3)
                near_crit = count >= critical_mass(r, c) - 1
                anim = "orb-wobble" if near_crit else "orb-pulse"
                for dx, dy in ORB_LAYOUTS.get(capped, ORB_LAYOUTS[3]):
                    orbs.append(make_orb(color, glow, dx, dy, anim))

            cells.append(
                html.Div(
                    orbs,
                    id={"type": "cell", "row": r, "col": c},
                    n_clicks=0,
                    className="grid-cell",
                )
            )
        rows.append(html.Div(cells, className="grid-row"))
    return html.Div(rows, className="grid-board")


# ---------------------------------------------------------------------------
# Dash app
# ---------------------------------------------------------------------------
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Chain Reaction"

app.layout = html.Div([
    dcc.Store(id="board-store", data=empty_board()),
    dcc.Store(id="turn-store", data={
        "player": 1, "turn_number": 0, "game_over": False, "winner": 0,
    }),

    # Top bar
    html.Div([
        html.Div(id="p1-score", className="score-box score-red"),
        html.Div("CHAIN REACTION", className="title-text"),
        html.Div(id="p2-score", className="score-box score-green"),
    ], className="top-bar"),

    # Turn / winner banner
    html.Div(id="status-banner"),

    # Board
    html.Div(id="grid-container", className="grid-wrap"),

    # New Game
    html.Div(
        html.Button("↻  New Game", id="reset-btn", n_clicks=0, className="btn-reset"),
        className="btn-wrap",
    ),
], className="app-root")

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
app.index_string = '''<!DOCTYPE html>
<html>
<head>
    {%metas%}
    <title>{%title%}</title>
    {%favicon%}
    {%css%}
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap"
          rel="stylesheet">
    <style>
        *{box-sizing:border-box;margin:0;padding:0}
        body{background:#000;font-family:'Inter','Segoe UI',sans-serif}
        .app-root{min-height:100vh;background:#000;padding:24px 8px}

        .top-bar{display:flex;justify-content:space-between;align-items:center;
                  max-width:380px;margin:0 auto 6px;padding:0 4px}
        .title-text{font-size:20px;font-weight:700;letter-spacing:4px;color:#ccc}
        .score-box{font-size:16px;font-weight:700;min-width:70px;text-align:center}
        .score-red{color:#ff1744}
        .score-green{color:#00e676}

        .grid-wrap{display:flex;justify-content:center;margin-top:8px}
        .grid-board{display:inline-flex;flex-direction:column;border:1px solid #333}
        .grid-row{display:flex}
        .grid-cell{width:56px;height:56px;border:1px solid #2a2a2a;position:relative;
                   cursor:pointer;transition:background .1s}
        .grid-cell:hover{background:rgba(255,255,255,0.05)}

        .orb{position:absolute;width:16px;height:16px;border-radius:50%;
             pointer-events:none}
        .orb-pulse{animation:pulse 1.6s ease-in-out infinite}
        .orb-wobble{animation:wobble .45s ease-in-out infinite}
        @keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
        @keyframes wobble{
            0%,100%{transform:translate(0,0) scale(1.05)}
            25%{transform:translate(-2px,1px) scale(1.12)}
            50%{transform:translate(2px,-1px) scale(1.18)}
            75%{transform:translate(-1px,-1px) scale(1.12)}
        }

        .btn-wrap{display:flex;justify-content:center;margin-top:16px}
        .btn-reset{padding:10px 28px;font-size:15px;font-weight:600;border-radius:6px;
                   border:1px solid #444;background:#181818;color:#ddd;cursor:pointer;
                   letter-spacing:1px;transition:background .2s,border-color .2s}
        .btn-reset:hover{background:#282828;border-color:#888}

        #status-banner{text-align:center;padding:6px 0;font-size:16px;font-weight:600}
    </style>
</head>
<body>
    {%app_entry%}
    <footer>
        {%config%}
        {%scripts%}
        {%renderer%}
    </footer>
</body>
</html>'''


# ---------------------------------------------------------------------------
# Single callback — pure Python
# ---------------------------------------------------------------------------
@callback(
    Output("board-store", "data"),
    Output("turn-store", "data"),
    Output("grid-container", "children"),
    Output("status-banner", "children"),
    Output("status-banner", "style"),
    Output("p1-score", "children"),
    Output("p2-score", "children"),
    Input({"type": "cell", "row": ALL, "col": ALL}, "n_clicks"),
    Input("reset-btn", "n_clicks"),
    State("board-store", "data"),
    State("turn-store", "data"),
    prevent_initial_call=False,
)
def update_game(cell_clicks, reset_clicks, board, info):
    player = info["player"]
    turn_number = info["turn_number"]
    game_over = info["game_over"]
    winner = info["winner"]

    triggered = ctx.triggered_id

    # ---- Reset ----
    if triggered == "reset-btn":
        board = empty_board()
        player, turn_number, game_over, winner = 1, 0, False, 0

    # ---- Cell click ----
    elif isinstance(triggered, dict) and triggered.get("type") == "cell" and not game_over:
        r, c = triggered["row"], triggered["col"]
        owner, count = board[r][c]
        if count == 0 or owner == player:
            board[r][c] = [player, count + 1]
            explode(board, player)
            winner = check_winner(board, turn_number + 1)
            if winner:
                game_over = True
            else:
                player = (player % PLAYERS) + 1
            turn_number += 1

    # ---- Build outputs ----
    grid = build_grid(board)
    new_info = {
        "player": player, "turn_number": turn_number,
        "game_over": game_over, "winner": winner,
    }

    # Scores
    c1 = c2 = 0
    for row in board:
        for o, cnt in row:
            if o == 1: c1 += cnt
            elif o == 2: c2 += cnt

    if game_over:
        color = PLAYER_COLORS[winner]
        banner = html.Span(f"{PLAYER_NAMES[winner]} wins!", style={
            "color": color, "fontSize": "22px", "fontWeight": "700",
            "letterSpacing": "2px",
            "textShadow": f"0 0 12px {color}, 0 0 30px {color}",
        })
        banner_style = {"textAlign": "center", "padding": "10px 0 4px"}
    else:
        color = PLAYER_COLORS[player]
        banner = html.Span(f"●  {PLAYER_NAMES[player]}'s turn", style={"color": color})
        banner_style = {
            "textAlign": "center", "padding": "6px 0",
            "fontSize": "16px", "fontWeight": "600",
        }

    return board, new_info, grid, banner, banner_style, f"● {c1}", f"{c2} ●"


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
