
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cờ Tướng",
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
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
iframe {
    width: 100% !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

HTML = r'''
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box}
:root{
 --gold:#e4bd72;--gold2:#ffe7ae;--wood:#351c12;
 --panel:#21110c;--text:#f5e6c8;--muted:#cbb48e;
}
body{
 margin:0;color:var(--text);
 font-family:Georgia,"Times New Roman",serif;
 background:radial-gradient(ellipse at top,#68432b 0%,#28150e 55%,#100806 100%);
 min-height:100vh;
}
button{font:inherit;cursor:pointer}
button:focus-visible{outline:2px solid var(--gold2);outline-offset:3px}
#app{max-width:1100px;margin:auto;padding:14px}
.topbar{
 display:flex;justify-content:space-between;align-items:center;
 gap:10px;margin-bottom:12px;flex-wrap:wrap
}
.brand{font-size:13px;letter-spacing:3px;color:var(--gold)}
.small-btn,.btn,.tool{
 color:var(--text);border:1px solid #987044;
 background:linear-gradient(145deg,#563421,#29160e);
 border-radius:10px;padding:10px 15px;
 box-shadow:0 4px 12px #0004;transition:.18s;
}
.small-btn:hover,.btn:hover,.tool:hover{
 background:linear-gradient(145deg,#81562f,#482719);
 border-color:var(--gold2);transform:translateY(-1px)
}
.hero{
 position:relative;overflow:hidden;text-align:center;
 min-height:calc(100vh - 70px);display:flex;
 align-items:center;justify-content:center;padding:28px 16px;
 border:2px solid var(--gold);border-radius:20px;
 background:
 radial-gradient(ellipse at 50% 30%,#79502e 0%,#482719 48%,#1b0b08 100%);
 box-shadow:0 15px 45px #0008,inset 0 0 35px #0005;
}
.hero:before{
 content:"";position:absolute;inset:12px;border:1px solid #e5c47b70;
 border-radius:12px;pointer-events:none
}
.hero-inner{position:relative;z-index:1;width:min(100%,460px)}
.eyebrow{color:var(--gold);font-size:12px;letter-spacing:5px}
h1{font-size:clamp(35px,7vw,66px);letter-spacing:5px;
 color:#ffe6a4;text-shadow:0 4px 15px #000b;margin:18px 0 8px}
.subtitle{color:#dfc69c;letter-spacing:2px;font-size:13px;margin-bottom:28px}
.menu{display:grid;gap:12px;max-width:330px;margin:0 auto}
.btn{font-size:15px;padding:14px 18px}
.btn.gold{
 background:linear-gradient(135deg,#f0d18a,#b8893e);
 border-color:#ffe8b0;color:#2a160d;font-weight:bold
}
.btn.gold:hover{background:linear-gradient(135deg,#ffe9b1,#d3a34f)}
.btn.secondary{background:#29150f}
.footer-note{color:#c7ac81;font-size:11px;letter-spacing:1px;margin-top:28px}
#game{display:none}
.layout{
 padding:12px;border:1px solid #b58b4b;border-radius:15px;
 background:linear-gradient(145deg,#42271a,#1d100b);
 box-shadow:0 10px 30px #0007
}
.game-head{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;margin-bottom:10px}
.game-title{font-size:17px;color:var(--gold2);letter-spacing:2px}
.status{font-size:13px;color:var(--muted)}
.players{display:flex;gap:8px;margin-bottom:10px}
.player{
 flex:1;text-align:center;padding:9px 6px;border:1px solid #785333;
 border-radius:9px;background:#24130d;color:#d9c19a;font-size:12px
}
.player.active{border-color:#e7c77b;background:#51321e;color:#ffe9b2}
.player strong{display:block;font-size:14px;margin-bottom:3px}
.board-area{display:flex;justify-content:center}
#board{
 display:block;width:min(100%,610px);height:auto;
 border:2px solid #d0a45c;border-radius:5px;
 box-shadow:0 8px 24px #0008;background:#d8b77b;
 touch-action:manipulation
}
.tools-title{color:var(--gold);font-size:12px;letter-spacing:2px;margin:14px 0 8px}
.tools{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.tool{padding:11px 5px;font-size:12px}
.tool:disabled{opacity:.45;cursor:not-allowed;transform:none}
.hintline{font-size:12px;color:#d9c19a;min-height:18px;margin-top:10px}
#modal{
 display:none;position:fixed;inset:0;z-index:10;
 background:#080403d9;backdrop-filter:blur(7px);
 align-items:center;justify-content:center;padding:16px
}
.dialog{
 width:min(100%,420px);max-height:90vh;overflow:auto;
 border:1px solid #d0aa60;border-radius:16px;
 background:linear-gradient(145deg,#4a2a1b,#1b0d08);
 padding:23px;box-shadow:0 18px 55px #000b
}
.dialog h2{color:#ffe2a0;text-align:center;margin:0 0 18px;font-size:23px}
.dialog-buttons{display:grid;gap:10px}
.dialog .btn{width:100%}
.close-row{display:flex;justify-content:flex-end;margin-top:14px}
.setting-row{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 0;border-bottom:1px solid #755034}
.setting-row label{font-size:14px}
input[type=range]{width:130px;accent-color:#e4bd72}
input[type=checkbox]{accent-color:#d4a65b;width:18px;height:18px}
#result{
 display:none;position:fixed;inset:0;z-index:8;
 background:#120805eF;align-items:center;justify-content:center;
 text-align:center;padding:20px
}
.result-card{width:min(100%,480px);border:2px solid var(--gold);
 border-radius:18px;padding:35px 20px;background:linear-gradient(145deg,#57331e,#1b0b07);
 box-shadow:0 0 45px #000b}
#result h2{font-size:clamp(35px,8vw,60px);color:#ffe2a0;margin:0 0 12px}
#result p{color:#e1c69a;margin-bottom:22px}
@media(max-width:600px){
 #app{padding:7px}
 .hero{min-height:calc(100vh - 20px);padding:20px 12px}
 .layout{padding:7px}
 .game-title{font-size:14px}
 .small-btn{padding:8px 10px}
 .tools{gap:5px}
 .tool{font-size:11px;padding:10px 2px}
 .player{font-size:11px;padding:7px 3px}
 .player strong{font-size:12px}
}
</style>
</head>
<body>
<div id="app">
 <section id="home" class="hero">
  <div class="hero-inner">
   <div class="eyebrow">TRÍ TUỆ • CHIẾN LƯỢC</div>
   <h1>CỜ TƯỚNG</h1>
   <div class="subtitle">KHAI CUỘC · ĐẤU TRÍ · CHIẾN THẮNG</div>
   <div class="menu">
    <button class="btn gold" data-action="difficulty">♟ ĐẤU VỚI MÁY</button>
    <button class="btn" data-action="two">⚔ ĐẤU HAI NGƯỜI</button>
    <button class="btn" data-action="rules">📜 LUẬT CHƠI</button>
    <button class="btn secondary" data-action="settings">⚙ CÀI ĐẶT</button>
   </div>
   <div class="footer-note">TĨNH TÂM • QUAN SÁT • RA QUYẾT ĐỊNH</div>
  </div>
 </section>

 <section id="game">
  <div class="topbar">
   <div class="brand">♟ CỜ TƯỚNG</div>
   <button class="small-btn" data-action="settings">⚙ Cài đặt</button>
  </div>
  <div class="layout">
   <div class="game-head">
    <div>
     <div class="game-title" id="modeTitle">ĐẤU VỚI MÁY</div>
     <div class="status" id="status">Lượt quân Đen</div>
    </div>
    <div class="status" id="clock">00:00</div>
   </div>
   <div class="players">
    <div class="player" id="redPlayer"><strong>🔴 QUÂN ĐỎ</strong><span id="redDesc">Máy</span></div>
    <div class="player active" id="blackPlayer"><strong>⚫ QUÂN ĐEN</strong><span id="blackDesc">Bạn · đi trước</span></div>
   </div>
   <div class="board-area"><canvas id="board" width="720" height="800" aria-label="Bàn cờ tướng"></canvas></div>
   <div class="tools-title">CÔNG CỤ TRẬN ĐẤU</div>
   <div class="tools">
    <button class="tool" data-action="hint">✦ Gợi ý</button>
    <button class="tool" data-action="undo">↶ Đi lại</button>
    <button class="tool" data-action="new">⟳ Ván mới</button>
    <button class="tool" data-action="surrender">⚑ Đầu hàng</button>
   </div>
   <div class="hintline" id="hintline">Chọn quân Đen, sau đó chọn vị trí muốn đi.</div>
  </div>
 </section>
</div>

<div id="modal">
 <div class="dialog">
  <h2 id="modalTitle">CHỌN CHẾ ĐỘ</h2>
  <div id="modalContent"></div>
  <div class="close-row"><button class="small-btn" data-action="close">Đóng ✕</button></div>
 </div>
</div>

<div id="result">
 <div class="result-card">
  <h2 id="resultTitle">CHIẾN THẮNG</h2>
  <p id="resultText">Ván đấu đã kết thúc.</p>
  <div class="dialog-buttons">
   <button class="btn gold" data-action="new">Chơi lại</button>
   <button class="btn" data-action="home">Về màn hình chính</button>
  </div>
 </div>
</div>

<script>
"use strict";
const $=id=>document.getElementById(id);
const canvas=$("board"),ctx=canvas.getContext("2d");
const W=720,H=800,X0=40,Y0=40,DX=80,DY=80;
let board=[],turn="B",mode="bot",difficulty="medium";
let selected=null,legal=[],history=[],ended=false,startedAt=Date.now();
let soundOn=true,musicOn=false,volume=.35,audioCtx=null,musicTimer=null;
let lastMove=null,hintMove=null,elapsed=0;
const glyph={
 BR:"俥",BH:"傌",BE:"相",BA:"仕",BK:"帥",BC:"炮",BP:"兵",
 RR:"車",RH:"馬",RE:"象",RA:"士",RK:"將",RC:"砲",RP:"卒"
};
const difficultyNames={easy:"Dễ",medium:"Trung bình",hard:"Khó",expert:"Siêu khó"};

function initialBoard(){
 const b=Array.from({length:10},()=>Array(9).fill(null));
 const back=["R","H","E","A","K","A","E","H","R"];
 for(let c=0;c<9;c++){
  b[0][c]={s:"R",t:back[c]};
  b[9][c]={s:"B",t:back[c]};
 }
 b[2][1]={s:"R",t:"C"};b[2][7]={s:"R",t:"C"};
 b[7][1]={s:"B",t:"C"};b[7][7]={s:"B",t:"C"};
 for(const c of [0,2,4,6,8]){
  b[3][c]={s:"R",t:"P"};
  b[6][c]={s:"B",t:"P"};
 }
 return b;
}
function cloneBoard(b){return b.map(row=>row.map(p=>p?{...p}:null))}
function inside(r,c){return r>=0&&r<10&&c>=0&&c<9}
function palace(s,r,c){
 return c>=3&&c<=5&&(s==="R"?r>=0&&r<=2:r>=7&&r<=9);
}
function clearPath(r,c,nr,nc){
 const dr=Math.sign(nr-r),dc=Math.sign(nc-c);let count=0;
 let y=r+dr,x=c+dc;
 while(y!==nr||x!==nc){if(board[y][x])count++;y+=dr;x+=dc}
 return count;
}
function pseudoMoves(r,c,b=board){
 const p=b[r][c];if(!p)return [];
 const out=[],s=p.s,enemy=s==="B"?"R":"B";
 function add(nr,nc){
  if(!inside(nr,nc))return;
  if(b[nr][nc]&&b[nr][nc].s===s)return;
  out.push([nr,nc]);
 }
 if(p.t==="R"||p.t==="C"){
  for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let nr=r+dr,nc=c+dc,seen=false;
   while(inside(nr,nc)){
    if(p.t==="R"){
     if(!b[nr][nc])add(nr,nc);
     else{if(b[nr][nc].s===enemy)add(nr,nc);break}
    }else{
     if(!seen){if(!b[nr][nc])add(nr,nc);else seen=true}
     else if(b[nr][nc]){if(b[nr][nc].s===enemy)add(nr,nc);break}
    }
    nr+=dr;nc+=dc;
   }
  }
 }
 if(p.t==="H"){
  const hs=[
   [-2,-1,-1,0],[-2,1,-1,0],[2,-1,1,0],[2,1,1,0],
   [-1,-2,0,-1],[1,-2,0,-1],[-1,2,0,1],[1,2,0,1]
  ];
  for(const [dr,dc,lr,lc] of hs){
   const nr=r+dr,nc=c+dc;
   if(inside(nr,nc)&&inside(r+lr,c+lc)&&!b[r+lr][c+lc])add(nr,nc);
  }
 }
 if(p.t==="E"||p.t==="A"){
  const steps=p.t==="E"?[[2,2],[2,-2],[-2,2],[-2,-2]]:[[1,1],[1,-1],[-1,1],[-1,-1]];
  for(const [dr,dc] of steps){
   const nr=r+dr,nc=c+dc;
   if(!inside(nr,nc))continue;
   if(p.t==="E"&&((s==="B"&&nr<5)||(s==="R"&&nr>4)))continue;
   if(p.t==="A"&&!palace(s,nr,nc))continue;
   if(p.t==="E"&&b[r+dr/2][c+dc/2])continue;
   add(nr,nc);
  }
 }
 if(p.t==="K"){
  for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){
   const nr=r+dr,nc=c+dc;
   if(inside(nr,nc)&&palace(s,nr,nc))add(nr,nc);
  }
  for(const dr of [-1,1]){
   let nr=r+dr;
   while(inside(nr,c)){
    if(b[nr][c]){
     if(b[nr][c].t==="K"&&b[nr][c].s!==s)out.push([nr,c]);
     break;
    }
    nr+=dr;
   }
  }
 }
 if(p.t==="P"){
  const forward=s==="B"?-1:1;
  add(r+forward,c);
  const crossed=s==="B"?r<=4:r>=5;
  if(crossed){add(r,c-1);add(r,c+1)}
 }
 return out;
}
function movesFor(r,c,b=board){
 return pseudoMoves(r,c,b);
}
function draw(){
 ctx.clearRect(0,0,W,H);
 const grad=ctx.createLinearGradient(0,0,W,H);
 grad.addColorStop(0,"#edcf91");grad.addColorStop(1,"#c79a58");
 ctx.fillStyle=grad;ctx.fillRect(0,0,W,H);
 ctx.strokeStyle="#4b2b16";ctx.lineWidth=2.2;
 ctx.strokeRect(X0,Y0,DX*8,DY*9);
 for(let c=0;c<9;c++){
  ctx.beginPath();ctx.moveTo(X0+c*DX,Y0);ctx.lineTo(X0+c*DX,Y0+DY*9);ctx.stroke();
 }
 for(let r=0;r<10;r++){
  ctx.beginPath();ctx.moveTo(X0,Y0+r*DY);ctx.lineTo(X0+DX*8,Y0+r*DY);ctx.stroke();
 }
 ctx.clearRect(X0+1,Y0+DY*4+1,DX*8-2,DY-2);
 ctx.fillStyle="#cfa86c";ctx.fillRect(X0+1,Y0+DY*4+1,DX*8-2,DY-2);
 ctx.fillStyle="#5b321a";ctx.font="italic 30px Georgia";ctx.textAlign="center";
 ctx.fillText("楚 河",X0+DX*2,Y0+DY*4+46);
 ctx.fillText("漢 界",X0+DX*6,Y0+DY*4+46);
 ctx.strokeStyle="#4b2b16";ctx.lineWidth=2;
 for(const [x1,y1,x2,y2] of [
  [X0+3*DX,Y0,X0+5*DX,Y0+2*DY],
  [X0+5*DX,Y0,X0+3*DX,Y0+2*DY],
  [X0+3*DX,Y0+7*DY,X0+5*DX,Y0+9*DY],
  [X0+5*DX,Y0+7*DY,X0+3*DX,Y0+9*DY]
 ]){
  ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();
 }
 for(const [r,c] of legal){
  ctx.beginPath();ctx.arc(X0+c*DX,Y0+r*DY,10,0,Math.PI*2);
  ctx.fillStyle=board[r][c]?"#b43a24aa":"#3c8c47b8";ctx.fill();
 }
 if(lastMove){
  ctx.fillStyle="#f2df7d77";
  for(const [r,c] of [lastMove.from,lastMove.to]){
   ctx.fillRect(X0+c*DX-19,Y0+r*DY-19,38,38);
  }
 }
 if(hintMove){
  ctx.strokeStyle="#267b39";ctx.lineWidth=5;
  for(const [r,c] of [hintMove.from,hintMove.to]){
   ctx.beginPath();ctx.arc(X0+c*DX,Y0+r*DY,27,0,Math.PI*2);ctx.stroke();
  }
 }
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  const p=board[r][c];if(!p)continue;
  const x=X0+c*DX,y=Y0+r*DY;
  if(selected&&selected[0]===r&&selected[1]===c){
   ctx.beginPath();ctx.arc(x,y,34,0,Math.PI*2);ctx.fillStyle="#f9e6a4";ctx.fill();
  }
  ctx.beginPath();ctx.arc(x,y,29,0,Math.PI*2);
  ctx.fillStyle="#efd7a3";ctx.fill();
  ctx.strokeStyle=p.s==="B"?"#25201a":"#9d3026";ctx.lineWidth=4;ctx.stroke();
  ctx.beginPath();ctx.arc(x,y,24,0,Math.PI*2);
  ctx.strokeStyle=p.s==="B"?"#4a3727":"#c45137";ctx.lineWidth=1;ctx.stroke();
  ctx.fillStyle=p.s==="B"?"#25201a":"#a42f25";
  ctx.font="bold 34px serif";ctx.textAlign="center";ctx.textBaseline="middle";
  ctx.fillText(glyph[p.s+p.t],x,y+1);
 }
 ctx.textBaseline="alphabetic";
}
function snapshot(){
 history.push({board:cloneBoard(board),turn,mode,difficulty,lastMove});
 if(history.length>80)history.shift();
}
function playSound(freq=520,duration=.08){
 if(!soundOn)return;
 try{
  audioCtx=audioCtx||new(window.AudioContext||window.webkitAudioContext)();
  if(audioCtx.state==="suspended")audioCtx.resume();
  const o=audioCtx.createOscillator(),g=audioCtx.createGain();
  o.type="sine";o.frequency.value=freq;
  g.gain.value=volume*.12;o.connect(g);g.connect(audioCtx.destination);
  o.start();g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+duration);
  o.stop(audioCtx.currentTime+duration);
 }catch(e){}
}
function startMusic(){
 stopMusic();
 if(!musicOn)return;
 try{
  audioCtx=audioCtx||new(window.AudioContext||window.webkitAudioContext)();
  if(audioCtx.state==="suspended")audioCtx.resume();
  let notes=[196,246.94,293.66,246.94,220,293.66,329.63,293.66],i=0;
  musicTimer=setInterval(()=>{
   if(!musicOn)return;
   const o=audioCtx.createOscillator(),g=audioCtx.createGain();
   o.type="triangle";o.frequency.value=notes[i++%notes.length];
   g.gain.value=volume*.025;o.connect(g);g.connect(audioCtx.destination);
   o.start();g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+.65);
   o.stop(audioCtx.currentTime+.7);
  },700);
 }catch(e){}
}
function stopMusic(){if(musicTimer){clearInterval(musicTimer);musicTimer=null}}
function updateStatus(){
 $("status").textContent=ended?"Ván đấu đã kết thúc":("Lượt quân "+(turn==="B"?"Đen":"Đỏ"));
 $("blackPlayer").classList.toggle("active",turn==="B"&&!ended);
 $("redPlayer").classList.toggle("active",turn==="R"&&!ended);
}
function begin(which,level="medium"){
 mode=which;difficulty=level;board=initialBoard();turn="B";
 selected=null;legal=[];history=[];ended=false;lastMove=null;hintMove=null;
 startedAt=Date.now();elapsed=0;
 $("home").style.display="none";$("game").style.display="block";
 $("result").style.display="none";
 $("modeTitle").textContent=which==="two"?"ĐẤU HAI NGƯỜI":"ĐẤU VỚI MÁY · "+difficultyNames[level].toUpperCase();
 $("redDesc").textContent=which==="two"?"Người chơi 2":"Máy · "+difficultyNames[level];
 $("blackDesc").textContent=which==="two"?"Người chơi 1 · đi trước":"Bạn · đi trước";
 $("hintline").textContent="Chọn quân Đen, sau đó chọn vị trí muốn đi.";
 closeModal();updateStatus();draw();playSound(420);startMusic();
}
function closeModal(){$("modal").style.display="none"}
function showModal(kind){
 const content=$("modalContent");content.innerHTML="";
 $("modal").style.display="flex";
 if(kind==="difficulty"){
  $("modalTitle").textContent="CHỌN ĐỘ KHÓ";
  const list=[
   ["easy","DỄ","Dành cho người mới"],
   ["medium","TRUNG BÌNH","Thử thách vừa phải"],
   ["hard","KHÓ","Bot ưu tiên nước ăn quân"],
   ["expert","SIÊU KHÓ","Bot chọn nước có điểm cao hơn"]
  ];
  list.forEach(([v,label,desc])=>{
   const b=document.createElement("button");b.className="btn";b.innerHTML=label+"<br><small>"+desc+"</small>";
   b.onclick=()=>begin("bot",v);content.appendChild(b);
  });
 }else if(kind==="settings"){
  $("modalTitle").textContent="CÀI ĐẶT";
  content.innerHTML=`
   <div class="setting-row"><label for="music">Nhạc nền</label><input id="music" type="checkbox" ${musicOn?"checked":""}></div>
   <div class="setting-row"><label for="sound">Âm thanh</label><input id="sound" type="checkbox" ${soundOn?"checked":""}></div>
   <div class="setting-row"><label for="vol">Âm lượng</label><input id="vol" type="range" min="0" max="100" value="${Math.round(volume*100)}"></div>
   <div class="setting-row"><label>Tiếp tục chơi</label><button class="small-btn" id="resume">Tiếp tục</button></div>
   <div class="setting-row"><label>Về màn hình chính</label><button class="small-btn" id="gohome">Về trang chủ</button></div>`;
  $("music").onchange=e=>{musicOn=e.target.checked;if(musicOn)startMusic();else stopMusic()};
  $("sound").onchange=e=>soundOn=e.target.checked;
  $("vol").oninput=e=>volume=Number(e.target.value)/100;
  $("resume").onclick=closeModal;
  $("gohome").onclick=()=>{closeModal();$("game").style.display="none";$("home").style.display="flex";$("result").style.display="none";stopMusic()};
 }else if(kind==="rules"){
  $("modalTitle").textContent="LUẬT CHƠI CƠ BẢN";
  content.innerHTML=`
   <p>• Đỏ đi trước theo luật truyền thống; trong phiên bản này, bạn cầm quân Đen và được đi trước.</p>
   <p>• Chọn quân của mình rồi chọn điểm đến được đánh dấu.</p>
   <p>• Xe đi thẳng; Mã đi chữ L; Tượng đi chéo hai điểm; Sĩ đi chéo một điểm.</p>
   <p>• Pháo đi như Xe khi không ăn quân; khi ăn phải có đúng một quân chắn.</p>
   <p>• Tốt đi thẳng về phía trước, qua sông mới được đi ngang.</p>
   <p>• Bản hiện tại là phiên bản chơi thử: chưa kiểm tra đầy đủ chiếu tướng, tự chiếu và mọi luật kết thúc ván.</p>`;
 }
}
function finish(title,text){
 ended=true;selected=null;legal=[];hintMove=null;draw();updateStatus();
 $("resultTitle").textContent=title;$("resultText").textContent=text;
 $("result").style.display="flex";playSound(260,.3);
}
function move(from,to){
 snapshot();
 const p=board[from[0]][from[1]],captured=board[to[0]][to[1]];
 board[to[0]][to[1]]=p;board[from[0]][from[1]]=null;
 lastMove={from,to};selected=null;legal=[];hintMove=null;
 playSound(captured?260:520);
 if(captured&&captured.t==="K"){
  draw();finish(p.s==="B"?"CHIẾN THẮNG":"THẤT BẠI",p.s==="B"?"Bạn đã ăn được Tướng đối phương!":"Tướng của bạn đã bị ăn.");
  return;
 }
 turn=turn==="B"?"R":"B";updateStatus();draw();
 $("hintline").textContent="Đã đi xong. Đến lượt quân "+(turn==="B"?"Đen":"Đỏ")+".";
 if(mode==="bot"&&turn==="R"&&!ended)setTimeout(botMove,350);
}
function onBoardClick(e){
 if(ended)return;
 if(mode==="bot"&&turn==="R")return;
 const rect=canvas.getBoundingClientRect();
 const x=(e.clientX-rect.left)*canvas.width/rect.width;
 const y=(e.clientY-rect.top)*canvas.height/rect.height;
 const c=Math.round((x-X0)/DX),r=Math.round((y-Y0)/DY);
 if(!inside(r,c)||Math.abs(x-(X0+c*DX))>DX*.48||Math.abs(y-(Y0+r*DY))>DY*.48)return;
 const p=board[r][c];
 if(selected&&legal.some(([rr,cc])=>rr===r&&cc===c)){
  move(selected,[r,c]);return;
 }
 if(p&&p.s===turn){
  selected=[r,c];legal=movesFor(r,c);hintMove=null;draw();playSound(620,.05);
 }else{
  selected=null;legal=[];draw();
 }
}
function allMoves(s){
 const out=[];
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  if(board[r][c]?.s!==s)continue;
  for(const [nr,nc] of movesFor(r,c))out.push({from:[r,c],to:[nr,nc],piece:board[r][c],capture:board[nr][nc]});
 }
 return out;
}
function pieceValue(p){
 if(!p)return 0;
 return ({K:10000,R:900,C:450,H:400,E:200,A:200,P:100})[p.t]||0;
}
function botMove(){
 if(ended||mode!=="bot"||turn!=="R")return;
 let candidates=allMoves("R");
 if(!candidates.length){finish("CHIẾN THẮNG","Bot không còn nước đi theo bộ luật đơn giản này.");return}
 candidates=candidates.map(m=>{
  let score=Math.random()*20;
  if(m.capture)score+=pieceValue(m.capture)*({easy:.25,medium:.6,hard:1,expert:1.25}[difficulty]);
  if(m.piece.t==="P")score+=Math.random()*10;
  if(difficulty==="easy")score+=Math.random()*160;
  if(difficulty==="expert")score+=Math.random()*8;
  return {...m,score};
 }).sort((a,b)=>b.score-a.score);
 let pool=difficulty==="easy"?candidates.slice(0,Math.min(8,candidates.length)):
          difficulty==="medium"?candidates.slice(0,Math.min(4,candidates.length)):
          difficulty==="hard"?candidates.slice(0,Math.min(2,candidates.length)):candidates.slice(0,1);
 const m=pool[Math.floor(Math.random()*pool.length)];
 move(m.from,m.to);
}
function undo(){
 if(!history.length||ended)return;
 if(mode==="bot"&&history.length>=2){
  let snap=history[history.length-2];history=history.slice(0,-2);
  board=cloneBoard(snap.board);turn=snap.turn;lastMove=snap.lastMove;
 }else{
  const snap=history.pop();board=cloneBoard(snap.board);turn=snap.turn;lastMove=snap.lastMove;
 }
 selected=null;legal=[];hintMove=null;updateStatus();draw();
 $("hintline").textContent="Đã quay lại nước đi trước.";
}
function hint(){
 if(ended)return;
 const side=turn;
 let moves=allMoves(side);
 if(!moves.length){$("hintline").textContent="Chưa tìm được nước gợi ý.";return}
 moves.sort((a,b)=>pieceValue(b.capture)-pieceValue(a.capture));
 const m=moves[0];
 hintMove={from:m.from,to:m.to};draw();
 $("hintline").textContent="Gợi ý: thử đi quân ở hàng "+(m.from[0]+1)+", cột "+(m.from[1]+1)+".";
}
function newGame(){
 $("result").style.display="none";
 if(mode==="bot")begin("bot",difficulty);else begin("two");
}
function surrender(){
 if(ended)return;
 if(!confirm("Bạn muốn đầu hàng ván này?"))return;
 finish(mode==="bot"?"THẤT BẠI":"KẾT THÚC VÁN",mode==="bot"?"Bạn đã đầu hàng.":"Ván đấu đã được kết thúc.");
}
document.addEventListener("click",e=>{
 const b=e.target.closest("button");if(!b)return;
 const a=b.dataset.action;if(!a)return;
 if(a==="difficulty")showModal("difficulty");
 else if(a==="two")begin("two");
 else if(a==="settings")showModal("settings");
 else if(a==="rules")showModal("rules");
 else if(a==="close")closeModal();
 else if(a==="home"){closeModal();$("result").style.display="none";$("game").style.display="none";$("home").style.display="flex";stopMusic()}
 else if(a==="new")newGame();
 else if(a==="undo")undo();
 else if(a==="hint")hint();
 else if(a==="surrender")surrender();
});
canvas.addEventListener("click",onBoardClick);
$("modal").addEventListener("click",e=>{if(e.target===$("modal"))closeModal()});
setInterval(()=>{
 if($("game").style.display!=="none"&&!ended){
  elapsed=Math.floor((Date.now()-startedAt)/1000);
  $("clock").textContent=String(Math.floor(elapsed/60)).padStart(2,"0")+":"+String(elapsed%60).padStart(2,"0");
 }
},1000);
draw();
</script>
</body>
</html>
'''

components.html(HTML, height=1050, scrolling=False)
