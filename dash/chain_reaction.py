"""
Chain Reaction Game — built with Dash (clientside rendering)

All game logic runs in the browser via a clientside callback — zero
server round-trips, so every click is instant.

Run:
    python chain_reaction.py
    Then open http://127.0.0.1:8050 in a browser.
"""

import json
from dash import Dash, html, dcc, Input, Output, State, ALL

# ---------------------------------------------------------------------------
# Constants (also duplicated in the JS below)
# ---------------------------------------------------------------------------
ROWS = 9
COLS = 6

def empty_board():
    return [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]

def _initial_state():
    return {"player": 1, "turn_number": 0, "game_over": False, "winner": 0}

# ---------------------------------------------------------------------------
# Dash app
# ---------------------------------------------------------------------------
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Chain Reaction"

# Build the static grid of clickable cells (content filled by JS)
def _static_grid():
    rows = []
    for r in range(ROWS):
        cells = []
        for c in range(COLS):
            cells.append(
                html.Div(
                    id={"type": "cell", "row": r, "col": c},
                    n_clicks=0,
                    className="grid-cell",
                )
            )
        rows.append(html.Div(cells, className="grid-row"))
    return html.Div(rows, className="grid-board")

app.layout = html.Div([
    dcc.Store(id="board-store", data=empty_board()),
    dcc.Store(id="turn-store", data=_initial_state()),

    # Top bar
    html.Div([
        html.Div(id="p1-score", className="score-box score-red"),
        html.Div("CHAIN REACTION", className="title-text"),
        html.Div(id="p2-score", className="score-box score-green"),
    ], className="top-bar"),

    # Turn / winner banner
    html.Div(id="status-banner"),

    # Board
    html.Div(_static_grid(), id="grid-container", className="grid-wrap"),

    # New Game
    html.Div(
        html.Button("↻  New Game", id="reset-btn", n_clicks=0, className="btn-reset"),
        className="btn-wrap",
    ),
], className="app-root")

# ---------------------------------------------------------------------------
# Full CSS + JS in a single index_string — everything runs client-side
# ---------------------------------------------------------------------------
app.index_string = r'''<!DOCTYPE html>
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

        /* ---- top bar ---- */
        .top-bar{display:flex;justify-content:space-between;align-items:center;
                  max-width:380px;margin:0 auto 6px;padding:0 4px}
        .title-text{font-size:20px;font-weight:700;letter-spacing:4px;color:#ccc}
        .score-box{font-size:16px;font-weight:700;min-width:70px;text-align:center}
        .score-red{color:#ff1744}
        .score-green{color:#00e676}

        /* ---- grid ---- */
        .grid-wrap{display:flex;justify-content:center;margin-top:8px}
        .grid-board{display:inline-flex;flex-direction:column;border:1px solid #333}
        .grid-row{display:flex}
        .grid-cell{width:56px;height:56px;border:1px solid #2a2a2a;position:relative;
                   cursor:pointer;transition:background .1s}
        .grid-cell:hover{background:rgba(255,255,255,0.05)}

        /* ---- orbs ---- */
        .orb{position:absolute;width:16px;height:16px;border-radius:50%;
             pointer-events:none}
        .orb-p1{background:radial-gradient(circle at 35% 35%,#fff 0%,#ff1744 50%,#111 100%);
                box-shadow:0 0 8px 2px rgba(255,23,68,.6),inset 0 -3px 6px rgba(0,0,0,.45)}
        .orb-p2{background:radial-gradient(circle at 35% 35%,#fff 0%,#00e676 50%,#111 100%);
                box-shadow:0 0 8px 2px rgba(0,230,118,.6),inset 0 -3px 6px rgba(0,0,0,.45)}
        .orb-pulse{animation:pulse 1.6s ease-in-out infinite}
        .orb-wobble{animation:wobble .45s ease-in-out infinite}

        @keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
        @keyframes wobble{
            0%,100%{transform:translate(0,0) scale(1.05)}
            25%{transform:translate(-2px,1px) scale(1.12)}
            50%{transform:translate(2px,-1px) scale(1.18)}
            75%{transform:translate(-1px,-1px) scale(1.12)}
        }

        /* ---- button ---- */
        .btn-wrap{display:flex;justify-content:center;margin-top:16px}
        .btn-reset{padding:10px 28px;font-size:15px;font-weight:600;border-radius:6px;
                   border:1px solid #444;background:#181818;color:#ddd;cursor:pointer;
                   letter-spacing:1px;transition:background .2s,border-color .2s}
        .btn-reset:hover{background:#282828;border-color:#888}

        /* ---- status ---- */
        #status-banner{text-align:center;padding:6px 0;font-size:16px;font-weight:600}
        .turn-dot{display:inline-block;width:14px;height:14px;border-radius:50%;
                  margin-right:8px;vertical-align:middle}
        .winner-banner{text-align:center;font-size:22px;font-weight:700;
                        padding:10px 0 4px;letter-spacing:2px;
                        animation:glow 1.5s ease-in-out infinite alternate}
        @keyframes glow{
            from{text-shadow:0 0 6px currentColor}
            to{text-shadow:0 0 20px currentColor,0 0 40px currentColor}
        }
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
# Clientside callback — ALL game logic in JS, zero server round-trips
# ---------------------------------------------------------------------------

app.clientside_callback(
    """
    function(cellClicks, resetClicks, boardData, turnData) {
        const ROWS = 9, COLS = 6, PLAYERS = 2;
        const COLORS = {1: '#ff1744', 2: '#00e676'};
        const NAMES  = {1: 'Red', 2: 'Green'};

        // ---- deep copy board & state ----
        let board = JSON.parse(JSON.stringify(boardData));
        let st    = JSON.parse(JSON.stringify(turnData));

        // ---- which input fired? ----
        const ctx = window.dash_clientside.callback_context;
        let trig = null;
        if (ctx && ctx.triggered && ctx.triggered.length) {
            try { trig = JSON.parse(ctx.triggered[0].prop_id.split('.')[0]); }
            catch(e) { trig = ctx.triggered[0].prop_id.split('.')[0]; }
        }

        // ---- helpers ----
        function critMass(r,c) {
            const corner = (r===0||r===ROWS-1) && (c===0||c===COLS-1);
            if (corner) return 2;
            if (r===0||r===ROWS-1||c===0||c===COLS-1) return 3;
            return 4;
        }
        function nbrs(r,c) {
            const out=[];
            [[-1,0],[1,0],[0,-1],[0,1]].forEach(function(d){
                const nr=r+d[0], nc=c+d[1];
                if(nr>=0&&nr<ROWS&&nc>=0&&nc<COLS) out.push([nr,nc]);
            });
            return out;
        }
        function explode(board, player) {
            let changed=true, safety=ROWS*COLS*10;
            while(changed && safety-->0){
                changed=false;
                for(let r=0;r<ROWS;r++) for(let c=0;c<COLS;c++){
                    if(board[r][c][1]>=critMass(r,c)){
                        board[r][c]=[0,0];
                        nbrs(r,c).forEach(function(n){
                            board[n[0]][n[1]][0]=player;
                            board[n[0]][n[1]][1]+=1;
                        });
                        changed=true;
                    }
                }
            }
        }
        function checkWinner(board, tn) {
            if(tn<PLAYERS) return 0;
            const alive=new Set();
            for(let r=0;r<ROWS;r++) for(let c=0;c<COLS;c++)
                if(board[r][c][1]>0) alive.add(board[r][c][0]);
            if(alive.size===1) return alive.values().next().value;
            return 0;
        }

        // ---- Reset ----
        if (trig === 'reset-btn') {
            board = Array.from({length:ROWS},()=>Array.from({length:COLS},()=>[0,0]));
            st = {player:1, turn_number:0, game_over:false, winner:0};
        }
        // ---- Cell click ----
        else if (trig && typeof trig === 'object' && trig.type === 'cell' && !st.game_over) {
            const r=trig.row, c=trig.col;
            const owner=board[r][c][0], count=board[r][c][1];
            if (count===0 || owner===st.player) {
                board[r][c] = [st.player, count+1];
                explode(board, st.player);
                const w = checkWinner(board, st.turn_number+1);
                if (w) { st.game_over=true; st.winner=w; }
                else   { st.player = (st.player % PLAYERS)+1; }
                st.turn_number++;
            }
        }

        // ---- Render cells (direct DOM manipulation for speed) ----
        // Orb layout offsets (dx,dy from centre in px)
        const layouts = {1:[[0,0]], 2:[[-9,-9],[9,9]], 3:[[0,-10],[-9,8],[9,8]]};

        for (let r=0; r<ROWS; r++) {
            for (let c=0; c<COLS; c++) {
                const id = JSON.stringify({type:'cell',row:r,col:c});
                const el = document.querySelector('[id="'+id+'"]');
                if (!el) continue;
                // clear old orbs
                el.innerHTML = '';
                const own=board[r][c][0], cnt=board[r][c][1];
                if (cnt===0) continue;
                const capped = Math.min(cnt,3);
                const nearCrit = cnt >= critMass(r,c)-1;
                const pos = layouts[capped] || layouts[3];
                const pClass = own===1 ? 'orb-p1' : 'orb-p2';
                const anim = nearCrit ? 'orb-wobble' : 'orb-pulse';
                pos.forEach(function(p){
                    const orb = document.createElement('div');
                    orb.className = 'orb ' + pClass + ' ' + anim;
                    orb.style.left = 'calc(50% + '+p[0]+'px - 8px)';
                    orb.style.top  = 'calc(50% + '+p[1]+'px - 8px)';
                    el.appendChild(orb);
                });
            }
        }

        // ---- Scores ----
        let c1=0, c2=0;
        for(let r=0;r<ROWS;r++) for(let c=0;c<COLS;c++){
            if(board[r][c][0]===1) c1+=board[r][c][1];
            if(board[r][c][0]===2) c2+=board[r][c][1];
        }
        const p1Score = '● ' + c1;
        const p2Score = c2 + ' ●';

        // ---- Banner ----
        let bannerHTML = '';
        if (st.game_over) {
            const col = COLORS[st.winner];
            bannerHTML = '<div class="winner-banner" style="color:'+col+'">' +
                         NAMES[st.winner]+' wins!</div>';
        } else {
            const col = COLORS[st.player];
            bannerHTML = '<span class="turn-dot" style="background:'+col+
                         ';box-shadow:0 0 8px 2px '+col+'"></span>' +
                         '<span style="color:'+col+'">'+NAMES[st.player]+"'s turn</span>";
        }
        // directly set banner DOM
        const bannerEl = document.getElementById('status-banner');
        if (bannerEl) bannerEl.innerHTML = bannerHTML;

        // directly set scores DOM
        const p1El = document.getElementById('p1-score');
        const p2El = document.getElementById('p2-score');
        if (p1El) p1El.textContent = p1Score;
        if (p2El) p2El.textContent = p2Score;

        // Return updated stores only (grid/banner/scores updated via DOM)
        return [board, st, window.dash_clientside.no_update,
                window.dash_clientside.no_update,
                window.dash_clientside.no_update];
    }
    """,
    Output("board-store", "data"),
    Output("turn-store", "data"),
    Output("p1-score", "children"),
    Output("p2-score", "children"),
    Output("status-banner", "children"),
    Input({"type": "cell", "row": ALL, "col": ALL}, "n_clicks"),
    Input("reset-btn", "n_clicks"),
    State("board-store", "data"),
    State("turn-store", "data"),
    prevent_initial_call=False,
)

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
