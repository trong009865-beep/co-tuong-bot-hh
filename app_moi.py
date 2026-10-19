
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
:root{
 --gold:#e4bd72;--gold2:#f5dca1;--red:#8e252b;
 --dark:#160e0c;--panel:#251713;--cream:#e5c58c;
}
html,body{margin:0;padding:0;background:#160e0c;color:#f8ead0;
 font-family:Georgia,"Times New Roman",serif}
button,select,input{font:inherit}
button{cursor:pointer;transition:.2s}
button:hover{filter:brightness(1.15);transform:translateY(-2px)}
button:disabled{opacity:.4;cursor:not-allowed;transform:none}
#app{min-height:970px;position:relative;overflow:hidden;
 background:radial-gradient(ellipse at 75% 35%,#51271c 0%,#251510 45%,#100b09 100%);
 border:1px solid #79502a}
.topline{height:5px;background:linear-gradient(90deg,#5c171a,#f0ce85,#8d262a)}
.brand{display:flex;align-items:center;gap:12px;color:var(--gold);
 font-size:15px;letter-spacing:4px;text-transform:uppercase}
.brand-icon{border:1px solid #b38a4e;border-radius:50%;width:40px;height:40px;
 display:grid;place-items:center;font-size:23px}
.home{min-height:950px;position:relative;display:flex;align-items:center;
 padding:55px 6%;overflow:hidden}
.home-content{position:relative;z-index:4;width:48%;max-width:560px}
.eyebrow{font-size:13px;letter-spacing:5px;color:#d5aa65;margin:26px 0 12px}
h1{font-size:clamp(48px,6vw,84px);line-height:1.03;margin:0;
 color:#f4d99d;font-weight:normal;text-shadow:0 4px 20px #000}
h1 span{display:block;font-size:.52em;letter-spacing:9px;margin-top:18px}
.intro{color:#d0bca2;font-family:Arial,sans-serif;line-height:1.9;
 max-width:420px;font-size:15px;margin:25px 0 30px}
.hero-buttons{display:flex;flex-direction:column;gap:16px;
 width:min(350px,100%);margin-top:25px}
.hero-buttons button{width:100%;min-height:66px;padding:17px 24px;
 font-size:19px;font-weight:bold;letter-spacing:2px;border:1px solid #d2ac6b;
 border-radius:10px;box-shadow:0 7px 20px #0007}
.primary{background:linear-gradient(135deg,#b13b32,#65191c);color:#fff0d2}
.secondary{background:#211510;color:#f0d29a}
.gold-button{background:linear-gradient(135deg,#e5c98b,#ad7a38);color:#29170e}
.home-foot{margin-top:35px;color:#92775b;font:11px Arial,sans-serif;letter-spacing:3px}
.board-showcase{position:absolute;right:4%;top:50%;transform:translateY(-50%);
 width:min(43vw,510px);filter:drop-shadow(0 25px 25px #000b)}
.board-frame{padding:12px;background:linear-gradient(135deg,#98602e,#e2bb72,#63391d);
 border:2px solid #d5a858;box-shadow:inset 0 0 0 4px #563018}
#decorBoard{display:block;width:100%;height:auto;background:#d8b578}
.game{display:none;padding:24px 4% 40px;min-height:960px}
.game-top{display:flex;align-items:center;justify-content:space-between;
 gap:12px;flex-wrap:wrap;margin-bottom:20px}
.game-title{font-size:28px;color:var(--gold2)}
.small-btn{padding:10px 15px;border:1px solid #947044;border-radius:8px;
 color:#f5dfb2;background:#2c1b14;font-size:14px}
.game-layout{display:grid;grid-template-columns:minmax(280px,650px) minmax(240px,1fr);
 gap:28px;align-items:start;max-width:1200px;margin:auto}
.play-area{position:relative;padding:12px;background:linear-gradient(135deg,#a87339,#e5c580,#68401f);
 border:2px solid #e1b66a;box-shadow:0 18px 40px #0009}
#board{display:block;width:100%;height:auto;touch-action:manipulation}
.game-side{background:#241713;border:1px solid #73502e;border-radius:12px;
 padding:22px}
.game-side h2{font-size:23px;color:var(--gold2);font-weight:normal;margin:0 0 14px}
.status{background:#160e0c;border:1px solid #503321;border-radius:8px;
 padding:14px;margin-bottom:15px;line-height:1.6;color:#ead6b5}
.side-buttons{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.side-buttons button{padding:12px 8px;border:1px solid #89643a;border-radius:7px;
 background:#3a2419;color:#f4dfb7}
.side-buttons .danger{background:#6e2021}
.side-buttons .wide{grid-column:1/-1}
.section-title{color:#dcb76e;font-size:13px;letter-spacing:2px;margin:24px 0 10px}
.tip{color:#c8b59b;font:14px/1.8 Arial,sans-serif}
.overlay{display:none;position:fixed;z-index:1000;inset:0;
 background:#080504dc;align-items:center;justify-content:center;padding:18px}
.overlay.show{display:flex}
.modal{position:relative;width:min(520px,100%);max-height:90vh;overflow:auto;
 padding:28px;background:linear-gradient(145deg,#352017,#170e0c);
 border:1px solid #c59a55;border-radius:14px;box-shadow:0 20px 80px #000}
.modal h2{margin:0 0 20px;color:var(--gold2);font-size:28px;font-weight:normal}
.modal p,.modal li{font:15px/1.8 Arial,sans-serif;color:#e1cdb0}
.modal-buttons{display:grid;grid-template-columns:1fr;gap:12px}
.modal-buttons button{min-height:54px;padding:13px;border:1px solid #c6a063;
 border-radius:8px;background:#42251a;color:#f7e4bd;font-size:16px}
.modal-buttons button.selected{background:#8b292b}
.close{position:absolute;right:14px;top:10px;border:0;background:transparent;
 color:#d9c4a3;font-size:27px}
.setting-row{display:flex;align-items:center;justify-content:space-between;
 gap:15px;padding:14px 0;border-bottom:1px solid #4b3022;
 font:15px Arial,sans-serif}
.setting-row select{background:#160e0c;color:#f5dfb2;border:1px solid #96713d;
 border-radius:6px;padding:9px;max-width:55%}
.setting-row input[type=range]{width:45%;accent-color:#d6a34f}
.setting-row input[type=checkbox]{width:20px;height:20px;accent-color:#b38a4e}
.result{display:none;position:absolute;inset:0;z-index:20;
 background:#100907df;align-items:center;justify-content:center;text-align:center}
.result.show{display:flex}
.result-box{padding:30px 18px}
.result h2{font-size:clamp(38px,7vw,72px);color:#f6d783;
 text-shadow:0 5px 20px #000;margin:0 0 15px}
.result p{font:16px Arial,sans-serif;color:#f4e2c5}
.result button{margin:7px;padding:14px 20px;border:1px solid #e0bb70;
 border-radius:8px;background:#772326;color:#fff0ce}
@media(max-width:800px){
 .home{padding:35px 6%;min-height:1050px;align-items:flex-start}
 .home-content{width:100%;max-width:none}
 .home .intro{max-width:380px}
 .board-showcase{position:relative;right:auto;top:auto;transform:none;
 width:min(80%,380px);margin:35px auto 0}
 .home{display:block}
 .hero-buttons{width:min(360px,100%)}
 .hero-buttons button{min-height:62px;font-size:18px}
 .game-layout{grid-template-columns:1fr}
 .game-side{order:2}
 .game{padding:15px 3%}
}
</style>
</head>
<body>
<div id="app">
<div class="topline"></div>

<section class="home" id="home">
  <div class="home-content">
    <div class="brand"><div class="brand-icon">帥</div><span>KỲ ĐẠO · XIANGQI</span></div>
    <div class="eyebrow" data-i18n="eyebrow">NGHỆ THUẬT CỦA CHIẾN THUẬT</div>
    <h1>象棋<span data-i18n="title">CỜ TƯỚNG</span></h1>
    <p class="intro" data-i18n="intro">Một bàn cờ, hai chiến tuyến. Rèn luyện tư duy, tính toán từng nước đi và bảo vệ Tướng của bạn.</p>
    <div class="hero-buttons">
      <button class="primary" onclick="openModes()" data-i18n="start">♟ &nbsp; BẮT ĐẦU</button>
      <button class="secondary" onclick="openModal('helpModal')" data-i18n="help">📖 &nbsp; HƯỚNG DẪN</button>
      <button class="secondary" onclick="openModal('settingsModal')" data-i18n="settings">⚙ &nbsp; CÀI ĐẶT</button>
    </div>
    <div class="home-foot">STRATEGY · PATIENCE · WISDOM</div>
  </div>
  <div class="board-showcase">
    <div class="board-frame"><canvas id="decorBoard" width="450" height="500"></canvas></div>
  </div>
</section>

<section class="game" id="game">
  <div class="game-top">
    <div class="brand"><div class="brand-icon">帥</div><span>KỲ ĐẠO</span></div>
    <div class="game-title" data-i18n="gameTitle">BÀN CỜ TƯỚNG</div>
    <button class="small-btn" onclick="openModal('settingsModal')" data-i18n="settings">⚙ CÀI ĐẶT</button>
  </div>
  <div class="game-layout">
    <div class="play-area">
      <canvas id="board" width="540" height="600"></canvas>
      <div class="result" id="result">
        <div class="result-box">
          <h2 id="resultTitle">CHIẾN THẮNG!</h2>
          <p id="resultText"></p>
          <button onclick="newGame()" data-i18n="again">Chơi lại</button>
          <button onclick="goHome()" data-i18n="home">Về sảnh</button>
        </div>
      </div>
    </div>
    <aside class="game-side">
      <h2 data-i18n="matchInfo">Thông tin ván đấu</h2>
      <div class="status" id="status">Đến lượt Đỏ. Chọn một quân cờ.</div>
      <div class="side-buttons">
        <button onclick="hintMove()" data-i18n="hint">💡 Gợi ý</button>
        <button onclick="undoMove()" data-i18n="undo">↶ Đi lại</button>
        <button onclick="newGame()" data-i18n="restart">⟳ Ván mới</button>
        <button class="danger" onclick="resign()" data-i18n="resign">Đầu hàng</button>
        <button class="wide" onclick="goHome()" data-i18n="home">⌂ Về sảnh chính</button>
      </div>
      <div class="section-title" data-i18n="tools">CÔNG CỤ</div>
      <p class="tip" data-i18n="toolTip">Gợi ý sẽ đánh dấu một nước đi tham khảo. Đi lại sẽ hoàn tác nước đi gần nhất. Ván mới sẽ bắt đầu lại từ đầu.</p>
      <div class="section-title" data-i18n="quickRules">NHẮC NHANH LUẬT CHƠI</div>
      <p class="tip" data-i18n="quickTip">Mục tiêu là chiếu bí Tướng đối phương. Không được đi một nước khiến Tướng của mình bị chiếu. Pháo cần một quân làm ngòi khi ăn quân.</p>
    </aside>
  </div>
</section>
</div>

<div class="overlay" id="modeModal">
 <div class="modal">
  <button class="close" onclick="closeModal('modeModal')">×</button>
  <h2 data-i18n="chooseMode">Chọn chế độ chơi</h2>
  <div class="modal-buttons">
   <button onclick="showDifficulties()" data-i18n="vsBot">♟ Đấu với máy</button>
   <button onclick="startGame('human',1)" data-i18n="vsHuman">♟ Đấu hai người</button>
  </div>
  <div id="difficultyList" style="display:none;margin-top:18px">
   <p data-i18n="chooseLevel">Chọn độ khó của máy:</p>
   <div class="modal-buttons">
    <button onclick="startGame('bot',1)" data-i18n="easy">Dễ</button>
    <button onclick="startGame('bot',2)" data-i18n="medium">Trung bình</button>
    <button onclick="startGame('bot',3)" data-i18n="hard">Khó</button>
    <button onclick="startGame('bot',4)" data-i18n="expert">Siêu khó</button>
   </div>
  </div>
 </div>
</div>

<div class="overlay" id="helpModal">
 <div class="modal">
  <button class="close" onclick="closeModal('helpModal')">×</button>
  <h2 data-i18n="guideTitle">Hướng dẫn chơi cờ tướng</h2>
  <div id="guideContent"></div>
  <div class="modal-buttons"><button onclick="closeModal('helpModal')" data-i18n="gotIt">Đã hiểu</button></div>
 </div>
</div>

<div class="overlay" id="settingsModal">
 <div class="modal">
  <button class="close" onclick="closeModal('settingsModal')">×</button>
  <h2 data-i18n="settingsTitle">Cài đặt trò chơi</h2>
  <div class="setting-row"><span data-i18n="language">Ngôn ngữ</span>
   <select id="language" onchange="changeLanguage(this.value)">
    <option value="vi">Tiếng Việt</option><option value="en">English</option>
   </select>
  </div>
  <div class="setting-row"><span data-i18n="soundEffects">Hiệu ứng âm thanh</span>
   <input id="soundToggle" type="checkbox" checked onchange="settings.sound=this.checked">
  </div>
  <div class="setting-row"><span data-i18n="soundVolume">Âm lượng hiệu ứng</span>
   <input id="soundVolume" type="range" min="0" max="100" value="55" oninput="settings.volume=this.value/100">
  </div>
  <div class="setting-row"><span data-i18n="music">Nhạc nền</span>
   <input id="musicToggle" type="checkbox" onchange="toggleMusic(this.checked)">
  </div>
  <div class="setting-row"><span data-i18n="musicVolume">Âm lượng nhạc nền</span>
   <input id="musicVolume" type="range" min="0" max="100" value="18" oninput="settings.musicVolume=this.value/100;updateMusicVolume()">
  </div>
  <p class="tip" data-i18n="musicNote">Nhạc nền bắt đầu phát sau khi bạn bật nhạc và tương tác với trang. Trình duyệt có thể chặn tự động phát.</p>
  <div class="modal-buttons"><button onclick="closeModal('settingsModal')" data-i18n="save">Hoàn tất</button></div>
 </div>
</div>

<script>
const $=id=>document.getElementById(id);
const translations={
vi:{
eyebrow:"NGHỆ THUẬT CỦA CHIẾN THUẬT",title:"CỜ TƯỚNG",
intro:"Một bàn cờ, hai chiến tuyến. Rèn luyện tư duy, tính toán từng nước đi và bảo vệ Tướng của bạn.",
start:"♟  BẮT ĐẦU",help:"📖  HƯỚNG DẪN",settings:"⚙  CÀI ĐẶT",
gameTitle:"BÀN CỜ TƯỚNG",again:"Chơi lại",home:"⌂ Về sảnh chính",
matchInfo:"Thông tin ván đấu",hint:"💡 Gợi ý",undo:"↶ Đi lại",
restart:"⟳ Ván mới",resign:"Đầu hàng",tools:"CÔNG CỤ",
toolTip:"Gợi ý sẽ đánh dấu một nước đi tham khảo. Đi lại sẽ hoàn tác nước đi gần nhất. Ván mới sẽ bắt đầu lại từ đầu.",
quickRules:"NHẮC NHANH LUẬT CHƠI",quickTip:"Mục tiêu là chiếu bí Tướng đối phương. Không được đi một nước khiến Tướng của mình bị chiếu. Pháo cần một quân làm ngòi khi ăn quân.",
chooseMode:"Chọn chế độ chơi",vsBot:"♟ Đấu với máy",vsHuman:"♟ Đấu hai người",
chooseLevel:"Chọn độ khó của máy:",easy:"Dễ",medium:"Trung bình",hard:"Khó",expert:"Siêu khó",
guideTitle:"Hướng dẫn chơi cờ tướng",gotIt:"Đã hiểu",settingsTitle:"Cài đặt trò chơi",
language:"Ngôn ngữ",soundEffects:"Hiệu ứng âm thanh",soundVolume:"Âm lượng hiệu ứng",
music:"Nhạc nền",musicVolume:"Âm lượng nhạc nền",
musicNote:"Nhạc nền bắt đầu phát sau khi bạn bật nhạc và tương tác với trang. Trình duyệt có thể chặn tự động phát.",
save:"Hoàn tất",redTurn:"Đến lượt Đỏ.",blackTurn:"Đến lượt Đen.",
selectPiece:"Chọn một quân cờ.",botThinking:"Máy đang suy nghĩ…",check:"Chiếu Tướng!",
redWins:"ĐỎ CHIẾN THẮNG!",blackWins:"ĐEN CHIẾN THẮNG!",
resigned:"Đối phương đã đầu hàng.",draw:"Ván đấu kết thúc.",
guide:`<p><b>1. Mục tiêu</b><br>Chiếu bí Tướng đối phương: Tướng bị tấn công và không còn nước hợp lệ để thoát.</p>
<p><b>2. Cách di chuyển các quân</b></p>
<ul><li><b>Tướng:</b> đi ngang hoặc dọc một ô trong cung 3×3.</li>
<li><b>Sĩ:</b> đi chéo một ô trong cung Tướng.</li>
<li><b>Tượng:</b> đi chéo hai ô, không qua sông và không được bị cản mắt.</li>
<li><b>Xe:</b> đi ngang hoặc dọc tùy số ô trống.</li>
<li><b>Pháo:</b> đi như Xe khi không ăn; khi ăn phải nhảy qua đúng một quân làm ngòi.</li>
<li><b>Mã:</b> đi kiểu chữ L; đường chân Mã không được bị cản.</li>
<li><b>Tốt:</b> đi thẳng một ô; qua sông được đi ngang, không được đi lùi.</li></ul>
<p><b>3. Cách thao tác</b><br>Chạm hoặc nhấp vào quân của mình, sau đó chọn ô muốn đi. Những nước không hợp lệ sẽ bị từ chối.</p>
<p><b>4. Các công cụ</b><br>Gợi ý đánh dấu một nước tham khảo; Đi lại hoàn tác nước trước; Ván mới khởi động lại; Đầu hàng kết thúc ván.</p>
<p><b>5. Mẹo chơi</b><br>Bảo vệ Tướng, phát triển Xe và Mã, chú ý quân đang bị tấn công và tránh để hai Tướng đối mặt trên cùng một cột không có quân chắn.</p>`
},
en:{
eyebrow:"THE ART OF STRATEGY",title:"XIANGQI",
intro:"One board, two sides. Train your mind, plan each move, and protect your General.",
start:"♟  PLAY",help:"📖  HOW TO PLAY",settings:"⚙  SETTINGS",
gameTitle:"XIANGQI BOARD",again:"Play again",home:"⌂ Main menu",
matchInfo:"Game information",hint:"💡 Hint",undo:"↶ Undo",
restart:"⟳ New game",resign:"Resign",tools:"TOOLS",
toolTip:"Hint marks a suggested move. Undo reverses the last move. New game starts over.",
quickRules:"QUICK RULES",quickTip:"Checkmate the enemy General. Do not leave your own General in check. A Cannon needs exactly one screen to capture.",
chooseMode:"Choose a game mode",vsBot:"♟ Play against computer",vsHuman:"♟ Two players",
chooseLevel:"Choose computer difficulty:",easy:"Easy",medium:"Medium",hard:"Hard",expert:"Very hard",
guideTitle:"How to play Xiangqi",gotIt:"Got it",settingsTitle:"Game settings",
language:"Language",soundEffects:"Sound effects",soundVolume:"Effects volume",
music:"Background music",musicVolume:"Music volume",
musicNote:"Music starts after you enable it and interact with the page. Your browser may block autoplay.",
save:"Done",redTurn:"Red to move.",blackTurn:"Black to move.",
selectPiece:"Select a piece.",botThinking:"Computer is thinking…",check:"Check!",
redWins:"RED WINS!",blackWins:"BLACK WINS!",
resigned:"The opponent resigned.",draw:"Game over.",
guide:`<p><b>1. Goal</b><br>Checkmate the enemy General so it has no legal escape.</p>
<p><b>2. Pieces</b></p>
<ul><li><b>General:</b> one square orthogonally inside the 3×3 palace.</li>
<li><b>Advisor:</b> one diagonal square inside the palace.</li>
<li><b>Elephant:</b> two diagonal squares; cannot cross the river or jump a blocked eye.</li>
<li><b>Chariot:</b> any number of empty squares horizontally or vertically.</li>
<li><b>Cannon:</b> moves like a Chariot, but needs exactly one screen to capture.</li>
<li><b>Horse:</b> moves in an L shape; its leg must be clear.</li>
<li><b>Soldier:</b> moves forward one square; after crossing the river it may also move sideways, never backward.</li></ul>
<p><b>3. Controls</b><br>Click your piece, then click the destination square. Illegal moves are rejected.</p>
<p><b>4. Tools</b><br>Hint shows a suggested move; Undo reverses the last move; New game restarts; Resign ends the game.</p>
<p><b>5. Tips</b><br>Protect your General, develop your Chariots and Horses, and watch for attacked pieces.</p>`
}
};
let lang="vi";
let settings={sound:true,volume:.55,musicVolume:.18};
let audioCtx=null, musicTimer=null, musicOn=false, musicOsc=[];
function tr(key){return (translations[lang]||translations.vi)[key]||key}
function changeLanguage(v){
 lang=v;
 document.querySelectorAll("[data-i18n]").forEach(el=>{
  const k=el.getAttribute("data-i18n");if(translations[lang][k])el.textContent=translations[lang][k];
 });
 $("guideContent").innerHTML=tr("guide");
 updateStatus();
}
function openModal(id){$(id).classList.add("show")}
function closeModal(id){$(id).classList.remove("show")}
function openModes(){ $("difficultyList").style.display="none";openModal("modeModal")}
function showDifficulties(){$("difficultyList").style.display="block"}
function ensureAudio(){
 if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();
 if(audioCtx.state==="suspended")audioCtx.resume();
}
function beep(freq=440,duration=.09,type="sine",volume=null){
 if(!settings.sound)return;
 try{
  ensureAudio();const o=audioCtx.createOscillator(),g=audioCtx.createGain();
  o.type=type;o.frequency.value=freq;
  g.gain.value=(volume===null?settings.volume:volume)*.12;
  o.connect(g);g.connect(audioCtx.destination);o.start();
  g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+duration);
  o.stop(audioCtx.currentTime+duration);
 }catch(e){}
}
function updateMusicVolume(){
 musicOsc.forEach(x=>{try{x.gain.gain.value=settings.musicVolume*.025}catch(e){}});
}
function toggleMusic(on){
 musicOn=on;ensureAudio();
 if(musicTimer){clearInterval(musicTimer);musicTimer=null}
 musicOsc.forEach(x=>{try{x.osc.stop()}catch(e){}});
 musicOsc=[];
 if(!on)return;
 // Nhạc nền nhẹ tạo bằng âm thanh tổng hợp, không cần tệp nhạc ngoài.
 const notes=[220,261.63,329.63,293.66,196,246.94,293.66,261.63];
 let i=0;
 function playNote(){
  if(!musicOn)return;
  try{
   const osc=audioCtx.createOscillator(),gain=audioCtx.createGain();
   osc.type="sine";osc.frequency.value=notes[i++%notes.length];
   gain.gain.value=settings.musicVolume*.025;
   osc.connect(gain);gain.connect(audioCtx.destination);
   osc.start();gain.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+1.5);
   osc.stop(audioCtx.currentTime+1.6);
   musicOsc.push({osc,gain});
   if(musicOsc.length>20)musicOsc.shift();
  }catch(e){}
 }
 playNote();musicTimer=setInterval(playNote,1300);
}
const ROWS=10,COLS=9;
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
const redPieces={K:"帥",A:"仕",E:"相",R:"俥",H:"傌",C:"炮",S:"兵"};
const blackPieces={k:"將",a:"士",e:"象",r:"車",h:"馬",c:"砲",s:"卒"};
function side(p){return p===null?null:(p===p.toUpperCase()?"R":"B")}
function inside(r,c){return r>=0&&r<10&&c>=0&&c<9}
function pieceAt(r,c){return inside(r,c)?board[r][c]:null}
function palace(s,r,c){return c>=3&&c<=5&&(s==="R"?r>=7&&r<=9:r>=0&&r<=2)}
function riverCrossed(s,r){return s==="R"?r<=4:r>=5}
function clearPath(r,c,nr,nc){
 const dr=Math.sign(nr-r),dc=Math.sign(nc-c);let x=r+dr,y=c+dc,count=0;
 while(x!==nr||y!==nc){if(board[x][y])count++;x+=dr;y+=dc}
 return count;
}
function pseudoMoves(r,c){
 const p=pieceAt(r,c);if(!p)return [];
 const s=side(p),lower=p.toLowerCase(),out=[];
 function add(nr,nc){if(inside(nr,nc)&&side(pieceAt(nr,nc))!==s)out.push([nr,nc])}
 const orth=[[1,0],[-1,0],[0,1],[0,-1]];
 if(lower==="k"){
  orth.forEach(([dr,dc])=>{let nr=r+dr,nc=c+dc;if(palace(s,nr,nc))add(nr,nc)});
  // Flying General capture
  const dr=s==="R"?-1:1;
  for(let nr=r+dr;inside(nr,c);nr+=dr){
   if(board[nr][c]){if(board[nr][c].toLowerCase()==="k"&&side(board[nr][c])!==s)out.push([nr,c]);break}
  }
 }else if(lower==="a"){
  [[1,1],[1,-1],[-1,1],[-1,-1]].forEach(([dr,dc])=>{let nr=r+dr,nc=c+dc;if(palace(s,nr,nc))add(nr,nc)});
 }else if(lower==="e"){
  [[2,2],[2,-2],[-2,2],[-2,-2]].forEach(([dr,dc])=>{
   const nr=r+dr,nc=c+dc;
   if(inside(nr,nc)&&!riverCrossed(s,nr)&&!board[r+dr/2][c+dc/2])add(nr,nc);
  });
 }else if(lower==="r"){
  orth.forEach(([dr,dc])=>{
   let nr=r+dr,nc=c+dc;
   while(inside(nr,nc)){
    if(!board[nr][nc])out.push([nr,nc]);
    else{if(side(board[nr][nc])!==s)out.push([nr,nc]);break}
    nr+=dr;nc+=dc;
   }
  });
 }else if(lower==="c"){
  orth.forEach(([dr,dc])=>{
   let nr=r+dr,nc=c+dc,screen=false;
   while(inside(nr,nc)){
    if(!screen){
     if(!board[nr][nc])out.push([nr,nc]);
     else screen=true;
    }else if(board[nr][nc]){
     if(side(board[nr][nc])!==s)out.push([nr,nc]);break;
    }
    nr+=dr;nc+=dc;
   }
  });
 }else if(lower==="h"){
  const moves=[
   [-2,-1,-1,0],[-2,1,-1,0],[2,-1,1,0],[2,1,1,0],
   [-1,-2,0,-1],[1,-2,0,-1],[-1,2,0,1],[1,2,0,1]
  ];
  moves.forEach(([dr,dc,lr,lc])=>{
   const nr=r+dr,nc=c+dc;
   if(inside(nr,nc)&&!board[r+lr][c+lc])add(nr,nc);
  });
 }else if(lower==="s"){
  const forward=s==="R"?-1:1;
  add(r+forward,c);
  if(riverCrossed(s,r)){add(r,c-1);add(r,c+1)}
 }
 return out;
}
function findGeneral(s){
 const k=s==="R"?"K":"k";
 for(let r=0;r<10;r++)for(let c=0;c<9;c++)if(board[r][c]===k)return [r,c];
 return null;
}
function isAttacked(r,c,bySide){
 for(let y=0;y<10;y++)for(let x=0;x<9;x++){
  const p=board[y][x];if(p&&side(p)===bySide){
   if(pseudoMoves(y,x).some(([nr,nc])=>nr===r&&nc===c))return true;
  }
 }
 return false;
}
function inCheck(s){
 const k=findGeneral(s);if(!k)return true;
 return isAttacked(k[0],k[1],s==="R"?"B":"R");
}
function legalMoves(r,c){
 const p=pieceAt(r,c);if(!p)return [];
 const s=side(p);
 return pseudoMoves(r,c).filter(([nr,nc])=>{
  const captured=board[nr][nc];board[nr][nc]=p;board[r][c]=null;
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
function newGame(){
 board=initial.map(row=>row.slice());turn="R";selected=null;legal=[];
 history=[];lastMove=null;ended=false;botBusy=false;hint=null;
 $("result").classList.remove("show");
 closeModal("modeModal");$("status").textContent=tr("redTurn")+" "+tr("selectPiece");
 drawBoard();beep(330,.1);
}
function startGame(m,l){
 mode=m;level=l;newGame();
 $("home").style.display="none";$("game").style.display="block";
 closeModal("modeModal");drawBoard();
}
function goHome(){
 $("game").style.display="none";$("home").style.display="flex";
 $("home").style.minHeight="950px";closeModal("settingsModal");
 closeModal("helpModal");closeModal("modeModal");
}
function updateStatus(){
 if(!ended)$("status").textContent=(turn==="R"?tr("redTurn"):tr("blackTurn"))+" "+tr("selectPiece");
}
function makeMove(m){
 if(ended)return;
 history.push({board:cloneBoard(),turn,lastMove:lastMove?{...lastMove}:null});
 const captured=board[m.nr][m.nc];
 board[m.nr][m.nc]=board[m.r][m.c];board[m.r][m.c]=null;
 lastMove={r:m.r,c:m.c,nr:m.nr,nc:m.nc};
 selected=null;legal=[];hint=null;
 beep(captured?680:430,.08,captured?"triangle":"sine");
 turn=turn==="R"?"B":"R";
 if(!findGeneral(turn)){finish(turn==="R"?"B":"R");return}
 if(inCheck(turn))$("status").textContent=tr("check")+" "+(turn==="R"?tr("redTurn"):tr("blackTurn"));
 else updateStatus();
 drawBoard();
 const moves=allMoves(turn);
 if(moves.length===0){finish(turn==="R"?"B":"R");return}
 if(mode==="bot"&&turn==="B"){
  botBusy=true;$("status").textContent=tr("botThinking");
  setTimeout(botMove,350);
 }
}
function finish(winner){
 ended=true;botBusy=false;
 $("resultTitle").textContent=winner==="R"?tr("redWins"):tr("blackWins");
 $("resultText").textContent=winner==="R"?"":"";
 $("result").classList.add("show");drawBoard();beep(740,.25,"triangle");
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
  const prev=history.pop();board=prev.board;turn=prev.turn;lastMove=prev.lastMove;
 }
 selected=null;legal=[];hint=null;botBusy=false;ended=false;
 $("result").classList.remove("show");updateStatus();drawBoard();beep(300,.08);
}
function hintMove(){
 if(ended||botBusy)return;
 let moves=allMoves(turn);if(!moves.length)return;
 let best=moves[0],bestScore=-9999;
 moves.forEach(m=>{
  let score=Math.random()*2;
  const target=board[m.nr][m.nc];
  if(target)score+=({k:1000,r:9,c:5,h:4,e:2,a:2,s:1})[target.toLowerCase()]||0;
  if(target&&target.toLowerCase()==="k")score+=10000;
  if(score>bestScore){bestScore=score;best=m}
 });
 hint=best;drawBoard();$("status").textContent=lang==="vi"?"Gợi ý: quân được viền vàng.":"Hint: the suggested move is marked in gold.";
 beep(580,.1);
}
function botMove(){
 if(ended||turn!=="B"||mode!=="bot"){botBusy=false;return}
 const moves=allMoves("B");if(!moves.length){finish("R");return}
 const value={k:10000,r:900,c:450,h:400,e:200,a:200,s:100};
 function scoreMove(m){
  const target=board[m.nr][m.nc];let score=Math.random()*25;
  if(target)score+=(value[target.toLowerCase()]||0)*1.5;
  // Try not to leave the General under attack.
  const p=board[m.r][m.c];board[m.nr][m.nc]=p;board[m.r][m.c]=null;
  if(inCheck("B"))score-=1000;
  if(inCheck("R"))score+=80;
  board[m.r][m.c]=p;board[m.nr][m.nc]=target;
  // Difficulty changes how consistently the bot selects a strong move.
  if(level===1)score=Math.random()*100+(target?50:0);
  if(level===2)score+=Math.random()*35;
  if(level===3)score+=Math.random()*12;
  if(level===4)score+=Math.random()*3;
  return score;
 }
 moves.sort((a,b)=>scoreMove(b)-scoreMove(a));
 let chosen=moves[0];
 if(level===1&&Math.random()<.55)chosen=moves[Math.floor(Math.random()*moves.length)];
 botBusy=false;makeMove(chosen);
}
function clickBoard(e){
 if(ended||botBusy||(mode==="bot"&&turn==="B"))return;
 const canvas=$("board"),rect=canvas.getBoundingClientRect();
 const x=(e.clientX-rect.left)*canvas.width/rect.width;
 const y=(e.clientY-rect.top)*canvas.height/rect.height;
 const c=Math.round((x-30)/60),r=Math.round((y-30)/60);
 if(!inside(r,c)||Math.abs(x-(30+c*60))>29||Math.abs(y-(30+r*60))>29)return;
 const p=board[r][c];
 if(selected&&legal.some(([nr,nc])=>nr===r&&nc===c)){
  makeMove({r:selected[0],c:selected[1],nr:r,nc:c});return;
 }
 if(p&&side(p)===turn){
  selected=[r,c];legal=legalMoves(r,c);hint=null;beep(510,.06);drawBoard();
 }else{
  selected=null;legal=[];drawBoard();
 }
}
function drawBoardCanvas(canvas,isDecor=false){
 if(!canvas)return;
 const ctx=canvas.getContext("2d"),w=canvas.width,h=canvas.height;
 ctx.clearRect(0,0,w,h);
 ctx.fillStyle="#d9b87c";ctx.fillRect(0,0,w,h);
 // Wood grain
 for(let i=0;i<10;i++){
  ctx.strokeStyle="rgba(105,61,27,.08)";ctx.lineWidth=1;
  ctx.beginPath();ctx.moveTo(0,i*h/10);ctx.lineTo(w,i*h/10+8);ctx.stroke();
 }
 const pad=30,dx=(w-pad*2)/8,dy=(h-pad*2)/9;
 ctx.strokeStyle="#55341c";ctx.lineWidth=isDecor?1.8:1.5;
 // 10 horizontal lines
 for(let r=0;r<10;r++){
  ctx.beginPath();ctx.moveTo(pad,pad+r*dy);ctx.lineTo(w-pad,pad+r*dy);ctx.stroke();
 }
 // vertical lines split around the river
 for(let c=0;c<9;c++){
  const x=pad+c*dx;ctx.beginPath();
  if(c===0||c===8){ctx.moveTo(x,pad);ctx.lineTo(x,h-pad)}
  else{ctx.moveTo(x,pad);ctx.lineTo(x,pad+4*dy);
       ctx.moveTo(x,pad+5*dy);ctx.lineTo(x,h-pad)}
  ctx.stroke();
 }
 // Palace diagonals
 [[3,0],[5,2],[3,2],[5,0],[3,7],[5,9],[3,9],[5,7]].forEach(([c,r],i)=>{
  if(i%2===0){
   ctx.beginPath();ctx.moveTo(pad+3*dx,pad+(i<4?0:7)*dy);
   ctx.lineTo(pad+5*dx,pad+(i<4?2:9)*dy);ctx.stroke();
  }
 });
 // More accurate palace Xs
 ctx.beginPath();ctx.moveTo(pad+3*dx,pad);ctx.lineTo(pad+5*dx,pad+2*dy);
 ctx.moveTo(pad+5*dx,pad);ctx.lineTo(pad+3*dx,pad+2*dy);
 ctx.moveTo(pad+3*dx,pad+7*dy);ctx.lineTo(pad+5*dx,pad+9*dy);
 ctx.moveTo(pad+5*dx,pad+7*dy);ctx.lineTo(pad+3*dx,pad+9*dy);ctx.stroke();
 ctx.fillStyle="#624322";ctx.font=`bold ${isDecor?17:15}px Georgia`;
 ctx.textAlign="center";ctx.textBaseline="middle";
 ctx.fillText("楚 河",w/2,pad+4.5*dy);
 ctx.fillText("漢 界",w/2,pad+4.5*dy);
 // River label on top of board lines
 ctx.fillStyle="#d9b87c";ctx.fillRect(w/2-43,pad+4.5*dy-13,86,26);
 ctx.fillStyle="#624322";ctx.fillText("楚 河   漢 界",w/2,pad+4.5*dy);
 if(isDecor){
  const pieces=[
   [0,0,"車","B"],[0,4,"將","B"],[0,8,"車","B"],
   [2,1,"砲","B"],[2,7,"砲","B"],[3,0,"卒","B"],[3,2,"卒","B"],[3,4,"卒","B"],[3,6,"卒","B"],[3,8,"卒","B"],
   [9,0,"俥","R"],[9,4,"帥","R"],[9,8,"俥","R"],
   [7,1,"炮","R"],[7,7,"炮","R"],[6,0,"兵","R"],[6,2,"兵","R"],[6,4,"兵","R"],[6,6,"兵","R"],[6,8,"兵","R"]
  ];
  pieces.forEach(([r,c,t,s])=>drawPiece(ctx,pad+c*dx,pad+r*dy,Math.min(dx,dy)*.38,t,s));
 }
}
function drawPiece(ctx,x,y,rad,text,s){
 ctx.beginPath();ctx.arc(x+1,y+2,rad+1,0,Math.PI*2);ctx.fillStyle="#684222";ctx.fill();
 ctx.beginPath();ctx.arc(x,y,rad,0,Math.PI*2);
 ctx.fillStyle=s==="R"?"#f0d6a0":"#ead5a5";ctx.fill();
 ctx.lineWidth=2;ctx.strokeStyle=s==="R"?"#a22b2c":"#302019";ctx.stroke();
 ctx.beginPath();ctx.arc(x,y,rad-4,0,Math.PI*2);ctx.lineWidth=1;
 ctx.strokeStyle=s==="R"?"#bb4840":"#8d6b42";ctx.stroke();
 ctx.fillStyle=s==="R"?"#a31e27":"#29201b";
 ctx.font=`bold ${Math.max(13,rad*1.12)}px Georgia`;
 ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillText(text,x,y+1);
}
function drawBoard(){
 const canvas=$("board");if(!canvas)return;
 const ctx=canvas.getContext("2d");
 drawBoardCanvas(canvas,false);
 const pad=30,dx=60,dy=60;
 if(lastMove){
  ctx.fillStyle="rgba(55,140,65,.35)";
  [[lastMove.r,lastMove.c],[lastMove.nr,lastMove.nc]].forEach(([r,c])=>{
   ctx.fillRect(pad+c*dx-13,pad+r*dy-13,26,26);
  });
 }
 if(hint){
  ctx.strokeStyle="#e5a829";ctx.lineWidth=4;
  [[hint.r,hint.c],[hint.nr,hint.nc]].forEach(([r,c])=>{
   ctx.beginPath();ctx.arc(pad+c*dx,pad+r*dy,20,0,Math.PI*2);ctx.stroke();
  });
 }
 legal.forEach(([r,c])=>{
  ctx.beginPath();ctx.arc(pad+c*dx,pad+r*dy,7,0,Math.PI*2);
  ctx.fillStyle=board[r][c]?"rgba(180,35,30,.75)":"rgba(45,110,52,.7)";ctx.fill();
 });
 for(let r=0;r<10;r++)for(let c=0;c<9;c++){
  const p=board[r][c];if(!p)continue;
  const x=pad+c*dx,y=pad+r*dy;
  if(selected&&selected[0]===r&&selected[1]===c){
   ctx.beginPath();ctx.arc(x,y,25,0,Math.PI*2);ctx.fillStyle="#e9bd56";ctx.fill();
  }
  drawPiece(ctx,x,y,22,side(p)==="R"?redPieces[p]:blackPieces[p],side(p));
 }
}
$("board").addEventListener("click",clickBoard);
function init(){
 $("guideContent").innerHTML=tr("guide");
 drawBoardCanvas($("decorBoard"),true);
 changeLanguage("vi");
 newGame();
}
init();
</script>
</body>
</html>
"""

components.html(HTML, height=1150, scrolling=True)

