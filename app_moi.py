
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cờ Tướng",
    page_icon="♟️",
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
*{box-sizing:border-box}
body{margin:0;font-family:Arial,sans-serif;color:#fff;background:#17120e}
button,select,input{font:inherit}
button{cursor:pointer}
#app{min-height:100vh;padding:20px;background:
linear-gradient(135deg,rgba(15,12,9,.86),rgba(29,17,10,.66)),
url('https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=1800&q=85') center/cover fixed}
.top{display:flex;justify-content:space-between;align-items:center;gap:10px;max-width:1100px;margin:auto}
.brand{font-size:23px;font-weight:900;color:#ffd987}
.btn{border:1px solid #b98b51;background:#50351f;color:#fff;padding:11px 16px;border-radius:10px;font-weight:bold}
.btn:hover{filter:brightness(1.2)}
.primary{background:linear-gradient(135deg,#ffdf94,#c58a3e);color:#28170a;border:0}
#home{max-width:720px;margin:9vh auto 0;text-align:center;padding:30px 22px;background:rgba(17,12,8,.7);border:1px solid #8e653d;border-radius:22px;backdrop-filter:blur(7px)}
h1{font-size:clamp(38px,8vw,70px);margin:0 0 10px;color:#ffda91;text-shadow:0 3px 14px #000}
.subtitle{color:#eee0cd;font-size:17px;line-height:1.6}
.menu{display:grid;gap:12px;max-width:360px;margin:28px auto 0}
.menu button{font-size:17px;padding:15px}
#game{display:none;max-width:1100px;margin:24px auto}
.gamegrid{display:grid;grid-template-columns:minmax(280px,620px) minmax(220px,1fr);gap:22px;align-items:start}
.panel{background:rgba(24,16,10,.9);border:1px solid #8c6237;border-radius:15px;padding:15px}
.status{display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;margin-bottom:12px;color:#ffe0a2;font-weight:bold}
#board{width:100%;aspect-ratio:9/10;display:grid;grid-template-columns:repeat(9,1fr);grid-template-rows:repeat(10,1fr);position:relative;background:#e8bd79;border:5px solid #75431f;box-shadow:0 8px 28px #0009;touch-action:manipulation}
.cell{position:relative;display:flex;align-items:center;justify-content:center;min-width:0;min-height:0}
.cell:before{content:"";position:absolute;left:0;right:0;top:50%;height:1px;background:#74431f;z-index:0}
.cell:after{content:"";position:absolute;top:0;bottom:0;left:50%;width:1px;background:#74431f;z-index:0}
.cell:nth-child(9n+1):after{left:50%}
.cell.river:before{height:0}
.cell.selected{background:#ffe68b99}
.cell.legal:before{content:"";position:absolute;width:28%;height:28%;left:36%;top:36%;border-radius:50%;background:#267c36aa;z-index:1}
.piece{z-index:2;width:83%;height:83%;display:flex;align-items:center;justify-content:center;border-radius:50%;font-family:"Noto Serif",serif;font-size:clamp(15px,3.5vw,31px);font-weight:900;background:radial-gradient(circle at 35% 25%,#fff0c7,#d6a75c 70%,#88572a);border:2px solid #6e421f;box-shadow:0 2px 4px #0007;cursor:pointer;user-select:none}
.piece.red{color:#b32218;border-color:#b32218}
.piece.black{color:#28211b;border-color:#28211b}
.cell.selected .piece{box-shadow:0 0 0 3px #fff36a,0 2px 4px #0007}
#side h3{margin:3px 0 12px;color:#ffdc98}
#side .btn{width:100%;margin:5px 0}
#message{min-height:44px;padding:10px;margin:8px 0;background:#fff1;border-radius:8px;line-height:1.45}
#history{max-height:150px;overflow:auto;font-size:13px;color:#e7d7c2;line-height:1.8}
#settings,#rules{display:none;max-width:620px;margin:25px auto;background:#20160feF;border:1px solid #a57742;border-radius:16px;padding:20px}
.settingrow{display:flex;justify-content:space-between;gap:12px;align-items:center;margin:15px 0}
select{max-width:58%;padding:8px;border-radius:7px}
input[type=range]{max-width:55%}
.small{font-size:13px;color:#d9c7b1;line-height:1.6}
#toast{color:#ffd989;font-size:13px;margin-top:8px}
@media(max-width:720px){
 #app{padding:12px}
 #home{margin-top:6vh;padding:24px 15px}
 .gamegrid{grid-template-columns:1fr}
 #board{max-width:520px;margin:auto}
 #side{display:grid;grid-template-columns:1fr 1fr;gap:5px}
 #side h3,#message,#history{grid-column:1/-1}
 #side .btn{margin:2px 0;padding:10px 5px;font-size:13px}
 .piece{font-size:clamp(13px,4.5vw,25px)}
}
</style>
</head>
<body>
<div id="app">
 <div class="top">
  <div class="brand">♟ CỜ TƯỚNG</div>
  <button class="btn" onclick="showSettings()">⚙ <span data-t="settings">Cài đặt</span></button>
 </div>

 <section id="home">
  <h1 data-t="title">CỜ TƯỚNG</h1>
  <div class="subtitle" data-t="subtitle">Đấu trí từng nước đi · Thử thách bản lĩnh của bạn</div>
  <div class="menu">
   <button class="btn primary" onclick="startGame('bot')" data-t="vsbot">🤖 Đấu với máy</button>
   <button class="btn" onclick="startGame('two')" data-t="two">♟ Hai người chơi</button>
   <button class="btn" onclick="showRules()" data-t="rules">📖 Luật chơi</button>
  </div>
  <p class="small">Chọn quân · Tìm nước đi · Chiếu bí đối thủ</p>
 </section>

 <section id="settings">
  <h2 data-t="settings">⚙ Cài đặt</h2>
  <div class="settingrow"><label data-t="language">Ngôn ngữ</label>
   <select id="language" onchange="setLanguage(this.value)"><option value="vi">Tiếng Việt</option><option value="en">English</option></select>
  </div>
  <div class="settingrow"><label data-t="difficulty">Độ khó của máy</label>
   <select id="difficulty"><option value="0">Dễ</option><option value="1" selected>Trung bình</option><option value="2">Khó</option><option value="3">Siêu khó</option></select>
  </div>
  <div class="settingrow"><label data-t="sound">Âm thanh nước đi</label><input id="sound" type="checkbox" checked></div>
  <div class="settingrow"><label data-t="music">Nhạc nền</label><input id="music" type="checkbox" onchange="toggleMusic(this.checked)"></div>
  <div class="settingrow"><label data-t="volume">Âm lượng</label><input id="volume" type="range" min="0" max="100" value="35"></div>
  <button class="btn primary" onclick="hideSettings()" data-t="done">Xong</button>
 </section>

 <section id="rules">
  <h2 data-t="rules">Luật chơi cờ tướng</h2>
  <p><b>Tướng:</b> đi từng bước ngang hoặc dọc trong cung 3×3.</p>
  <p><b>Sĩ:</b> đi chéo một bước trong cung.</p>
  <p><b>Tượng:</b> đi chéo hai điểm, không qua sông và không bị cản mắt tượng.</p>
  <p><b>Xe:</b> đi ngang hoặc dọc, không nhảy qua quân.</p>
  <p><b>Pháo:</b> đi như xe; muốn ăn quân phải nhảy qua đúng một quân.</p>
  <p><b>Mã:</b> đi kiểu chữ L; bị cản chân thì không đi được.</p>
  <p><b>Tốt:</b> đi thẳng về phía trước; qua sông được đi ngang, không đi lùi.</p>
  <p>Không được để tướng của mình bị chiếu. Chiếu bí đối thủ thì thắng.</p>
  <p class="small">Bàn cờ trong bản này kiểm tra nước đi hợp lệ cơ bản và tình trạng chiếu. Nếu chơi thi đấu, hãy đối chiếu thêm các quy tắc xử hòa và quy định chính thức.</p>
  <button class="btn primary" onclick="hideRules()" data-t="back">Quay lại</button>
 </section>

 <section id="game">
  <div class="gamegrid">
   <div class="panel">
    <div class="status"><span id="turn">Lượt: Đỏ</span><span id="mode">Đấu với máy</span></div>
    <div id="board" aria-label="Bàn cờ tướng"></div>
   </div>
   <div class="panel" id="side">
    <h3 data-t="gamecontrols">Điều khiển trận đấu</h3>
    <div id="message">Chọn một quân của bạn để bắt đầu.</div>
    <button class="btn" onclick="hint()" data-t="hint">💡 Gợi ý</button>
    <button class="btn" onclick="undo()" data-t="undo">↩ Đi lại</button>
    <button class="btn" onclick="newGame()" data-t="newgame">⟳ Chơi mới</button>
    <button class="btn" onclick="resign()" data-t="resign">🏳 Xin thua</button>
    <button class="btn" onclick="goHome()" data-t="home">⌂ Về màn hình chính</button>
    <h3 data-t="history">Lịch sử nước đi</h3>
    <div id="history">Chưa có nước đi.</div>
    <div class="small">Mẹo: nhấn quân của mình, sau đó nhấn ô muốn đi.</div>
  </div>
 </div>
</div>
<script>
const $=id=>document.getElementById(id);
let lang='vi', mode='bot', board=[], turn='r', selected=null, legal=[], history=[], snapshots=[], ended=false;
let audioCtx=null, musicTimer=null, musicOsc=null;
const names={
 r:{K:'帥',A:'仕',E:'相',H:'傌',R:'俥',C:'炮',P:'兵'},
 b:{K:'將',A:'士',E:'象',H:'馬',R:'車',C:'砲',P:'卒'}
};
const words={
 vi:{settings:'Cài đặt',title:'CỜ TƯỚNG',subtitle:'Đấu trí từng nước đi · Thử thách bản lĩnh của bạn',vsbot:'🤖 Đấu với máy',two:'♟ Hai người chơi',rules:'📖 Luật chơi',language:'Ngôn ngữ',difficulty:'Độ khó của máy',sound:'Âm thanh nước đi',music:'Nhạc nền',volume:'Âm lượng',done:'Xong',back:'Quay lại',gamecontrols:'Điều khiển trận đấu',hint:'💡 Gợi ý',undo:'↩ Đi lại',newgame:'⟳ Chơi mới',resign:'🏳 Xin thua',home:'⌂ Về màn hình chính',history:'Lịch sử nước đi',red:'Đỏ',black:'Đen',bot:'Đấu với máy',twoMode:'Hai người chơi',choose:'Chọn quân của bạn để đi.',thinking:'Máy đang suy nghĩ...',check:'Chiếu tướng!',win:'Thắng!',lose:'Thua!',nomove:'Không có nước đi gợi ý.',confirm:'Bạn muốn xin thua và kết thúc ván này?',empty:'Chưa có nước đi.',checkmate:'Chiếu bí! ',stalemate:'Hết nước đi hợp lệ! ',hintText:'Nước gợi ý: ',move:' đi ',capture:'Ăn quân'},
 en:{settings:'Settings',title:'XIANGQI',subtitle:'Think ahead · Challenge your strategy',vsbot:'🤖 Play vs computer',two:'♟ Two players',rules:'📖 Rules',language:'Language',difficulty:'Bot difficulty',sound:'Move sounds',music:'Background music',volume:'Volume',done:'Done',back:'Back',gamecontrols:'Game controls',hint:'💡 Hint',undo:'↩ Undo',newgame:'⟳ New game',resign:'🏳 Resign',home:'⌂ Home',history:'Move history',red:'Red',black:'Black',bot:'Play vs computer',twoMode:'Two players',choose:'Select one of your pieces.',thinking:'Computer thinking...',check:'Check!',win:'You win!',lose:'You lose!',nomove:'No hint available.',confirm:'Resign and end this game?',empty:'No moves yet.',checkmate:'Checkmate! ',stalemate:'No legal moves! ',hintText:'Suggested move: ',move:' to ',capture:'Capture'}
};
function t(k){return (words[lang]||words.vi)[k]||k}
function setLanguage(v){lang=v;document.documentElement.lang=v;document.querySelectorAll('[data-t]').forEach(el=>{let k=el.getAttribute('data-t');if(words[lang][k])el.textContent=words[lang][k]});render()}
function showSettings(){$('settings').style.display='block';$('home').style.display='none';$('game').style.display='none';$('rules').style.display='none'}
function hideSettings(){ $('settings').style.display='none';if(mode==='bot'||mode==='two'){$('game').style.display='block';$('home').style.display='none'}else $('home').style.display='block'}
function showRules(){$('rules').style.display='block';$('home').style.display='none';$('game').style.display='none';$('settings').style.display='none'}
function hideRules(){$('rules').style.display='none';$('home').style.display='block'}
function fresh(){
 board=Array.from({length:10},()=>Array(9).fill(null));
 const back=['R','H','E','A','K','A','E','H','R'];
 for(let c=0;c<9;c++){board[0][c]={s:'b',p:back[c]};board[9][c]={s:'r',p:back[c]};}
 board[2][1]={s:'b',p:'C'};board[2][7]={s:'b',p:'C'};
 board[7][1]={s:'r',p:'C'};board[7][7]={s:'r',p:'C'};
 for(let c=0;c<9;c+=2){board[3][c]={s:'b',p:'P'};board[6][c]={s:'r',p:'P'};}
 turn='r';selected=null;legal=[];history=[];snapshots=[];ended=false;
 $('message').textContent=t('choose');render();
}
function startGame(m){mode=m;$('home').style.display='none';$('rules').style.display='none';$('settings').style.display='none';$('game').style.display='block';$('mode').textContent=m==='bot'?t('bot'):t('twoMode');fresh()}
function newGame(){if(confirm(lang==='vi'?'Chơi ván mới?':'Start a new game?'))fresh()}
function goHome(){if(!ended&&history.length&& !confirm(lang==='vi'?'Về màn hình chính? Ván hiện tại sẽ kết thúc.':'Return home and end this game?'))return;$('game').style.display='none';$('home').style.display='block';mode='';}
function resign(){if(ended)return;if(confirm(t('confirm'))){ended=true;$('message').textContent=(turn==='r'?t('black'):t('red'))+' '+t('win');playTone(150,.18,'sawtooth')}}
function inside(r,c){return r>=0&&r<10&&c>=0&&c<9}
function clone(b){return b.map(row=>row.map(p=>p?{s:p.s,p:p.p}:null))}
function palace(s,r,c){return c>=3&&c<=5&&(s==='r'?r>=7&&r<=9:r>=0&&r<=2)}
function pseudo(b,r,c){
 const q=b[r][c];if(!q)return [];
 let out=[],s=q.s,p=q.p,enemy=s==='r'?'b':'r';
 const add=(rr,cc)=>{if(inside(rr,cc)&&(!b[rr][cc]||b[rr][cc].s===enemy))out.push([rr,cc])};
 if(p==='R'||p==='C'){
  for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){
   let screen=false;
   for(let rr=r+dr,cc=c+dc;inside(rr,cc);rr+=dr,cc+=dc){
    if(p==='R'){if(!b[rr][cc])out.push([rr,cc]);else{if(b[rr][cc].s===enemy)out.push([rr,cc]);break}}
    else if(!screen){if(!b[rr][cc])out.push([rr,cc]);else screen=true}
    else if(b[rr][cc]){if(b[rr][cc].s===enemy)out.push([rr,cc]);break}
   }
  }
 }else if(p==='H'){
  const steps=[[-2,-1,-1,0],[-2,1,-1,0],[2,-1,1,0],[2,1,1,0],[-1,-2,0,-1],[1,-2,0,-1],[-1,2,0,1],[1,2,0,1]];
  for(const [dr,dc,br,bc] of steps)if(inside(r+br,c+bc)&&!b[r+br][c+bc])add(r+dr,c+dc);
 }else if(p==='E'){
  for(const [dr,dc] of [[-2,-2],[-2,2],[2,-2],[2,2]]){
   let rr=r+dr,cc=c+dc;if(!inside(rr,cc)||b[r+dr/2][c+dc/2])continue;
   if(s==='r'&&rr<5)continue;if(s==='b'&&rr>4)continue;add(rr,cc)
  }
 }else if(p==='A'){
  for(const [dr,dc] of [[-1,-1],[-1,1],[1,-1],[1,1]]){let rr=r+dr,cc=c+dc;if(palace(s,rr,cc))add(rr,cc)}
 }else if(p==='K'){
  for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){let rr=r+dr,cc=c+dc;if(palace(s,rr,cc))add(rr,cc)}
  for(let dr of [-1,1])for(let rr=r+dr;inside(rr,c);rr+=dr){if(b[rr][c]){if(b[rr][c].p==='K'&&b[rr][c].s!==s)out.push([rr,c]);break}}
 }else if(p==='P'){
  let dr=s==='r'?-1:1;add(r+dr,c);
  const crossed=s==='r'?r<=4:r>=5;
  if(crossed){add(r,c-1);add(r,c+1)}
 }
 return out;
}
function kingPos(b,s){for(let r=0;r<10;r++)for(let c=0;c<9;c++)if(b[r][c]?.s===s&&b[r][c].p==='K')return [r,c];return null}
function attacked(b,r,c,by){
 for(let rr=0;rr<10;rr++)for(let cc=0;cc<9;cc++)if(b[rr][cc]?.s===by&&pseudo(b,rr,cc).some(x=>x[0]===r&&x[1]===c))return true;
 return false;
}
function inCheck(b,s){
 const k=kingPos(b,s);if(!k)return true;
 return attacked(b,k[0],k[1],s==='r'?'b':'r');
}
function legalMoves(b,r,c){
 const q=b[r][c];if(!q)return [];
 return pseudo(b,r,c).filter(([rr,cc])=>{
  let nb=clone(b);nb[rr][cc]=nb[r][c];nb[r][c]=null;
  return !inCheck(nb,q.s);
 });
}
function allMoves(b,s){
 let a=[];for(let r=0;r<10;r++)for(let c=0;c<9;c++)if(b[r][c]?.s===s)for(const to of legalMoves(b,r,c))a.push({from:[r,c],to});
 return a;
}
function render(){
 const el=$('board');el.innerHTML='';
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  let cell=document.createElement('div');cell.className='cell';
  if(r===4||r===5)cell.classList.add('river');
  if(selected&&selected[0]===r&&selected[1]===c)cell.classList.add('selected');
  if(legal.some(x=>x[0]===r&&x[1]===c))cell.classList.add('legal');
  const q=board[r][c];
  if(q){let piece=document.createElement('div');piece.className='piece '+(q.s==='r'?'red':'black');piece.textContent=names[q.s][q.p];cell.appendChild(piece)}
  cell.addEventListener('click',()=>clickCell(r,c));el.appendChild(cell);
 }
 $('turn').textContent=(turn==='r'?t('red'):t('black'))+' · '+(turn==='r'?'●':'○');
 $('history').textContent=history.length?history.map((m,i)=>(i+1)+'. '+m).join('\n'):t('empty');
 $('history').style.whiteSpace='pre-line';
}
function clickCell(r,c){
 if(ended|| (mode==='bot'&&turn==='b'))return;
 const q=board[r][c];
 if(selected&&legal.some(x=>x[0]===r&&x[1]===c)){move(selected,[r,c]);return}
 if(q&&q.s===turn){selected=[r,c];legal=legalMoves(board,r,c);$('message').textContent=lang==='vi'?'Đã chọn quân. Hãy chọn ô được đánh dấu.':'Piece selected. Choose a marked square.'}
 else {selected=null;legal=[]}
 render();
}
function move(from,to,botMove=false){
 if(ended)return;
 const [r,c]=from,[rr,cc]=to, piece=board[r][c];if(!piece)return;
 const captured=board[rr][cc];
 snapshots.push({board:clone(board),turn,history:history.slice()});
 board[rr][cc]=piece;board[r][c]=null;
 history.push((piece.s==='r'?'Đỏ':'Đen')+' '+names[piece.s][piece.p]+' '+String.fromCharCode(65+c)+(10-r)+' → '+String.fromCharCode(65+cc)+(10-rr)+(captured?' ×':''));
 selected=null;legal=[];turn=turn==='r'?'b':'r';
 playTone(captured?190:330,captured?0.12:0.07,captured?'square':'sine');
 if(inCheck(board,turn)){$('message').textContent=t('check');playTone(520,.09,'sine')}
 else $('message').textContent=t('choose');
 render();
 const moves=allMoves(board,turn);
 if(!moves.length){ended=true;$('message').textContent=t('checkmate')+(turn==='r'?t('black'):t('red'))+' '+t('win');render();return}
 if(mode==='bot'&&turn==='b'&&!ended){$('message').textContent=t('thinking');setTimeout(botTurn,350)}
}
function undo(){
 if(!snapshots.length||ended)return;
 if(mode==='bot'&&snapshots.length>=2){snapshots.pop();let s=snapshots.pop();board=s.board;turn=s.turn;history=s.history}
 else {let s=snapshots.pop();board=s.board;turn=s.turn;history=s.history}
 selected=null;legal=[];$('message').textContent=t('choose');render()
}
const val={K:10000,A:20,E:25,H:45,R:90,C:50,P:15};
function scoreBoard(b,s){
 let total=0;
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){let q=b[r][c];if(!q)continue;
  let v=val[q.p]||10;
  if(q.p==='P')v+=q.s==='r'?(6-r)*1.5:(r-3)*1.5;
  if(q.p==='H'||q.p==='R'||q.p==='C')v+=Math.max(0,4-Math.abs(4-c))*0.6;
  total+=q.s===s?v:-v;
 }
 if(inCheck(b,s==='r'?'b':'r'))total+=s==='r'?8:-8;
 return total;
}
function botTurn(){
 if(ended||mode!=='bot'||turn!=='b')return;
 const moves=allMoves(board,'b');if(!moves.length){ended=true;$('message').textContent=t('win');return}
 const level=+$('difficulty').value;
 let scored=moves.map(m=>{
  const nb=clone(board),q=nb[m.from[0]][m.from[1]],capt=nb[m.to[0]][m.to[1]];
  nb[m.to[0]][m.to[1]]=q;nb[m.from[0]][m.from[1]]=null;
  let sc=scoreBoard(nb,'b')-scoreBoard(board,'b')*.15;
  if(capt)sc+=val[capt.p]*0.8;
  if(inCheck(nb,'r'))sc+=level*5+8;
  sc+=(Math.random()-.5)*(level===0?32:level===1?17:level===2?7:2);
  if(level>=2){
   const replies=allMoves(nb,'r');
   if(replies.length===0)sc+=10000;
   else if(level===3){
    let worst=Infinity;
    for(const rep of replies.slice(0,45)){
     const b2=clone(nb),qq=b2[rep.from[0]][rep.from[1]];
     b2[rep.to[0]][rep.to[1]]=qq;b2[rep.from[0]][rep.from[1]]=null;
     worst=Math.min(worst,scoreBoard(b2,'b'));
    }
    sc+=worst*.2;
   }
  }
  return {m,sc}
 });
 scored.sort((a,b)=>b.sc-a.sc);
 let choice=scored[0].m;
 if(level===0)choice=scored[Math.floor(Math.random()*Math.min(6,scored.length))].m;
 move(choice.from,choice.to,true);
}
function hint(){
 if(ended){$('message').textContent=t('nomove');return}
 let ms=allMoves(board,turn);if(!ms.length){$('message').textContent=t('nomove');return}
 let best=ms[0],bestScore=-Infinity;
 for(const m of ms){
  let nb=clone(board),q=nb[m.from[0]][m.from[1]],cap=nb[m.to[0]][m.to[1]];
  nb[m.to[0]][m.to[1]]=q;nb[m.from[0]][m.from[1]]=null;
  let sc=scoreBoard(nb,turn)+(cap?(val[cap.p]||0)*.8:0);
  if(sc>bestScore){bestScore=sc;best=m}
 }
 selected=best.from;legal=legalMoves(board,...best.from);$('message').textContent=t('hintText')+String.fromCharCode(65+best.from[1])+(10-best.from[0])+' → '+String.fromCharCode(65+best.to[1])+(10-best.to[0]);render()
}
function playTone(freq,duration,type){
 if(!$('sound').checked)return;
 try{audioCtx=audioCtx||new(window.AudioContext||window.webkitAudioContext)();let o=audioCtx.createOscillator(),g=audioCtx.createGain();o.type=type||'sine';o.frequency.value=freq;g.gain.value=(+$('volume').value/100)*.12;o.connect(g);g.connect(audioCtx.destination);o.start();g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+duration);o.stop(audioCtx.currentTime+duration)}catch(e){}
}
function toggleMusic(on){
 if(on){try{audioCtx=audioCtx||new(window.AudioContext||window.webkitAudioContext)();if(musicTimer)return;let notes=[196,247,294,247,220,262,330,262],i=0;musicTimer=setInterval(()=>{if(!$('music').checked)return;let o=audioCtx.createOscillator(),g=audioCtx.createGain();o.type='sine';o.frequency.value=notes[i++%notes.length];g.gain.value=(+$('volume').value/100)*.018;o.connect(g);g.connect(audioCtx.destination);o.start();g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+.45);o.stop(audioCtx.currentTime+.46)},500)}catch(e){}}
 else if(musicTimer){clearInterval(musicTimer);musicTimer=null}
}
fresh();
</script>
</body>
</html>
"""

components.html(HTML, height=1150, scrolling=True)
