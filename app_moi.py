
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cờ Tướng",
    page_icon="♟️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu, footer, header, [data-testid="stToolbar"],
[data-testid="stDecoration"] {visibility:hidden;}
.block-container {padding:0 !important; max-width:100% !important;}
iframe {border:0 !important;}
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
body{margin:0;color:#f9e8c4;background:#21120e;
font-family:Georgia,'Times New Roman',serif}
button{cursor:pointer;font-family:inherit;transition:.2s}
button:hover{filter:brightness(1.15);transform:translateY(-1px)}
.page{max-width:1050px;margin:auto;padding:20px}
.panel{background:linear-gradient(145deg,#51281c,#29150f);
border:1px solid #bd8b45;border-radius:18px;padding:22px;
box-shadow:0 12px 35px #0007}
.hero{min-height:360px;display:flex;flex-direction:column;
align-items:center;justify-content:center;text-align:center;
background:linear-gradient(#190b08a8,#190b08d9),
radial-gradient(ellipse at top,#b56b27,#3c1a10 55%,#180b08);
border:2px solid #b88740;border-radius:22px;padding:35px}
.lantern{font-size:38px}
h1{font-size:clamp(38px,7vw,72px);color:#f7d27d;
letter-spacing:5px;margin:14px 0;text-shadow:0 4px 15px #000}
h2{color:#f7d27d;text-align:center}
.sub{color:#e9cba0;font-size:17px}
.btn{border:1px solid #e5bb6d;background:linear-gradient(#9d4c25,#642619);
color:#fff0cd;border-radius:10px;padding:13px 18px;font-size:17px;
font-weight:bold;width:100%;margin:5px 0}
.btn.secondary{background:#392019;border-color:#9e7847}
.btn.gold{background:linear-gradient(#e2bd70,#a36b2a);color:#29170d}
.modes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;
max-width:620px;width:100%;margin:18px auto}
.hidden{display:none!important}
.topbar{display:flex;align-items:center;justify-content:space-between;
gap:10px;flex-wrap:wrap;margin-bottom:12px}
.smallbtn{border:1px solid #bd8b45;border-radius:9px;background:#392019;
color:#ffe5b0;padding:10px 14px;font-size:15px}
.board-wrap{max-width:700px;margin:0 auto;position:relative}
#board{width:100%;display:block;border-radius:8px;
box-shadow:0 8px 25px #0009;touch-action:manipulation}
.tools{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));
gap:10px;margin-top:15px}
.tool{background:#392019;color:#ffe6b4;border:1px solid #9e7847;
border-radius:10px;padding:13px 5px;font-size:15px}
.status{text-align:center;padding:10px;color:#f7d27d;font-size:17px}
.overlay{position:absolute;inset:0;background:#160905e8;
border:2px solid #f1c66c;border-radius:8px;display:flex;
align-items:center;justify-content:center;text-align:center;padding:20px}
.overlay h2{font-size:clamp(32px,6vw,58px);margin:8px 0}
.overlay-inner{max-width:430px;width:100%}
.settings{margin-top:16px}
.settings label{display:block;margin:12px 0}
select,input{background:#24130f;color:#ffe8bd;border:1px solid #bd8b45;
border-radius:7px;padding:8px}
.note{color:#d7b994;font-size:13px;text-align:center;line-height:1.6}
@media(max-width:600px){
.page{padding:10px}.panel{padding:12px}.hero{min-height:300px;padding:20px}
.tools{grid-template-columns:repeat(2,minmax(0,1fr))}
.btn{padding:12px 8px;font-size:15px}.modes{gap:6px}
}
</style>
</head>
<body>
<div class="page">

<section id="home" class="panel">
 <div class="hero">
  <div class="lantern">🏮　♟️　🏮</div>
  <h1>CỜ TƯỚNG</h1>
  <p class="sub">Bàn cờ của trí tuệ và bản lĩnh</p>
  <div class="modes">
   <button class="btn gold" onclick="showModes()">⚔ Đấu với máy</button>
   <button class="btn" onclick="startGame('human')">♟ Đấu hai người</button>
   <button class="btn secondary" onclick="showRules()">📜 Luật chơi</button>
   <button class="btn secondary" onclick="showSettings()">⚙ Cài đặt</button>
  </div>
 </div>
 <div id="difficulty" class="hidden">
  <h2>CHỌN ĐỘ KHÓ</h2>
  <div class="modes">
   <button class="btn" onclick="startGame('easy')">🌱 Dễ</button>
   <button class="btn" onclick="startGame('medium')">🗡 Trung bình</button>
   <button class="btn" onclick="startGame('hard')">🔥 Khó</button>
   <button class="btn gold" onclick="startGame('expert')">👑 Siêu khó</button>
  </div>
  <button class="btn secondary" onclick="hideModes()">← Quay lại</button>
 </div>
 <div id="rules" class="hidden">
  <h2>LUẬT CHƠI CƠ BẢN</h2>
  <p>• Mỗi bên có một Tướng và các quân cờ khác.</p>
  <p>• Tướng đi từng bước trong cung; Xe đi ngang dọc.</p>
  <p>• Mã đi theo hình chữ L; Pháo ăn quân bằng cách nhảy qua một quân.</p>
  <p>• Tốt đi thẳng, sau khi qua sông có thể đi ngang.</p>
  <button class="btn secondary" onclick="hideRules()">← Quay lại</button>
 </div>
 <div id="homeSettings" class="settings hidden">
  <h2>CÀI ĐẶT</h2>
  <label>Âm thanh <input id="soundHome" type="checkbox" checked onchange="soundOn=this.checked"></label>
  <label>Nhạc nền <input id="musicHome" type="checkbox" onchange="toggleMusic(this.checked)"></label>
  <label>Âm lượng <input type="range" min="0" max="100" value="35" onchange="volume=this.value/100"></label>
  <button class="btn secondary" onclick="hideSettings()">Đóng</button>
 </div>
</section>

<section id="game" class="panel hidden">
 <div class="topbar">
  <button class="smallbtn" onclick="openGameSettings()">⚙ Cài đặt</button>
  <strong id="modeLabel">CỜ TƯỚNG</strong>
  <button class="smallbtn" onclick="goHome()">⌂ Trang chủ</button>
 </div>
 <div id="status" class="status">Lượt Đỏ</div>
 <div class="board-wrap">
  <canvas id="board" width="680" height="760"></canvas>
  <div id="result" class="overlay hidden">
   <div class="overlay-inner">
    <div style="font-size:45px">🏆</div>
    <h2 id="resultTitle">CHIẾN THẮNG!</h2>
    <p id="resultText">Ván đấu đã kết thúc</p>
    <button class="btn gold" onclick="newGame()">↻ Chơi lại</button>
    <button class="btn secondary" onclick="goHome()">⌂ Về trang chủ</button>
   </div>
  </div>
 </div>
 <div class="tools">
  <button class="tool" onclick="hint()">💡 Gợi ý</button>
  <button class="tool" onclick="undoMove()">↶ Đi lại</button>
  <button class="tool" onclick="newGame()">⟳ Ván mới</button>
  <button class="tool" onclick="resign()">🏳 Đầu hàng</button>
 </div>
 <div id="gameSettings" class="settings hidden">
  <h2>CÀI ĐẶT VÁN ĐẤU</h2>
  <label>Âm thanh quân cờ <input id="soundGame" type="checkbox" checked onchange="soundOn=this.checked"></label>
  <label>Nhạc nền <input id="musicGame" type="checkbox" onchange="toggleMusic(this.checked)"></label>
  <label>Âm lượng <input type="range" min="0" max="100" value="35" onchange="volume=this.value/100"></label>
  <button class="btn secondary" onclick="closeGameSettings()">Tiếp tục</button>
  <button class="btn secondary" onclick="goHome()">Về trang chủ</button>
 </div>
 <p class="note">Bản thử nghiệm: bot và luật đi quân ở mức cơ bản. Hãy kiểm tra nước đi trước khi chơi.</p>
</section>
</div>

<script>
const canvas=document.getElementById('board');
const ctx=canvas.getContext('2d');
const LEFT=42, TOP=38, DX=74.5, DY=75.5;
let board=[], turn='r', selected=null, moves=[], history=[];
let mode='human', ended=false, soundOn=true, volume=.35;
let musicOn=false, audio=null, musicTimer=null, hintMove=null;
const names={K:'帥',A:'仕',E:'相',H:'傌',R:'俥',C:'炮',P:'兵',
 k:'將',a:'士',e:'象',h:'馬',r:'車',c:'砲',p:'卒'};
const value={K:10000,k:10000,R:900,r:900,C:450,c:450,
 H:400,h:400,E:200,e:200,A:200,a:200,P:100,p:100};

function freshBoard(){
 let b=Array.from({length:10},()=>Array(9).fill(null));
 const put=(y,x,p)=>b[y][x]=p;
 ['r','h','e','a','k','a','e','h','r'].forEach((p,x)=>put(0,x,p));
 put(2,1,'c');put(2,7,'c');
 [0,2,4,6,8].forEach(x=>put(3,x,'p'));
 ['R','H','E','A','K','A','E','H','R'].forEach((p,x)=>put(9,x,p));
 put(7,1,'C');put(7,7,'C');
 [0,2,4,6,8].forEach(x=>put(6,x,'P'));
 return b;
}
function clone(b){return b.map(r=>r.slice())}
function side(p){return p===p.toUpperCase()?'r':'b'}
function inside(y,x){return y>=0&&y<10&&x>=0&&x<9}
function palace(y,x,s){return x>=3&&x<=5&&(s==='r'?y>=7&&y<=9:y>=0&&y<=2)}
function river(y,s){return s==='r'?y<=4:y>=5}
function pathClear(b,y,x,ny,nx){
 let dy=Math.sign(ny-y),dx=Math.sign(nx-x),cy=y+dy,cx=x+dx,n=0;
 while(cy!==ny||cx!==nx){if(b[cy][cx])n++;cy+=dy;cx+=dx}
 return n;
}
function pseudo(b,y,x){
 let p=b[y][x];if(!p)return [];
 let s=side(p),t=p.toUpperCase(),out=[];
 const add=(ny,nx)=>{if(inside(ny,nx)&&(!b[ny][nx]||side(b[ny][nx])!==s))out.push([ny,nx])};
 if(t==='K'||t==='A'){
  let ds=t==='K'?[[1,0],[-1,0],[0,1],[0,-1]]:[[1,1],[1,-1],[-1,1],[-1,-1]];
  for(let [dy,dx] of ds){let ny=y+dy,nx=x+dx;if(palace(ny,nx,s))add(ny,nx)}
  if(t==='K'){
   for(let d of [-1,1]){let ny=y+d;while(inside(ny,x)){if(b[ny][x]){if(b[ny][x].toUpperCase()==='K'&&side(b[ny][x])!==s)out.push([ny,x]);break}ny+=d}}
  }
 }else if(t==='E'){
  for(let [dy,dx] of [[2,2],[2,-2],[-2,2],[-2,-2]]){
   let ny=y+dy,nx=x+dx,ey=y+dy/2,ex=x+dx/2;
   if(inside(ny,nx)&&!b[ey][ex]&&!river(ny,s))add(ny,nx);
  }
 }else if(t==='H'){
  for(let [dy,dx,by,bx] of [[-2,-1,-1,0],[-2,1,-1,0],[2,-1,1,0],[2,1,1,0],
   [-1,-2,0,-1],[1,-2,0,-1],[-1,2,0,1],[1,2,0,1]]){
   let ny=y+dy,nx=x+dx;if(inside(ny,nx)&&!b[y+by][x+bx])add(ny,nx);
  }
 }else if(t==='R'||t==='C'){
  for(let [dy,dx] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let ny=y+dy,nx=x+dx,screen=false;
   while(inside(ny,nx)){
    if(!b[ny][nx]){if(t==='R'||!screen)add(ny,nx)}
    else {if(!screen){if(t==='C')screen=true;else break}
      else {if(side(b[ny][nx])!==s)add(ny,nx);break}}
    ny+=dy;nx+=dx;
   }
  }
 }else if(t==='P'){
  let dy=s==='r'?-1:1;add(y+dy,x);
  if(river(y,s)){add(y,x-1);add(y,x+1)}
 }
 return out;
}
function kingPos(b,s){
 for(let y=0;y<10;y++)for(let x=0;x<9;x++)
  if(b[y][x]&&b[y][x].toUpperCase()==='K'&&side(b[y][x])===s)return [y,x];
 return null;
}
function attacked(b,y,x,bySide){
 for(let yy=0;yy<10;yy++)for(let xx=0;xx<9;xx++){
  let p=b[yy][xx];if(p&&side(p)===bySide){
   if(pseudo(b,yy,xx).some(q=>q[0]===y&&q[1]===x))return true;
  }
 }
 return false;
}
function inCheck(b,s){
 let k=kingPos(b,s);return !k||attacked(b,k[0],k[1],s==='r'?'b':'r');
}
function legal(b,y,x){
 let s=side(b[y][x]);
 return pseudo(b,y,x).filter(([ny,nx])=>{
  let nb=clone(b);nb[ny][nx]=nb[y][x];nb[y][x]=null;
  return !inCheck(nb,s);
 });
}
function allMoves(b,s){
 let a=[];
 for(let y=0;y<10;y++)for(let x=0;x<9;x++)
  if(b[y][x]&&side(b[y][x])===s)
   for(let [ny,nx] of legal(b,y,x))a.push({y,x,ny,nx});
 return a;
}
function drawBoard(){
 ctx.clearRect(0,0,680,760);
 ctx.fillStyle='#d8a45c';ctx.fillRect(12,10,656,740);
 ctx.fillStyle='#e8c27f';ctx.fillRect(20,18,640,724);
 ctx.strokeStyle='#4b2412';ctx.lineWidth=2;
 for(let x=0;x<9;x++){ctx.beginPath();ctx.moveTo(LEFT+x*DX,TOP);ctx.lineTo(LEFT+x*DX,TOP+9*DY);ctx.stroke()}
 for(let y=0;y<10;y++){
  ctx.beginPath();ctx.moveTo(LEFT,TOP+y*DY);ctx.lineTo(LEFT+8*DX,TOP+y*DY);ctx.stroke()
 }
 ctx.fillStyle='#613017';ctx.font='bold 23px serif';ctx.textAlign='center';
 ctx.fillText('楚 河',LEFT+2*DX,TOP+4.65*DY);
 ctx.fillText('漢 界',LEFT+6*DX,TOP+4.65*DY);
 ctx.strokeStyle='#4b2412';ctx.lineWidth=2;
 for(let y of [0,7]){
  ctx.beginPath();ctx.moveTo(LEFT+3*DX,TOP+y*DY);
  ctx.lineTo(LEFT+5*DX,TOP+(y+2)*DY);ctx.stroke();
  ctx.beginPath();ctx.moveTo(LEFT+5*DX,TOP+y*DY);
  ctx.lineTo(LEFT+3*DX,TOP+(y+2)*DY);ctx.stroke();
 }
 if(selected){
  ctx.fillStyle='#49a66b88';ctx.fillRect(LEFT+selected[1]*DX-22,TOP+selected[0]*DY-22,44,44);
  moves.forEach(([y,x])=>{ctx.beginPath();ctx.arc(LEFT+x*DX,TOP+y*DY,7,0,Math.PI*2);ctx.fillStyle='#347a3f';ctx.fill()});
 }
 if(hintMove){
  ctx.strokeStyle='#167b42';ctx.lineWidth=4;
  for(let [y,x] of [[hintMove.y,hintMove.x],[hintMove.ny,hintMove.nx]]){
   ctx.beginPath();ctx.arc(LEFT+x*DX,TOP+y*DY,25,0,Math.PI*2);ctx.stroke();
  }
 }
 for(let y=0;y<10;y++)for(let x=0;x<9;x++){
  let p=board[y][x];if(!p)continue;
  let px=LEFT+x*DX,py=TOP+y*DY;
  ctx.beginPath();ctx.arc(px,py,26,0,Math.PI*2);
  ctx.fillStyle='#f3d8a0';ctx.fill();ctx.lineWidth=3;
  ctx.strokeStyle=side(p)==='r'?'#b92f22':'#30241c';ctx.stroke();
  ctx.fillStyle=side(p)==='r'?'#bd2b20':'#29221c';
  ctx.font='bold 31px serif';ctx.textAlign='center';ctx.textBaseline='middle';
  ctx.fillText(names[p],px,py+1);
 }
}
function audioBeep(freq=400,dur=.08){
 if(!soundOn)return;
 try{audio=audio||new (window.AudioContext||window.webkitAudioContext)();
 let o=audio.createOscillator(),g=audio.createGain();
 o.frequency.value=freq;g.gain.value=volume*.12;o.connect(g);g.connect(audio.destination);
 o.start();g.gain.exponentialRampToValueAtTime(.001,audio.currentTime+dur);o.stop(audio.currentTime+dur);
 }catch(e){}
}
function setStatus(t){document.getElementById('status').textContent=t}
function movePiece(y,x,ny,nx){
 history.push({board:clone(board),turn});
 let taken=board[ny][nx];board[ny][nx]=board[y][x];board[y][x]=null;
 selected=null;moves=[];hintMove=null;audioBeep(taken?650:420,.09);
 turn=turn==='r'?'b':'r';
 if(taken&&taken.toUpperCase()==='K'){endGame(turn==='r'?'b':'r');return}
 let s=turn==='r'?'r':'b';
 let ms=allMoves(board,s);
 if(ms.length===0){endGame(s==='r'?'b':'r');return}
 setStatus(turn==='r'?'Lượt Đỏ':'Lượt Đen');
 drawBoard();
 if(mode!=='human'&&turn==='b'&&!ended)setTimeout(botMove,350);
}
function onBoardClick(e){
 if(ended|| (mode!=='human'&&turn==='b'))return;
 const rect=canvas.getBoundingClientRect();
 let x=Math.round(((e.clientX-rect.left)*canvas.width/rect.width-LEFT)/DX);
 let y=Math.round(((e.clientY-rect.top)*canvas.height/rect.height-TOP)/DY);
 if(!inside(y,x))return;
 if(selected&&moves.some(q=>q[0]===y&&q[1]===x)){
  movePiece(selected[0],selected[1],y,x);return;
 }
 if(board[y][x]&&side(board[y][x])===turn){
  selected=[y,x];moves=legal(board,y,x);drawBoard();
 }else{selected=null;moves=[];drawBoard()}
}
canvas.addEventListener('click',onBoardClick);
function botMove(){
 if(ended||turn!=='b')return;
 let ms=allMoves(board,'b');if(!ms.length){endGame('r');return}
 let best=[],bestScore=-1e9;
 ms.forEach(m=>{
  let score=Math.random()*40+(value[board[m.ny][m.nx]]||0)*1.3;
  let nb=clone(board);nb[m.ny][m.nx]=nb[m.y][m.x];nb[m.y][m.x]=null;
  if(inCheck(nb,'r'))score+=mode==='expert'?100:mode==='hard'?60:25;
  if(mode==='easy')score=Math.random()*100;
  if(mode==='medium')score+=Math.random()*35;
  if(mode==='hard')score+=Math.random()*15;
  if(score>bestScore){bestScore=score;best=[m]}else if(score===bestScore)best.push(m);
 });
 let m=best[Math.floor(Math.random()*best.length)];
 movePiece(m.y,m.x,m.ny,m.nx);
}
function endGame(winner){
 ended=true;selected=null;moves=[];drawBoard();
 document.getElementById('resultTitle').textContent=winner==='r'?'ĐỎ CHIẾN THẮNG!':'ĐEN CHIẾN THẮNG!';
 document.getElementById('resultText').textContent='Ván đấu đã kết thúc.';
 document.getElementById('result').classList.remove('hidden');
}
function newGame(){
 board=freshBoard();turn='r';selected=null;moves=[];history=[];ended=false;hintMove=null;
 document.getElementById('result').classList.add('hidden');
 document.getElementById('gameSettings').classList.add('hidden');
 setStatus('Lượt Đỏ');drawBoard();
}
function startGame(m){
 mode=m;document.getElementById('home').classList.add('hidden');
 document.getElementById('game').classList.remove('hidden');
 document.getElementById('modeLabel').textContent=
 m==='human'?'ĐẤU HAI NGƯỜI':'ĐẤU VỚI MÁY • '+({easy:'DỄ',medium:'TRUNG BÌNH',hard:'KHÓ',expert:'SIÊU KHÓ'}[m]);
 newGame();
}
function goHome(){
 document.getElementById('game').classList.add('hidden');
 document.getElementById('home').classList.remove('hidden');
}
function showModes(){document.getElementById('difficulty').classList.remove('hidden')}
function hideModes(){document.getElementById('difficulty').classList.add('hidden')}
function showRules(){document.getElementById('rules').classList.remove('hidden')}
function hideRules(){document.getElementById('rules').classList.add('hidden')}
function showSettings(){document.getElementById('homeSettings').classList.remove('hidden')}
function hideSettings(){document.getElementById('homeSettings').classList.add('hidden')}
function openGameSettings(){document.getElementById('gameSettings').classList.remove('hidden')}
function closeGameSettings(){document.getElementById('gameSettings').classList.add('hidden')}
function undoMove(){
 if(!history.length||ended)return;
 let n=(mode!=='human'&&history.length>=2)?2:1;
 while(n--&&history.length){let h=history.pop();board=clone(h.board);turn=h.turn}
 selected=null;moves=[];hintMove=null;
 setStatus(turn==='r'?'Lượt Đỏ':'Lượt Đen');drawBoard();
}
function hint(){
 if(ended)return;
 let s=turn,ms=allMoves(board,s);if(!ms.length)return;
 let best=ms[0],score=-1e9;
 ms.forEach(m=>{
  let sc=Math.random()*10+(value[board[m.ny][m.nx]]||0);
  if(sc>score){score=sc;best=m}
 });
 hintMove=best;drawBoard();
 setTimeout(()=>{hintMove=null;drawBoard()},2200);
}
function resign(){
 if(ended)return;
 endGame(turn==='r'?'b':'r');
}
function toggleMusic(on){
 musicOn=on;
 if(on){musicStart()}else{if(musicTimer){clearInterval(musicTimer);musicTimer=null}}
}
function musicStart(){
 if(!musicOn||musicTimer)return;
 try{
  audio=audio||new (window.AudioContext||window.webkitAudioContext)();
  let notes=[261.6,329.6,392,329.6,293.7,349.2,392,349.2],i=0;
  musicTimer=setInterval(()=>{
   if(!musicOn)return;
   let o=audio.createOscillator(),g=audio.createGain();
   o.type='sine';o.frequency.value=notes[i++%notes.length];
   g.gain.value=volume*.025;o.connect(g);g.connect(audio.destination);
   o.start();g.gain.exponentialRampToValueAtTime(.001,audio.currentTime+.35);
   o.stop(audio.currentTime+.36);
  },450);
 }catch(e){}
}
board=freshBoard();drawBoard();
</script>
</body>
</html>
"""

components.html(HTML, height=1700, scrolling=True)
