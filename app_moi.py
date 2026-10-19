
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cờ Tướng",
    page_icon="♟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu,footer,header,[data-testid="stToolbar"],
[data-testid="stDecoration"]{display:none!important}
.block-container{padding:0!important;max-width:100%!important}
iframe{border:0!important}
</style>
""", unsafe_allow_html=True)

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box}
:root{--gold:#e8c47b;--cream:#fff0ce;--red:#8e3021;--dark:#21100d}
body{margin:0;background:#1a0c09;color:var(--cream);
font-family:Georgia,"Noto Serif",serif}
button,select,input{font:inherit}
button{cursor:pointer;transition:filter .2s,transform .2s}
button:hover{filter:brightness(1.17)}
button:active{transform:scale(.98)}
.hidden{display:none!important}
.page{max-width:1100px;margin:auto;padding:16px}
.panel{border:1px solid #b88745;border-radius:18px;
background:linear-gradient(145deg,#452219,#25120e);
box-shadow:0 12px 36px #0008;padding:20px}
.hero{position:relative;overflow:hidden;min-height:610px;
border:2px solid #c79b52;border-radius:16px;
display:flex;align-items:center;justify-content:center;
text-align:center;padding:25px;
background:
radial-gradient(ellipse at 50% 44%,#6f391f55,transparent 55%),
linear-gradient(90deg,#1a0908dc,#35160cc9 45%,#1b0909dc),
repeating-linear-gradient(90deg,#63321c 0,#63321c 2px,#482315 3px,#32170f 12px);
}
.hero:before{content:"";position:absolute;inset:15px;
border:1px solid #d1a15b66;pointer-events:none}
.decor-board{position:absolute;width:min(78%,670px);height:330px;
bottom:22px;left:50%;transform:translateX(-50%) perspective(650px) rotateX(13deg);
border:9px solid #67371c;border-radius:4px;
background:
linear-gradient(#9d6839aa,#c08b4c88),
repeating-linear-gradient(0deg,transparent 0 32px,#482a18 33px 34px),
repeating-linear-gradient(90deg,transparent 0 32px,#482a18 33px 34px);
box-shadow:0 18px 30px #0009;opacity:.72}
.decor-board:after{content:"帥 仕 相 傌 俥 炮 兵　　將 士 象 馬 車 砲 卒";
position:absolute;left:0;right:0;bottom:26px;text-align:center;
font-size:clamp(13px,2vw,23px);color:#5c1e16;
text-shadow:1px 1px #f0c984;word-spacing:8px}
.hero-content{position:relative;z-index:2;width:min(100%,680px);
margin-top:-75px;text-shadow:0 3px 10px #000}
.lanterns{font-size:31px;letter-spacing:12px}
h1{font-size:clamp(42px,8vw,76px);letter-spacing:5px;
color:#f4d38a;margin:12px 0 5px;
text-shadow:0 2px 0 #7b461d,0 5px 16px #000}
.subtitle{color:#f3d9a9;font-size:17px;margin:8px 0 25px}
.modes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));
gap:11px;width:min(100%,480px);margin:20px auto}
.btn{width:100%;border:1px solid #e3bd76;border-radius:9px;
padding:13px 10px;background:linear-gradient(#9c4b2b,#65271c);
color:#fff0d1;font-weight:bold;font-size:16px;
box-shadow:0 4px 9px #0005}
.btn.gold{background:linear-gradient(#f0d391,#b77c35);color:#32170e}
.btn.dark{background:#301914eF}
.btn.small{font-size:14px;padding:10px}
.screen-title{text-align:center;color:#f1ce83;letter-spacing:2px}
.backline{max-width:480px;margin:12px auto}
.gamebar{display:flex;align-items:center;justify-content:space-between;
gap:8px;flex-wrap:wrap;margin-bottom:10px}
.pill{background:#29150f;border:1px solid #986a37;border-radius:9px;
padding:9px 12px;color:#f5d79b}
.board-wrap{position:relative;width:min(100%,680px);margin:0 auto}
#board{display:block;width:100%;height:auto;border:1px solid #c49450;
border-radius:6px;box-shadow:0 10px 28px #0008;touch-action:manipulation}
.status{text-align:center;color:#f4d18b;padding:9px;font-size:17px}
.tools{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));
gap:9px;margin:15px auto 5px}
.tool{border:1px solid #9c7545;border-radius:9px;background:#321b14;
color:#ffe6b5;padding:13px 5px;font-size:15px}
.note{text-align:center;color:#c9a77e;font-size:12px;line-height:1.6}
.overlay{position:absolute;inset:0;z-index:5;
display:flex;align-items:center;justify-content:center;
padding:18px;text-align:center;background:#160805eF;
border:2px solid var(--gold);border-radius:6px}
.dialog{width:min(100%,430px);padding:22px;
border:1px solid #c99c56;border-radius:15px;
background:linear-gradient(145deg,#51281d,#21100d);
box-shadow:0 15px 45px #000b}
.dialog h2{color:#f4d38a;font-size:clamp(25px,5vw,42px);margin:8px 0 16px}
.dialog label{display:flex;align-items:center;justify-content:space-between;
gap:10px;margin:15px 0;text-align:left}
.dialog input[type=range]{width:48%;accent-color:#d9ac61}
.dialog input[type=checkbox]{width:19px;height:19px;accent-color:#bd8b44}
.dialog select{max-width:130px;background:#2b1710;color:#fff0ce;
border:1px solid #a17a47;border-radius:6px;padding:7px}
@media(max-width:600px){
 .page{padding:7px}.panel{padding:9px}.hero{min-height:540px;padding:14px}
 .hero-content{margin-top:-60px}.subtitle{font-size:14px}
 .decor-board{width:91%;height:270px;bottom:16px}
 .tools{grid-template-columns:repeat(2,minmax(0,1fr))}
 .tool{padding:12px 4px;font-size:14px}
 .btn{font-size:14px;padding:12px 6px}
 .gamebar{justify-content:center}
}
</style>
</head>
<body>
<div class="page">

<section id="home" class="panel">
 <div class="hero">
  <div class="decor-board"></div>
  <div class="hero-content">
   <div class="lanterns">🏮　♟　🏮</div>
   <h1>CỜ TƯỚNG</h1>
   <div class="subtitle">Khai cuộc • Đối trí • Phá thế cờ</div>
   <div class="modes">
    <button class="btn gold" onclick="showDifficulty()">⚔ Đấu với máy</button>
    <button class="btn" onclick="startGame('human')">♟ Đấu hai người</button>
    <button class="btn dark" onclick="openDialog('rulesDialog')">📜 Luật chơi</button>
    <button class="btn dark" onclick="openDialog('settingsDialog')">⚙ Cài đặt</button>
   </div>
  </div>
 </div>
 <div id="difficulty" class="hidden">
  <h2 class="screen-title">CHỌN CẤP ĐỘ</h2>
  <div class="modes">
   <button class="btn" onclick="startGame('easy')">🌱 Dễ</button>
   <button class="btn" onclick="startGame('medium')">🗡 Trung bình</button>
   <button class="btn" onclick="startGame('hard')">🔥 Khó</button>
   <button class="btn gold" onclick="startGame('expert')">👑 Siêu khó</button>
  </div>
  <div class="backline"><button class="btn dark" onclick="hideDifficulty()">← Quay lại</button></div>
 </div>
</section>

<section id="game" class="panel hidden">
 <div class="gamebar">
  <button class="btn dark small" onclick="openDialog('settingsDialog')">⚙ Cài đặt</button>
  <div class="pill" id="modeLabel">CỜ TƯỚNG</div>
  <button class="btn dark small" onclick="goHome()">⌂ Trang chủ</button>
 </div>
 <div id="status" class="status">Lượt Đỏ</div>
 <div class="board-wrap">
  <canvas id="board" width="680" height="760"></canvas>
  <div id="resultOverlay" class="overlay hidden">
   <div class="dialog">
    <div style="font-size:42px">🏆</div>
    <h2 id="resultTitle">CHIẾN THẮNG!</h2>
    <p id="resultText">Ván đấu đã kết thúc.</p>
    <button class="btn gold" onclick="newGame()">↻ Chơi lại</button>
    <button class="btn dark" onclick="goHome()" style="margin-top:8px">⌂ Trang chủ</button>
   </div>
  </div>
 </div>
 <div class="tools">
  <button class="tool" onclick="hint()">💡 Gợi ý</button>
  <button class="tool" onclick="undoMove()">↶ Đi lại</button>
  <button class="tool" onclick="newGame()">⟳ Ván mới</button>
  <button class="tool" onclick="resign()">🏳 Đầu hàng</button>
 </div>
 <p class="note">Chọn quân của mình, sau đó chọn ô muốn đi.</p>
</section>

<!-- Cửa sổ nổi, đè lên màn hình hiện tại -->
<div id="settingsDialog" class="overlay hidden">
 <div class="dialog">
  <h2>CÀI ĐẶT</h2>
  <label>Âm thanh quân cờ <input id="soundToggle" type="checkbox" checked onchange="soundOn=this.checked"></label>
  <label>Nhạc nền <input id="musicToggle" type="checkbox" onchange="toggleMusic(this.checked)"></label>
  <label>Âm lượng <input id="volume" type="range" min="0" max="100" value="35" oninput="volume=this.value/100"></label>
  <label>Ngôn ngữ
   <select id="language" onchange="changeLanguage(this.value)">
    <option value="vi">Tiếng Việt</option>
    <option value="en">English</option>
   </select>
  </label>
  <button class="btn gold" onclick="closeDialog('settingsDialog')">Lưu và đóng</button>
 </div>
</div>

<div id="rulesDialog" class="overlay hidden">
 <div class="dialog">
  <h2>LUẬT CHƠI CƠ BẢN</h2>
  <p>Xe đi ngang hoặc dọc, không được nhảy qua quân khác.</p>
  <p>Mã đi hình chữ L, nhưng bị cản nếu có quân ở chân Mã.</p>
  <p>Pháo đi như Xe; khi ăn quân phải nhảy qua đúng một quân.</p>
  <p>Tướng và Sĩ đi trong cung. Tượng đi chéo hai ô và không qua sông.</p>
  <p>Tốt đi thẳng; qua sông có thể đi ngang.</p>
  <button class="btn gold" onclick="closeDialog('rulesDialog')">Đã hiểu</button>
 </div>
</div>

</div>
<script>
const canvas=document.getElementById('board');
const ctx=canvas.getContext('2d');
const L=48,T=40,DX=73,DY=75;
const chars={K:'帥',A:'仕',E:'相',H:'傌',R:'俥',C:'炮',P:'兵',
 k:'將',a:'士',e:'象',h:'馬',r:'車',c:'砲',p:'卒'};
const vals={K:10000,k:10000,R:900,r:900,C:450,c:450,
 H:400,h:400,E:200,e:200,A:200,a:200,P:100,p:100};
let board,turn,selected,moves,history,mode='human',ended=false;
let soundOn=true,volume=.35,musicOn=false,audio=null,musicTimer=null;
let hintMove=null,lang='vi';

function initialBoard(){
 let b=Array.from({length:10},()=>Array(9).fill(null));
 const put=(y,x,p)=>b[y][x]=p;
 ['r','h','e','a','k','a','e','h','r'].forEach((p,x)=>put(0,x,p));
 put(2,1,'c');put(2,7,'c');[0,2,4,6,8].forEach(x=>put(3,x,'p'));
 ['R','H','E','A','K','A','E','H','R'].forEach((p,x)=>put(9,x,p));
 put(7,1,'C');put(7,7,'C');[0,2,4,6,8].forEach(x=>put(6,x,'P'));
 return b;
}
const clone=b=>b.map(r=>r.slice());
const side=p=>p===p.toUpperCase()?'r':'b';
const inside=(y,x)=>y>=0&&y<10&&x>=0&&x<9;
function palace(y,x,s){return x>=3&&x<=5&&(s==='r'?y>=7&&y<=9:y>=0&&y<=2)}
function crossed(y,s){return s==='r'?y<=4:y>=5}
function addMove(b,out,s,y,x){if(inside(y,x)&&(!b[y][x]||side(b[y][x])!==s))out.push([y,x])}
function pseudo(b,y,x){
 const p=b[y][x];if(!p)return [];
 const s=side(p),t=p.toUpperCase(),out=[];
 if(t==='K'||t==='A'){
  const ds=t==='K'?[[1,0],[-1,0],[0,1],[0,-1]]:[[1,1],[1,-1],[-1,1],[-1,-1]];
  for(const [dy,dx] of ds){const ny=y+dy,nx=x+dx;if(palace(ny,nx,s))addMove(b,out,s,ny,nx)}
  if(t==='K'){
   for(const d of [-1,1]){
    let ny=y+d;
    while(inside(ny,x)){
     if(b[ny][x]){if(b[ny][x].toUpperCase()==='K'&&side(b[ny][x])!==s)out.push([ny,x]);break}
     ny+=d;
    }
   }
  }
 }else if(t==='E'){
  for(const [dy,dx] of [[2,2],[2,-2],[-2,2],[-2,-2]]){
   const ny=y+dy,nx=x+dx;
   if(inside(ny,nx)&&!b[y+dy/2][x+dx/2]&&!crossed(ny,s))addMove(b,out,s,ny,nx);
  }
 }else if(t==='H'){
  const jumps=[[-2,-1,-1,0],[-2,1,-1,0],[2,-1,1,0],[2,1,1,0],
   [-1,-2,0,-1],[1,-2,0,-1],[-1,2,0,1],[1,2,0,1]];
  for(const [dy,dx,by,bx] of jumps){
   const ny=y+dy,nx=x+dx;
   if(inside(ny,nx)&&!b[y+by][x+bx])addMove(b,out,s,ny,nx);
  }
 }else if(t==='R'||t==='C'){
  // Xe: đi đến ô trống hoặc ăn quân đối phương đầu tiên trên mỗi hướng.
  // Pháo: đi qua ô trống; ăn quân sau khi nhảy qua đúng một quân.
  for(const [dy,dx] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let ny=y+dy,nx=x+dx,screen=false;
   while(inside(ny,nx)){
    const target=b[ny][nx];
    if(t==='R'){
     if(!target)addMove(b,out,s,ny,nx);
     else{if(side(target)!==s)addMove(b,out,s,ny,nx);break}
    }else{
     if(!screen){
      if(!target)addMove(b,out,s,ny,nx);
      else screen=true;
     }else if(target){
      if(side(target)!==s)addMove(b,out,s,ny,nx);
      break;
     }
    }
    ny+=dy;nx+=dx;
   }
  }
 }else if(t==='P'){
  const dy=s==='r'?-1:1;
  addMove(b,out,s,y+dy,x);
  if(crossed(y,s)){addMove(b,out,s,y,x-1);addMove(b,out,s,y,x+1)}
 }
 return out;
}
function kingPos(b,s){
 for(let y=0;y<10;y++)for(let x=0;x<9;x++)
  if(b[y][x]&&b[y][x].toUpperCase()==='K'&&side(b[y][x])===s)return [y,x];
 return null;
}
function attacked(b,y,x,by){
 for(let yy=0;yy<10;yy++)for(let xx=0;xx<9;xx++){
  const p=b[yy][xx];
  if(p&&side(p)===by&&pseudo(b,yy,xx).some(q=>q[0]===y&&q[1]===x))return true;
 }
 return false;
}
function inCheck(b,s){
 const k=kingPos(b,s);
 return !k||attacked(b,k[0],k[1],s==='r'?'b':'r');
}
function legal(b,y,x){
 if(!b[y][x])return [];
 const s=side(b[y][x]);
 return pseudo(b,y,x).filter(([ny,nx])=>{
  const nb=clone(b);nb[ny][nx]=nb[y][x];nb[y][x]=null;
  return !inCheck(nb,s);
 });
}
function allMoves(b,s){
 const out=[];
 for(let y=0;y<10;y++)for(let x=0;x<9;x++)
  if(b[y][x]&&side(b[y][x])===s)
   for(const [ny,nx] of legal(b,y,x))out.push({y,x,ny,nx});
 return out;
}
function drawBoard(){
 ctx.clearRect(0,0,680,760);
 ctx.fillStyle='#70401f';ctx.fillRect(10,10,660,740);
 ctx.fillStyle='#d9b476';ctx.fillRect(19,19,642,722);
 const grad=ctx.createLinearGradient(0,20,0,740);
 grad.addColorStop(0,'#e6c98b');grad.addColorStop(1,'#c99b59');
 ctx.fillStyle=grad;ctx.fillRect(22,22,636,716);
 ctx.strokeStyle='#563019';ctx.lineWidth=2;
 for(let x=0;x<9;x++){
  ctx.beginPath();ctx.moveTo(L+x*DX,T);ctx.lineTo(L+x*DX,T+9*DY);ctx.stroke();
 }
 for(let y=0;y<10;y++){
  ctx.beginPath();ctx.moveTo(L,T+y*DY);ctx.lineTo(L+8*DX,T+y*DY);ctx.stroke();
 }
 // Hai đường chéo trong cung Tướng.
 for(const y of [0,7]){
  ctx.beginPath();ctx.moveTo(L+3*DX,T+y*DY);ctx.lineTo(L+5*DX,T+(y+2)*DY);ctx.stroke();
  ctx.beginPath();ctx.moveTo(L+5*DX,T+y*DY);ctx.lineTo(L+3*DX,T+(y+2)*DY);ctx.stroke();
 }
 ctx.fillStyle='#63331b';ctx.font='bold 23px serif';ctx.textAlign='center';
 ctx.fillText('楚 河',L+2*DX,T+4.65*DY);ctx.fillText('漢 界',L+6*DX,T+4.65*DY);
 if(selected){
  ctx.fillStyle='#36884c55';ctx.fillRect(L+selected[1]*DX-22,T+selected[0]*DY-22,44,44);
  for(const [y,x] of moves){
   ctx.beginPath();ctx.arc(L+x*DX,T+y*DY,7,0,Math.PI*2);
   ctx.fillStyle='#237b43';ctx.fill();
  }
 }
 if(hintMove){
  ctx.strokeStyle='#147544';ctx.lineWidth=4;
  for(const [y,x] of [[hintMove.y,hintMove.x],[hintMove.ny,hintMove.nx]]){
   ctx.beginPath();ctx.arc(L+x*DX,T+y*DY,25,0,Math.PI*2);ctx.stroke();
  }
 }
 for(let y=0;y<10;y++)for(let x=0;x<9;x++){
  const p=board[y][x];if(!p)continue;
  const px=L+x*DX,py=T+y*DY;
  ctx.beginPath();ctx.arc(px+1,py+2,27,0,Math.PI*2);
  ctx.fillStyle='#7e4a25';ctx.fill();
  ctx.beginPath();ctx.arc(px,py,25,0,Math.PI*2);
  ctx.fillStyle='#f3d9a1';ctx.fill();
  ctx.lineWidth=3;ctx.strokeStyle=side(p)==='r'?'#a7271d':'#30221a';ctx.stroke();
  ctx.lineWidth=1;ctx.beginPath();ctx.arc(px,py,20,0,Math.PI*2);
  ctx.strokeStyle='#b68a4b';ctx.stroke();
  ctx.fillStyle=side(p)==='r'?'#b62920':'#29211c';
  ctx.font='bold 29px serif';ctx.textAlign='center';ctx.textBaseline='middle';
  ctx.fillText(chars[p],px,py+1);
 }
}
function beep(freq=430,dur=.09){
 if(!soundOn)return;
 try{
  audio=audio||new(window.AudioContext||window.webkitAudioContext)();
  const o=audio.createOscillator(),g=audio.createGain();
  o.frequency.value=freq;g.gain.value=volume*.12;
  o.connect(g);g.connect(audio.destination);o.start();
  g.gain.exponentialRampToValueAtTime(.001,audio.currentTime+dur);
  o.stop(audio.currentTime+dur);
 }catch(e){}
}
function updateStatus(){
 document.getElementById('status').textContent=
 turn==='r'?'Lượt Đỏ':'Lượt Đen';
}
function playMove(y,x,ny,nx){
 history.push({board:clone(board),turn});
 const captured=board[ny][nx];
 board[ny][nx]=board[y][x];board[y][x]=null;
 selected=null;moves=[];hintMove=null;turn=turn==='r'?'b':'r';
 beep(captured?650:420);
 drawBoard();updateStatus();
 const next=allMoves(board,turn);
 if(next.length===0){
  finish(turn==='r'?'b':'r');return;
 }
 if(mode!=='human'&&turn==='b'&&!ended)setTimeout(botMove,300);
}
function boardClick(e){
 if(ended||(mode!=='human'&&turn==='b'))return;
 const rect=canvas.getBoundingClientRect();
 const px=(e.clientX-rect.left)*canvas.width/rect.width;
 const py=(e.clientY-rect.top)*canvas.height/rect.height;
 const x=Math.round((px-L)/DX),y=Math.round((py-T)/DY);
 if(!inside(y,x))return;
 if(selected&&moves.some(q=>q[0]===y&&q[1]===x)){
  playMove(selected[0],selected[1],y,x);return;
 }
 if(board[y][x]&&side(board[y][x])===turn){
  selected=[y,x];moves=legal(board,y,x);
 }else{selected=null;moves=[]}
 drawBoard();
}
canvas.addEventListener('click',boardClick);
function botMove(){
 if(ended||turn!=='b')return;
 const ms=allMoves(board,'b');
 if(!ms.length){finish('r');return}
 let best=ms[0],bestScore=-Infinity;
 for(const m of ms){
  const captured=board[m.ny][m.nx];
  let score=(vals[captured]||0)*1.4+Math.random()*20;
  const nb=clone(board);nb[m.ny][m.nx]=nb[m.y][m.x];nb[m.y][m.x]=null;
  if(inCheck(nb,'r'))score+=mode==='expert'?120:mode==='hard'?70:30;
  if(mode==='easy')score=Math.random()*100;
  if(mode==='medium')score+=Math.random()*40;
  if(mode==='hard')score+=Math.random()*15;
  if(score>bestScore){bestScore=score;best=m}
 }
 playMove(best.y,best.x,best.ny,best.nx);
}
function finish(winner){
 ended=true;selected=null;moves=[];hintMove=null;drawBoard();
 document.getElementById('resultTitle').textContent=
 winner==='r'?'ĐỎ CHIẾN THẮNG!':'ĐEN CHIẾN THẮNG!';
 document.getElementById('resultText').textContent='Ván đấu đã kết thúc.';
 document.getElementById('resultOverlay').classList.remove('hidden');
}
function newGame(){
 board=initialBoard();turn='r';selected=null;moves=[];history=[];
 ended=false;hintMove=null;
 document.getElementById('resultOverlay').classList.add('hidden');
 drawBoard();updateStatus();
}
function startGame(m){
 mode=m;
 document.getElementById('home').classList.add('hidden');
 document.getElementById('difficulty').classList.add('hidden');
 document.getElementById('game').classList.remove('hidden');
 const labels={human:'ĐẤU HAI NGƯỜI',easy:'ĐẤU MÁY • DỄ',
 medium:'ĐẤU MÁY • TRUNG BÌNH',hard:'ĐẤU MÁY • KHÓ',expert:'ĐẤU MÁY • SIÊU KHÓ'};
 document.getElementById('modeLabel').textContent=labels[m];
 newGame();
}
function goHome(){
 document.getElementById('game').classList.add('hidden');
 document.getElementById('home').classList.remove('hidden');
 document.getElementById('resultOverlay').classList.add('hidden');
}
function showDifficulty(){document.getElementById('difficulty').classList.remove('hidden')}
function hideDifficulty(){document.getElementById('difficulty').classList.add('hidden')}
function openDialog(id){document.getElementById(id).classList.remove('hidden')}
function closeDialog(id){document.getElementById(id).classList.add('hidden')}
function undoMove(){
 if(!history.length||ended)return;
 let n=mode==='human'?1:Math.min(2,history.length);
 while(n--&&history.length){
  const h=history.pop();board=clone(h.board);turn=h.turn;
 }
 selected=null;moves=[];hintMove=null;drawBoard();updateStatus();
}
function hint(){
 if(ended)return;
 const ms=allMoves(board,turn);if(!ms.length)return;
 let best=ms[0],score=-Infinity;
 for(const m of ms){
  let v=(vals[board[m.ny][m.nx]]||0)+Math.random()*10;
  if(v>score){score=v;best=m}
 }
 hintMove=best;drawBoard();
 setTimeout(()=>{hintMove=null;drawBoard()},2200);
}
function resign(){if(!ended)finish(turn==='r'?'b':'r')}
function toggleMusic(on){
 musicOn=on;
 if(musicTimer){clearInterval(musicTimer);musicTimer=null}
 if(!on)return;
 try{
  audio=audio||new(window.AudioContext||window.webkitAudioContext)();
  const notes=[261.6,329.6,392,329.6,293.7,349.2,392,349.2];let i=0;
  musicTimer=setInterval(()=>{
   if(!musicOn||!audio)return;
   const o=audio.createOscillator(),g=audio.createGain();
   o.type='sine';o.frequency.value=notes[i++%notes.length];
   g.gain.value=volume*.025;o.connect(g);g.connect(audio.destination);
   o.start();g.gain.exponentialRampToValueAtTime(.001,audio.currentTime+.32);
   o.stop(audio.currentTime+.33);
  },480);
 }catch(e){}
}
function changeLanguage(v){
 lang=v;
 if(v==='en'){
  document.querySelector('h1').textContent='XIANGQI';
  document.querySelector('.subtitle').textContent='Strategy • Focus • Challenge';
 }else{
  document.querySelector('h1').textContent='CỜ TƯỚNG';
  document.querySelector('.subtitle').textContent='Khai cuộc • Đối trí • Phá thế cờ';
 }
}
board=initialBoard();drawBoard();
</script>
</body>
</html>
"""

components.html(HTML, height=1900, scrolling=True)

