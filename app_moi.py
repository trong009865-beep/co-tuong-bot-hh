
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cờ Tướng", page_icon="♟", layout="wide")

st.markdown("""
<style>
#MainMenu,header,footer,[data-testid="stToolbar"]{display:none!important}
.block-container{padding:0!important;max-width:100%!important}
iframe{width:100%!important;border:0!important}
</style>
""", unsafe_allow_html=True)

HTML = r'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box}
html,body{margin:0;width:100%;height:100%;overflow:hidden}
body{font-family:Arial,"DejaVu Sans",sans-serif;color:#ffedce;background:#190b08}
button{cursor:pointer;font-family:inherit}
#app{height:100dvh;display:flex;justify-content:center;align-items:center;padding:8px}
.screen{display:none;width:min(100%,850px);height:100%;min-height:0}
.screen.active{display:flex}
#home{align-items:center;justify-content:center}
.hero{width:100%;height:100%;max-height:740px;display:flex;align-items:center;
justify-content:center;text-align:center;border:2px solid #e6bb68;border-radius:15px;
background:radial-gradient(ellipse,#78451f,#321811 58%,#170907);position:relative;overflow:hidden}
.hero:before{content:"";position:absolute;inset:5%;border:1px solid #e6bb6860}
.hero-content{position:relative;width:min(88%,360px)}
h1{font-size:clamp(36px,7vw,58px);letter-spacing:4px;color:#ffe3a0;margin:0 0 8px}
.subtitle{letter-spacing:3px;font-size:12px;margin-bottom:25px;color:#e6c58c}
.btn{display:block;width:100%;padding:12px;margin:8px 0;border:1px solid #e6bb68;
border-radius:8px;background:linear-gradient(135deg,#674022,#321811);
color:#fff0d0;font-weight:bold;font-size:15px}
.btn.gold{background:linear-gradient(135deg,#f5d891,#bd8539);color:#291409}
.btn.dark{background:#21110e}
#game{align-items:center;justify-content:center}
.layout{width:min(100%,650px);height:100%;display:flex;flex-direction:column;
justify-content:center;gap:5px;min-height:0}
.top{display:flex;align-items:center;justify-content:space-between;gap:7px}
.top button{width:auto;margin:0;padding:7px 10px}
.title{font-weight:bold;letter-spacing:2px;color:#ffe3a0}
.players{display:flex;justify-content:space-between;background:#321a12;
border:1px solid #8d6539;padding:5px 8px;border-radius:6px;font-size:12px}
#boardWrap{position:relative;width:min(100%,calc((100dvh - 205px)*.78));
max-height:calc(100dvh - 205px);aspect-ratio:680/760;margin:0 auto}
canvas{width:100%;height:100%;display:block;touch-action:manipulation}
.tools{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:5px}
.tools button{margin:0;padding:8px 1px;font-size:12px;color:#ffedce;
background:#352018;border:1px solid #90683e;border-radius:7px}
#status{text-align:center;font-size:12px;color:#e6c58c;min-height:16px}
.modal{position:fixed;inset:0;z-index:20;display:flex;align-items:center;
justify-content:center;padding:12px;background:#080403e8}
.hidden{display:none!important}
.dialog{width:min(100%,370px);max-height:90dvh;overflow:auto;padding:20px;
border:2px solid #e6bb68;border-radius:12px;background:linear-gradient(145deg,#48271b,#1b0c09)}
.dialog h2{text-align:center;color:#ffe3a0;margin:0 0 15px;font-size:21px}
.dialog label{font-size:14px}
.setting{display:flex;justify-content:space-between;align-items:center;gap:10px;margin:15px 0}
.setting input[type=range]{width:45%}
.setting input[type=checkbox]{width:18px;height:18px;accent-color:#e6bb68}
.result{position:absolute;inset:0;z-index:10;background:#130705ed;
display:flex;align-items:center;justify-content:center;text-align:center}
.result h2{font-size:clamp(30px,7vw,50px);color:#ffe3a0}
@media(max-height:740px){
 #boardWrap{width:min(100%,calc((100dvh - 180px)*.78));max-height:calc(100dvh - 180px)}
 .btn{padding:9px;margin:6px 0}
 .tools button{padding:6px 1px}
}
@media(max-width:500px){
 #app{padding:3px}
 #boardWrap{width:min(100%,calc((100dvh - 200px)*.78));max-height:calc(100dvh - 200px)}
 .tools button{font-size:10px}
}
</style>
</head>
<body>
<div id="app">
<section id="home" class="screen active">
 <div class="hero">
  <div class="hero-content">
   <h1>CỜ TƯỚNG</h1>
   <div class="subtitle">TRÍ TUỆ • CHIẾN LƯỢC</div>
   <button class="btn gold" data-action="difficulty">♟ Đấu với máy</button>
   <button class="btn" data-action="two">⚔ Đấu hai người</button>
   <button class="btn" data-action="rules">📜 Luật chơi</button>
   <button class="btn dark" data-action="settings">⚙ Cài đặt</button>
  </div>
 </div>
</section>

<section id="game" class="screen">
 <div class="layout">
  <div class="top">
   <button class="btn" style="width:auto" data-action="settings">⚙</button>
   <div class="title">CỜ TƯỚNG</div>
   <button class="btn" style="width:auto" data-action="home">⌂ Menu</button>
  </div>
  <div class="players"><span id="redLabel">🔴 ĐỎ: Bot</span><span id="clock">00:00</span><span>⚫ ĐEN: Bạn</span></div>
  <div id="boardWrap">
   <canvas id="board" width="680" height="760"></canvas>
   <div id="result" class="result hidden">
    <div><h2 id="resultText">CHIẾN THẮNG</h2>
     <button class="btn gold" data-action="new">Ván mới</button>
     <button class="btn" data-action="home">Về menu</button>
    </div>
   </div>
  </div>
  <div class="tools">
   <button data-action="hint">💡 Gợi ý</button>
   <button data-action="undo">↶ Đi lại</button>
   <button data-action="new">⟳ Ván mới</button>
   <button data-action="surrender">🏳 Đầu hàng</button>
  </div>
  <div id="status">ĐEN đi trước</div>
 </div>
</section>
</div>

<div id="difficulty" class="modal hidden">
 <div class="dialog">
  <h2>CHỌN ĐỘ KHÓ</h2>
  <button class="btn" data-mode="easy">🌱 Dễ</button>
  <button class="btn" data-mode="medium">🗡 Trung bình</button>
  <button class="btn" data-mode="hard">🔥 Khó</button>
  <button class="btn gold" data-mode="expert">👑 Siêu khó</button>
  <button class="btn dark" data-action="close">Quay lại</button>
 </div>
</div>

<div id="settings" class="modal hidden">
 <div class="dialog">
  <h2>CÀI ĐẶT</h2>
  <div class="setting"><label for="music">Nhạc nền mặc định bật</label><input id="music" type="checkbox" checked></div>
  <div class="setting"><label for="effects">Âm thanh nước đi</label><input id="effects" type="checkbox" checked></div>
  <div class="setting"><label for="volume">Âm lượng</label><input id="volume" type="range" min="0" max="100" value="30"></div>
  <button class="btn gold" data-action="close">Lưu và đóng</button>
 </div>
</div>

<div id="rules" class="modal hidden">
 <div class="dialog">
  <h2>LUẬT CHƠI</h2>
  <p>• ĐEN đi trước, ĐỎ đi sau.</p>
  <p>• Xe đi ngang hoặc dọc, không nhảy qua quân.</p>
  <p>• Pháo đi ngang hoặc dọc; khi ăn phải nhảy qua một quân.</p>
  <p>• Mã đi hình chữ L và có thể bị cản.</p>
  <p>• Tượng đi chéo hai ô; Sĩ đi chéo một ô trong cung.</p>
  <p>• Tốt đi thẳng; qua sông được đi ngang.</p>
  <button class="btn gold" data-action="close">Đã hiểu</button>
 </div>
</div>

<script>
"use strict";
const $=id=>document.getElementById(id);
const canvas=$("board"),ctx=canvas.getContext("2d");
const L=50,T=40,DX=72.5,DY=75;
let board,turn="b",selected=null,moves=[],history=[],lastMove=null;
let mode="easy",gameType="bot",finished=false,hintMove=null;
let audioCtx=null,osc=null,musicGain=null,musicTimer=null;
let startTime=Date.now(),volume=.3;

function screen(id){
 document.querySelectorAll(".screen").forEach(e=>e.classList.remove("active"));
 $(id).classList.add("active");
}
function closeModals(){document.querySelectorAll(".modal").forEach(e=>e.classList.add("hidden"))}
function modal(id){closeModals();$(id).classList.remove("hidden")}
function status(s){$("status").textContent=s}
function opponent(s){return s==="b"?"r":"b"}
function side(p){return p?p[0]:null}
function type(p){return p?p[1]:null}
function inside(y,x){return y>=0&&y<10&&x>=0&&x<9}
function clone(b){return b.map(r=>r.slice())}
function palace(s,y,x){return x>=3&&x<=5&&(s==="r"?y<=2:y>=7)}
function initial(){
 let b=Array.from({length:10},()=>Array(9).fill(null));
 let back=["R","H","E","A","K","A","E","H","R"];
 for(let x=0;x<9;x++){b[0][x]="r"+back[x];b[9][x]="b"+back[x]}
 b[2][1]="rC";b[2][7]="rC";b[7][1]="bC";b[7][7]="bC";
 for(let x=0;x<9;x+=2){b[3][x]="rP";b[6][x]="bP"}
 return b;
}
function add(a,y,x,ny,nx,s){
 if(!inside(ny,nx))return;
 if(!board[ny][nx]||side(board[ny][nx])!==s)a.push({y,x,ny,nx});
}
function pseudo(y,x){
 let p=board[y][x];if(!p)return [];
 let s=side(p),t=type(p),a=[],step=s==="r"?1:-1;
 if(t==="K"){
  for(let [dy,dx] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let ny=y+dy,nx=x+dx;if(palace(s,ny,nx))add(a,y,x,ny,nx,s);
  }
  for(let ny=y+step;inside(ny,x);ny+=step){
   if(board[ny][x]){
    if(type(board[ny][x])==="K"&&side(board[ny][x])!==s)a.push({y,x,ny,nx:x});
    break;
   }
  }
 }else if(t==="A"){
  for(let [dy,dx] of [[1,1],[1,-1],[-1,1],[-1,-1]]){
   let ny=y+dy,nx=x+dx;if(palace(s,ny,nx))add(a,y,x,ny,nx,s);
  }
 }else if(t==="E"){
  for(let [dy,dx] of [[2,2],[2,-2],[-2,2],[-2,-2]]){
   let ny=y+dy,nx=x+dx;
   if(!inside(ny,nx)||(s==="r"&&ny>4)||(s==="b"&&ny<5))continue;
   if(!board[y+dy/2][x+dx/2])add(a,y,x,ny,nx,s);
  }
 }else if(t==="H"){
  for(let [dy,dx,ly,lx] of [
   [-2,-1,-1,0],[-2,1,-1,0],[2,-1,1,0],[2,1,1,0],
   [-1,-2,0,-1],[1,-2,0,-1],[-1,2,0,1],[1,2,0,1]
  ]){
   let ny=y+dy,nx=x+dx;
   if(inside(ny,nx)&&!board[y+ly][x+lx])add(a,y,x,ny,nx,s);
  }
 }else if(t==="R"||t==="C"){
  for(let [dy,dx] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let ny=y+dy,nx=x+dx,screened=false;
   while(inside(ny,nx)){
    let q=board[ny][nx];
    if(t==="R"){
     if(!q)add(a,y,x,ny,nx,s);
     else{if(side(q)!==s)add(a,y,x,ny,nx,s);break}
    }else{
     if(!screened){if(!q)add(a,y,x,ny,nx,s);else screened=true}
     else if(q){if(side(q)!==s)add(a,y,x,ny,nx,s);break}
    }
    ny+=dy;nx+=dx;
   }
  }
 }else if(t==="P"){
  add(a,y,x,y+step,x,s);
  if(s==="b"?y<=4:y>=5){add(a,y,x,y,x-1,s);add(a,y,x,y,x+1,s)}
 }
 return a;
}
function allMoves(s){
 let a=[];
 for(let y=0;y<10;y++)for(let x=0;x<9;x++)
  if(side(board[y][x])===s)a.push(...pseudo(y,x));
 return a;
}
function draw(){
 ctx.clearRect(0,0,680,760);
 let grad=ctx.createLinearGradient(0,0,680,760);
 grad.addColorStop(0,"#f0d59a");grad.addColorStop(1,"#c18b47");
 ctx.fillStyle=grad;ctx.fillRect(0,0,680,760);
 ctx.strokeStyle="#59341c";ctx.lineWidth=2;
 for(let y=0;y<10;y++){
  ctx.beginPath();ctx.moveTo(L,T+y*DY);ctx.lineTo(L+8*DX,T+y*DY);ctx.stroke();
 }
 for(let x=0;x<9;x++){
  ctx.beginPath();ctx.moveTo(L+x*DX,T);ctx.lineTo(L+x*DX,T+4*DY);ctx.stroke();
  ctx.beginPath();ctx.moveTo(L+x*DX,T+5*DY);ctx.lineTo(L+x*DX,T+9*DY);ctx.stroke();
 }
 for(let x of [3,5]){
  ctx.beginPath();ctx.moveTo(L+x*DX,T);ctx.lineTo(L+(8-x)*DX,T+2*DY);ctx.stroke();
  ctx.beginPath();ctx.moveTo(L+(8-x)*DX,T);ctx.lineTo(L+x*DX,T+2*DY);ctx.stroke();
  ctx.beginPath();ctx.moveTo(L+x*DX,T+7*DY);ctx.lineTo(L+(8-x)*DX,T+9*DY);ctx.stroke();
  ctx.beginPath();ctx.moveTo(L+(8-x)*DX,T+7*DY);ctx.lineTo(L+x*DX,T+9*DY);ctx.stroke();
 }
 ctx.fillStyle="#59341c";ctx.font="bold 24px Arial";ctx.textAlign="center";
 ctx.fillText("楚 河",L+2*DX,T+4.72*DY);ctx.fillText("漢 界",L+6*DX,T+4.72*DY);
 ctx.strokeRect(L,T,8*DX,9*DY);
 function ring(y,x,c){ctx.beginPath();ctx.arc(L+x*DX,T+y*DY,27,0,Math.PI*2);ctx.strokeStyle=c;ctx.lineWidth=4;ctx.stroke()}
 if(selected)ring(selected.y,selected.x,"#21844e");
 if(lastMove)ring(lastMove.ny,lastMove.nx,"#c3972e");
 if(hintMove){ring(hintMove.y,hintMove.x,"#267ac5");ring(hintMove.ny,hintMove.nx,"#267ac5")}
 for(let m of moves){
  ctx.beginPath();ctx.arc(L+m.nx*DX,T+m.ny*DY,7,0,Math.PI*2);
  ctx.fillStyle=board[m.ny][m.nx]?"#bd3025":"#27804c";ctx.fill();
 }
 const red={K:"帥",A:"仕",E:"相",H:"傌",R:"俥",C:"炮",P:"兵"};
 const black={K:"將",A:"士",E:"象",H:"馬",R:"車",C:"炮",P:"卒"};
 for(let y=0;y<10;y++)for(let x=0;x<9;x++){
  let p=board[y][x];if(!p)continue;
  let cx=L+x*DX,cy=T+y*DY;
  ctx.beginPath();ctx.arc(cx,cy,24,0,Math.PI*2);
  ctx.fillStyle="#f7e6bd";ctx.fill();ctx.strokeStyle="#754522";ctx.lineWidth=2.5;ctx.stroke();
  ctx.beginPath();ctx.arc(cx,cy,19,0,Math.PI*2);
  ctx.strokeStyle=side(p)==="r"?"#b32620":"#24201b";ctx.lineWidth=1.5;ctx.stroke();
  ctx.fillStyle=side(p)==="r"?"#b32620":"#24201b";
  ctx.font="bold 25px Arial";ctx.textAlign="center";ctx.textBaseline="middle";
  ctx.fillText((side(p)==="r"?red:black)[type(p)],cx,cy+1);
 }
}
function begin(which){
 closeModals();startAudio();
 if(which==="two"){gameType="two";mode="two";$("redLabel").textContent="🔴 ĐỎ: Người chơi 2"}
 else{gameType="bot";mode=which;$("redLabel").textContent="🔴 ĐỎ: Bot"}
 screen("game");newGame();
}
function newGame(){
 board=initial();turn="b";selected=null;moves=[];history=[];
 lastMove=null;hintMove=null;finished=false;startTime=Date.now();
 $("result").classList.add("hidden");status("ĐEN đi trước");draw();
}
function finish(text){
 finished=true;$("resultText").textContent=text;$("result").classList.remove("hidden");status(text);effect(660);
}
function move(m){
 history.push({board:clone(board),turn,lastMove});
 let captured=board[m.ny][m.nx];
 board[m.ny][m.nx]=board[m.y][m.x];board[m.y][m.x]=null;
 lastMove=m;selected=null;moves=[];hintMove=null;turn=opponent(turn);
 draw();effect(captured?620:420);
 if(captured&&type(captured)==="K"){finish(captured[0]==="b"?"ĐỎ THẮNG!":"ĐEN THẮNG!");return}
 if(!allMoves(turn).length){finish(turn==="b"?"ĐỎ THẮNG!":"ĐEN THẮNG!");return}
 status("Đến lượt "+(turn==="b"?"ĐEN":"ĐỎ"));
 if(gameType==="bot"&&turn==="r")setTimeout(botMove,350);
}
function botMove(){
 if(finished||turn!=="r")return;
 let a=allMoves("r");if(!a.length){finish("ĐEN THẮNG!");return}
 function score(m){
  let p=board[m.ny][m.nx],v=p?({K:1000,R:90,C:50,H:45,E:20,A:20,P:10}[type(p)]):0;
  return v+(mode==="easy"?Math.random()*100:Math.random()*8);
 }
 a.sort((x,y)=>score(y)-score(x));
 let m=mode==="easy"?a[Math.floor(Math.random()*a.length)]:a[0];
 move(m);
}
canvas.addEventListener("click",e=>{
 if(finished||(gameType==="bot"&&turn==="r"))return;
 startAudio();
 let r=canvas.getBoundingClientRect();
 let x=Math.round(((e.clientX-r.left)*680/r.width-L)/DX);
 let y=Math.round(((e.clientY-r.top)*760/r.height-T)/DY);
 if(!inside(y,x))return;
 if(selected&&moves.some(m=>m.ny===y&&m.nx===x)){
  move(moves.find(m=>m.ny===y&&m.nx===x));return;
 }
 if(board[y][x]&&side(board[y][x])===turn){
  selected={y,x};moves=pseudo(y,x);draw();
 }else{selected=null;moves=[];draw()}
});
function undo(){
 if(!history.length||finished)return;
 let n=gameType==="bot"&&history.length>=2?2:1;
 while(n--&&history.length){let h=history.pop();board=h.board;turn=h.turn;lastMove=h.lastMove}
 selected=null;moves=[];hintMove=null;draw();status("Đã đi lại");
}
function hint(){
 let a=allMoves(turn);if(!a.length)return;
 let m=a[Math.floor(Math.random()*a.length)];
 hintMove=m;draw();status("Gợi ý: viền xanh là nước đi tham khảo");
}
function surrender(){if(!finished)finish(turn==="b"?"ĐỎ THẮNG!":"ĐEN THẮNG!")}
function startAudio(){
 try{
  if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();
  if(audioCtx.state==="suspended")audioCtx.resume();
  if(!$("music").checked||musicTimer)return;
  let notes=[196,246.94,293.66,246.94,220,261.63];
  let i=0;
  musicTimer=setInterval(()=>{
   if(!$("music").checked){clearInterval(musicTimer);musicTimer=null;return}
   let o=audioCtx.createOscillator(),g=audioCtx.createGain();
   o.type="triangle";o.frequency.value=notes[i++%notes.length];
   g.gain.value=volume*.035;o.connect(g);g.connect(audioCtx.destination);
   o.start();o.stop(audioCtx.currentTime+0.7);
  },900);
 }catch(e){console.log(e)}
}
function effect(freq){
 if(!$("effects").checked)return;
 try{
  startAudio();if(!audioCtx)return;
  let o=audioCtx.createOscillator(),g=audioCtx.createGain();
  o.frequency.value=freq;g.gain.value=volume*.12;
  o.connect(g);g.connect(audioCtx.destination);o.start();o.stop(audioCtx.currentTime+.12);
 }catch(e){}
}
document.addEventListener("input",e=>{
 if(e.target.id==="volume")volume=Number(e.target.value)/100;
 if(e.target.id==="music"&&!e.target.checked&&musicTimer){clearInterval(musicTimer);musicTimer=null}
 if(e.target.id==="music"&&e.target.checked)startAudio();
});
document.addEventListener("click",e=>{
 const b=e.target.closest("button");if(!b)return;
 const action=b.dataset.action;
 if(action){
  if(action==="difficulty")modal("difficulty");
  else if(action==="settings"){modal("settings");startAudio()}
  else if(action==="rules")modal("rules");
  else if(action==="two")begin("two");
  else if(action==="close")closeModals();
  else if(action==="home"){closeModals();screen("home")}
  else if(action==="new")newGame();
  else if(action==="undo")undo();
  else if(action==="hint")hint();
  else if(action==="surrender")surrender();
 }
 if(b.dataset.mode)begin(b.dataset.mode);
});
setInterval(()=>{
 let n=Math.floor((Date.now()-startTime)/1000);
 $("clock").textContent=String(Math.floor(n/60)).padStart(2,"0")+":"+String(n%60).padStart(2,"0");
},1000);
window.addEventListener("error",e=>{
 let s=$("status");if(s)s.textContent="Lỗi game: "+e.message;
});
board=initial();draw();
</script>
</body>
</html>'''

components.html(HTML, height=1000, scrolling=False)

