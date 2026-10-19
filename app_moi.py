
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Kỳ Đạo | Cờ Tướng",
    page_icon="♟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
*{box-sizing:border-box}
:root{--gold:#e7c27b;--gold2:#f8e3b1}
html,body{margin:0;padding:0;background:#130c09;color:#f8ead0;font-family:Georgia,"Times New Roman",serif}
button,select,input{font:inherit}
button{cursor:pointer;transition:.18s}
button:hover{filter:brightness(1.15);transform:translateY(-1px)}
#app{min-height:100vh;background:radial-gradient(ellipse at 75% 25%,#573020,#25140e 50%,#100a08)}
.topline{height:5px;background:linear-gradient(90deg,#651619,#f4d48e,#7e2226)}
.home{min-height:900px;position:relative;display:flex;align-items:center;padding:48px 6%;overflow:hidden}
.home-content{position:relative;z-index:2;width:49%;max-width:570px}
.brand{display:flex;align-items:center;gap:12px;color:var(--gold);font-size:14px;letter-spacing:4px}
.brand-icon{border:1px solid #b38a4e;border-radius:50%;width:44px;height:44px;display:grid;place-items:center;font-size:23px;flex-shrink:0}
.eyebrow{font-size:12px;letter-spacing:3px;color:#d5aa65;margin:28px 0 12px}
h1{font-size:clamp(48px,6vw,82px);line-height:1.04;margin:0;color:#f4d99d;font-weight:normal;text-shadow:0 4px 20px #000}
h1 span{display:block;font-size:.5em;letter-spacing:8px;margin-top:16px}
.intro{color:#d0bca2;font:15px/1.9 Arial,sans-serif;max-width:430px;margin:25px 0}
.hero-buttons{display:flex;flex-direction:column;gap:14px;width:min(360px,100%);margin-top:24px}
.hero-buttons button{width:100%;min-height:64px;padding:16px 22px;font-size:18px;font-weight:bold;letter-spacing:1px;border:1px solid #d2ac6b;border-radius:9px;box-shadow:0 7px 20px #0007}
.primary{background:linear-gradient(135deg,#b13b32,#65191c);color:#fff0d2}
.secondary{background:#211510;color:#f0d29a}
.home-foot{margin-top:30px;color:#a38a6b;font:11px Arial,sans-serif;letter-spacing:3px}
.board-showcase{position:absolute;right:4%;top:50%;transform:translateY(-50%);width:min(43vw,510px);filter:drop-shadow(0 25px 25px #000b)}
.board-frame{padding:10px;background:linear-gradient(135deg,#98602e,#e2bb72,#63391d);border:2px solid #d5a858;box-shadow:inset 0 0 0 4px #563018}
canvas{display:block;width:100%;height:auto}
#decorBoard{background:#d8b578}
.game{display:none;padding:24px 4% 35px;min-height:900px}
.game-top{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:20px}
.game-title{font-size:25px;color:var(--gold2)}
.small-btn{padding:11px 15px;border:1px solid #947044;border-radius:8px;color:#f5dfb2;background:#2c1b14;font-size:14px}
.game-layout{display:grid;grid-template-columns:minmax(0,650px) minmax(240px,1fr);gap:25px;align-items:start;max-width:1200px;margin:auto}
.play-area{position:relative;width:100%;padding:10px;background:linear-gradient(135deg,#a87339,#e5c580,#68401f);border:2px solid #e1b66a;box-shadow:0 18px 40px #0009}
#board{width:100%;height:auto;background:#d9b87c;touch-action:manipulation}
.game-side{background:#241713;border:1px solid #73502e;border-radius:12px;padding:20px}
.game-side h2{font-size:22px;color:var(--gold2);font-weight:normal;margin:0 0 14px}
.status{background:#160e0c;border:1px solid #503321;border-radius:8px;padding:13px;margin-bottom:14px;line-height:1.6;color:#ead6b5;font:14px/1.7 Arial,sans-serif}
.side-buttons{display:grid;grid-template-columns:1fr 1fr;gap:9px}
.side-buttons button{padding:12px 7px;border:1px solid #89643a;border-radius:7px;background:#3a2419;color:#f4dfb7;font-size:14px}
.side-buttons .danger{background:#6e2021}
.side-buttons .wide{grid-column:1/-1}
.section-title{color:#dcb76e;font-size:12px;letter-spacing:2px;margin:22px 0 9px}
.tip{color:#c8b59b;font:14px/1.8 Arial,sans-serif}
.overlay{display:none;position:fixed;z-index:1000;inset:0;background:#080504e8;align-items:center;justify-content:center;padding:15px}
.overlay.show{display:flex}
.modal{position:relative;width:min(540px,100%);max-height:90vh;overflow:auto;padding:27px;background:linear-gradient(145deg,#352017,#170e0c);border:1px solid #c59a55;border-radius:14px;box-shadow:0 20px 80px #000}
.modal h2{margin:0 0 17px;color:var(--gold2);font-size:27px;font-weight:normal;padding-right:25px}
.modal p,.modal li{font:14px/1.8 Arial,sans-serif;color:#e1cdb0}
.modal-buttons{display:grid;grid-template-columns:1fr;gap:11px}
.modal-buttons button{min-height:52px;padding:12px;border:1px solid #c6a063;border-radius:8px;background:#42251a;color:#f7e4bd;font-size:16px}
.close{position:absolute;right:13px;top:8px;border:0;background:transparent;color:#d9c4a3;font-size:28px}
.difficulty-card{display:grid;grid-template-columns:45px 1fr 18px;align-items:center;gap:12px;margin:10px 0;padding:13px;background:linear-gradient(120deg,#382117,#21130f);border:1px solid #76512e;border-radius:10px;color:#f5dfb2;cursor:pointer}
.difficulty-card:hover{border-color:#e4bd72;background:#4b291b}
.difficulty-icon{width:42px;height:42px;display:grid;place-items:center;border:1px solid #b68b4c;border-radius:50%;color:#edca83;font-size:23px}
.difficulty-card b{color:#f0d092;letter-spacing:1px}
.difficulty-card p{margin:5px 0 0;color:#cbb49a;font:13px/1.6 Arial,sans-serif}
.setting-row{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:13px 0;border-bottom:1px solid #4b3022;font:14px Arial,sans-serif}
.setting-row select{background:#160e0c;color:#f5dfb2;border:1px solid #96713d;border-radius:6px;padding:8px}
.setting-row input[type=range]{width:43%;accent-color:#d6a34f}
.setting-row input[type=checkbox]{width:19px;height:19px;accent-color:#b38a4e}
.result{display:none;position:absolute;inset:0;z-index:20;background:#100907e8;align-items:center;justify-content:center;text-align:center}
.result.show{display:flex}
.result-box{padding:20px}
.result h2{font-size:clamp(36px,7vw,70px);color:#f6d783;text-shadow:0 5px 20px #000;margin:0 0 15px}
.result p{font:16px Arial,sans-serif;color:#f4e2c5}
.result button{margin:6px;padding:13px 18px;border:1px solid #e0bb70;border-radius:8px;background:#772326;color:#fff0ce}
@media(max-width:800px){
 .home{padding:35px 6%;min-height:unset;display:flex;flex-direction:column;align-items:stretch}
 .home-content{width:100%;max-width:none}
 .board-showcase{position:relative;right:auto;top:auto;transform:none;width:min(88%,390px);margin:35px auto 0}
 .hero-buttons{width:min(390px,100%)}
 .game-layout{grid-template-columns:minmax(0,1fr)}
 .game-side{order:2}.game{padding:15px 3%}.game-title{font-size:20px}
}
</style>
</head>
<body>
<div id="app">
<div class="topline"></div>

<section class="home" id="home">
 <div class="home-content">
  <div class="brand"><div class="brand-icon">帥</div><span>KỲ ĐẠO · XIANGQI</span></div>
  <div class="eyebrow">NGHỆ THUẬT CỦA CHIẾN THUẬT</div>
  <h1>象棋<span>CỜ TƯỚNG</span></h1>
  <p class="intro">Một bàn cờ, hai chiến tuyến. Rèn luyện tư duy, tính toán từng nước đi và bảo vệ Tướng của bạn.</p>
  <div class="hero-buttons">
   <button class="primary" onclick="openModes()">♟ BẮT ĐẦU</button>
   <button class="secondary" onclick="openModal('helpModal')">📖 HƯỚNG DẪN</button>
   <button class="secondary" onclick="openModal('settingsModal')">⚙ CÀI ĐẶT</button>
  </div>
  <div class="home-foot">STRATEGY · PATIENCE · WISDOM</div>
 </div>
 <div class="board-showcase"><div class="board-frame"><canvas id="decorBoard" width="450" height="500"></canvas></div></div>
</section>

<section class="game" id="game">
 <div class="game-top">
  <div class="brand"><div class="brand-icon">帥</div><span>KỲ ĐẠO</span></div>
  <div class="game-title">BÀN CỜ TƯỚNG</div>
  <button class="small-btn" onclick="openModal('settingsModal')">⚙ CÀI ĐẶT</button>
 </div>
 <div class="game-layout">
  <div class="play-area">
   <canvas id="board" width="540" height="600"></canvas>
   <div class="result" id="result"><div class="result-box">
    <h2 id="resultTitle">CHIẾN THẮNG!</h2><p id="resultText"></p>
    <button onclick="newGame()">Chơi lại</button>
    <button onclick="goHome()">Về sảnh</button>
   </div></div>
  </div>
  <aside class="game-side">
   <h2>Thông tin ván đấu</h2>
   <div class="status" id="status">Đến lượt Đỏ. Chọn một quân cờ.</div>
   <div class="side-buttons">
    <button onclick="hintMove()">💡 Gợi ý</button>
    <button onclick="undoMove()">↶ Đi lại</button>
    <button onclick="newGame()">⟳ Ván mới</button>
    <button class="danger" onclick="resign()">Đầu hàng</button>
    <button class="wide" onclick="goHome()">⌂ Về sảnh chính</button>
   </div>
   <div class="section-title">CÔNG CỤ</div>
   <p class="tip">Gợi ý đánh dấu một nước tham khảo. Đi lại hoàn tác nước đi gần nhất.</p>
   <div class="section-title">NHẮC NHANH LUẬT CHƠI</div>
   <p class="tip">Mục tiêu là chiếu bí Tướng đối phương. Không được để Tướng mình bị chiếu. Pháo cần một quân làm ngòi khi ăn.</p>
  </aside>
 </div>
</section>
</div>

<div class="overlay" id="modeModal">
 <div class="modal">
  <button class="close" onclick="closeModal('modeModal')">×</button>
  <h2 id="modeTitle">Chọn chế độ chơi</h2>
  <p id="modeIntro">Chọn cách chơi phù hợp với bạn.</p>

  <div class="modal-buttons" id="mainModeButtons">
   <button onclick="showDifficulties()">♟ Đấu với máy</button>
   <button onclick="startGame('human',1)">♟ Đấu hai người</button>
  </div>

  <div id="difficultyList" style="display:none;margin-top:12px">
   <div class="difficulty-card" onclick="startGame('bot',1)">
    <div class="difficulty-icon">♟</div>
    <div><b>DỄ</b><p>Phù hợp cho người mới tập chơi.</p></div><span>›</span>
   </div>
   <div class="difficulty-card" onclick="startGame('bot',2)">
    <div class="difficulty-icon">⚔</div>
    <div><b>TRUNG BÌNH</b><p>Máy ưu tiên ăn quân và bảo vệ quân.</p></div><span>›</span>
   </div>
   <div class="difficulty-card" onclick="startGame('bot',3)">
    <div class="difficulty-icon">♜</div>
    <div><b>KHÓ</b><p>Thử thách khả năng tính toán chiến thuật.</p></div><span>›</span>
   </div>
   <div class="difficulty-card" onclick="startGame('bot',4)">
    <div class="difficulty-icon">冠</div>
    <div><b>SIÊU KHÓ</b><p>Mức thử thách cao nhất.</p></div><span>›</span>
   </div>
   <button class="small-btn" style="width:100%;margin-top:12px" onclick="backToModes()">← QUAY LẠI</button>
  </div>
 </div>
</div>

<div class="overlay" id="helpModal">
 <div class="modal">
  <button class="close" onclick="closeModal('helpModal')">×</button>
  <h2>Hướng dẫn chơi cờ tướng</h2>
  <p><b>1. Mục tiêu:</b> Chiếu bí Tướng đối phương để đối thủ không còn nước đi hợp lệ.</p>
  <p><b>2. Cách đi quân:</b></p>
  <ul>
   <li><b>Tướng:</b> đi ngang hoặc dọc một ô trong cung 3×3.</li>
   <li><b>Sĩ:</b> đi chéo một ô trong cung Tướng.</li>
   <li><b>Tượng:</b> đi chéo hai ô, không qua sông và không bị cản mắt.</li>
   <li><b>Xe:</b> đi ngang hoặc dọc qua các ô trống.</li>
   <li><b>Pháo:</b> đi như Xe; khi ăn quân phải nhảy qua một quân làm ngòi.</li>
   <li><b>Mã:</b> đi kiểu chữ L; chân Mã không được bị cản.</li>
   <li><b>Tốt:</b> đi thẳng một ô; qua sông được đi ngang, không đi lùi.</li>
  </ul>
  <p><b>3. Cách thao tác:</b> Nhấp quân của mình rồi nhấp ô muốn đi.</p>
  <p><b>4. Công cụ:</b> Gợi ý đánh dấu nước tham khảo; Đi lại hoàn tác nước trước; Ván mới khởi động lại; Đầu hàng kết thúc ván.</p>
  <div class="modal-buttons"><button onclick="closeModal('helpModal')">Đã hiểu</button></div>
 </div>
</div>

<div class="overlay" id="settingsModal">
 <div class="modal">
  <button class="close" onclick="closeModal('settingsModal')">×</button>
  <h2>Cài đặt trò chơi</h2>
  <div class="setting-row"><span>Ngôn ngữ</span>
   <select id="language" onchange="changeLanguage(this.value)">
    <option value="vi">Tiếng Việt</option><option value="en">English</option>
   </select>
  </div>
  <div class="setting-row"><span>Hiệu ứng âm thanh</span><input id="soundToggle" type="checkbox" checked onchange="settings.sound=this.checked"></div>
  <div class="setting-row"><span>Âm lượng hiệu ứng</span><input id="soundVolume" type="range" min="0" max="100" value="55" oninput="settings.volume=this.value/100"></div>
  <div class="setting-row"><span>Nhạc nền</span><input id="musicToggle" type="checkbox" onchange="toggleMusic(this.checked)"></div>
  <div class="setting-row"><span>Âm lượng nhạc nền</span><input id="musicVolume" type="range" min="0" max="100" value="18" oninput="settings.musicVolume=this.value/100;updateMusicVolume()"></div>
  <p class="tip">Nhạc nền bắt đầu phát sau khi bạn bật nhạc và tương tác với trang.</p>
  <div class="modal-buttons"><button onclick="closeModal('settingsModal')">Hoàn tất</button></div>
 </div>
</div>

<script>
const $=id=>document.getElementById(id);
let lang="vi";
let settings={sound:true,volume:.55,musicVolume:.18};
let audioCtx=null,musicTimer=null,musicOn=false,musicOsc=[];

const translations={
 vi:{
  red:"Đến lượt Đỏ. Chọn một quân cờ.",black:"Đến lượt Đen. Chọn một quân cờ.",
  thinking:"Máy đang suy nghĩ…",check:"Chiếu Tướng!",
  redWins:"ĐỎ CHIẾN THẮNG!",blackWins:"ĐEN CHIẾN THẮNG!"
 },
 en:{
  red:"Red to move. Select a piece.",black:"Black to move. Select a piece.",
  thinking:"Computer is thinking…",check:"Check!",
  redWins:"RED WINS!",blackWins:"BLACK WINS!"
 }
};
function tr(k){return translations[lang][k]||translations.vi[k]||k}
function changeLanguage(v){
 lang=v;
 updateStatus();
 $("resultTitle").textContent=ended?(turn==="R"?tr("blackWins"):tr("redWins")):"";
 if(ended)$("resultTitle").textContent=$("resultTitle").textContent||"";
 drawBoardCanvas($("decorBoard"),true);
 drawBoard();
}
function openModal(id){$(id).classList.add("show")}
function closeModal(id){$(id).classList.remove("show")}
function openModes(){
 $("mainModeButtons").style.display="grid";
 $("difficultyList").style.display="none";
 $("modeTitle").textContent="Chọn chế độ chơi";
 $("modeIntro").textContent="Chọn cách chơi phù hợp với bạn.";
 openModal("modeModal");
}
function showDifficulties(){
 $("mainModeButtons").style.display="none";
 $("difficultyList").style.display="block";
 $("modeTitle").textContent="Chọn độ khó";
 $("modeIntro").textContent="Chọn một trong 4 chế độ đấu máy.";
}
function backToModes(){
 $("difficultyList").style.display="none";
 $("mainModeButtons").style.display="grid";
 $("modeTitle").textContent="Chọn chế độ chơi";
 $("modeIntro").textContent="Chọn cách chơi phù hợp với bạn.";
}
function ensureAudio(){
 if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();
 if(audioCtx.state==="suspended")audioCtx.resume();
}
function beep(freq=440,duration=.09,type="sine"){
 if(!settings.sound)return;
 try{
  ensureAudio();
  const o=audioCtx.createOscillator(),g=audioCtx.createGain();
  o.type=type;o.frequency.value=freq;g.gain.value=settings.volume*.12;
  o.connect(g);g.connect(audioCtx.destination);o.start();
  g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+duration);
  o.stop(audioCtx.currentTime+duration);
 }catch(e){}
}
function updateMusicVolume(){
 musicOsc.forEach(x=>{try{x.gain.gain.value=settings.musicVolume*.025}catch(e){}});
}
function toggleMusic(on){
 musicOn=on;
 try{ensureAudio()}catch(e){return}
 if(musicTimer){clearInterval(musicTimer);musicTimer=null}
 musicOsc.forEach(x=>{try{x.osc.stop()}catch(e){}});
 musicOsc=[];
 if(!on)return;
 const notes=[220,261.63,329.63,293.66,196,246.94,293.66,261.63];
 let i=0;
 function playNote(){
  if(!musicOn)return;
  try{
   const osc=audioCtx.createOscillator(),gain=audioCtx.createGain();
   osc.type="sine";osc.frequency.value=notes[i++%notes.length];
   gain.gain.value=settings.musicVolume*.025;
   osc.connect(gain);gain.connect(audioCtx.destination);
   osc.start();
   gain.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+1.5);
   osc.stop(audioCtx.currentTime+1.6);
   musicOsc.push({osc,gain});
   if(musicOsc.length>20)musicOsc.shift();
  }catch(e){}
 }
 playNote();musicTimer=setInterval(playNote,1300);
}

const initial=[
 ["r","h","e","a","k","a","e","h","r"],
 [null,null,null,null,null,null,null,null,null],
 [null,"c",null,null,null,null,null,"c",null],
 ["s",null,"s",null,"s",null,"s",null,"s"],
 [null,null,null,null,null,null,null,null,null],
 [null,null,null,null,null,null,null,null,null],
 ["S",null,"S",null,"S",null,"S",null,"S"],
 [null,"C",null,null,null,null,null,"C",null],
 [null,null,null,null,null,null,null,null,null],
 ["R","H","E","A","K","A","E","H","R"]
];

let board=[],turn="R",selected=null,legal=[],history=[],lastMove=null;
let mode="human",level=1,ended=false,botBusy=false,hint=null;
let pieceAnimation=null;
const ANIMATION_DURATION=400;

const redPieces={K:"帥",A:"仕",E:"相",R:"俥",H:"傌",C:"炮",S:"兵"};
const blackPieces={k:"將",a:"士",e:"象",r:"車",h:"馬",c:"砲",s:"卒"};

function side(p){return p===null?null:(p===p.toUpperCase()?"R":"B")}
function inside(r,c){return r>=0&&r<10&&c>=0&&c<9}
function palace(s,r,c){return c>=3&&c<=5&&(s==="R"?r>=7&&r<=9:r>=0&&r<=2)}
function riverCrossed(s,r){return s==="R"?r<=4:r>=5}

function pseudoMoves(r,c){
 const p=board[r][c];if(!p)return [];
 const s=side(p),t=p.toLowerCase(),out=[];
 function add(nr,nc){if(inside(nr,nc)&&side(board[nr][nc])!==s)out.push([nr,nc])}
 const orth=[[1,0],[-1,0],[0,1],[0,-1]];
 if(t==="k"){
  orth.forEach(([dr,dc])=>{let nr=r+dr,nc=c+dc;if(palace(s,nr,nc))add(nr,nc)});
  const dr=s==="R"?-1:1;
  for(let nr=r+dr;inside(nr,c);nr+=dr){
   if(board[nr][c]){
    if(board[nr][c].toLowerCase()==="k"&&side(board[nr][c])!==s)out.push([nr,c]);
    break;
   }
  }
 }else if(t==="a"){
  [[1,1],[1,-1],[-1,1],[-1,-1]].forEach(([dr,dc])=>{
   let nr=r+dr,nc=c+dc;if(palace(s,nr,nc))add(nr,nc);
  });
 }else if(t==="e"){
  [[2,2],[2,-2],[-2,2],[-2,-2]].forEach(([dr,dc])=>{
   const nr=r+dr,nc=c+dc;
   if(inside(nr,nc)&&!riverCrossed(s,nr)&&!board[r+dr/2][c+dc/2])add(nr,nc);
  });
 }else if(t==="r"){
  orth.forEach(([dr,dc])=>{
   let nr=r+dr,nc=c+dc;
   while(inside(nr,nc)){
    if(!board[nr][nc])out.push([nr,nc]);
    else{if(side(board[nr][nc])!==s)out.push([nr,nc]);break}
    nr+=dr;nc+=dc;
   }
  });
 }else if(t==="c"){
  orth.forEach(([dr,dc])=>{
   let nr=r+dr,nc=c+dc,screen=false;
   while(inside(nr,nc)){
    if(!screen){if(!board[nr][nc])out.push([nr,nc]);else screen=true}
    else if(board[nr][nc]){if(side(board[nr][nc])!==s)out.push([nr,nc]);break}
    nr+=dr;nc+=dc;
   }
  });
 }else if(t==="h"){
  [[-2,-1,-1,0],[-2,1,-1,0],[2,-1,1,0],[2,1,1,0],
   [-1,-2,0,-1],[1,-2,0,-1],[-1,2,0,1],[1,2,0,1]].forEach(([dr,dc,lr,lc])=>{
   const nr=r+dr,nc=c+dc;
   if(inside(nr,nc)&&!board[r+lr][c+lc])add(nr,nc);
  });
 }else if(t==="s"){
  const f=s==="R"?-1:1;
  add(r+f,c);
  if(riverCrossed(s,r)){add(r,c-1);add(r,c+1)}
 }
 return out;
}
function findGeneral(s){
 const k=s==="R"?"K":"k";
 for(let r=0;r<10;r++)for(let c=0;c<9;c++)if(board[r][c]===k)return [r,c];
 return null;
}
function isAttacked(r,c,by){
 for(let y=0;y<10;y++)for(let x=0;x<9;x++){
  const p=board[y][x];
  if(p&&side(p)===by&&pseudoMoves(y,x).some(([nr,nc])=>nr===r&&nc===c))return true;
 }
 return false;
}
function inCheck(s){
 const k=findGeneral(s);if(!k)return true;
 return isAttacked(k[0],k[1],s==="R"?"B":"R");
}
function legalMoves(r,c){
 const p=board[r][c];if(!p)return [];
 const s=side(p);
 return pseudoMoves(r,c).filter(([nr,nc])=>{
  const captured=board[nr][nc];
  board[nr][nc]=p;board[r][c]=null;
  const safe=!inCheck(s);
  board[r][c]=p;board[nr][nc]=captured;
  return safe;
 });
}
function allMoves(s){
 const arr=[];
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  if(side(board[r][c])===s)legalMoves(r,c).forEach(([nr,nc])=>arr.push({r,c,nr,nc}));
 }
 return arr;
}
function cloneBoard(){return board.map(row=>row.slice())}

function updateStatus(){
 if(!ended&&!botBusy)$("status").textContent=turn==="R"?tr("red"):tr("black");
}
function newGame(){
 pieceAnimation=null;
 board=initial.map(row=>row.slice());
 turn="R";selected=null;legal=[];history=[];lastMove=null;
 ended=false;botBusy=false;hint=null;
 $("result").classList.remove("show");
 updateStatus();drawBoard();beep(330,.1);
}
function startGame(m,l){
 mode=m;level=l;
 closeModal("modeModal");
 $("home").style.display="none";
 $("game").style.display="block";
 newGame();
}
function goHome(){
 pieceAnimation=null;
 $("game").style.display="none";
 $("home").style.display="flex";
 closeModal("settingsModal");closeModal("helpModal");closeModal("modeModal");
 drawBoard();
}

/* Hoạt ảnh quân cờ kéo dài 0,4 giây */
function animatePieceMove(m,piece){
 pieceAnimation={r:m.r,c:m.c,nr:m.nr,nc:m.nc,piece,start:performance.now()};
 drawBoard();
 requestAnimationFrame(animationFrame);
}
function animationFrame(now){
 if(!pieceAnimation)return;
 if(now-pieceAnimation.start>=ANIMATION_DURATION){
  pieceAnimation=null;
  drawBoard();
  return;
 }
 drawBoard(now);
 requestAnimationFrame(animationFrame);
}

function makeMove(m){
 if(ended)return;
 const movingPiece=board[m.r][m.c];
 const captured=board[m.nr][m.nc];

 history.push({board:cloneBoard(),turn,lastMove:lastMove?{...lastMove}:null});
 board[m.nr][m.nc]=movingPiece;
 board[m.r][m.c]=null;

 lastMove={r:m.r,c:m.c,nr:m.nr,nc:m.nc};
 selected=null;legal=[];hint=null;

 animatePieceMove(m,movingPiece);
 beep(captured?680:430,.08,captured?"triangle":"sine");

 turn=turn==="R"?"B":"R";
 if(!findGeneral(turn)){finish(turn==="R"?"B":"R");return}

 if(inCheck(turn))$("status").textContent=tr("check")+" "+(turn==="R"?tr("red"):tr("black"));
 else updateStatus();

 if(allMoves(turn).length===0){finish(turn==="R"?"B":"R");return}

 if(mode==="bot"&&turn==="B"){
  botBusy=true;
  $("status").textContent=tr("thinking");
  setTimeout(botMove,2000);
 }
}
function finish(winner){
 ended=true;botBusy=false;
 pieceAnimation=null;
 $("resultTitle").textContent=winner==="R"?tr("redWins"):tr("blackWins");
 $("resultText").textContent="";
 $("result").classList.add("show");
 drawBoard();beep(740,.25,"triangle");
}
function resign(){
 if(ended)return;
 if(!confirm(lang==="vi"?"Bạn có chắc muốn đầu hàng không?":"Are you sure you want to resign?"))return;
 finish(turn==="R"?"B":"R");
}
function undoMove(){
 if(!history.length||ended)return;
 let steps=(mode==="bot"&&turn==="R"&&history.length>=2)?2:1;
 while(steps--&&history.length){
  const prev=history.pop();
  board=prev.board;turn=prev.turn;lastMove=prev.lastMove;
 }
 pieceAnimation=null;
 selected=null;legal=[];hint=null;botBusy=false;ended=false;
 $("result").classList.remove("show");
 updateStatus();drawBoard();beep(300,.08);
}
function hintMove(){
 if(ended||botBusy||pieceAnimation)return;
 const moves=allMoves(turn);if(!moves.length)return;
 let best=moves[0],bestScore=-9999;
 const value={k:10000,r:9,c:5,h:4,e:2,a:2,s:1};
 moves.forEach(m=>{
  let score=Math.random()*2;
  const target=board[m.nr][m.nc];
  if(target)score+=(value[target.toLowerCase()]||0);
  if(target&&target.toLowerCase()==="k")score+=10000;
  if(score>bestScore){bestScore=score;best=m}
 });
 hint=best;drawBoard();
 $("status").textContent=lang==="vi"?"Gợi ý: nước đi được viền vàng.":"Hint: the suggested move is marked in gold.";
 beep(580,.1);
}
function botMove(){
 if(ended||turn!=="B"||mode!=="bot"){botBusy=false;return}
 const moves=allMoves("B");
 if(!moves.length){finish("R");return}
 const value={k:10000,r:900,c:450,h:400,e:200,a:200,s:100};
 function scoreMove(m){
  const target=board[m.nr][m.nc];
  let score=Math.random()*20;
  if(target)score+=(value[target.toLowerCase()]||0)*1.5;
  const p=board[m.r][m.c];
  board[m.nr][m.nc]=p;board[m.r][m.c]=null;
  if(inCheck("B"))score-=1000;
  if(inCheck("R"))score+=80;
  board[m.r][m.c]=p;board[m.nr][m.nc]=target;
  if(level===1)score=Math.random()*100+(target?50:0);
  if(level===2)score+=Math.random()*35;
  if(level===3)score+=Math.random()*12;
  if(level===4)score+=Math.random()*3;
  return score;
 }
 moves.sort((a,b)=>scoreMove(b)-scoreMove(a));
 let chosen=moves[0];
 if(level===1&&Math.random()<.55)chosen=moves[Math.floor(Math.random()*moves.length)];
 botBusy=false;
 makeMove(chosen);
}
function clickBoard(e){
 if(ended||botBusy||pieceAnimation||(mode==="bot"&&turn==="B"))return;
 const canvas=$("board"),rect=canvas.getBoundingClientRect();
 const x=(e.clientX-rect.left)*canvas.width/rect.width;
 const y=(e.clientY-rect.top)*canvas.height/rect.height;
 const c=Math.round((x-30)/60),r=Math.round((y-30)/60);
 if(!inside(r,c)||Math.abs(x-(30+c*60))>29||Math.abs(y-(30+r*60))>29)return;
 const p=board[r][c];
 if(selected&&legal.some(([nr,nc])=>nr===r&&nc===c)){
  makeMove({r:selected[0],c:selected[1],nr:r,nc:c});
  return;
 }
 if(p&&side(p)===turn){
  selected=[r,c];legal=legalMoves(r,c);hint=null;beep(510,.06);drawBoard();
 }else{
  selected=null;legal=[];drawBoard();
 }
}
function drawPiece(ctx,x,y,rad,text,s){
 ctx.beginPath();ctx.arc(x+1,y+2,rad+1,0,Math.PI*2);ctx.fillStyle="#684222";ctx.fill();
 ctx.beginPath();ctx.arc(x,y,rad,0,Math.PI*2);ctx.fillStyle="#ead5a5";ctx.fill();
 ctx.lineWidth=2;ctx.strokeStyle=s==="R"?"#a22b2c":"#302019";ctx.stroke();
 ctx.beginPath();ctx.arc(x,y,rad-4,0,Math.PI*2);ctx.lineWidth=1;
 ctx.strokeStyle=s==="R"?"#bb4840":"#8d6b42";ctx.stroke();
 ctx.fillStyle=s==="R"?"#a31e27":"#29201b";
 ctx.font=`bold ${Math.max(13,rad*1.12)}px Georgia`;
 ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillText(text,x,y+1);
}
function drawBoardCanvas(canvas,isDecor=false){
 if(!canvas)return;
 const ctx=canvas.getContext("2d"),w=canvas.width,h=canvas.height;
 ctx.clearRect(0,0,w,h);
 ctx.fillStyle="#d9b87c";ctx.fillRect(0,0,w,h);
 for(let i=0;i<10;i++){
  ctx.strokeStyle="rgba(105,61,27,.08)";ctx.beginPath();
  ctx.moveTo(0,i*h/10);ctx.lineTo(w,i*h/10+8);ctx.stroke();
 }
 const pad=30,dx=(w-pad*2)/8,dy=(h-pad*2)/9;
 ctx.strokeStyle="#55341c";ctx.lineWidth=isDecor?1.8:1.5;
 for(let r=0;r<10;r++){
  ctx.beginPath();ctx.moveTo(pad,pad+r*dy);ctx.lineTo(w-pad,pad+r*dy);ctx.stroke();
 }
 for(let c=0;c<9;c++){
  const x=pad+c*dx;ctx.beginPath();
  if(c===0||c===8){ctx.moveTo(x,pad);ctx.lineTo(x,h-pad)}
  else{
   ctx.moveTo(x,pad);ctx.lineTo(x,pad+4*dy);
   ctx.moveTo(x,pad+5*dy);ctx.lineTo(x,h-pad);
  }
  ctx.stroke();
 }
 ctx.beginPath();
 ctx.moveTo(pad+3*dx,pad);ctx.lineTo(pad+5*dx,pad+2*dy);
 ctx.moveTo(pad+5*dx,pad);ctx.lineTo(pad+3*dx,pad+2*dy);
 ctx.moveTo(pad+3*dx,pad+7*dy);ctx.lineTo(pad+5*dx,pad+9*dy);
 ctx.moveTo(pad+5*dx,pad+7*dy);ctx.lineTo(pad+3*dx,pad+9*dy);
 ctx.stroke();
 ctx.fillStyle="#d9b87c";ctx.fillRect(w/2-45,pad+4.5*dy-13,90,26);
 ctx.fillStyle="#624322";ctx.font=`bold ${isDecor?15:13}px Georgia`;
 ctx.textAlign="center";ctx.textBaseline="middle";
 ctx.fillText(lang==="vi"?"楚 河   漢 界":"RIVER",w/2,pad+4.5*dy);
 if(isDecor){
  const pieces=[
   [0,0,"車","B"],[0,4,"將","B"],[0,8,"車","B"],
   [2,1,"砲","B"],[2,7,"砲","B"],
   [3,0,"卒","B"],[3,2,"卒","B"],[3,4,"卒","B"],[3,6,"卒","B"],[3,8,"卒","B"],
   [9,0,"俥","R"],[9,4,"帥","R"],[9,8,"俥","R"],
   [7,1,"炮","R"],[7,7,"炮","R"],
   [6,0,"兵","R"],[6,2,"兵","R"],[6,4,"兵","R"],[6,6,"兵","R"],[6,8,"兵","R"]
  ];
  pieces.forEach(([r,c,t,s])=>drawPiece(ctx,pad+c*dx,pad+r*dy,Math.min(dx,dy)*.38,t,s));
 }
}
function drawBoard(now){
 const canvas=$("board");if(!canvas)return;
 const ctx=canvas.getContext("2d");
 drawBoardCanvas(canvas,false);
 const pad=30,dx=60,dy=60;

 if(lastMove){
  ctx.fillStyle="rgba(55,140,65,.35)";
  [[lastMove.r,lastMove.c],[lastMove.nr,lastMove.nc]].forEach(([r,c])=>ctx.fillRect(pad+c*dx-13,pad+r*dy-13,26,26));
 }
 if(hint){
  ctx.strokeStyle="#e5a829";ctx.lineWidth=4;
  [[hint.r,hint.c],[hint.nr,hint.nc]].forEach(([r,c])=>{
   ctx.beginPath();ctx.arc(pad+c*dx,pad+r*dy,20,0,Math.PI*2);ctx.stroke();
  });
 }
 legal.forEach(([r,c])=>{
  ctx.beginPath();ctx.arc(pad+c*dx,pad+r*dy,7,0,Math.PI*2);
  ctx.fillStyle=board[r][c]?"rgba(180,35,30,.75)":"rgba(45,110,52,.7)";
  ctx.fill();
 });

 const anim=pieceAnimation;
 let animX=0,animY=0;
 if(anim){
  const elapsed=Math.min((now===undefined?performance.now():now)-anim.start,ANIMATION_DURATION);
  const progress=Math.max(0,elapsed/ANIMATION_DURATION);
  const eased=progress<.5?2*progress*progress:1-Math.pow(-2*progress+2,2)/2;
  animX=pad+(anim.c+(anim.nc-anim.c)*eased)*dx;
  animY=pad+(anim.r+(anim.nr-anim.r)*eased)*dy;
 }
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  const p=board[r][c];if(!p)continue;
  if(anim&&r===anim.nr&&c===anim.nc)continue;
  const x=pad+c*dx,y=pad+r*dy;
  if(selected&&selected[0]===r&&selected[1]===c){
   ctx.beginPath();ctx.arc(x,y,25,0,Math.PI*2);ctx.fillStyle="#e9bd56";ctx.fill();
  }
  drawPiece(ctx,x,y,22,side(p)==="R"?redPieces[p]:blackPieces[p],side(p));
 }
 if(anim){
  const p=anim.piece,s=side(p);
  drawPiece(ctx,animX,animY,22,s==="R"?redPieces[p]:blackPieces[p],s);
 }
}
$("board").addEventListener("click",clickBoard);

function init(){
 drawBoardCanvas($("decorBoard"),true);
 newGame();
}
init();
</script>
</body>
</html>
"""

components.html(HTML, height=1500, scrolling=True)

