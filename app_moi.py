
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Kỳ Đạo | Cờ Tướng",
    page_icon="♟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root {
  --gold:#e8bd72;
  --gold2:#ffe4a8;
  --bg:#151913;
  --panel:#22271f;
  --line:#6d4a28;
}
* {box-sizing:border-box}
body {
  margin:0;
  color:#f5eddd;
  background:radial-gradient(ellipse at top,#343b2a,#11140f 75%);
  font-family:Arial,sans-serif;
}
button,select,input {font:inherit}
button {
  cursor:pointer;
  color:#f9edda;
  background:#343b2d;
  border:1px solid #76603c;
  border-radius:11px;
  padding:11px 15px;
  transition:background .2s,transform .2s,border-color .2s;
}
button:hover {
  background:#4a503a;
  border-color:var(--gold);
}
button:active {transform:scale(.97)}
button:disabled {opacity:.4;cursor:not-allowed}
#app {max-width:1100px;margin:auto;padding:16px}
.brand {
  text-align:center;
  font-size:clamp(30px,6vw,53px);
  font-weight:900;
  letter-spacing:5px;
  color:var(--gold2);
  text-shadow:0 3px 20px #d7a45144;
}
.subtitle {
  text-align:center;color:#c5b69a;
  margin:8px 0 25px;letter-spacing:2px;
}
.panel {
  background:#20251deF;
  border:1px solid #685437;
  border-radius:18px;
  padding:20px;
  box-shadow:0 15px 45px #0005;
}
.home {
  min-height:65vh;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  text-align:center;
  background:
    radial-gradient(ellipse at center,#5b462555,transparent 65%),
    linear-gradient(135deg,#292e21,#161913);
}
.home-mark {
  font-size:clamp(70px,14vw,130px);
  color:var(--gold);
  line-height:1.1;
  text-shadow:0 0 35px #c59c4d44;
}
.home h1 {font-size:clamp(25px,5vw,42px);margin:12px}
.home p {color:#c5bda9;line-height:1.7;max-width:550px}
.main-buttons {
  display:grid;grid-template-columns:repeat(2,minmax(0,1fr));
  gap:12px;width:min(100%,500px);margin-top:20px;
}
.primary {
  background:linear-gradient(135deg,#b88a45,#80602f);
  color:#fff7e6;border:1px solid #f0cd88;
  font-weight:bold;padding:15px 12px;
}
.primary:hover {background:linear-gradient(135deg,#d0a45d,#98743d)}
.small-note {font-size:12px;color:#a9a18f;margin-top:20px}
.hidden {display:none!important}
#gameView {max-width:900px;margin:auto}
.topbar {
  display:flex;align-items:center;justify-content:space-between;
  gap:8px;flex-wrap:wrap;margin-bottom:12px;
}
.topbar strong {color:var(--gold2);font-size:20px}
.status {
  text-align:center;padding:11px;border-radius:12px;
  background:#171b14;border:1px solid #49442f;
  margin:10px 0;color:#ead6a9;
  min-height:43px;
}
.board-wrap {width:min(100%,650px);margin:0 auto;position:relative}
.board {
  position:relative;width:100%;aspect-ratio:8/9;
  overflow:hidden;border:5px solid #664222;border-radius:5px;
  background-color:#e5c58b;
  background-image:
    linear-gradient(#654322 1.2px,transparent 1.2px),
    linear-gradient(90deg,#654322 1.2px,transparent 1.2px);
  background-size:12.5% 11.111111%;
  background-position:6.25% 5.555555%;
  box-shadow:0 12px 28px #0008,inset 0 0 0 2px #b99055;
}
.river {
  position:absolute;left:6.25%;width:87.5%;
  top:50%;transform:translateY(-50%);
  height:11.111%;display:flex;align-items:center;
  justify-content:space-around;color:#704723;
  font-size:clamp(12px,2.5vw,22px);letter-spacing:5px;
  background:#e5c58b;pointer-events:none;
}
.palace {
  position:absolute;left:31.25%;width:37.5%;
  height:22.222%;pointer-events:none;opacity:.9;
}
.palace.top {top:5.555%}
.palace.bottom {bottom:5.555%}
.palace:before,.palace:after {
  content:"";position:absolute;left:0;top:0;
  width:100%;height:100%;border-top:1.2px solid #654322;
  transform:rotate(26.565deg);transform-origin:center;
}
.palace:after {transform:rotate(-26.565deg)}
.piece {
  position:absolute;width:10.6%;aspect-ratio:1;
  border-radius:50%;display:flex;align-items:center;
  justify-content:center;z-index:3;
  transform:translate(-50%,-50%);
  transition:left .4s ease-in-out,top .4s ease-in-out,
    box-shadow .18s,filter .18s;
  font-family:"KaiTi","STKaiti",serif;
  font-weight:900;font-size:clamp(17px,4vw,29px);
  background:radial-gradient(circle at 35% 28%,#fff3d2,#dfc18a 60%,#a77a3f);
  border:2px solid #76502b;color:#29251e;
  box-shadow:0 3px 4px #0005,inset 0 0 0 2px #f7e0ae;
  padding:0;line-height:1;
}
.piece.black {
  color:#20221c;background:radial-gradient(circle at 35% 28%,#fff,#d5d1c6 65%,#99958a);
  border-color:#55564d;
  box-shadow:0 3px 4px #0005,inset 0 0 0 2px #f8f5e9;
}
.piece.selected {
  box-shadow:0 0 0 4px #f7d36a,0 0 20px #f7d36a;
  z-index:5;
}
.piece.last {
  box-shadow:0 0 0 3px #75a96b,0 3px 4px #0005;
}
.piece.hint {
  box-shadow:0 0 0 4px #6cb8ee,0 0 20px #6cb8ee;
}
.piece:disabled {opacity:1;cursor:default}
.controls {
  display:grid;grid-template-columns:repeat(4,minmax(0,1fr));
  gap:8px;margin-top:14px;
}
.controls button {padding:11px 5px;font-size:13px}
.section-title {color:var(--gold2);margin:0 0 10px}
.extras {
  display:grid;grid-template-columns:repeat(2,minmax(0,1fr));
  gap:12px;margin-top:14px;
}
.extras .panel {padding:15px}
.extras p {color:#c6c0b1;font-size:14px;line-height:1.6}
.overlay {
  position:fixed;inset:0;z-index:20;
  display:flex;align-items:center;justify-content:center;
  padding:14px;background:#080a08d9;
  backdrop-filter:blur(7px);
}
.modal {
  width:min(100%,510px);max-height:92vh;overflow:auto;
  padding:24px;background:#22271f;border:1px solid #8c7044;
  border-radius:20px;box-shadow:0 20px 80px #0009;
  position:relative;
}
.modal h2 {color:var(--gold2);margin:0 30px 8px 0}
.modal p {color:#c6c0b1;line-height:1.6}
.close {
  position:absolute;right:12px;top:12px;
  padding:5px 11px;font-size:22px;border:0;
  background:transparent;
}
.modal-buttons {
  display:grid;grid-template-columns:repeat(2,minmax(0,1fr));
  gap:10px;margin-top:18px;
}
.difficulties {
  display:grid;grid-template-columns:repeat(2,minmax(0,1fr));
  gap:10px;margin-top:15px;
}
.difficulty-card {
  min-height:86px;text-align:left;padding:14px;
  background:#2b3025;
}
.difficulty-card b {display:block;color:var(--gold2);margin-bottom:7px}
.difficulty-card span {font-size:12px;color:#c0b7a4}
.field {margin:16px 0}
.field label {display:block;margin-bottom:8px;color:#e9d9b9}
.field input[type=range] {width:100%;accent-color:#d5ad65}
.field select {width:100%;padding:10px;background:#303528;color:white;border-radius:8px}
.tutorial li {margin:9px 0;color:#ded5c2;line-height:1.6}
#resultOverlay {z-index:40;background:#090b09eF}
.result-box {
  text-align:center;width:min(100%,650px);
  padding:35px 18px;border:1px solid #b69350;
  border-radius:22px;background:linear-gradient(140deg,#353a29,#151912);
  box-shadow:0 0 70px #000b;
}
.result-title {
  font-size:clamp(38px,9vw,76px);font-weight:1000;
  color:#ffdf92;text-shadow:0 0 24px #e6b45177;
  animation:appear .7s ease both;
}
@keyframes appear {
  from {opacity:0;transform:scale(.7)}
  to {opacity:1;transform:scale(1)}
}
.thinking-dots:after {content:"";animation:dots 1.2s infinite}
@keyframes dots {
  0%{content:""} 25%{content:"."}
  50%{content:".."} 75%{content:"..."}
}
@media(max-width:560px) {
  #app {padding:8px}
  .panel {padding:12px}
  .board {border-width:3px}
  .piece {width:10.7%;border-width:1.5px}
  .controls {grid-template-columns:repeat(2,minmax(0,1fr))}
  .extras {grid-template-columns:1fr}
  .modal {padding:20px 15px}
  .main-buttons {grid-template-columns:1fr}
}
</style>
</head>
<body>
<div id="app">
  <div class="brand">KỲ ĐẠO</div>
  <div class="subtitle" data-t="subtitle">CỜ TƯỚNG · KHAI CUỘC CỦA RIÊNG BẠN</div>

  <section id="homeView" class="panel home">
    <div class="home-mark">帥　將</div>
    <h1 data-t="welcome">Chào mừng đến Kỳ Đạo</h1>
    <p data-t="intro">Một bàn cờ, nhiều chiến thuật. Luyện tư duy, tìm nước đi và thử sức với máy.</p>
    <div class="main-buttons">
      <button class="primary" onclick="openModes()" data-t="play">♟ BẮT ĐẦU CHƠI</button>
      <button onclick="openModal('tutorialModal')" data-t="learn">📖 HƯỚNG DẪN</button>
      <button onclick="openSettings()" data-t="settings">⚙ CÀI ĐẶT</button>
      <button onclick="openModal('aboutModal')" data-t="about">ⓘ GIỚI THIỆU</button>
    </div>
    <div class="small-note">KỲ ĐẠO · XIANGQI</div>
  </section>

  <section id="gameView" class="hidden">
    <div class="topbar">
      <button onclick="openSettings()">⚙ <span data-t="settingsShort">Cài đặt</span></button>
      <strong>KỲ ĐẠO</strong>
      <button onclick="goHome()" data-t="home">⌂ Sảnh chính</button>
    </div>
    <div class="status" id="status" data-t="redTurn">Đến lượt Đỏ</div>
    <div class="board-wrap">
      <div class="board" id="board">
        <div class="palace top"></div>
        <div class="palace bottom"></div>
        <div class="river" data-t="river">楚 河　　漢 界</div>
      </div>
    </div>
    <div class="controls">
      <button onclick="showHint()" data-t="hint">💡 Gợi ý</button>
      <button onclick="undoMove()" data-t="undo">↶ Hoàn tác</button>
      <button onclick="newGame()" data-t="newGame">⟳ Ván mới</button>
      <button onclick="resign()" data-t="resign">⚑ Đầu hàng</button>
    </div>
    <div class="extras">
      <div class="panel">
        <h3 class="section-title" data-t="tools">Công cụ</h3>
        <p data-t="toolText">Chọn quân cờ của bạn, sau đó chọn giao điểm muốn đi. Nước đi hợp lệ sẽ được kiểm tra tự động.</p>
        <button onclick="openModal('tutorialModal')" data-t="rules">📖 Xem luật chơi</button>
      </div>
      <div class="panel">
        <h3 class="section-title" data-t="gameInfo">Thông tin ván đấu</h3>
        <p id="modeInfo">Chế độ: Đấu với máy</p>
        <p><span data-t="elapsed">Thời gian</span>: <b id="clock">00:00</b></p>
        <p id="moveInfo">Số nước đi: 0</p>
      </div>
    </div>
  </section>
</div>

<div class="overlay hidden" id="modeModal">
  <div class="modal">
    <button class="close" onclick="closeModal('modeModal')">×</button>
    <h2 data-t="chooseMode">Chọn chế độ chơi</h2>
    <p id="modeIntro" data-t="modeIntro">Chọn cách chơi phù hợp với bạn.</p>
    <div class="modal-buttons" id="modeButtons">
      <button class="primary" onclick="showDifficulties()" data-t="vsBot">♟ Đấu với máy</button>
      <button onclick="startGame('human',1)" data-t="vsHuman">♟ Đấu hai người</button>
    </div>
    <div class="difficulties hidden" id="difficultyList">
      <button class="difficulty-card" onclick="startGame('bot',1)"><b data-t="easy">🌱 Dễ</b><span data-t="easyDesc">Làm quen chiến thuật</span></button>
      <button class="difficulty-card" onclick="startGame('bot',2)"><b data-t="medium">⚔️ Trung bình</b><span data-t="mediumDesc">Biết bảo vệ quân</span></button>
      <button class="difficulty-card" onclick="startGame('bot',3)"><b data-t="hard">🔥 Khó</b><span data-t="hardDesc">Tính toán sâu hơn</span></button>
      <button class="difficulty-card" onclick="startGame('bot',4)"><b data-t="expert">👑 Siêu khó</b><span data-t="expertDesc">Đối thủ mạnh nhất</span></button>
      <button style="grid-column:1/-1" onclick="backToModes()" data-t="back">← QUAY LẠI</button>
    </div>
  </div>
</div>

<div class="overlay hidden" id="settingsModal">
  <div class="modal">
    <button class="close" onclick="closeModal('settingsModal')">×</button>
    <h2 data-t="settingsTitle">Cài đặt Kỳ Đạo</h2>
    <div class="field">
      <label data-t="language">Ngôn ngữ</label>
      <select id="language" onchange="setLanguage(this.value)">
        <option value="vi">Tiếng Việt</option>
        <option value="en">English</option>
      </select>
    </div>
    <div class="field">
      <label data-t="sound">Âm thanh hiệu ứng</label>
      <input id="soundToggle" type="checkbox" checked onchange="soundOn=this.checked">
    </div>
    <div class="field">
      <label data-t="soundVolume">Âm lượng hiệu ứng</label>
      <input id="soundVolume" type="range" min="0" max="100" value="45" oninput="soundVol=this.value/100">
    </div>
    <div class="field">
      <label data-t="music">Nhạc nền</label>
      <input id="musicToggle" type="checkbox" onchange="toggleMusic(this.checked)">
    </div>
    <div class="field">
      <label data-t="musicVolume">Âm lượng nhạc nền</label>
      <input id="musicVolume" type="range" min="0" max="100" value="12" oninput="musicVol=this.value/100;updateMusicVolume()">
    </div>
    <button class="primary" style="width:100%" onclick="closeModal('settingsModal')" data-t="done">XONG</button>
  </div>
</div>

<div class="overlay hidden" id="tutorialModal">
  <div class="modal">
    <button class="close" onclick="closeModal('tutorialModal')">×</button>
    <h2 data-t="tutorialTitle">Hướng dẫn chơi cờ tướng</h2>
    <ul class="tutorial" id="tutorialList">
      <li><b>Tướng:</b> đi một ô ngang hoặc dọc trong cung.</li>
      <li><b>Sĩ:</b> đi chéo một ô trong cung.</li>
      <li><b>Tượng:</b> đi chéo hai ô, không qua sông và không bị cản mắt.</li>
      <li><b>Mã:</b> đi theo hình chữ L, có thể bị cản chân.</li>
      <li><b>Xe:</b> đi ngang hoặc dọc, không bị quân cản.</li>
      <li><b>Pháo:</b> đi như xe; khi ăn phải nhảy qua đúng một quân.</li>
      <li><b>Tốt:</b> tiến một ô; qua sông có thể đi ngang, không đi lùi.</li>
    </ul>
    <p data-t="tutorialTip">Mục tiêu là chiếu bí tướng đối phương. Không được đi nước khiến tướng của mình bị chiếu.</p>
    <button class="primary" style="width:100%" onclick="closeModal('tutorialModal')" data-t="gotIt">ĐÃ HIỂU</button>
  </div>
</div>

<div class="overlay hidden" id="aboutModal">
  <div class="modal">
    <button class="close" onclick="closeModal('aboutModal')">×</button>
    <h2 data-t="aboutTitle">Kỳ Đạo</h2>
    <p data-t="aboutText">Trò chơi cờ tướng chạy trực tiếp trên trình duyệt, có đấu hai người, đấu máy và các công cụ hỗ trợ luyện tập.</p>
    <button onclick="closeModal('aboutModal')" data-t="gotIt">ĐÃ HIỂU</button>
  </div>
</div>

<div class="overlay hidden" id="resultOverlay">
  <div class="result-box">
    <div class="result-title" id="resultTitle">CHIẾN THẮNG</div>
    <p id="resultText"></p>
    <div class="modal-buttons">
      <button class="primary" onclick="newGame()" data-t="playAgain">Chơi lại</button>
      <button onclick="goHome()" data-t="home">Sảnh chính</button>
    </div>
  </div>
</div>

<script>
const $ = id => document.getElementById(id);

const T = {
vi:{
 subtitle:"CỜ TƯỚNG · KHAI CUỘC CỦA RIÊNG BẠN",
 welcome:"Chào mừng đến Kỳ Đạo",
 intro:"Một bàn cờ, nhiều chiến thuật. Luyện tư duy, tìm nước đi và thử sức với máy.",
 play:"♟ BẮT ĐẦU CHƠI",learn:"📖 HƯỚNG DẪN",settings:"⚙ CÀI ĐẶT",
 about:"ⓘ GIỚI THIỆU",settingsShort:"Cài đặt",home:"⌂ Sảnh chính",
 redTurn:"Đến lượt Đỏ",blackTurn:"Đến lượt Đen",
 chooseMode:"Chọn chế độ chơi",modeIntro:"Chọn cách chơi phù hợp với bạn.",
 vsBot:"♟ Đấu với máy",vsHuman:"♟ Đấu hai người",
 easy:"🌱 Dễ",medium:"⚔️ Trung bình",hard:"🔥 Khó",expert:"👑 Siêu khó",
 easyDesc:"Làm quen chiến thuật",mediumDesc:"Biết bảo vệ quân",
 hardDesc:"Tính toán sâu hơn",expertDesc:"Đối thủ mạnh nhất",
 back:"← QUAY LẠI",settingsTitle:"Cài đặt Kỳ Đạo",
 language:"Ngôn ngữ",sound:"Âm thanh hiệu ứng",
 soundVolume:"Âm lượng hiệu ứng",music:"Nhạc nền",
 musicVolume:"Âm lượng nhạc nền",done:"XONG",
 tutorialTitle:"Hướng dẫn chơi cờ tướng",
 tutorialTip:"Mục tiêu là chiếu bí tướng đối phương. Không được đi nước khiến tướng của mình bị chiếu.",
 gotIt:"ĐÃ HIỂU",aboutTitle:"Kỳ Đạo",
 aboutText:"Trò chơi cờ tướng chạy trực tiếp trên trình duyệt, có đấu hai người, đấu máy và các công cụ hỗ trợ luyện tập.",
 hint:"💡 Gợi ý",undo:"↶ Hoàn tác",newGame:"⟳ Ván mới",
 resign:"⚑ Đầu hàng",tools:"Công cụ",
 toolText:"Chọn quân cờ của bạn, sau đó chọn giao điểm muốn đi. Nước đi hợp lệ sẽ được kiểm tra tự động.",
 rules:"📖 Xem luật chơi",gameInfo:"Thông tin ván đấu",
 elapsed:"Thời gian",river:"楚 河　　漢 界",
 playAgain:"Chơi lại",botThinking:"Máy đang suy nghĩ",
 yourTurn:"Đến lượt bạn",choosePiece:"Hãy chọn quân của bạn.",
 invalid:"Nước đi không hợp lệ.",check:"CHIẾU TƯỚNG!",
 checkmate:"Chiếu bí!",stalemate:"Hết nước đi hợp lệ!",
 redWins:"ĐỎ CHIẾN THẮNG",blackWins:"ĐEN CHIẾN THẮNG",
 draw:"VÁN ĐẤU KẾT THÚC",resignAsk:"Bạn có chắc muốn đầu hàng?",
 noHint:"Chưa tìm được gợi ý.",hintText:"Nước gợi ý đã được đánh dấu.",
 noUndo:"Không có nước đi để hoàn tác.",modeBot:"Đấu với máy",
 modeHuman:"Đấu hai người",moveCount:"Số nước đi",
 tutorialItems:[
 "<b>Tướng:</b> đi một ô ngang hoặc dọc trong cung.",
 "<b>Sĩ:</b> đi chéo một ô trong cung.",
 "<b>Tượng:</b> đi chéo hai ô, không qua sông và không bị cản mắt.",
 "<b>Mã:</b> đi theo hình chữ L, có thể bị cản chân.",
 "<b>Xe:</b> đi ngang hoặc dọc, không bị quân cản.",
 "<b>Pháo:</b> đi như xe; khi ăn phải nhảy qua đúng một quân.",
 "<b>Tốt:</b> tiến một ô; qua sông có thể đi ngang, không đi lùi."
]},
en:{
 subtitle:"XIANGQI · YOUR NEXT MOVE STARTS HERE",
 welcome:"Welcome to Ky Dao",
 intro:"One board, countless strategies. Train your mind and challenge the computer.",
 play:"♟ START GAME",learn:"📖 HOW TO PLAY",settings:"⚙ SETTINGS",
 about:"ⓘ ABOUT",settingsShort:"Settings",home:"⌂ Main menu",
 redTurn:"Red to move",blackTurn:"Black to move",
 chooseMode:"Choose game mode",modeIntro:"Choose how you want to play.",
 vsBot:"♟ Play computer",vsHuman:"♟ Two players",
 easy:"🌱 Easy",medium:"⚔️ Medium",hard:"🔥 Hard",expert:"👑 Expert",
 easyDesc:"Learn the basics",mediumDesc:"Defends its pieces",
 hardDesc:"Deeper calculation",expertDesc:"Strongest opponent",
 back:"← BACK",settingsTitle:"Ky Dao settings",
 language:"Language",sound:"Sound effects",
 soundVolume:"Sound volume",music:"Background music",
 musicVolume:"Music volume",done:"DONE",
 tutorialTitle:"How to play Xiangqi",
 tutorialTip:"The goal is to checkmate the enemy general. Never make a move that leaves your own general in check.",
 gotIt:"GOT IT",aboutTitle:"Ky Dao",
 aboutText:"A browser-based Xiangqi game with two-player mode, computer opponents and training tools.",
 hint:"💡 Hint",undo:"↶ Undo",newGame:"⟳ New game",
 resign:"⚑ Resign",tools:"Tools",
 toolText:"Select one of your pieces, then select its destination. Legal moves are checked automatically.",
 rules:"📖 Rules",gameInfo:"Game information",
 elapsed:"Time",river:"楚 河　　漢 界",
 playAgain:"Play again",botThinking:"Computer thinking",
 yourTurn:"Your turn",choosePiece:"Select one of your pieces.",
 invalid:"Illegal move.",check:"CHECK!",
 checkmate:"Checkmate!",stalemate:"No legal moves!",
 redWins:"RED WINS",blackWins:"BLACK WINS",
 draw:"GAME OVER",resignAsk:"Are you sure you want to resign?",
 noHint:"No hint available.",hintText:"Suggested move highlighted.",
 noUndo:"No move to undo.",modeBot:"Play computer",
 modeHuman:"Two players",moveCount:"Moves",
 tutorialItems:[
 "<b>General:</b> one step orthogonally inside the palace.",
 "<b>Advisor:</b> one diagonal step inside the palace.",
 "<b>Elephant:</b> two diagonal steps, cannot cross the river or jump a blocked eye.",
 "<b>Horse:</b> moves in an L shape and can be blocked at its leg.",
 "<b>Chariot:</b> moves orthogonally without jumping pieces.",
 "<b>Cannon:</b> moves like a chariot; captures by jumping exactly one piece.",
 "<b>Soldier:</b> moves forward; after crossing the river it may also move sideways."
]}
};

let lang="vi",soundOn=true,soundVol=.45,musicVol=.12;
let musicOn=false,audioCtx=null,musicTimer=null,musicOsc=null;
let mode="bot",level=2,turn="r",board=[],selected=null;
let history=[],lastMove=null,hintMove=null,gameOver=false;
let busy=false,startedAt=0,clockTimer=null,moveCount=0;
let humanSide="r";

function tr(k){return T[lang][k]||T.vi[k]||k}
function applyTranslations(){
 document.querySelectorAll("[data-t]").forEach(el=>{
  const k=el.getAttribute("data-t"); if(T[lang][k]) el.innerHTML=T[lang][k];
 });
 $("tutorialList").innerHTML=T[lang].tutorialItems.map(x=>"<li>"+x+"</li>").join("");
 if(!busy&&!gameOver)updateStatus();
}
function setLanguage(v){lang=v;applyTranslations()}
function openModal(id){$(id).classList.remove("hidden")}
function closeModal(id){$(id).classList.add("hidden")}
function openSettings(){$("language").value=lang;openModal("settingsModal")}
function openModes(){
 $("modeIntro").classList.remove("hidden");
 $("modeButtons").classList.remove("hidden");
 $("difficultyList").classList.add("hidden");
 openModal("modeModal");
}
function showDifficulties(){
 $("modeIntro").classList.add("hidden");
 $("modeButtons").classList.add("hidden");
 $("difficultyList").classList.remove("hidden");
}
function backToModes(){
 $("modeIntro").classList.remove("hidden");
 $("modeButtons").classList.remove("hidden");
 $("difficultyList").classList.add("hidden");
}
function goHome(){
 stopClock();busy=false;
 $("gameView").classList.add("hidden");
 $("homeView").classList.remove("hidden");
 document.querySelectorAll(".overlay").forEach(x=>x.classList.add("hidden"));
}
function startGame(m,l){
 mode=m;level=l;humanSide="r";
 closeModal("modeModal");
 $("homeView").classList.add("hidden");
 $("gameView").classList.remove("hidden");
 $("modeInfo").textContent=(lang==="vi"?"Chế độ: ":"Mode: ")+(mode==="human"?tr("modeHuman"):tr("modeBot")+" · "+[tr("easy"),tr("medium"),tr("hard"),tr("expert")][level-1]);
 newGame();
}
function initialBoard(){
 const b=Array.from({length:10},()=>Array(9).fill(null));
 const back=["R","H","E","A","K","A","E","H","R"];
 for(let x=0;x<9;x++){
  b[0][x]="b"+back[x]; b[9][x]="r"+back[x];
 }
 b[2][1]="bC";b[2][7]="bC";b[7][1]="rC";b[7][7]="rC";
 for(let x=0;x<9;x+=2){b[3][x]="bP";b[6][x]="rP"}
 return b;
}
function newGame(){
 stopClock();board=initialBoard();turn="r";selected=null;
 history=[];lastMove=null;hintMove=null;gameOver=false;busy=false;moveCount=0;
 startedAt=Date.now();$("resultOverlay").classList.add("hidden");
 drawBoard();updateStatus();updateInfo();startClock();
}
function stopClock(){if(clockTimer){clearInterval(clockTimer);clockTimer=null}}
function startClock(){
 stopClock();
 clockTimer=setInterval(()=>{
  if(!startedAt)return;
  let s=Math.floor((Date.now()-startedAt)/1000);
  $("clock").textContent=String(Math.floor(s/60)).padStart(2,"0")+":"+String(s%60).padStart(2,"0");
 },1000);
}
function updateInfo(){
 $("moveInfo").textContent=tr("moveCount")+": "+moveCount;
}
function updateStatus(msg){
 if(msg){$("status").textContent=msg;return}
 if(gameOver)return;
 $("status").textContent=busy?tr("botThinking")+"…":(turn===humanSide?tr("yourTurn"):(turn==="r"?tr("redTurn"):tr("blackTurn")));
}
function coords(x,y){
 return {left:(6.25+x*12.5)+"%",top:(5.555555+y*11.111111)+"%"};
}
const names={
 rK:"帥",rA:"仕",rE:"相",rH:"傌",rR:"俥",rC:"炮",rP:"兵",
 bK:"將",bA:"士",bE:"象",bH:"馬",bR:"車",bC:"砲",bP:"卒"
};
function drawBoard(){
 const el=$("board");
 el.querySelectorAll(".piece").forEach(p=>p.remove());
 for(let y=0;y<10;y++)for(let x=0;x<9;x++){
  const p=board[y][x];if(!p)continue;
  const btn=document.createElement("button");
  btn.className="piece "+(p[0]==="b"?"black":"");
  if(selected&&selected.x===x&&selected.y===y)btn.classList.add("selected");
  if(lastMove&&((lastMove.fx===x&&lastMove.fy===y)||(lastMove.tx===x&&lastMove.ty===y)))btn.classList.add("last");
  if(hintMove&&((hintMove.fx===x&&hintMove.fy===y)||(hintMove.tx===x&&hintMove.ty===y)))btn.classList.add("hint");
  btn.textContent=names[p]||"?";
  btn.setAttribute("aria-label",p);
  const pos=coords(x,y);btn.style.left=pos.left;btn.style.top=pos.top;
  btn.onclick=()=>clickSquare(x,y);
  el.appendChild(btn);
 }
}
function inside(x,y){return x>=0&&x<9&&y>=0&&y<10}
function palace(s,x,y){return x>=3&&x<=5&&(s==="r"?y>=7&&y<=9:y>=0&&y<=2)}
function riverSide(s,y){return s==="r"?y<=4:y>=5}
function addMove(out,x,y,nx,ny,b,side){
 if(inside(nx,ny)&&(!b[ny][nx]||b[ny][nx][0]!==side))out.push({fx:x,fy:y,tx:nx,ty:ny});
}
function pseudoMoves(b,x,y){
 const p=b[y][x];if(!p)return [];
 const s=p[0],t=p[1],out=[];
 const step=(dx,dy)=>addMove(out,x,y,x+dx,y+dy,b,s);
 if(t==="K"){
  for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){
   const nx=x+dx,ny=y+dy;if(palace(s,nx,ny))step(dx,dy);
  }
  for(let ny=y+(s==="r"?-1:1);inside(x,ny);ny+=(s==="r"?-1:1)){
   if(b[ny][x]){
    if(b[ny][x][1]==="K"&&b[ny][x][0]!==s)out.push({fx:x,fy:y,tx:x,ty:ny});
    break;
   }
  }
 }else if(t==="A"){
  for(const [dx,dy] of [[1,1],[1,-1],[-1,1],[-1,-1]]){
   const nx=x+dx,ny=y+dy;if(palace(s,nx,ny))step(dx,dy);
  }
 }else if(t==="E"){
  for(const [dx,dy] of [[2,2],[2,-2],[-2,2],[-2,-2]]){
   const nx=x+dx,ny=y+dy,mx=x+dx/2,my=y+dy/2;
   if(inside(nx,ny)&&!riverSide(s,ny)&&!b[my][mx])step(dx,dy);
  }
 }else if(t==="H"){
  const opts=[
   [1,2,0,1],[-1,2,0,1],[1,-2,0,-1],[-1,-2,0,-1],
   [2,1,1,0],[2,-1,1,0],[-2,1,-1,0],[-2,-1,-1,0]
  ];
  for(const [dx,dy,lx,ly] of opts){
   if(!b[y+ly]?.[x+lx])step(dx,dy);
  }
 }else if(t==="R"||t==="C"){
  for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let nx=x+dx,ny=y+dy,screen=false;
   while(inside(nx,ny)){
    const target=b[ny][nx];
    if(t==="R"){
     if(!target)out.push({fx:x,fy:y,tx:nx,ty:ny});
     else {if(target[0]!==s)out.push({fx:x,fy:y,tx:nx,ty:ny});break}
    }else{
     if(!screen){
      if(!target)out.push({fx:x,fy:y,tx:nx,ty:ny});
      else screen=true;
     }else if(target){
      if(target[0]!==s)out.push({fx:x,fy:y,tx:nx,ty:ny});
      break;
     }
    }
    nx+=dx;ny+=dy;
   }
  }
 }else if(t==="P"){
  const forward=s==="r"?-1:1;
  step(0,forward);
  if(riverSide(s,y)){step(1,0);step(-1,0)}
 }
 return out;
}
function copyBoard(b){return b.map(row=>row.slice())}
function applyMove(b,m){
 const n=copyBoard(b);n[m.ty][m.tx]=n[m.fy][m.fx];n[m.fy][m.fx]=null;return n;
}
function findGeneral(b,s){
 for(let y=0;y<10;y++)for(let x=0;x<9;x++)if(b[y][x]===s+"K")return {x,y};
 return null;
}
function attacked(b,x,y,bySide){
 for(let yy=0;yy<10;yy++)for(let xx=0;xx<9;xx++){
  const p=b[yy][xx];
  if(p&&p[0]===bySide&&pseudoMoves(b,xx,yy).some(m=>m.tx===x&&m.ty===y))return true;
 }
 return false;
}
function inCheck(b,s){
 const k=findGeneral(b,s);
 if(!k)return true;
 return attacked(b,k.x,k.y,s==="r"?"b":"r");
}
function legalMoves(b,s){
 const out=[];
 for(let y=0;y<10;y++)for(let x=0;x<9;x++){
  if(b[y][x]?.[0]!==s)continue;
  for(const m of pseudoMoves(b,x,y)){
   const n=applyMove(b,m);
   if(!inCheck(n,s))out.push(m);
  }
 }
 return out;
}
function legalFrom(x,y){return pseudoMoves(board,x,y).filter(m=>!inCheck(applyMove(board,m),turn))}
function clickSquare(x,y){
 if(gameOver||busy)return;
 if(mode==="bot"&&turn!==humanSide)return;
 const p=board[y][x];
 if(selected){
  const m=legalFrom(selected.x,selected.y).find(a=>a.tx===x&&a.ty===y);
  if(m){makeMove(m);return}
 }
 if(p&&p[0]===turn){
  selected={x,y};hintMove=null;drawBoard();playSound(420,.045);
 }else{
  selected=null;drawBoard();updateStatus(tr("invalid"));
 }
}
function makeMove(m,fromBot=false){
 if(gameOver)return;
 const mover=turn, captured=board[m.ty][m.tx];
 history.push({
  board:copyBoard(board),turn,selected,lastMove: lastMove?{...lastMove}:null,
  hintMove:hintMove?{...hintMove}:null,moveCount
 });
 board=applyMove(board,m);turn=turn==="r"?"b":"r";
 selected=null;hintMove=null;lastMove={...m};moveCount++;
 drawBoard();updateInfo();
 playSound(captured?260:520,captured?.12:.06);
 if(inCheck(board,turn))updateStatus(tr("check"));
 else updateStatus();
 const moves=legalMoves(board,turn);
 if(!moves.length){
  gameOver=true;busy=false;stopClock();
  const winner=mover;
  finishGame(winner===humanSide?tr("redWins").replace("ĐỎ","ĐỎ"):winner==="r"?tr("redWins"):tr("blackWins"),winner);
  return;
 }
 if(mode==="bot"&&turn!==humanSide){
  busy=true;updateStatus(tr("botThinking")+"…");
  window.setTimeout(()=>{
   if(gameOver||mode!=="bot"||turn===humanSide)return;
   const move=chooseBotMove();
   if(move){busy=false;makeMove(move,true)}
   else {busy=false;finishGame(tr("draw"),null)}
  },2000);
 }
}
function finishGame(title,winner){
 gameOver=true;busy=false;stopClock();
 $("resultTitle").textContent=title;
 $("resultText").textContent=winner?(lang==="vi"?"Ván đấu đã kết thúc.":"The game has ended."):(lang==="vi"?"Không còn nước đi hợp lệ.":"No legal moves remain.");
 $("resultOverlay").classList.remove("hidden");
}
function resign(){
 if(gameOver)return;
 if(!confirm(tr("resignAsk")))return;
 const winner=turn==="r"?"b":"r";
 finishGame(winner==="r"?tr("redWins"):tr("blackWins"),winner);
}
function undoMove(){
 if(!history.length||gameOver){updateStatus(tr("noUndo"));return}
 let count=1;
 if(mode==="bot"&&history.length>=2&&turn===humanSide)count=2;
 for(let i=0;i<count&&history.length;i++){
  const h=history.pop();board=copyBoard(h.board);turn=h.turn;
  lastMove=h.lastMove;selected=h.selected;hintMove=h.hintMove;moveCount=h.moveCount;
 }
 busy=false;gameOver=false;$("resultOverlay").classList.add("hidden");
 drawBoard();updateInfo();updateStatus();playSound(320,.06);
}
function showHint(){
 if(gameOver||busy)return;
 const moves=legalMoves(board,turn);
 if(!moves.length){updateStatus(tr("noHint"));return}
 let best=moves[0],bestScore=-Infinity;
 for(const m of moves){
  const captured=board[m.ty][m.tx];
  let score=captured?pieceValue(captured[1])*1.4:0;
  const n=applyMove(board,m);
  if(inCheck(n,turn==="r"?"b":"r"))score+=8;
  score+=Math.random()*.1;
  if(score>bestScore){bestScore=score;best=m}
 }
 hintMove={...best};drawBoard();updateStatus(tr("hintText"));playSound(650,.06);
}
const VALUES={K:10000,R:900,C:450,H:400,E:200,A:200,P:100};
function pieceValue(t){return VALUES[t]||0}
function evaluate(b,side){
 let score=0;
 for(let y=0;y<10;y++)for(let x=0;x<9;x++){
  const p=b[y][x];if(!p)continue;
  let v=pieceValue(p[1]);
  if(p[1]==="P")v+=(p[0]==="r"?(9-y):y)*3;
  if(p[1]==="H"||p[1]==="R")v+=2;
  score+=p[0]===side?v:-v;
 }
 return score;
}
function chooseBotMove(){
 const moves=legalMoves(board,turn);
 if(!moves.length)return null;
 // Four levels: progressively deeper search with alpha-beta pruning.
 const depth=[1,1,2,2][level-1];
 let best=moves[0],bestScore=-Infinity;
 // At higher levels, shuffle order a little to vary equal moves.
 moves.sort(()=>Math.random()-.5);
 for(const m of moves){
  const n=applyMove(board,m);
  const score=-search(n,turn==="r"?"b":"r",depth-1,-Infinity,Infinity,turn);
  if(score>bestScore){bestScore=score;best=m}
 }
 return best;
}
function search(b,side,depth,alpha,beta,rootSide){
 const moves=legalMoves(b,side);
 if(!moves.length)return inCheck(b,side)?-100000-depth:0;
 if(depth<=0)return evaluate(b,rootSide);
 moves.sort((a,c)=>{
  const va=b[a.ty][a.tx]?pieceValue(b[a.ty][a.tx][1]):0;
  const vc=b[c.ty][c.tx]?pieceValue(b[c.ty][c.tx][1]):0;
  return vc-va;
 });
 let best=-Infinity;
 for(const m of moves){
  const n=applyMove(b,m);
  const v=-search(n,side==="r"?"b":"r",depth-1,-beta,-alpha,side);
  // Search returns scores from the side-to-move perspective.
  const adjusted=side===rootSide?v:-v;
  if(adjusted>best)best=adjusted;
  alpha=Math.max(alpha,adjusted);
  if(alpha>=beta)break;
 }
 return best===-Infinity?evaluate(b,rootSide):best;
}
function playSound(freq,duration){
 if(!soundOn||soundVol<=0)return;
 try{
  audioCtx=audioCtx||new (window.AudioContext||window.webkitAudioContext)();
  const o=audioCtx.createOscillator(),g=audioCtx.createGain();
  o.type="sine";o.frequency.value=freq;
  g.gain.value=soundVol*.08;
  o.connect(g);g.connect(audioCtx.destination);
  o.start();g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+duration);
  o.stop(audioCtx.currentTime+duration);
 }catch(e){}
}
function toggleMusic(on){
 musicOn=on;
 if(!on){if(musicTimer)clearInterval(musicTimer);musicTimer=null;return}
 try{
  audioCtx=audioCtx||new (window.AudioContext||window.webkitAudioContext)();
  if(musicTimer)clearInterval(musicTimer);
  const notes=[196,246.94,293.66,246.94,174.61,220,261.63,220];
  let i=0;
  musicTimer=setInterval(()=>{
   if(!musicOn||musicVol<=0)return;
   try{
    const o=audioCtx.createOscillator(),g=audioCtx.createGain();
    o.type="sine";o.frequency.value=notes[i++%notes.length];
    g.gain.value=musicVol*.035;
    o.connect(g);g.connect(audioCtx.destination);
    o.start();g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+1.1);
    o.stop(audioCtx.currentTime+1.1);
   }catch(e){}
  },1250);
 }catch(e){}
}
function updateMusicVolume(){/* Volume is read when each note plays. */}
applyTranslations();
</script>
</body>
</html>
"""

components.html(HTML, height=1800, scrolling=True)
