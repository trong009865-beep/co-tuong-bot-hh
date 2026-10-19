
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
    display:none !important;
}
.stApp {
    background: #100d0c;
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
*{box-sizing:border-box}
body{
 margin:0;background:#100d0c;color:#f7e8c3;
 font-family:Georgia,'Times New Roman',serif;
}
button{font:inherit;cursor:pointer}
#app{max-width:1050px;margin:auto;padding:14px}
.hero{
 min-height:250px;position:relative;overflow:hidden;
 border:1px solid #99723a;border-radius:18px;
 padding:27px 18px;text-align:center;
 background:
 radial-gradient(ellipse at 50% 110%,#9e3021 0%,transparent 48%),
 radial-gradient(circle at 12% 10%,#75451d 0%,transparent 32%),
 linear-gradient(135deg,#321512,#17100f 48%,#3b1714);
 box-shadow:0 8px 32px #0008;
}
.hero:before,.hero:after{
 content:"";position:absolute;width:180px;height:180px;
 border:1px solid #c49b53;border-radius:50%;opacity:.25;
 top:35px;left:-95px;
}
.hero:after{left:auto;right:-95px}
.kicker{letter-spacing:5px;color:#d6b36e;font-size:12px}
h1{font-size:clamp(36px,7vw,65px);margin:14px 0 4px;
 color:#f5d99a;text-shadow:0 3px 14px #000}
.subtitle{color:#d5b98b;font-size:14px;margin:8px 0 22px}
.gold{
 border:1px solid #c8a35a;color:#ffe5a5;
 background:linear-gradient(#774025,#421d18);
 border-radius:10px;padding:11px 16px;
 transition:.15s;box-shadow:0 3px 9px #0005;
}
.gold:hover{filter:brightness(1.25);transform:translateY(-1px)}
.secondary{background:#211816;border-color:#6d5234}
.menu{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));
 gap:12px;margin:16px 0}
.menu button{min-height:65px;font-size:17px}
.panel{
 background:linear-gradient(145deg,#241916,#171211);
 border:1px solid #6c4d30;border-radius:14px;
 padding:15px;margin:12px 0;
}
h2{font-size:23px;color:#efd093;margin:4px 0 12px}
h3{color:#e4c17c;margin:8px 0}
.small{font-size:13px;color:#b9a38b;line-height:1.6}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.row button{flex:1;min-width:105px}
#game{display:none}
#boardWrap{
 position:relative;max-width:650px;margin:12px auto;
 border:2px solid #b18a48;border-radius:8px;
 overflow:hidden;background:#d8ae70;
 box-shadow:0 8px 30px #0009;
}
canvas{display:block;width:100%;height:auto;touch-action:manipulation}
#overlay{
 display:none;position:absolute;inset:0;z-index:5;
 background:#120b0bea;align-items:center;justify-content:center;
 text-align:center;padding:18px;
}
#overlay.show{display:flex}
.overlaybox{
 width:min(420px,100%);border:1px solid #d2aa61;
 background:linear-gradient(145deg,#411a17,#160f0e);
 border-radius:16px;padding:24px;box-shadow:0 0 35px #000;
}
#result{font-size:clamp(32px,7vw,54px);color:#ffe3a0;
 font-weight:bold;margin:10px 0 18px}
#status{color:#f1d39b;font-size:15px}
#thinking{color:#b9a38b;font-size:12px;min-height:18px}
#settings,#modePanel,#rulesPanel{display:none}
#settings.show,#modePanel.show,#rulesPanel.show{display:block}
input[type=range]{accent-color:#d2a454;width:100%}
select{background:#241916;color:#f8e7bf;padding:9px;border-radius:8px;
 border:1px solid #886a3c;width:100%}
footer{padding:14px;text-align:center;color:#8f7861;font-size:12px}
@media(max-width:520px){
 #app{padding:8px}
 .hero{padding:22px 10px;min-height:220px}
 .menu{gap:8px}
 .menu button{font-size:15px;padding:10px 6px}
 .panel{padding:11px}
}
</style>
</head>
<body>
<div id="app">
 <section id="home">
  <div class="hero">
   <div class="kicker">東方棋藝 · KỲ ĐẠO</div>
   <h1>象棋</h1>
   <div style="font-size:22px;color:#f0d49b">CỜ TƯỚNG</div>
   <div class="subtitle">Một bàn cờ · Vạn thế biến hóa</div>
   <button class="gold" onclick="openModes()">⚔ BẮT ĐẦU TRẬN ĐẤU</button>
  </div>
  <div class="menu">
   <button class="gold" onclick="openModes()">♟ Đấu với máy</button>
   <button class="gold secondary" onclick="startGame('human',2)">♟ Đấu hai người</button>
   <button class="gold secondary" onclick="togglePanel('rulesPanel')">📜 Luật chơi</button>
   <button class="gold secondary" onclick="togglePanel('settings')">⚙ Cài đặt</button>
  </div>
  <div id="modePanel" class="panel">
   <h2>Chọn đối thủ</h2>
   <div class="small">Bạn cầm quân ĐEN và đi trước.</div>
   <div class="menu">
    <button class="gold" onclick="startGame('bot',1)">🌱 Dễ</button>
    <button class="gold" onclick="startGame('bot',2)">⚔ Trung bình</button>
    <button class="gold" onclick="startGame('bot',3)">🔥 Khó</button>
    <button class="gold" onclick="startGame('bot',4)">👑 Siêu khó</button>
   </div>
   <button class="gold secondary" onclick="togglePanel('modePanel')">Quay lại</button>
  </div>
  <div id="rulesPanel" class="panel">
   <h2>Luật cờ tướng</h2>
   <p class="small">
    • Mỗi lượt đi một quân theo đúng luật của quân đó.<br>
    • Tướng không được đi vào ô đang bị đối phương tấn công.<br>
    • Hai Tướng không được nhìn thẳng mặt nhau khi không có quân chắn.<br>
    • Khi bị chiếu, phải thoát chiếu bằng một nước hợp lệ.<br>
    • Nếu đến lượt mà không có nước hợp lệ, ván đấu kết thúc.
   </p>
   <button class="gold secondary" onclick="togglePanel('rulesPanel')">Đóng</button>
  </div>
  <div id="settings" class="panel">
   <h2>⚙ Cài đặt</h2>
   <label class="small">Âm lượng hiệu ứng</label>
   <input id="volume" type="range" min="0" max="100" value="45">
   <p class="small">Âm thanh hiện chỉ dùng cho các hiệu ứng được hỗ trợ trong bản này.</p>
   <button class="gold secondary" onclick="togglePanel('settings')">Đóng</button>
  </div>
 </section>

 <section id="game">
  <div class="row" style="justify-content:space-between">
   <button class="gold secondary" onclick="openSettingsGame()">⚙ Cài đặt</button>
   <div style="text-align:center">
    <div style="color:#efd093;font-size:20px">KỲ ĐẠO</div>
    <div class="small" id="modeLabel">Đấu với máy</div>
   </div>
   <button class="gold secondary" onclick="goHome()">⌂ Trang chủ</button>
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
      <button class="gold" onclick="newGame()">Chơi lại</button>
      <button class="gold secondary" onclick="goHome()">Trang chủ</button>
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
  <div id="gameSettings" class="panel" style="display:none">
   <h2>Cài đặt trận đấu</h2>
   <p class="small">Chọn tiếp tục hoặc trở về màn hình chính.</p>
   <div class="row">
    <button class="gold" onclick="closeSettingsGame()">Tiếp tục</button>
    <button class="gold secondary" onclick="goHome()">Trang chủ</button>
   </div>
  </div>
 </section>
 <footer>KỲ ĐẠO · Cờ tướng dành cho người yêu chiến thuật</footer>
</div>
<script>
const canvas=document.getElementById('board');
const ctx=canvas.getContext('2d');
const NAMES={K:'將',A:'士',E:'象',H:'馬',R:'車',C:'炮',P:'卒',
             k:'帥',a:'仕',e:'相',h:'傌',r:'俥',c:'砲',p:'兵'};
const VALUE={K:10000,A:20,E:22,H:45,R:90,C:48,P:12};
let board,turn='B',selected=null,legal=[],history=[];
let mode='bot',level=2,ended=false,hint=null,locked=false;
let cell=60,ox=60,oy=30;

function initialBoard(){
 const b=Array.from({length:10},()=>Array(9).fill(null));
 const back=['R','H','E','A','K','A','E','H','R'];
 for(let c=0;c<9;c++){
  b[0][c]=back[c];b[9][c]=back[c].toLowerCase();
  b[2][c]=null;b[7][c]=null;
 }
 b[2][1]='C';b[2][7]='C';
 b[7][1]='c';b[7][7]='c';
 for(let c=0;c<9;c+=2){b[3][c]='P';b[6][c]='p';}
 return b;
}
function inside(r,c){return r>=0&&r<10&&c>=0&&c<9}
function side(p){return !p?null:(p===p.toUpperCase()?'R':'B')}
function copyBoard(b){return b.map(row=>row.slice())}
function palace(s,r,c){
 return c>=3&&c<=5&&(s==='R'?r>=0&&r<=2:r>=7&&r<=9);
}
function river(s,r){return s==='R'?r>=5:r<=4}
function clearPath(r,c,nr,nc,b){
 let dr=Math.sign(nr-r),dc=Math.sign(nc-c),n=0;
 let y=r+dr,x=c+dc;
 while(y!==nr||x!==nc){
  if(b[y][x])n++;
  y+=dr;x+=dc;
 }
 return n;
}
function pseudo(r,c,b){
 const p=b[r][c];if(!p)return [];
 const s=side(p),t=p.toUpperCase(),out=[];
 function add(nr,nc){
  if(!inside(nr,nc))return;
  if(side(b[nr][nc])===s)return;
  out.push([nr,nc]);
 }
 if(t==='K'){
  for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let nr=r+dr,nc=c+dc;
   if(palace(s,nr,nc))add(nr,nc);
  }
  // Flying general: capture the opposing general on the same open file.
  for(let d of [-1,1]){
   for(let nr=r+d;inside(nr,c);nr+=d){
    if(b[nr][c]){
     if(b[nr][c].toUpperCase()==='K'&&side(b[nr][c])!==s)add(nr,c);
     break;
    }
   }
  }
 }else if(t==='A'){
  for(const [dr,dc] of [[1,1],[1,-1],[-1,1],[-1,-1]]){
   let nr=r+dr,nc=c+dc;if(palace(s,nr,nc))add(nr,nc);
  }
 }else if(t==='E'){
  for(const [dr,dc] of [[2,2],[2,-2],[-2,2],[-2,-2]]){
   let nr=r+dr,nc=c+dc;
   if(!inside(nr,nc)||b[r+dr/2][c+dc/2])continue;
   if(s==='R'&&nr>4)continue;
   if(s==='B'&&nr<5)continue;
   add(nr,nc);
  }
 }else if(t==='H'){
  const steps=[
   [-2,-1,-1,0],[-2,1,-1,0],[2,-1,1,0],[2,1,1,0],
   [-1,-2,0,-1],[1,-2,0,-1],[-1,2,0,1],[1,2,0,1]
  ];
  for(const [dr,dc,lr,lc] of steps){
   if(inside(r+dr,c+dc)&&!b[r+lr][c+lc])add(r+dr,c+dc);
  }
 }else if(t==='R'||t==='C'){
  for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let nr=r+dr,nc=c+dc,screen=false;
   while(inside(nr,nc)){
    if(t==='R'){
     if(!b[nr][nc])out.push([nr,nc]);
     else{if(side(b[nr][nc])!==s)out.push([nr,nc]);break;}
    }else{
     if(!screen){if(!b[nr][nc])out.push([nr,nc]);else screen=true;}
     else if(b[nr][nc]){
      if(side(b[nr][nc])!==s)out.push([nr,nc]);
      break;
     }
    }
    nr+=dr;nc+=dc;
   }
  }
 }else if(t==='P'){
  let dr=s==='R'?1:-1;
  add(r+dr,c);
  if(river(s,r)){add(r,c-1);add(r,c+1);}
 }
 return out;
}
function findKing(s,b){
 const k=s==='R'?'K':'k';
 for(let r=0;r<10;r++)for(let c=0;c<9;c++)if(b[r][c]===k)return [r,c];
 return null;
}
function attacked(r,c,by,b){
 for(let y=0;y<10;y++)for(let x=0;x<9;x++){
  if(side(b[y][x])===by){
   if(pseudo(y,x,b).some(m=>m[0]===r&&m[1]===c))return true;
  }
 }
 return false;
}
function inCheck(s,b){
 const k=findKing(s,b);
 if(!k)return true;
 return attacked(k[0],k[1],s==='R'?'B':'R',b);
}
function apply(b,from,to){
 const n=copyBoard(b);n[to[0]][to[1]]=n[from[0]][from[1]];
 n[from[0]][from[1]]=null;return n;
}
function legalFor(r,c,b){
 const s=side(b[r][c]);if(!s)return [];
 return pseudo(r,c,b).filter(to=>{
  const n=apply(b,[r,c],to);
  return !inCheck(s,n);
 });
}
function allMoves(s,b){
 const a=[];
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  if(side(b[r][c])===s){
   for(const to of legalFor(r,c,b))a.push({from:[r,c],to});
  }
 }
 return a;
}
function evaluate(b){
 let score=0;
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  const p=b[r][c];if(!p)continue;
  const v=VALUE[p.toUpperCase()]||0;
  const progress=p.toUpperCase()==='P'?
   (side(p)==='R'?r:9-r)*1.5:0;
  score+=(side(p)==='R'?1:-1)*(v+progress);
 }
 return score;
}
function ordered(moves,b){
 return moves.sort((a,z)=>{
  const av=b[a.to[0]][a.to[1]]?VALUE[b[a.to[0]][a.to[1]].toUpperCase()]:0;
  const zv=b[z.to[0]][z.to[1]]?VALUE[b[z.to[0]][z.to[1]].toUpperCase()]:0;
  return zv-av;
 });
}
function search(b,depth,alpha,beta,sideToMove){
 if(depth===0)return evaluate(b);
 const moves=ordered(allMoves(sideToMove,b),b);
 if(!moves.length)return sideToMove==='R'?-99999:99999;
 if(sideToMove==='R'){
  let best=-Infinity;
  for(const m of moves){
   best=Math.max(best,search(apply(b,m.from,m.to),depth-1,alpha,beta,'B'));
   alpha=Math.max(alpha,best);if(beta<=alpha)break;
  }
  return best;
 }else{
  let best=Infinity;
  for(const m of moves){
   best=Math.min(best,search(apply(b,m.from,m.to),depth-1,alpha,beta,'R'));
   beta=Math.min(beta,best);if(beta<=alpha)break;
  }
  return best;
 }
}
function botMove(){
 if(ended||turn!=='R')return;
 locked=true;
 document.getElementById('thinking').textContent='Đang tính toán nước đi…';
 setTimeout(()=>{
  if(ended){locked=false;return;}
  const moves=ordered(allMoves('R',board),board);
  if(!moves.length){finish('B');return;}
  let chosen=moves[0];
  if(level===1){
   chosen=moves[Math.floor(Math.random()*Math.min(5,moves.length))];
  }else{
   let best=-Infinity;
   const depth=level===2?1:level===3?2:2;
   for(const m of moves){
    const n=apply(board,m.from,m.to);
    let v=search(n,depth-1,-Infinity,Infinity,'B');
    v+=Math.random()*0.15;
    if(v>best){best=v;chosen=m;}
   }
  }
  makeMove(chosen.from,chosen.to);
  locked=false;
 },80);
}
function draw(){
 const W=600,H=660;
 ctx.clearRect(0,0,W,H);
 ctx.fillStyle='#d7b174';ctx.fillRect(0,0,W,H);
 const left=36,right=564,top=30,bottom=630;
 ctx.strokeStyle='#57371c';ctx.lineWidth=1.5;
 for(let r=0;r<10;r++){
  const y=top+r*(bottom-top)/9;
  ctx.beginPath();ctx.moveTo(left,y);ctx.lineTo(right,y);ctx.stroke();
 }
 for(let c=0;c<9;c++){
  const x=left+c*(right-left)/8;
  ctx.beginPath();ctx.moveTo(x,top);ctx.lineTo(x,top+4*(bottom-top)/9);ctx.stroke();
  ctx.beginPath();ctx.moveTo(x,top+5*(bottom-top)/9);ctx.lineTo(x,bottom);ctx.stroke();
 }
 // Side edges are continuous.
 ctx.beginPath();ctx.moveTo(left,top);ctx.lineTo(left,bottom);
 ctx.moveTo(right,top);ctx.lineTo(right,bottom);ctx.stroke();
 function palace(c1,r1,c2,r2){
  ctx.beginPath();ctx.moveTo(left+c1*(right-left)/8,top+r1*(bottom-top)/9);
  ctx.lineTo(left+c2*(right-left)/8,top+r2*(bottom-top)/9);ctx.stroke();
 }
 palace(3,0,5,2);palace(5,0,3,2);
 palace(3,7,5,9);palace(5,7,3,9);
 ctx.fillStyle='#795027';ctx.font='18px serif';ctx.textAlign='center';
 ctx.fillText('楚 河',210,top+4.5*(bottom-top)/9+7);
 ctx.fillText('漢 界',390,top+4.5*(bottom-top)/9+7);
 function pos(r,c){return [left+c*(right-left)/8,top+r*(bottom-top)/9]}
 if(selected){
  const [x,y]=pos(selected[0],selected[1]);
  ctx.fillStyle='#e8c45a55';ctx.beginPath();ctx.arc(x,y,25,0,Math.PI*2);ctx.fill();
 }
 for(const m of legal){
  const [x,y]=pos(m[0],m[1]);
  ctx.fillStyle=board[m[0]][m[1]]?'#9f2f22aa':'#3c6d37aa';
  ctx.beginPath();ctx.arc(x,y,board[m[0]][m[1]]?23:7,0,Math.PI*2);ctx.fill();
 }
 const king=findKing(turn,board);
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  const p=board[r][c];if(!p)continue;
  const [x,y]=pos(r,c),red=side(p)==='R';
  ctx.beginPath();ctx.arc(x,y,24,0,Math.PI*2);
  ctx.fillStyle='#f0d6a0';ctx.fill();
  ctx.lineWidth=red?3:2.5;ctx.strokeStyle=red?'#a22b20':'#29201a';ctx.stroke();
  ctx.beginPath();ctx.arc(x,y,19,0,Math.PI*2);
  ctx.lineWidth=1;ctx.strokeStyle=red?'#c15c40':'#6c5842';ctx.stroke();
  ctx.fillStyle=red?'#a51f19':'#28201a';
  ctx.font='bold 25px serif';ctx.textAlign='center';ctx.textBaseline='middle';
  ctx.fillText(NAMES[p],x,y+1);
 }
 if(king&&inCheck(turn,board)){
  const [x,y]=pos(king[0],king[1]);
  ctx.strokeStyle='#ff3025';ctx.lineWidth=4;
  ctx.beginPath();ctx.arc(x,y,29,0,Math.PI*2);ctx.stroke();
 }
 if(hint){
  const [x1,y1]=pos(hint.from[0],hint.from[1]);
  const [x2,y2]=pos(hint.to[0],hint.to[1]);
  ctx.strokeStyle='#00a8ff';ctx.lineWidth=4;
  ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();
  hint=null;
 }
}
function coordinates(e){
 const rect=canvas.getBoundingClientRect();
 const x=(e.clientX-rect.left)*600/rect.width;
 const y=(e.clientY-rect.top)*660/rect.height;
 const c=Math.round((x-36)/(528/8));
 const r=Math.round((y-30)/(600/9));
 return inside(r,c)?[r,c]:null;
}
canvas.addEventListener('click',e=>{
 if(ended||locked)return;
 if(mode==='bot'&&turn==='R')return;
 const at=coordinates(e);if(!at)return;
 const [r,c]=at;
 if(selected&&legal.some(m=>m[0]===r&&m[1]===c)){
  makeMove(selected,[r,c]);return;
 }
 if(side(board[r][c])===turn){
  selected=at;legal=legalFor(r,c,board);
 }else{selected=null;legal=[];}
 draw();
});
function makeMove(from,to){
 if(ended)return;
 history.push({board:copyBoard(board),turn});
 board=apply(board,from,to);turn=turn==='B'?'R':'B';
 selected=null;legal=[];hint=null;draw();updateStatus();
 const kingR=findKing('R',board),kingB=findKing('B',board);
 if(!kingR){finish('B');return;}
 if(!kingB){finish('R');return;}
 const moves=allMoves(turn,board);
 if(!moves.length){finish(turn==='R'?'B':'R');return;}
 if(mode==='bot'&&turn==='R')botMove();
}
function updateStatus(){
 let s=turn==='B'?'Đen':'Đỏ';
 let msg='Đến lượt '+s;
 if(inCheck(turn,board))msg+=' — ĐANG BỊ CHIẾU!';
 document.getElementById('status').textContent=msg;
 document.getElementById('thinking').textContent='';
}
function finish(winner){
 ended=true;locked=false;
 const win=(mode==='human')?
  (winner==='B'?'ĐEN CHIẾN THẮNG':'ĐỎ CHIẾN THẮNG'):
  (winner==='B'?'CHIẾN THẮNG':'THẤT BẠI');
 document.getElementById('result').textContent=win;
 document.getElementById('resultText').textContent=
  'Ván đấu đã kết thúc. Bạn có thể chơi lại hoặc trở về trang chủ.';
 document.getElementById('overlay').classList.add('show');
 document.getElementById('status').textContent='Ván đấu kết thúc';
}
function startGame(m,l){
 mode=m;level=l;newGame();
 document.getElementById('home').style.display='none';
 document.getElementById('game').style.display='block';
 document.getElementById('modeLabel').textContent=
  m==='human'?'Đấu hai người':
  'Đấu với máy · '+['','Dễ','Trung bình','Khó','Siêu khó'][l];
}
function newGame(){
 board=initialBoard();turn='B';selected=null;legal=[];
 history=[];ended=false;locked=false;hint=null;
 document.getElementById('overlay').classList.remove('show');
 document.getElementById('gameSettings').style.display='none';
 draw();updateStatus();
}
function goHome(){
 ended=true;locked=false;
 document.getElementById('game').style.display='none';
 document.getElementById('home').style.display='block';
 document.getElementById('overlay').classList.remove('show');
}
function openModes(){
 document.getElementById('modePanel').classList.add('show');
}
function togglePanel(id){
 document.getElementById(id).classList.toggle('show');
}
function openSettingsGame(){
 document.getElementById('gameSettings').style.display='block';
}
function closeSettingsGame(){
 document.getElementById('gameSettings').style.display='none';
}
function undoMove(){
 if(!history.length||ended)return;
 let n=mode==='bot'&&history.length>=2?2:1;
 while(n--&&history.length){
  const h=history.pop();board=h.board;turn=h.turn;
 }
 selected=null;legal=[];hint=null;draw();updateStatus();
}
function showHint(){
 if(ended||locked)return;
 const moves=allMoves(turn,board);
 if(!moves.length)return;
 let m=moves[Math.floor(Math.random()*moves.length)];
 if(mode==='bot'&&turn==='B'){
  let best=-Infinity;
  for(const x of moves){
   let v=search(apply(board,x.from,x.to),1,-Infinity,Infinity,'R');
   if(v>best){best=v;m=x;}
  }
 }
 hint={from:m.from,to:m.to};draw();
}
function surrender(){
 if(ended)return;
 finish(turn==='B'?'R':'B');
}
board=initialBoard();draw();updateStatus();
</script>
</body>
</html>
"""

components.html(HTML, height=1300, scrolling=True)

