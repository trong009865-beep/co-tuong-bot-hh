
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cờ Tướng", page_icon="♟️", layout="wide")

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box}
body{margin:0;background:#1b100b;color:#fff0d4;font-family:Arial,sans-serif}
button,select,input{font:inherit}
button{cursor:pointer}
#app{
 min-height:100vh;padding:20px;
 background:
 radial-gradient(ellipse at 50% 0%,#75432655,transparent 55%),
 repeating-linear-gradient(100deg,#28160f,#351c12 45px,#29160f 90px);
}
.top{max-width:1100px;margin:auto;display:flex;justify-content:space-between;align-items:center}
.brand{font-weight:900;font-size:24px;color:#f2ce8b}
.btn{background:#4b2919;color:#ffedcf;border:1px solid #bc8b4a;border-radius:10px;padding:11px 15px;font-weight:bold}
.btn:hover{filter:brightness(1.2)}
.primary{background:linear-gradient(135deg,#f3d18c,#bd8139);color:#29170c;border:0}
#home{
 max-width:700px;margin:9vh auto 0;text-align:center;padding:38px 22px;
 background:linear-gradient(145deg,#452719f5,#1b110cf7);
 border:2px solid #bd8c4b;border-radius:20px;
 box-shadow:0 18px 60px #0009;
}
h1{font-size:clamp(42px,8vw,70px);color:#f3d18c;margin:0 0 25px;text-shadow:0 3px 12px #000}
.menu{display:grid;gap:12px;max-width:350px;margin:auto}
.menu button{padding:15px;font-size:17px}
.small{font-size:13px;line-height:1.6;color:#d8c1a2}
#game{display:none;max-width:1100px;margin:25px auto}
.gamegrid{display:grid;grid-template-columns:minmax(280px,620px) minmax(220px,1fr);gap:20px;align-items:start}
.panel{background:#24170ff2;border:1px solid #956738;border-radius:15px;padding:15px}
.status{display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;color:#f3d18c;margin-bottom:12px;font-weight:bold}
#board{
 width:100%;max-width:620px;margin:auto;aspect-ratio:8/9;
 display:grid;grid-template-columns:repeat(9,minmax(0,1fr));
 grid-template-rows:repeat(10,minmax(0,1fr));
 background:#e8c58a;border:3px solid #6a3a1b;
 box-shadow:0 8px 25px #0009;overflow:hidden;
}
.cell{position:relative;min-width:0;min-height:0;display:flex;align-items:center;justify-content:center;border-right:1px solid #70421f;border-bottom:1px solid #70421f}
.cell:nth-child(9n){border-right:0}
.cell:nth-last-child(-n+9){border-bottom:0}
.cell.selected{background:#ffe68b}
.cell.legal:before{content:"";position:absolute;width:28%;height:28%;left:36%;top:36%;border-radius:50%;background:#287b37aa;z-index:1}
.piece{
 position:relative;z-index:2;width:86%;height:86%;display:flex;
 align-items:center;justify-content:center;border-radius:50%;
 font-family:"Noto Serif",serif;font-size:clamp(15px,3.3vw,29px);
 font-weight:900;background:radial-gradient(circle at 35% 25%,#fff0c7,#d6a75c 70%,#88572a);
 border:2px solid #6e421f;box-shadow:0 2px 4px #0007;cursor:pointer;user-select:none
}
.piece.red{color:#b32218;border-color:#b32218}
.piece.black{color:#28211b;border-color:#28211b}
.cell.selected .piece{box-shadow:0 0 0 3px #fff36a,0 2px 4px #0007}
#side h3{color:#f3d18c;margin:4px 0 12px}
#side .btn{width:100%;margin:5px 0}
#message{min-height:42px;padding:10px;background:#ffffff10;border-radius:8px;line-height:1.5;margin:8px 0}
#history{max-height:160px;overflow:auto;white-space:pre-line;font-size:13px;line-height:1.8;color:#e5d3b8}
#settings,#rules{display:none;max-width:600px;margin:25px auto;padding:22px;background:#24170ff5;border:1px solid #bd8c4b;border-radius:15px}
.settingrow{display:flex;justify-content:space-between;align-items:center;gap:12px;margin:17px 0}
select{max-width:60%;padding:8px;border-radius:7px}
input[type=range]{max-width:55%}
@media(max-width:720px){
 #app{padding:12px}
 #home{margin-top:6vh;padding:27px 15px}
 .gamegrid{grid-template-columns:1fr}
 #side{display:grid;grid-template-columns:1fr 1fr;gap:5px}
 #side h3,#message,#history{grid-column:1/-1}
 #side .btn{margin:2px 0;padding:10px 4px;font-size:13px}
 .piece{font-size:clamp(13px,4.5vw,25px)}
}
</style>
</head>
<body>
<div id="app">
 <div class="top">
  <div class="brand">♟ CỜ TƯỚNG</div>
  <button class="btn" onclick="showSettings()">⚙ Cài đặt</button>
 </div>

 <section id="home">
  <h1>CỜ TƯỚNG</h1>
  <div class="menu">
   <button class="btn primary" onclick="startGame('bot')">🤖 Đấu với máy</button>
   <button class="btn" onclick="startGame('two')">♟ Hai người chơi</button>
   <button class="btn" onclick="showRules()">📖 Luật chơi</button>
  </div>
 </section>

 <section id="settings">
  <h2>⚙ Cài đặt</h2>
  <div class="settingrow"><label>Ngôn ngữ</label>
   <select id="language" onchange="setLanguage(this.value)">
    <option value="vi">Tiếng Việt</option><option value="en">English</option>
   </select>
  </div>
  <div class="settingrow"><label>Độ khó của máy</label>
   <select id="difficulty">
    <option value="0">Dễ</option><option value="1" selected>Trung bình</option>
    <option value="2">Khó</option><option value="3">Siêu khó</option>
   </select>
  </div>
  <div class="settingrow"><label>Âm thanh nước đi</label><input id="sound" type="checkbox" checked></div>
  <div class="settingrow"><label>Nhạc nền</label><input id="music" type="checkbox" onchange="toggleMusic(this.checked)"></div>
  <div class="settingrow"><label>Âm lượng</label><input id="volume" type="range" min="0" max="100" value="35"></div>
  <button class="btn primary" onclick="hideSettings()">Xong</button>
 </section>

 <section id="rules">
  <h2>📖 Luật chơi cờ tướng</h2>
  <p><b>Tướng:</b> đi ngang hoặc dọc một bước trong cung.</p>
  <p><b>Sĩ:</b> đi chéo một bước trong cung.</p>
  <p><b>Tượng:</b> đi chéo hai điểm, không qua sông, không bị cản mắt.</p>
  <p><b>Xe:</b> đi ngang hoặc dọc, không nhảy qua quân.</p>
  <p><b>Pháo:</b> đi như xe; khi ăn phải nhảy qua đúng một quân.</p>
  <p><b>Mã:</b> đi kiểu chữ L; không đi được nếu bị cản chân.</p>
  <p><b>Tốt:</b> đi thẳng về phía trước; qua sông được đi ngang, không đi lùi.</p>
  <p>Không được để tướng của mình bị chiếu.</p>
  <button class="btn primary" onclick="hideRules()">Quay lại</button>
 </section>

 <section id="game">
  <div class="gamegrid">
   <div class="panel">
    <div class="status"><span id="turn">Lượt: Đỏ</span><span id="mode">Đấu với máy</span></div>
    <div id="board"></div>
   </div>
   <div class="panel" id="side">
    <h3>Điều khiển trận đấu</h3>
    <div id="message">Chọn quân của bạn để đi.</div>
    <button class="btn" onclick="hint()">💡 Gợi ý</button>
    <button class="btn" onclick="undo()">↩ Đi lại</button>
    <button class="btn" onclick="newGame()">⟳ Chơi mới</button>
    <button class="btn" onclick="resign()">🏳 Xin thua</button>
    <button class="btn" onclick="goHome()">⌂ Màn hình chính</button>
    <h3>Lịch sử nước đi</h3>
    <div id="history">Chưa có nước đi.</div>
    <p class="small">Chọn quân, sau đó chọn ô đích được đánh dấu.</p>
  </div>
 </div>
</div>

<script>
const $=id=>document.getElementById(id);
let mode='',board=[],turn='r',selected=null,legal=[],history=[],snapshots=[],ended=false;
let audioCtx=null,musicTimer=null;
let lang='vi';
const labels={
 vi:{red:'Đỏ',black:'Đen',bot:'Đấu với máy',two:'Hai người chơi',choose:'Chọn quân của bạn để đi.',thinking:'Máy đang suy nghĩ...',check:'Chiếu tướng!',hint:'Nước gợi ý: ',none:'Không có nước đi gợi ý.',empty:'Chưa có nước đi.',win:'Thắng!',checkmate:'Chiếu bí! ',confirm:'Bạn muốn xin thua?',move:' đi ',settings:'Cài đặt',rules:'Luật chơi',home:'Màn hình chính',undo:'Đi lại'},
 en:{red:'Red',black:'Black',bot:'Play vs computer',two:'Two players',choose:'Select one of your pieces.',thinking:'Computer thinking...',check:'Check!',hint:'Suggested move: ',none:'No hint available.',empty:'No moves yet.',win:'You win!',checkmate:'Checkmate! ',confirm:'Do you want to resign?',move:' to ',settings:'Settings',rules:'Rules',home:'Home',undo:'Undo'}
};
function t(k){return labels[lang][k]||k}
const names={r:{K:'帥',A:'仕',E:'相',H:'傌',R:'俥',C:'炮',P:'兵'},b:{K:'將',A:'士',E:'象',H:'馬',R:'車',C:'砲',P:'卒'}};
const value={K:10000,A:20,E:25,H:45,R:90,C:50,P:15};

function setLanguage(v){
 lang=v;
 $('mode').textContent=mode==='bot'?t('bot'):t('two');
 $('turn').textContent=(turn==='r'?t('red'):t('black'));
 render();
}
function showSettings(){
 $('home').style.display='none';$('game').style.display='none';
 $('rules').style.display='none';$('settings').style.display='block';
}
function hideSettings(){
 $('settings').style.display='none';
 if(mode){$('game').style.display='block';$('home').style.display='none'}
 else $('home').style.display='block';
}
function showRules(){
 $('home').style.display='none';$('game').style.display='none';
 $('settings').style.display='none';$('rules').style.display='block';
}
function hideRules(){$('rules').style.display='none';$('home').style.display='block'}
function inside(r,c){return r>=0&&r<10&&c>=0&&c<9}
function clone(b){return b.map(row=>row.map(q=>q?{...q}:null))}
function fresh(){
 board=Array.from({length:10},()=>Array(9).fill(null));
 const back=['R','H','E','A','K','A','E','H','R'];
 for(let c=0;c<9;c++){board[0][c]={s:'b',p:back[c]};board[9][c]={s:'r',p:back[c]}}
 board[2][1]={s:'b',p:'C'};board[2][7]={s:'b',p:'C'};
 board[7][1]={s:'r',p:'C'};board[7][7]={s:'r',p:'C'};
 for(let c=0;c<9;c+=2){board[3][c]={s:'b',p:'P'};board[6][c]={s:'r',p:'P'}}
 turn='r';selected=null;legal=[];history=[];snapshots=[];ended=false;
 $('message').textContent=t('choose');render();
}
function startGame(m){
 mode=m;$('home').style.display='none';$('settings').style.display='none';
 $('rules').style.display='none';$('game').style.display='block';
 $('mode').textContent=m==='bot'?t('bot'):t('two');fresh();
}
function newGame(){if(confirm('Bắt đầu ván mới?'))fresh()}
function goHome(){
 if(!ended&&history.length&&!confirm('Về màn hình chính?'))return;
 mode='';$('game').style.display='none';$('home').style.display='block';
}
function resign(){
 if(!ended&&confirm(t('confirm'))){ended=true;$('message').textContent=t('win');}
}
function palace(s,r,c){return c>=3&&c<=5&&(s==='r'?r>=7&&r<=9:r>=0&&r<=2)}
function pseudo(b,r,c){
 const q=b[r][c];if(!q)return [];
 const {s,p}=q,enemy=s==='r'?'b':'r',out=[];
 const add=(rr,cc)=>{if(inside(rr,cc)&&(!b[rr][cc]||b[rr][cc].s===enemy))out.push([rr,cc])};
 if(p==='R'||p==='C'){
  for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let screen=false;
   for(let rr=r+dr,cc=c+dc;inside(rr,cc);rr+=dr,cc+=dc){
    if(p==='R'){
     if(!b[rr][cc])out.push([rr,cc]);
     else{if(b[rr][cc].s===enemy)out.push([rr,cc]);break}
    }else if(!screen){
     if(!b[rr][cc])out.push([rr,cc]);else screen=true;
    }else if(b[rr][cc]){
     if(b[rr][cc].s===enemy)out.push([rr,cc]);break;
    }
   }
  }
 }else if(p==='H'){
  const steps=[[-2,-1,-1,0],[-2,1,-1,0],[2,-1,1,0],[2,1,1,0],[-1,-2,0,-1],[1,-2,0,-1],[-1,2,0,1],[1,2,0,1]];
  for(const [dr,dc,br,bc] of steps)if(inside(r+br,c+bc)&&!b[r+br][c+bc])add(r+dr,c+dc);
 }else if(p==='E'){
  for(const [dr,dc] of [[-2,-2],[-2,2],[2,-2],[2,2]]){
   let rr=r+dr,cc=c+dc;
   if(!inside(rr,cc)||b[r+dr/2][c+dc/2])continue;
   if(s==='r'&&rr<5)continue;if(s==='b'&&rr>4)continue;add(rr,cc);
  }
 }else if(p==='A'){
  for(const [dr,dc] of [[-1,-1],[-1,1],[1,-1],[1,1]]){
   let rr=r+dr,cc=c+dc;if(palace(s,rr,cc))add(rr,cc);
  }
 }else if(p==='K'){
  for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let rr=r+dr,cc=c+dc;if(palace(s,rr,cc))add(rr,cc);
  }
  for(const dr of [-1,1])for(let rr=r+dr;inside(rr,c);rr+=dr){
   if(b[rr][c]){if(b[rr][c].p==='K'&&b[rr][c].s!==s)out.push([rr,c]);break}
  }
 }else if(p==='P'){
  add(r+(s==='r'?-1:1),c);
  if(s==='r'?r<=4:r>=5){add(r,c-1);add(r,c+1)}
 }
 return out;
}
function kingPos(b,s){
 for(let r=0;r<10;r++)for(let c=0;c<9;c++)if(b[r][c]?.s===s&&b[r][c].p==='K')return [r,c];
 return null;
}
function attacked(b,r,c,by){
 for(let rr=0;rr<10;rr++)for(let cc=0;cc<9;cc++)
  if(b[rr][cc]?.s===by&&pseudo(b,rr,cc).some(x=>x[0]===r&&x[1]===c))return true;
 return false;
}
function inCheck(b,s){
 const k=kingPos(b,s);if(!k)return true;
 return attacked(b,k[0],k[1],s==='r'?'b':'r');
}
function legalMoves(b,r,c){
 const q=b[r][c];if(!q)return [];
 return pseudo(b,r,c).filter(([rr,cc])=>{
  const nb=clone(b);nb[rr][cc]=nb[r][c];nb[r][c]=null;
  return !inCheck(nb,q.s);
 });
}
function allMoves(b,s){
 const a=[];
 for(let r=0;r<10;r++)for(let c=0;c<9;c++)
  if(b[r][c]?.s===s)for(const to of legalMoves(b,r,c))a.push({from:[r,c],to});
 return a;
}
function render(){
 const el=$('board');el.innerHTML='';
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  const cell=document.createElement('div');cell.className='cell';
  if(selected&&selected[0]===r&&selected[1]===c)cell.classList.add('selected');
  if(legal.some(x=>x[0]===r&&x[1]===c))cell.classList.add('legal');
  const q=board[r][c];
  if(q){const p=document.createElement('div');p.className='piece '+(q.s==='r'?'red':'black');p.textContent=names[q.s][q.p];cell.appendChild(p)}
  cell.addEventListener('click',()=>clickCell(r,c));el.appendChild(cell);
 }
 $('turn').textContent=(turn==='r'?t('red'):t('black'));
 $('history').textContent=history.length?history.map((m,i)=>(i+1)+'. '+m).join('\n'):t('empty');
}
function clickCell(r,c){
 if(ended||(mode==='bot'&&turn==='b'))return;
 const q=board[r][c];
 if(selected&&legal.some(x=>x[0]===r&&x[1]===c)){move(selected,[r,c]);return}
 if(q&&q.s===turn){selected=[r,c];legal=legalMoves(board,r,c);$('message').textContent=t('choose')}
 else{selected=null;legal=[]}
 render();
}
function move(from,to){
 if(ended)return;
 const [r,c]=from,[rr,cc]=to,q=board[r][c];
 if(!q)return;
 const captured=board[rr][cc];
 snapshots.push({board:clone(board),turn,history:history.slice()});
 board[rr][cc]=q;board[r][c]=null;
 history.push((q.s==='r'?'Đỏ':'Đen')+' '+names[q.s][q.p]+' '+String.fromCharCode(65+c)+(10-r)+' → '+String.fromCharCode(65+cc)+(10-rr)+(captured?' ×':''));
 turn=turn==='r'?'b':'r';selected=null;legal=[];
 playTone(captured?180:330,captured?.13:.07);
 if(inCheck(board,turn)){$('message').textContent=t('check');playTone(520,.1)}
 else $('message').textContent=t('choose');
 render();
 if(!allMoves(board,turn).length){ended=true;$('message').textContent=t('checkmate')+(turn==='r'?t('black'):t('red'));return}
 if(mode==='bot'&&turn==='b'){$('message').textContent=t('thinking');setTimeout(botTurn,350)}
}
function undo(){
 if(!snapshots.length||ended)return;
 if(mode==='bot'&&turn==='r'&&snapshots.length>=2)snapshots.pop();
 const s=snapshots.pop();board=s.board;turn=s.turn;history=s.history;
 selected=null;legal=[];$('message').textContent=t('choose');render();
}
function score(b,s){
 let total=0;
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  const q=b[r][c];if(!q)continue;
  let v=value[q.p]||10;
  if(q.p==='P')v+=(q.s==='r'?(6-r):(r-3))*1.5;
  total+=q.s===s?v:-v;
 }
 return total;
}
function botTurn(){
 if(ended||mode!=='bot'||turn!=='b')return;
 const ms=allMoves(board,'b');if(!ms.length){ended=true;return}
 const level=+$('difficulty').value;
 const ranked=ms.map(m=>{
  const b=clone(board),q=b[m.from[0]][m.from[1]],cap=b[m.to[0]][m.to[1]];
  b[m.to[0]][m.to[1]]=q;b[m.from[0]][m.from[1]]=null;
  let sc=score(b,'b')+(cap?(value[cap.p]||0)*.8:0);
  if(inCheck(b,'r'))sc+=10;
  sc+=(Math.random()-.5)*(level===0?35:level===1?18:level===2?7:2);
  return {m,sc};
 }).sort((a,b)=>b.sc-a.sc);
 let pick=ranked[0].m;
 if(level===0)pick=ranked[Math.floor(Math.random()*Math.min(6,ranked.length))].m;
 move(pick.from,pick.to);
}
function hint(){
 if(ended){$('message').textContent=t('none');return}
 const ms=allMoves(board,turn);if(!ms.length){$('message').textContent=t('none');return}
 let best=ms[0],bestScore=-Infinity;
 for(const m of ms){
  const b=clone(board),q=b[m.from[0]][m.from[1]],cap=b[m.to[0]][m.to[1]];
  b[m.to[0]][m.to[1]]=q;b[m.from[0]][m.from[1]]=null;
  const sc=score(b,turn)+(cap?(value[cap.p]||0):0);
  if(sc>bestScore){bestScore=sc;best=m}
 }
 selected=best.from;legal=legalMoves(board,...best.from);
 $('message').textContent=t('hint')+String.fromCharCode(65+best.from[1])+(10-best.from[0])+' → '+String.fromCharCode(65+best.to[1])+(10-best.to[0]);
 render();
}
function playTone(freq,duration){
 if(!$('sound').checked)return;
 try{
  audioCtx=audioCtx||new(window.AudioContext||window.webkitAudioContext)();
  const o=audioCtx.createOscillator(),g=audioCtx.createGain();
  o.type='sine';o.frequency.value=freq;
  g.gain.value=(+$('volume').value/100)*.12;
  o.connect(g);g.connect(audioCtx.destination);o.start();
  g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+duration);
  o.stop(audioCtx.currentTime+duration);
 }catch(e){}
}
function toggleMusic(on){
 if(!on){if(musicTimer){clearInterval(musicTimer);musicTimer=null}return}
 try{
  audioCtx=audioCtx||new(window.AudioContext||window.webkitAudioContext)();
  if(musicTimer)return;
  const notes=[196,247,294,247,220,262,330,262];let i=0;
  musicTimer=setInterval(()=>{
   if(!$('music').checked)return;
   const o=audioCtx.createOscillator(),g=audioCtx.createGain();
   o.type='sine';o.frequency.value=notes[i++%notes.length];
   g.gain.value=(+$('volume').value/100)*.018;
   o.connect(g);g.connect(audioCtx.destination);o.start();
   g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+.45);
   o.stop(audioCtx.currentTime+.46);
  },500);
 }catch(e){}
}
fresh();
</script>
</body>
</html>
"""

components.html(HTML, height=1400, scrolling=True)
