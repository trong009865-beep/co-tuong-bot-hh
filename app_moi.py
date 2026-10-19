
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cờ Tướng | Kỳ Đạo",
    page_icon="♟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu, header, footer, [data-testid="stToolbar"],
[data-testid="stHeader"], [data-testid="stDecoration"] {
    display: none !important;
}
.stApp {
    background: #100b0b;
}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
iframe {
    border: 0 !important;
}
</style>
""", unsafe_allow_html=True)

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* { box-sizing: border-box; }

html, body {
    margin: 0;
    padding: 0;
    background: #100b0b;
    color: #f7e8c3;
    font-family: Georgia, "Times New Roman", serif;
}

button {
    font: inherit;
    cursor: pointer;
}

#app {
    width: 100%;
    min-height: 100vh;
    margin: auto;
    padding: 10px;
}

.gold {
    border: 1px solid #c7a15b;
    color: #ffe8b0;
    background: linear-gradient(145deg, #754023, #381715);
    border-radius: 9px;
    padding: 11px 16px;
    box-shadow: 0 4px 12px #0008;
    transition: .2s;
}

.gold:hover {
    filter: brightness(1.25);
    transform: translateY(-2px);
}

.secondary {
    background: linear-gradient(145deg, #28201b, #17100f);
    border-color: #795a35;
}

.small {
    color: #c4ae91;
    font-size: 13px;
    line-height: 1.7;
}

h2 {
    font-size: 23px;
    color: #f0d095;
    margin: 5px 0 14px;
}

h3 {
    color: #e9c47d;
}

.panel {
    background: linear-gradient(145deg, #281a15, #140e0d);
    border: 1px solid #846039;
    border-radius: 13px;
    padding: 17px;
    margin: 12px 0;
}

.row {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    align-items: center;
}

.row button {
    flex: 1;
    min-width: 105px;
}

/* ===== MÀN HÌNH CHÍNH ===== */

#home {
    position: relative;
}

.hero {
    position: relative;
    min-height: calc(100vh - 20px);
    overflow: hidden;
    display: flex;
    align-items: center;
    border: 1px solid #8f6837;
    background:
        radial-gradient(ellipse at 78% 43%,
            #703021 0%, transparent 36%),
        radial-gradient(ellipse at 17% 95%,
            #551819 0%, transparent 48%),
        linear-gradient(110deg,
            #100909 0%, #24100e 55%, #100a09 100%);
    box-shadow: 0 0 35px #000;
}

/* Họa tiết nền */
.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    pointer-events: none;
    opacity: .13;
    background:
        repeating-linear-gradient(
            45deg,
            transparent 0 44px,
            #d2ad62 45px,
            transparent 46px 88px
        );
}

/* Bàn cờ trang trí bên phải, dựng bằng CSS */
.hero::after {
    content: "";
    position: absolute;
    width: min(47vw, 590px);
    aspect-ratio: 1 / 1;
    right: 3%;
    top: 50%;
    transform: translateY(-50%) rotate(-7deg);
    border: 12px solid #70421f;
    border-radius: 5px;
    outline: 2px solid #c49b55;
    outline-offset: 5px;
    background-color: #c7a16b;
    background-image:
        linear-gradient(
            90deg,
            transparent 11%,
            #624020 11.3%,
            transparent 11.7%,
            transparent 22.5%,
            #624020 22.8%,
            transparent 23.2%,
            transparent 34%,
            #624020 34.3%,
            transparent 34.7%,
            transparent 45.5%,
            #624020 45.8%,
            transparent 46.2%,
            transparent 57%,
            #624020 57.3%,
            transparent 57.7%,
            transparent 68.5%,
            #624020 68.8%,
            transparent 69.2%,
            transparent 80%,
            #624020 80.3%,
            transparent 80.7%
        ),
        linear-gradient(
            0deg,
            transparent 11%,
            #624020 11.3%,
            transparent 11.7%,
            transparent 22.5%,
            #624020 22.8%,
            transparent 23.2%,
            transparent 34%,
            #624020 34.3%,
            transparent 34.7%,
            transparent 45.5%,
            #624020 45.8%,
            transparent 46.2%,
            transparent 57%,
            #624020 57.3%,
            transparent 57.7%,
            transparent 68.5%,
            #624020 68.8%,
            transparent 69.2%,
            transparent 80%,
            #624020 80.3%,
            transparent 80.7%
        ),
        #c7a16b;
    box-shadow: 0 22px 55px #000b;
    opacity: .72;
    pointer-events: none;
}

.hero-content {
    position: relative;
    z-index: 2;
    width: 47%;
    padding: 35px 0 35px 6%;
}

.kicker {
    color: #d9b76f;
    letter-spacing: 4px;
    font-size: 12px;
}

h1 {
    font-size: clamp(42px, 6vw, 76px);
    color: #f7d99a;
    margin: 15px 0 2px;
    text-shadow: 0 4px 20px #000;
}

.hero-subtitle {
    color: #d5b98b;
    font-size: 14px;
    line-height: 1.9;
    margin: 13px 0 25px;
}

.hero-buttons {
    display: flex;
    flex-direction: column;
    gap: 12px;
    max-width: 265px;
}

.hero-buttons button {
    width: 100%;
    min-height: 49px;
    font-size: 15px;
    letter-spacing: 1px;
}

/* ===== BẢNG CHỌN HIỆN ĐÈ LÊN MÀN HÌNH ===== */

.modal {
    display: none;
    position: fixed;
    inset: 0;
    z-index: 100;
    background: #080505d9;
    backdrop-filter: blur(5px);
    align-items: center;
    justify-content: center;
    padding: 18px;
}

.modal.show {
    display: flex;
}

.modal-box {
    width: min(440px, 100%);
    max-height: 90vh;
    overflow-y: auto;
    padding: 25px;
    border: 1px solid #c6a15e;
    border-radius: 15px;
    background:
        radial-gradient(ellipse at top, #54251b, transparent 70%),
        linear-gradient(145deg, #251511, #100b0a);
    box-shadow: 0 15px 60px #000;
    text-align: center;
}

.modal-box h2 {
    font-size: 26px;
}

.modal-box .row {
    margin-top: 15px;
}

.modal-box .row button {
    min-height: 45px;
}

#difficultyPanel {
    display: none;
}

#difficultyPanel.show {
    display: block;
}

#rulesPanel, #settingsPanel {
    display: none;
}

#rulesPanel.show, #settingsPanel.show {
    display: block;
}

input[type=range] {
    width: 100%;
    accent-color: #d0a052;
}

select {
    width: 100%;
    padding: 9px;
    background: #211613;
    color: #f7e8c3;
    border: 1px solid #896b42;
    border-radius: 8px;
}

/* ===== KHU VỰC CHƠI CỜ ===== */

#game {
    display: none;
}

.game-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}

.game-title {
    text-align: center;
    color: #efd093;
    font-size: 21px;
}

#status {
    color: #f1d39b;
    font-size: 15px;
}

#thinking {
    color: #b9a38b;
    font-size: 12px;
    min-height: 18px;
}

#boardWrap {
    position: relative;
    width: min(100%, 650px);
    margin: 12px auto;
    border: 2px solid #b18a48;
    border-radius: 7px;
    overflow: hidden;
    background: #d8ae70;
    box-shadow: 0 8px 30px #0009;
}

canvas {
    display: block;
    width: 100%;
    height: auto;
    touch-action: manipulation;
}

#overlay {
    display: none;
    position: absolute;
    inset: 0;
    z-index: 5;
    background: #120b0bed;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 18px;
}

#overlay.show {
    display: flex;
}

.overlaybox {
    width: min(420px, 100%);
    border: 1px solid #d2aa61;
    background: linear-gradient(145deg, #411a17, #160f0e);
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 0 35px #000;
}

#result {
    font-size: clamp(30px, 7vw, 52px);
    color: #ffe3a0;
    font-weight: bold;
    margin: 10px 0 18px;
}

footer {
    padding: 14px;
    text-align: center;
    color: #8f7861;
    font-size: 12px;
}

@media (max-width: 650px) {
    #app {
        padding: 5px;
    }

    .hero {
        min-height: calc(100vh - 10px);
    }

    .hero::after {
        width: 78vw;
        right: -28%;
        top: 28%;
        opacity: .25;
    }

    .hero-content {
        width: 100%;
        padding: 25px 22px;
    }

    .hero-buttons {
        max-width: 235px;
    }

    .game-header button {
        padding: 9px 10px;
        font-size: 12px;
    }

    .panel {
        padding: 12px;
    }
}
</style>
</head>

<body>
<div id="app">

    <!-- MÀN HÌNH CHÍNH -->
    <section id="home">
        <div class="hero">
            <div class="hero-content">
                <div class="kicker">東方棋藝 · KỲ ĐẠO</div>
                <h1>象棋</h1>

                <div style="
                    font-size:23px;
                    color:#f0d49b;
                    letter-spacing:4px">
                    CỜ TƯỚNG
                </div>

                <div class="hero-subtitle">
                    Nghệ thuật chiến thuật phương Đông<br>
                    Mỗi nước đi mở ra một thế cờ mới
                </div>

                <div class="hero-buttons">
                    <button class="gold" onclick="openModes()">
                        ♟ BẮT ĐẦU
                    </button>

                    <button class="gold secondary"
                        onclick="openModal('rulesModal')">
                        📜 HƯỚNG DẪN
                    </button>

                    <button class="gold secondary"
                        onclick="openModal('settingsModal')">
                        ⚙ CÀI ĐẶT
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- BẢNG CHỌN CHẾ ĐỘ -->
    <div id="modeModal" class="modal">
        <div class="modal-box">
            <h2>CHỌN CHẾ ĐỘ</h2>
            <p class="small">Bạn cầm quân Đen và đi trước.</p>

            <div class="row">
                <button class="gold" onclick="showDifficulties()">
                    ♟ Đấu với máy
                </button>
                <button class="gold secondary"
                    onclick="startGame('human', 2)">
                    ♟ Đấu hai người
                </button>
            </div>

            <div id="difficultyPanel">
                <h3>Chọn độ khó</h3>
                <div class="row">
                    <button class="gold"
                        onclick="startGame('bot',1)">🌱 Dễ</button>
                    <button class="gold"
                        onclick="startGame('bot',2)">⚔ Trung bình</button>
                    <button class="gold"
                        onclick="startGame('bot',3)">🔥 Khó</button>
                    <button class="gold"
                        onclick="startGame('bot',4)">👑 Siêu khó</button>
                </div>
            </div>

            <button class="gold secondary"
                style="margin-top:18px;width:100%"
                onclick="closeModal('modeModal')">
                Quay lại
            </button>
        </div>
    </div>

    <!-- HƯỚNG DẪN -->
    <div id="rulesModal" class="modal">
        <div class="modal-box">
            <h2>HƯỚNG DẪN CHƠI</h2>
            <p class="small" style="text-align:left">
                • Mỗi lượt đi một quân theo luật của quân đó.<br>
                • Tướng không được đi vào ô đang bị đối phương tấn công.<br>
                • Hai Tướng không được nhìn thẳng mặt nhau khi không có quân chắn.<br>
                • Khi bị chiếu, phải tìm nước đi để thoát chiếu.<br>
                • Nếu đến lượt mà không có nước hợp lệ, ván đấu kết thúc.<br><br>
                Nhấn vào quân của mình, sau đó nhấn vào ô muốn đi.
            </p>
            <button class="gold secondary"
                onclick="closeModal('rulesModal')">Đóng</button>
        </div>
    </div>

    <!-- CÀI ĐẶT -->
    <div id="settingsModal" class="modal">
        <div class="modal-box">
            <h2>CÀI ĐẶT</h2>
            <label class="small">Âm lượng hiệu ứng</label>
            <input id="volume" type="range" min="0" max="100" value="45">
            <p class="small">
                Thanh âm lượng là phần giao diện; âm thanh chưa được tích hợp trong bản này.
            </p>
            <button class="gold secondary"
                onclick="closeModal('settingsModal')">Đóng</button>
        </div>
    </div>

    <!-- MÀN HÌNH CHƠI -->
    <section id="game">
        <div class="game-header">
            <button class="gold secondary"
                onclick="openModal('gameSettingsModal')">
                ⚙ Cài đặt
            </button>

            <div class="game-title">
                <div>KỲ ĐẠO</div>
                <div class="small" id="modeLabel">Đấu với máy</div>
            </div>

            <button class="gold secondary" onclick="goHome()">
                ⌂ Trang chủ
            </button>
        </div>

        <div class="panel">
            <div id="status">Đến lượt Đen</div>
            <div id="thinking"></div>
        </div>

        <div id="boardWrap">
            <canvas id="board" width="600" height="660"></canvas>

            <div id="overlay">
                <div class="overlaybox">
                    <div id="result">CHIẾN THẮNG</div>
                    <p id="resultText" class="small"></p>
                    <div class="row">
                        <button class="gold" onclick="newGame()">
                            Chơi lại
                        </button>
                        <button class="gold secondary" onclick="goHome()">
                            Trang chủ
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div class="panel">
            <h2>Công cụ trận đấu</h2>
            <div class="row">
                <button class="gold" onclick="showHint()">💡 Gợi ý</button>
                <button class="gold secondary" onclick="undoMove()">↶ Đi lại</button>
                <button class="gold secondary" onclick="newGame()">⟳ Ván mới</button>
                <button class="gold secondary" onclick="surrender()">🏳 Đầu hàng</button>
            </div>
        </div>

        <div id="gameSettingsModal" class="modal">
            <div class="modal-box">
                <h2>CÀI ĐẶT TRẬN ĐẤU</h2>
                <p class="small">Bạn có thể tiếp tục ván cờ hoặc trở về trang chủ.</p>
                <div class="row">
                    <button class="gold"
                        onclick="closeModal('gameSettingsModal')">
                        Tiếp tục
                    </button>
                    <button class="gold secondary" onclick="goHome()">
                        Trang chủ
                    </button>
                </div>
            </div>
        </div>
    </section>

    <footer>KỲ ĐẠO · Cờ tướng dành cho người yêu chiến thuật</footer>
</div>

<script>
const canvas = document.getElementById('board');
const ctx = canvas.getContext('2d');

const NAMES = {
    K:'將', A:'士', E:'象', H:'馬', R:'車', C:'炮', P:'卒',
    k:'帥', a:'仕', e:'相', h:'傌', r:'俥', c:'砲', p:'兵'
};

const VALUE = {
    K:10000, A:20, E:22, H:45, R:90, C:48, P:12
};

let board, turn='B', selected=null, legal=[], history=[];
let mode='bot', level=2, ended=false, hint=null, locked=false;

function initialBoard() {
    const b = Array.from({length:10}, () => Array(9).fill(null));
    const back = ['R','H','E','A','K','A','E','H','R'];

    for (let c=0; c<9; c++) {
        b[0][c] = back[c];
        b[9][c] = back[c].toLowerCase();
    }

    b[2][1]='C'; b[2][7]='C';
    b[7][1]='c'; b[7][7]='c';

    for (let c=0; c<9; c+=2) {
        b[3][c]='P';
        b[6][c]='p';
    }

    return b;
}

function inside(r,c) {
    return r>=0 && r<10 && c>=0 && c<9;
}

function side(p) {
    if (!p) return null;
    return p===p.toUpperCase() ? 'R' : 'B';
}

function copyBoard(b) {
    return b.map(row => row.slice());
}

function palace(s,r,c) {
    return c>=3 && c<=5 &&
        (s==='R' ? r>=0 && r<=2 : r>=7 && r<=9);
}

function river(s,r) {
    return s==='R' ? r>=5 : r<=4;
}

function pseudo(r,c,b) {
    const p=b[r][c];
    if (!p) return [];

    const s=side(p), t=p.toUpperCase(), out=[];

    function add(nr,nc) {
        if (!inside(nr,nc)) return;
        if (side(b[nr][nc])===s) return;
        out.push([nr,nc]);
    }

    if (t==='K') {
        for (const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]) {
            const nr=r+dr, nc=c+dc;
            if (palace(s,nr,nc)) add(nr,nc);
        }

        // Tướng có thể bắt Tướng đối phương nếu cùng cột không có quân chắn.
        for (const d of [-1,1]) {
            for (let nr=r+d; inside(nr,c); nr+=d) {
                if (b[nr][c]) {
                    if (b[nr][c].toUpperCase()==='K' &&
                        side(b[nr][c])!==s) {
                        add(nr,c);
                    }
                    break;
                }
            }
        }
    } else if (t==='A') {
        for (const [dr,dc] of [[1,1],[1,-1],[-1,1],[-1,-1]]) {
            const nr=r+dr, nc=c+dc;
            if (palace(s,nr,nc)) add(nr,nc);
        }
    } else if (t==='E') {
        for (const [dr,dc] of [[2,2],[2,-2],[-2,2],[-2,-2]]) {
            const nr=r+dr, nc=c+dc;
            if (!inside(nr,nc) || b[r+dr/2][c+dc/2]) continue;
            if (s==='R' && nr>4) continue;
            if (s==='B' && nr<5) continue;
            add(nr,nc);
        }
    } else if (t==='H') {
        const steps=[
            [-2,-1,-1,0],[-2,1,-1,0],
            [2,-1,1,0],[2,1,1,0],
            [-1,-2,0,-1],[1,-2,0,-1],
            [-1,2,0,1],[1,2,0,1]
        ];

        for (const [dr,dc,lr,lc] of steps) {
            if (inside(r+dr,c+dc) && !b[r+lr][c+lc]) {
                add(r+dr,c+dc);
            }
        }
    } else if (t==='R' || t==='C') {
        for (const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]) {
            let nr=r+dr, nc=c+dc, screen=false;

            while (inside(nr,nc)) {
                if (t==='R') {
                    if (!b[nr][nc]) {
                        out.push([nr,nc]);
                    } else {
                        if (side(b[nr][nc])!==s) out.push([nr,nc]);
                        break;
                    }
                } else {
                    if (!screen) {
                        if (!b[nr][nc]) out.push([nr,nc]);
                        else screen=true;
                    } else if (b[nr][nc]) {
                        if (side(b[nr][nc])!==s) out.push([nr,nc]);
                        break;
                    }
                }

                nr+=dr;
                nc+=dc;
            }
        }
    } else if (t==='P') {
        const dr=s==='R' ? 1 : -1;
        add(r+dr,c);

        if (river(s,r)) {
            add(r,c-1);
            add(r,c+1);
        }
    }

    return out;
}

function findKing(s,b) {
    const k=s==='R' ? 'K' : 'k';

    for (let r=0; r<10; r++) {
        for (let c=0; c<9; c++) {
            if (b[r][c]===k) return [r,c];
        }
    }

    return null;
}

function attacked(r,c,by,b) {
    for (let y=0; y<10; y++) {
        for (let x=0; x<9; x++) {
            if (side(b[y][x])===by &&
                pseudo(y,x,b).some(m=>m[0]===r && m[1]===c)) {
                return true;
            }
        }
    }

    return false;
}

function inCheck(s,b) {
    const k=findKing(s,b);
    if (!k) return true;

    return attacked(k[0],k[1],s==='R'?'B':'R',b);
}

function apply(b,from,to) {
    const n=copyBoard(b);
    n[to[0]][to[1]]=n[from[0]][from[1]];
    n[from[0]][from[1]]=null;
    return n;
}

function legalFor(r,c,b) {
    const s=side(b[r][c]);
    if (!s) return [];

    return pseudo(r,c,b).filter(to => {
        const n=apply(b,[r,c],to);
        return !inCheck(s,n);
    });
}

function allMoves(s,b) {
    const a=[];

    for (let r=0; r<10; r++) {
        for (let c=0; c<9; c++) {
            if (side(b[r][c])===s) {
                for (const to of legalFor(r,c,b)) {
                    a.push({from:[r,c],to});
                }
            }
        }
    }

    return a;
}

function evaluate(b) {
    let score=0;

    for (let r=0; r<10; r++) {
        for (let c=0; c<9; c++) {
            const p=b[r][c];
            if (!p) continue;

            const v=VALUE[p.toUpperCase()]||0;
            const progress=p.toUpperCase()==='P'
                ? (side(p)==='R' ? r : 9-r)*1.5
                : 0;

            score+=(side(p)==='R' ? 1 : -1)*(v+progress);
        }
    }

    return score;
}

function ordered(moves,b) {
    return moves.sort((a,z) => {
        const av=b[a.to[0]][a.to[1]]
            ? VALUE[b[a.to[0]][a.to[1]].toUpperCase()] : 0;

        const zv=b[z.to[0]][z.to[1]]
            ? VALUE[b[z.to[0]][z.to[1]].toUpperCase()] : 0;

        return zv-av;
    });
}

function search(b,depth,alpha,beta,sideToMove) {
    if (depth===0) return evaluate(b);

    const moves=ordered(allMoves(sideToMove,b),b);

    if (!moves.length) {
        return sideToMove==='R' ? -99999 : 99999;
    }

    if (sideToMove==='R') {
        let best=-Infinity;

        for (const m of moves) {
            best=Math.max(
                best,
                search(apply(b,m.from,m.to),depth-1,alpha,beta,'B')
            );

            alpha=Math.max(alpha,best);
            if (beta<=alpha) break;
        }

        return best;
    }

    let best=Infinity;

    for (const m of moves) {
        best=Math.min(
            best,
            search(apply(b,m.from,m.to),depth-1,alpha,beta,'R')
        );

        beta=Math.min(beta,best);
        if (beta<=alpha) break;
    }

    return best;
}

function botMove() {
    if (ended || turn!=='R') return;

    locked=true;
    document.getElementById('thinking').textContent=
        'Đang tính toán nước đi…';

    setTimeout(() => {
        if (ended) {
            locked=false;
            return;
        }

        const moves=ordered(allMoves('R',board),board);

        if (!moves.length) {
            finish('B');
            return;
        }

        let chosen=moves[0];

        if (level===1) {
            chosen=moves[
                Math.floor(Math.random()*Math.min(5,moves.length))
            ];
        } else {
            let best=-Infinity;

            // Mức siêu khó tìm sâu hơn, nhưng có thể tính toán chậm hơn.
            const depth=level===2 ? 1 : level===3 ? 2 : 3;

            for (const m of moves) {
                const n=apply(board,m.from,m.to);
                let v=search(n,depth-1,-Infinity,Infinity,'B');

                v+=Math.random()*0.05;

                if (v>best) {
                    best=v;
                    chosen=m;
                }
            }
        }

        makeMove(chosen.from,chosen.to);
        locked=false;
    },80);
}

/* ===== VẼ BÀN CỜ ===== */

function draw() {
    const W=600, H=660;

    ctx.clearRect(0,0,W,H);
    ctx.fillStyle='#d7b174';
    ctx.fillRect(0,0,W,H);

    const left=36, right=564, top=30, bottom=630;

    ctx.strokeStyle='#57371c';
    ctx.lineWidth=1.5;

    for (let r=0; r<10; r++) {
        const y=top+r*(bottom-top)/9;
        ctx.beginPath();
        ctx.moveTo(left,y);
        ctx.lineTo(right,y);
        ctx.stroke();
    }

    for (let c=0; c<9; c++) {
        const x=left+c*(right-left)/8;

        ctx.beginPath();
        ctx.moveTo(x,top);
        ctx.lineTo(x,top+4*(bottom-top)/9);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(x,top+5*(bottom-top)/9);
        ctx.lineTo(x,bottom);
        ctx.stroke();
    }

    ctx.beginPath();
    ctx.moveTo(left,top);
    ctx.lineTo(left,bottom);
    ctx.moveTo(right,top);
    ctx.lineTo(right,bottom);
    ctx.stroke();

    function palaceLine(c1,r1,c2,r2) {
        ctx.beginPath();
        ctx.moveTo(
            left+c1*(right-left)/8,
            top+r1*(bottom-top)/9
        );
        ctx.lineTo(
            left+c2*(right-left)/8,
            top+r2*(bottom-top)/9
        );
        ctx.stroke();
    }

    palaceLine(3,0,5,2);
    palaceLine(5,0,3,2);
    palaceLine(3,7,5,9);
    palaceLine(5,7,3,9);

    ctx.fillStyle='#795027';
    ctx.font='18px serif';
    ctx.textAlign='center';
    ctx.fillText('楚 河',210,top+4.5*(bottom-top)/9+7);
    ctx.fillText('漢 界',390,top+4.5*(bottom-top)/9+7);

    function pos(r,c) {
        return [
            left+c*(right-left)/8,
            top+r*(bottom-top)/9
        ];
    }

    if (selected) {
        const [x,y]=pos(selected[0],selected[1]);
        ctx.fillStyle='#e8c45a55';
        ctx.beginPath();
        ctx.arc(x,y,25,0,Math.PI*2);
        ctx.fill();
    }

    for (const m of legal) {
        const [x,y]=pos(m[0],m[1]);

        ctx.fillStyle=board[m[0]][m[1]]
            ? '#9f2f22aa' : '#3c6d37aa';

        ctx.beginPath();
        ctx.arc(x,y,board[m[0]][m[1]] ? 23 : 7,0,Math.PI*2);
        ctx.fill();
    }

    for (let r=0; r<10; r++) {
        for (let c=0; c<9; c++) {
            const p=board[r][c];
            if (!p) continue;

            const [x,y]=pos(r,c);
            const red=side(p)==='R';

            ctx.beginPath();
            ctx.arc(x,y,24,0,Math.PI*2);
            ctx.fillStyle='#f0d6a0';
            ctx.fill();

            ctx.lineWidth=red ? 3 : 2.5;
            ctx.strokeStyle=red ? '#a22b20' : '#29201a';
            ctx.stroke();

            ctx.beginPath();
            ctx.arc(x,y,19,0,Math.PI*2);
            ctx.lineWidth=1;
            ctx.strokeStyle=red ? '#c15c40' : '#6c5842';
            ctx.stroke();

            ctx.fillStyle=red ? '#a51f19' : '#28201a';
            ctx.font='bold 25px serif';
            ctx.textAlign='center';
            ctx.textBaseline='middle';
            ctx.fillText(NAMES[p],x,y+1);
        }
    }

    const king=findKing(turn,board);

    if (king && inCheck(turn,board)) {
        const [x,y]=pos(king[0],king[1]);

        ctx.strokeStyle='#ff3025';
        ctx.lineWidth=4;
        ctx.beginPath();
        ctx.arc(x,y,29,0,Math.PI*2);
        ctx.stroke();
    }

    if (hint) {
        const [x1,y1]=pos(hint.from[0],hint.from[1]);
        const [x2,y2]=pos(hint.to[0],hint.to[1]);

        ctx.strokeStyle='#00a8ff';
        ctx.lineWidth=4;
        ctx.beginPath();
        ctx.moveTo(x1,y1);
        ctx.lineTo(x2,y2);
        ctx.stroke();
    }
}

function coordinates(e) {
    const rect=canvas.getBoundingClientRect();

    const x=(e.clientX-rect.left)*600/rect.width;
    const y=(e.clientY-rect.top)*660/rect.height;

    const c=Math.round((x-36)/(528/8));
    const r=Math.round((y-30)/(600/9));

    return inside(r,c) ? [r,c] : null;
}

canvas.addEventListener('click',e => {
    if (ended || locked) return;
    if (mode==='bot' && turn==='R') return;

    const at=coordinates(e);
    if (!at) return;

    const [r,c]=at;

    if (selected && legal.some(m=>m[0]===r && m[1]===c)) {
        makeMove(selected,[r,c]);
        return;
    }

    if (side(board[r][c])===turn) {
        selected=at;
        legal=legalFor(r,c,board);
        hint=null;
    } else {
        selected=null;
        legal=[];
    }

    draw();
});

function makeMove(from,to) {
    if (ended) return;

    history.push({
        board:copyBoard(board),
        turn:turn
    });

    board=apply(board,from,to);
    turn=turn==='B' ? 'R' : 'B';

    selected=null;
    legal=[];
    hint=null;

    draw();
    updateStatus();

    const kingR=findKing('R',board);
    const kingB=findKing('B',board);

    if (!kingR) {
        finish('B');
        return;
    }

    if (!kingB) {
        finish('R');
        return;
    }

    const moves=allMoves(turn,board);

    if (!moves.length) {
        finish(turn==='R' ? 'B' : 'R');
        return;
    }

    if (mode==='bot' && turn==='R') {
        botMove();
    }
}

function updateStatus() {
    const s=turn==='B' ? 'Đen' : 'Đỏ';
    let msg='Đến lượt '+s;

    if (inCheck(turn,board)) {
        msg+=' — ĐANG BỊ CHIẾU!';
    }

    document.getElementById('status').textContent=msg;
    document.getElementById('thinking').textContent='';
}

function finish(winner) {
    ended=true;
    locked=false;

    const win=mode==='human'
        ? (winner==='B' ? 'ĐEN CHIẾN THẮNG' : 'ĐỎ CHIẾN THẮNG')
        : (winner==='B' ? 'CHIẾN THẮNG' : 'THẤT BẠI');

    document.getElementById('result').textContent=win;

    document.getElementById('resultText').textContent=
        'Ván đấu đã kết thúc. Bạn có thể chơi lại hoặc trở về trang chủ.';

    document.getElementById('overlay').classList.add('show');
    document.getElementById('status').textContent='Ván đấu kết thúc';
}

function startGame(m,l) {
    mode=m;
    level=l;

    newGame();

    document.getElementById('home').style.display='none';
    document.getElementById('game').style.display='block';
    closeModal('modeModal');

    document.getElementById('modeLabel').textContent=
        m==='human'
        ? 'Đấu hai người'
        : 'Đấu với máy · '+['','Dễ','Trung bình','Khó','Siêu khó'][l];
}

function newGame() {
    board=initialBoard();
    turn='B';
    selected=null;
    legal=[];
    history=[];
    ended=false;
    locked=false;
    hint=null;

    document.getElementById('overlay').classList.remove('show');
    document.getElementById('gameSettingsModal').classList.remove('show');

    draw();
    updateStatus();
}

function goHome() {
    ended=true;
    locked=false;

    document.getElementById('game').style.display='none';
    document.getElementById('home').style.display='block';

    document.getElementById('overlay').classList.remove('show');
    closeModal('gameSettingsModal');
}

function openModal(id) {
    document.getElementById(id).classList.add('show');
}

function closeModal(id) {
    document.getElementById(id).classList.remove('show');
}

function openModes() {
    document.getElementById('difficultyPanel').classList.remove('show');
    openModal('modeModal');
}

function showDifficulties() {
    document.getElementById('difficultyPanel').classList.add('show');
}

function undoMove() {
    if (!history.length || ended || locked) return;

    let n=(mode==='bot' && history.length>=2) ? 2 : 1;

    while (n-- && history.length) {
        const h=history.pop();
        board=h.board;
        turn=h.turn;
    }

    selected=null;
    legal=[];
    hint=null;

    draw();
    updateStatus();
}

function showHint() {
    if (ended || locked) return;

    const moves=allMoves(turn,board);
    if (!moves.length) return;

    let m=moves[Math.floor(Math.random()*moves.length)];

    if (mode==='bot' && turn==='B') {
        let best=-Infinity;

        for (const x of moves) {
            const v=search(
                apply(board,x.from,x.to),
                1,-Infinity,Infinity,'R'
            );

            if (v>best) {
                best=v;
                m=x;
            }
        }
    }

    hint={from:m.from,to:m.to};
    draw();
}

function surrender() {
    if (ended) return;
    finish(turn==='B' ? 'R' : 'B');
}

/* Khởi tạo bàn cờ */
board=initialBoard();
draw();
updateStatus();
</script>
</body>
</html>
"""

components.html(HTML, height=1000, scrolling=True)
