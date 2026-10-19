
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
#MainMenu,header,footer,[data-testid="stToolbar"],
[data-testid="stDecoration"]{display:none!important}
.block-container{padding:0!important;max-width:100%!important}
iframe{display:block;width:100%!important;border:0!important}
</style>
""", unsafe_allow_html=True)

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
:root{--gold:#e8bd68;--cream:#fff0cf;--dark:#1a0c09}
*{box-sizing:border-box}
html,body{margin:0;width:100%;height:100%;overflow:hidden;
font-family:Arial,"DejaVu Sans",sans-serif;color:var(--cream);
background:radial-gradient(ellipse at top,#492619,#160907 75%)}
button,select,input{font:inherit}
button{cursor:pointer}
#app{height:100dvh;width:100%;padding:7px;display:flex;
justify-content:center;align-items:center;overflow:hidden}
.screen{display:none;width:min(100%,1000px);height:100%;
min-height:0}
.screen.active{display:flex}
#home{align-items:center;justify-content:center}
.hero{position:relative;isolation:isolate;overflow:hidden;
width:min(100%,950px);height:100%;max-height:750px;min-height:0;
display:flex;align-items:center;justify-content:center;
border:2px solid var(--gold);border-radius:15px;
background:linear-gradient(135deg,#633c21,#321810 48%,#170907);
box-shadow:0 0 35px #0009}
.hero:before{content:"";position:absolute;inset:5%;z-index:-1;
border:1px solid #dcb76b70;border-radius:9px}
.hero-board{position:absolute;width:min(66%,490px);aspect-ratio:9/10;
border:2px solid #dcb76b;background:
linear-gradient(#dcb76b 1px,transparent 1px),
linear-gradient(90deg,#dcb76b 1px,transparent 1px);
background-size:12.5% 11.11%;opacity:.16;transform:rotate(-5deg)}
.hero-content{width:min(90%,370px);text-align:center}
.brand{font-size:clamp(34px,6vw,61px);letter-spacing:5px;
color:#ffe3a0;text-shadow:0 3px 0 #572314;margin:0 0 10px}
.brand-sub{font-size:12px;letter-spacing:4px;color:#e6c58c;margin-bottom:25px}
.menu-buttons{display:grid;gap:10px}
.btn{padding:11px 14px;border-radius:8px;border:1px solid var(--gold);
color:#fff0d0;background:linear-gradient(135deg,#694022,#321a12);
font-weight:bold;box-shadow:0 3px 7px #0005}
.btn:hover,.tool:hover{filter:brightness(1.2)}
.btn.gold{background:linear-gradient(135deg,#f7df9c,#bd873d);color:#28150a}
.btn.dark{background:#21110e}
#game{align-items:center;justify-content:center}
.game-layout{width:min(100%,760px);height:100%;display:flex;
flex-direction:column;justify-content:center;gap:5px;min-height:0}
.gamebar{display:flex;align-items:center;justify-content:space-between;gap:8px}
.game-title{color:#ffe3a0;letter-spacing:2px;font-weight:bold;font-size:clamp(15px,2.5vw,22px)}
.icon-btn{padding:7px 10px;border:1px solid var(--gold);border-radius:7px;
background:#382018;color:#ffe3a0}
.playerbar{display:flex;justify-content:space-between;align-items:center;
gap:8px;background:#2c1712;border:1px solid #795634;border-radius:6px;
padding:5px 9px;font-size:12px}
.playerbar strong{color:#ffe3a0}
#board-wrap{position:relative;width:min(100%,calc((100dvh - 210px)*.80));
max-height:calc(100dvh - 210px);aspect-ratio:680/760;margin:0 auto;flex:0 1 auto}
#board{display:block;width:100%;height:100%;border-radius:7px;touch-action:manipulation}
.tools-title{text-align:center;color:var(--gold);font-size:11px;letter-spacing:2px}
.tools{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px}
.tool{min-width:0;padding:8px 2px;border:1px solid #90683e;border-radius:7px;
background:#352018;color:#ffedcc;font-size:12px}
.status{text-align:center;min-height:16px;color:#e5c68c;font-size:12px}
.modal{position:fixed;inset:0;z-index:1000;display:flex;align-items:center;
justify-content:center;padding:12px;background:#080403df;backdrop-filter:blur(4px)}
.hidden{display:none!important}
.dialog{width:min(100%,400px);max-height:88dvh;overflow:auto;padding:20px;
border:2px solid var(--gold);border-radius:13px;
background:linear-gradient(145deg,#48271b,#1b0c09);box-shadow:0 0 35px #000b}
.dialog h2{text-align:center;color:#ffe3a0;font-size:22px;margin:0 0 17px}
.dialog .btn{width:100%;display:block;margin:8px 0}
.setting-row{display:flex;justify-content:space-between;align-items:center;
gap:10px;margin:15px 0;font-size:14px}
.setting-row input[type=range]{width:45%;accent-color:var(--gold)}
.setting-row input[type=checkbox]{width:18px;height:18px;accent-color:var(--gold)}
.setting-row select{max-width:48%;padding:6px;background:#1c100c;color:white;
border:1px solid var(--gold);border-radius:5px}
.rules{font-size:14px;line-height:1.7}
.result-overlay{position:absolute;inset:0;z-index:10;display:flex;
align-items:center;justify-content:center;text-align:center;
background:#130705ed;border:2px solid var(--gold);border-radius:7px;padding:12px}
.result-title{font-size:clamp(30px,7vw,52px);font-weight:bold;
color:#ffe3a0;text-shadow:0 0 18px #f4c66a;margin-bottom:18px}
.result-overlay .btn{margin:4px}
@media(max-height:760px){
 #app{padding:4px}.game-layout{gap:3px}
 #board-wrap{width:min(100%,calc((100dvh - 185px)*.80));
 max-height:calc(100dvh - 185px)}
 .tool{padding:6px 1px;font-size:11px}
 .playerbar{padding:3px 7px}.hero{max-height:none}
 .menu-buttons{gap:7px}.btn{padding:9px 11px}
 .brand-sub{margin-bottom:16px}
}
@media(max-width:600px){
 #app{padding:3px}.game-layout{width:100%}
 #board-wrap{width:min(100%,calc((100dvh - 205px)*.80));
 max-height:calc(100dvh - 205px)}
 .game-title{letter-spacing:1px}.icon-btn{padding:6px}
 .tools{gap:4px}.tool{font-size:10px}
}
</style>
</head>
<body>
<div id="app">
<section id="home" class="screen active">
 <div class="hero">
  <div class="hero-board"></div>
  <div class="hero-content">
   <h1 class="brand">CỜ TƯỚNG</h1>
   <div class="brand-sub">TRÍ TUỆ • CHIẾN LƯỢC</div>
   <div class="menu-buttons">
    <button class="btn gold" onclick="showModal('difficulty')">♟ Đấu với máy</button>
    <button class="btn" onclick="startGame('two')">⚔ Đấu hai người</button>
    <button class="btn" onclick="showModal('rules')">📜 Luật chơi</button>
    <button class="btn dark" onclick="showModal('settings')">⚙ Cài đặt</button>
   </div>
  </div>
 </div>
</section>

<section id="game" class="screen">
 <div class="game-layout">
  <div class="gamebar">
   <button class="icon-btn" onclick="showModal('settings')">⚙</button>
   <div class="game-title">CỜ TƯỚNG</div>
   <button class="icon-btn" onclick="goHome()">⌂ Menu</button>
  </div>
  <div class="playerbar">
   <span id="red-label">🔴 ĐỎ: Bot</span>
   <span id="clock">00:00</span>
   <span id="black-label">⚫ ĐEN: Bạn</span>
  </div>
  <div id="board-wrap">
   <canvas id="board" width="680" height="760"></canvas>
   <div id="result" class="result-overlay hidden">
    <div>
     <div id="result-title" class="result-title">CHIẾN THẮNG</div>
     <button class="btn gold" onclick="newGame()">Ván mới</button>
     <button class="btn" onclick="goHome()">Về menu</button>
    </div>
   </div>
  </div>
  <div class="tools-title">CÔNG CỤ TRẬN ĐẤU</div>
  <div class="tools">
   <button class="tool" onclick="hint()">💡 Gợi ý</button>
   <button class="tool" onclick="undoMove()">↶ Đi lại</button>
   <button class="tool" onclick="newGame()">⟳ Ván mới</button>
   <button class="tool" onclick="surrender()">🏳 Đầu hàng</button>
  </div>
  <div id="status" class="status">ĐEN đi trước</div>
 </div>
</section>
</div>

<div id="difficulty" class="modal hidden">
 <div class="dialog">
  <h2>CHỌN ĐỘ KHÓ</h2>
  <button class="btn" onclick="startGame('easy')">🌱 Dễ</button>
  <button class="btn" onclick="startGame('medium')">🗡 Trung bình</button>
  <button class="btn" onclick="startGame('hard')">🔥 Khó</button>
  <button class="btn gold" onclick="startGame('expert')">👑 Siêu khó</button>
  <button class="btn dark" onclick="hideModals()">Quay lại</button>
 </div>
</div>

<div id="settings" class="modal hidden">
 <div class="dialog">
  <h2>CÀI ĐẶT</h2>
  <div class="setting-row"><label for="music">Nhạc nền</label><input id="music" type="checkbox" checked onchange="toggleMusic()"></div>
  <div class="setting-row"><label for="effects">Âm thanh</label><input id="effects" type="checkbox" checked></div>
  <div class="setting-row"><label for="volume">Âm lượng</label><input id="volume" type="range" min="0" max="100" value="30" oninput="setVolume(this.value)"></div>
  <div class="setting-row"><label for="language">Ngôn ngữ</label>
   <select id="language" onchange="setLanguage(this.value)">
    <option value="vi">Tiếng Việt</option><option value="en">English</option>
   </select>
  </div>
  <button class="btn gold" onclick="hideModals()">Lưu và đóng</button>
 </div>
</div>

<div id="rules" class="modal hidden">
 <div class="dialog">
  <h2>LUẬT CHƠI CỜ TƯỚNG</h2>
  <div class="rules">
   • ĐEN đi trước, ĐỎ đi sau.<br>
   • Tướng đi từng ô trong cung.<br>
   • Xe đi ngang hoặc dọc, không nhảy qua quân.<br>
   • Pháo đi như Xe khi không ăn; khi ăn phải nhảy qua đúng một quân.<br>
   • Mã đi theo hình chữ L nhưng bị cản nếu ô sát cạnh bị chiếm.<br>
   • Tượng đi chéo hai ô, không qua sông và bị cản ở giữa.<br>
   • Sĩ đi chéo một ô trong cung; Tốt đi thẳng, qua sông có thể đi ngang.
  </div>
  <button class="btn gold" onclick="hideModals()">Đã hiểu</button>
 </div>
</div>

<script>
"use strict";
const canvas=document.getElementById("board");
const ctx=canvas.getContext("2d");
const W=680,H=760,L=50,T=40,DX=72.5,DY=75;
let board=[],turn="b",mode="easy",gameType="bot",selected=null;
let legal=[],history=[],finished=false,startedAt=Date.now();
let audioCtx=null,oscillators=[],masterGain=null,musicTimer=null;
let volume=.30,moveCount=0,lastMove=null,hintMove=null;

const names={K:"將",A:"士",E:"象",H:"馬",R:"車",C:"炮",P:"卒"};
const redNames={K:"帥",A:"仕",E:"相",H:"傌",R:"俥",C:"炮",P:"兵"};
const values={K:10000,A:20,E:20,H:45,R:90,C:50,P:10};
const $=id=>document.getElementById(id);
function side(p){return p?p[0]:null}
function type(p){return p?p[1]:null}
function inside(y,x){return y>=0&&y<10&&x>=0&&x<9}
function clone(b){return b.map(r=>r.slice())}
function showModal(id){hideModals();$(id).classList.remove("hidden");if(id==="settings")startAudio()}
function hideModals(){document.querySelectorAll(".modal").forEach(x=>x.classList.add("hidden"))}
function showScreen(id){document.querySelectorAll(".screen").forEach(x=>x.classList.remove("active"));$(id).classList.add("active")}
function setStatus(s){$("status").textContent=s}
function label(p){return side(p)==="b"?"ĐEN":"ĐỎ"}
function opponent(s){return s==="b"?"r":"b"}

function initialBoard(){
 const b=Array.from({length:10},()=>Array(9).fill(null));
 const back=["R","H","E","A","K","A","E","H","R"];
 for(let x=0;x<9;x++){b[0][x]="r"+back[x];b[9][x]="b"+back[x]}
 b[2][1]="rC";b[2][7]="rC";b[7][1]="bC";b[7][7]="bC";
 for(let x=0;x<9;x+=2){b[3][x]="rP";b[6][x]="bP"}
 return b;
}
function startGame(which){
 hideModals();startAudio();
 if(which==="two"){gameType="two";mode="two"}
 else{gameType="bot";mode=which}
 showScreen("game");newGame();
}
function goHome(){hideModals();showScreen("home")}
function newGame(){
 board=initialBoard();turn="b";selected=null;legal=[];history=[];
 finished=false;moveCount=0;lastMove=null;hintMove=null;startedAt=Date.now();
 $("result").classList.add("hidden");
 $("red-label").textContent=gameType==="bot"?"🔴 ĐỎ: Bot":"🔴 ĐỎ: Người chơi 2";
 $("black-label").textContent="⚫ ĐEN: Người chơi 1";
 setStatus(gameType==="bot"?"Bạn cầm ĐEN và đi trước":"ĐEN đi trước");
 draw();startAudio();
}
function palace(s,y,x){
 return x>=3&&x<=5&&(s==="r"?y>=0&&y<=2:y>=7&&y<=9);
}
function add(out,y,x,ny,nx,s){
 if(!inside(ny,nx))return;
 const p=board[ny][nx];
 if(!p||side(p)!==s)out.push({y,x,ny,nx});
}
function pseudoMoves(y,x){
 const p=board[y][x];if(!p)return [];
 const s=side(p),t=type(p),out=[];
 const step=s==="r"?1:-1;
 if(t==="K"){
  for(const [dy,dx] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let ny=y+dy,nx=x+dx;
   if(palace(s,ny,nx))add(out,y,x,ny,nx,s);
  }
  // Tướng có thể bắt tướng đối phương khi cùng cột và không có quân chắn.
  for(let ny=y+step;inside(ny,x);ny+=step){
   if(board[ny][x]){
    if(type(board[ny][x])==="K"&&side(board[ny][x])!==s)out.push({y,x,ny,nx:x});
    break;
   }
  }
 }else if(t==="A"){
  for(const [dy,dx] of [[1,1],[1,-1],[-1,1],[-1,-1]]){
   let ny=y+dy,nx=x+dx;if(palace(s,ny,nx))add(out,y,x,ny,nx,s);
  }
 }else if(t==="E"){
  for(const [dy,dx] of [[2,2],[2,-2],[-2,2],[-2,-2]]){
   const ny=y+dy,nx=x+dx;
   if(!inside(ny,nx))continue;
   if(s==="r"&&ny>4)continue;if(s==="b"&&ny<5)continue;
   if(!board[y+dy/2][x+dx/2])add(out,y,x,ny,nx,s);
  }
 }else if(t==="H"){
  const moves=[
   [-2,-1,-1,0],[-2,1,-1,0],[2,-1,1,0],[2,1,1,0],
   [-1,-2,0,-1],[1,-2,0,-1],[-1,2,0,1],[1,2,0,1]
  ];
  for(const [dy,dx,ly,lx] of moves){
   const ny=y+dy,nx=x+dx;
   if(inside(ny,nx)&&!board[y+ly][x+lx])add(out,y,x,ny,nx,s);
  }
 }else if(t==="R"||t==="C"){
  for(const [dy,dx] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let ny=y+dy,nx=x+dx,screen=false;
   while(inside(ny,nx)){
    const target=board[ny][nx];
    if(t==="R"){
     if(!target)add(out,y,x,ny,nx,s);
     else{if(side(target)!==s)add(out,y,x,ny,nx,s);break}
    }else{
     if(!screen){if(!target)add(out,y,x,ny,nx,s);else screen=true}
     else if(target){if(side(target)!==s)add(out,y,x,ny,nx,s);break}
    }
    ny+=dy;nx+=dx;
   }
  }
 }else if(t==="P"){
  const ny=y+step;add(out,y,x,ny,x,s);
  const crossed=s==="b"?y<=4:y>=5;
  if(crossed){add(out,y,x,y,x-1,s);add(out,y,x,y,x+1,s)}
 }
 return out;
}
function kingPos(b,s){
 for(let y=0;y<10;y++)for(let x=0;x<9;x++)
  if(b[y][x]===s+"K")return [y,x];
 return null;
}
function attacked(b,y,x,by){
 const saved=board;board=b;
 let hit=false;
 for(let yy=0;yy<10&&!hit;yy++)for(let xx=0;xx<9&&!hit;xx++)
  if(side(b[yy][xx])===by&&pseudoMoves(yy,xx).some(m=>m.ny===y&&m.nx===x))hit=true;
 board=saved;return hit;
}
function legalMoves(y,x){
 const p=board[y][x];if(!p)return [];
 return pseudoMoves(y,x).filter(m=>{
  const b=clone(board),captured=b[m.ny][m.nx];b[m.ny][m.nx]=b[y][x];b[y][x]=null;
  const k=kingPos(b,side(p));
  if(!k)return false;
  const saved=board;board=b;
  const check=attacked(b,k[0],k[1],opponent(side(p)));
  board=saved;
  return !check || (captured&&type(captured)==="K");
 });
}
function draw(){
 ctx.clearRect(0,0,W,H);
 const g=ctx.createLinearGradient(0,0,W,H);
 g.addColorStop(0,"#edce8c");g.addColorStop(1,"#c18b47");
 ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
 ctx.strokeStyle="#59341c";ctx.lineWidth=2;
 for(let y=0;y<10;y++){
  ctx.beginPath();ctx.moveTo(L,T+y*DY);ctx.lineTo(L+8*DX,T+y*DY);ctx.stroke();
 }
 for(let x=0;x<9;x++){
  ctx.beginPath();ctx.moveTo(L+x*DX,T);ctx.lineTo(L+x*DX,T+4*DY);ctx.stroke();
  ctx.beginPath();ctx.moveTo(L+x*DX,T+5*DY);ctx.lineTo(L+x*DX,T+9*DY);ctx.stroke();
 }
 for(const x of [3,5]){
  ctx.beginPath();ctx.moveTo(L+x*DX,T);ctx.lineTo(L+(8-x)*DX,T+2*DY);ctx.stroke();
  ctx.beginPath();ctx.moveTo(L+(8-x)*DX,T);ctx.lineTo(L+x*DX,T+2*DY);ctx.stroke();
  ctx.beginPath();ctx.moveTo(L+x*DX,T+7*DY);ctx.lineTo(L+(8-x)*DX,T+9*DY);ctx.stroke();
  ctx.beginPath();ctx.moveTo(L+(8-x)*DX,T+7*DY);ctx.lineTo(L+x*DX,T+9*DY);ctx.stroke();
 }
 ctx.fillStyle="#59341c";ctx.font="bold 24px Arial";ctx.textAlign="center";
 ctx.fillText("楚 河",L+2*DX,T+4.72*DY);
 ctx.fillText("漢 界",L+6*DX,T+4.72*DY);
 // Nét viền bàn cờ
 ctx.strokeStyle="#59341c";ctx.lineWidth=3;
 ctx.strokeRect(L,T,8*DX,9*DY);
 // Ô chọn và gợi ý
 if(selected){
  mark(selected.y,selected.x,"#197b4a");
  for(const m of legal){
   const cx=L+m.nx*DX,cy=T+m.ny*DY;
   ctx.beginPath();ctx.arc(cx,cy,7,0,Math.PI*2);
   ctx.fillStyle=board[m.ny][m.nx]?"#c43125":"#287a47";ctx.fill();
  }
 }
 if(hintMove){mark(hintMove.y,hintMove.x,"#277ac9");mark(hintMove.ny,hintMove.nx,"#277ac9")}
 if(lastMove){mark(lastMove.ny,lastMove.nx,"#c59a2f")}
 for(let y=0;y<10;y++)for(let x=0;x<9;x++)if(board[y][x])drawPiece(y,x,board[y][x]);
}
function mark(y,x,color){
 ctx.beginPath();ctx.arc(L+x*DX,T+y*DY,27,0,Math.PI*2);
 ctx.strokeStyle=color;ctx.lineWidth=4;ctx.stroke();
}
function drawPiece(y,x,p){
 const cx=L+x*DX,cy=T+y*DY;
 ctx.beginPath();ctx.arc(cx,cy,24,0,Math.PI*2);
 ctx.fillStyle="#f7e6bd";ctx.fill();
 ctx.strokeStyle="#6c3b1b";ctx.lineWidth=2.5;ctx.stroke();
 ctx.beginPath();ctx.arc(cx,cy,19,0,Math.PI*2);
 ctx.strokeStyle=side(p)==="r"?"#b32620":"#24201b";ctx.lineWidth=1.5;ctx.stroke();
 ctx.fillStyle=side(p)==="r"?"#b32620":"#24201b";
 ctx.font="bold 25px Arial";ctx.textAlign="center";ctx.textBaseline="middle";
 ctx.fillText(side(p)==="r"?redNames[type(p)]:names[type(p)],cx,cy+1);
}
function canvasPoint(e){
 const r=canvas.getBoundingClientRect();
 const px=(e.clientX-r.left)*W/r.width,py=(e.clientY-r.top)*H/r.height;
 return {x:Math.round((px-L)/DX),y:Math.round((py-T)/DY)};
}
canvas.addEventListener("click",e=>{
 if(finished||!$("game").classList.contains("active"))return;
 if(gameType==="bot"&&turn==="r")return;
 startAudio();
 const q=canvasPoint(e);if(!inside(q.y,q.x))return;
 if(selected&&legal.some(m=>m.ny===q.y&&m.nx===q.x)){
  makeMove(legal.find(m=>m.ny===q.y&&m.nx===q.x));return;
 }
 if(board[q.y][q.x]&&side(board[q.y][q.x])===turn){
  selected=q;legal=legalMoves(q.y,q.x);draw();
 }else{selected=null;legal=[];draw()}
});
function makeMove(m){
 history.push({board:clone(board),turn,lastMove:{...m}});
 const captured=board[m.ny][m.nx];
 board[m.ny][m.nx]=board[m.y][m.x];board[m.y][m.x]=null;
 lastMove={...m};hintMove=null;selected=null;legal=[];moveCount++;
 playEffect(captured?"capture":"move");
 const lostKing=captured&&type(captured)==="K";
 turn=opponent(turn);draw();
 if(lostKing){finish(side(captured)==="b"?"ĐỎ THẮNG!":"ĐEN THẮNG!");return}
 if(!hasAnyMove(turn)){finish(turn==="b"?"ĐỎ THẮNG!":"ĐEN THẮNG!");return}
 setStatus("Đến lượt "+label(turn));
 if(gameType==="bot"&&turn==="r"){
  setStatus("Bot ĐỎ đang suy nghĩ...");
  setTimeout(botMove,350);
 }
}
function allMoves(s){
 const arr=[];
 for(let y=0;y<10;y++)for(let x=0;x<9;x++)if(side(board[y][x])===s)
  arr.push(...legalMoves(y,x));
 return arr;
}
function hasAnyMove(s){return allMoves(s).length>0}
function evaluateMove(m){
 let score=Math.random()*2;
 const p=board[m.y][m.x],target=board[m.ny][m.nx];
 if(target)score+=values[type(target)]*1.8;
 if(type(p)==="P")score+=m.ny*0.5;
 const center=4-Math.abs(4-m.nx);
 score+=center*0.4;
 return score;
}
function botMove(){
 if(finished||turn!=="r"||gameType!=="bot")return;
 let moves=allMoves("r");
 if(!moves.length){finish("ĐEN THẮNG!");return}
 moves.sort((a,b)=>evaluateMove(b)-evaluateMove(a));
 let m;
 if(mode==="easy")m=moves[Math.floor(Math.random()*moves.length)];
 else if(mode==="medium")m=moves[Math.min(moves.length-1,Math.floor(Math.random()*Math.min(5,moves.length)))];
 else if(mode==="hard")m=moves[0];
 else{
  // Siêu khó: ưu tiên ăn quân giá trị cao, phát triển quân và giữ an toàn vua.
  m=moves.map(a=>({a,score:evaluateMove(a)+
   (type(board[a.y][a.x])==="R"?2:0)+Math.random()*0.2}))
   .sort((a,b)=>b.score-a.score)[0].a;
 }
 makeMove(m);
}
function finish(message){
 finished=true;$("result-title").textContent=message;
 $("result").classList.remove("hidden");setStatus(message);playEffect("win");
}
function surrender(){
 if(finished)return;
 finish(turn==="b"?"ĐỎ THẮNG!":"ĐEN THẮNG!");
}
function undoMove(){
 if(!history.length||finished)return;
 let steps=gameType==="bot"&&history.length>=2?2:1;
 while(steps--&&history.length){
  const h=history.pop();board=h.board;turn=h.turn;lastMove=h.lastMove;
 }
 selected=null;legal=[];hintMove=null;draw();setStatus("Đã đi lại một nước");
}
function hint(){
 if(finished)return;
 const moves=allMoves(turn);
 if(!moves.length){setStatus("Không còn nước đi hợp lệ");return}
 moves.sort((a,b)=>evaluateMove(b)-evaluateMove(a));
 hintMove=moves[0];draw();setStatus("Gợi ý: chọn quân được viền xanh");
}

// Âm thanh tạo trực tiếp bằng Web Audio, không cần tệp nhạc ngoài.
function startAudio(){
 try{
  if(!audioCtx)audioCtx=new (window.AudioContext||window.webkitAudioContext)();
  if(audioCtx.state==="suspended")audioCtx.resume();
  if(!$("music").checked||musicTimer)return;
  masterGain=audioCtx.createGain();masterGain.gain.value=volume*0.12;
  masterGain.connect(audioCtx.destination);
  const notes=[196,246.94,293.66,246.94,220,261.63,293.66,261.63];
  let i=0;
  const playNote=()=>{
   if(!$("music").checked||!audioCtx)return;
   const osc=audioCtx.createOscillator(),gain=audioCtx.createGain();
   osc.type="triangle";osc.frequency.value=notes[i++%notes.length];
   gain.gain.setValueAtTime(0.0001,audioCtx.currentTime);
   gain.gain.linearRampToValueAtTime(Math.max(0.0001,volume*0.025),audioCtx.currentTime+0.15);
   gain.gain.linearRampToValueAtTime(0.0001,audioCtx.currentTime+1.1);
   osc.connect(gain);gain.connect(audioCtx.destination);
   osc.start();osc.stop(audioCtx.currentTime+1.15);
  };
  playNote();musicTimer=setInterval(playNote,1250);
 }catch(e){}
}
function stopMusic(){
 if(musicTimer){clearInterval(musicTimer);musicTimer=null}
}
function toggleMusic(){
 if($("music").checked){startAudio()}else{stopMusic()}
}
function setVolume(v){volume=Number(v)/100}
function playEffect(kind){
 if(!$("effects").checked)return;
 try{
  if(!audioCtx)startAudio();if(!audioCtx)return;
  const o=audioCtx.createOscillator(),g=audioCtx.createGain();
  o.type="sine";o.frequency.value=kind==="capture"?620:kind==="win"?760:420;
  g.gain.setValueAtTime(Math.max(0.001,volume*0.15),audioCtx.currentTime);
  g.gain.exponentialRampToValueAtTime(0.001,audioCtx.currentTime+0.16);
  o.connect(g);g.connect(audioCtx.destination);o.start();o.stop(audioCtx.currentTime+0.17);
 }catch(e){}
}
function setLanguage(lang){
 if(lang==="en"){
  $("status").textContent="Black moves first";
 }else{
  $("status").textContent="ĐEN đi trước";
 }
}
function tick(){
 const seconds=Math.floor((Date.now()-startedAt)/1000);
 $("clock").textContent=String(Math.floor(seconds/60)).padStart(2,"0")+":"+
 String(seconds%60).padStart(2,"0");
}
setInterval(tick,1000);
board=initialBoard();draw();
// Âm thanh sẽ bắt đầu ngay khi người chơi tương tác lần đầu với trang.
document.addEventListener("pointerdown",()=>{if($("music").checked)startAudio()},{once:true});
</script>
</body>
</html>
"""

components.html(HTML, height=1000, scrolling=False)
