from flask import Flask, send_from_directory, Response
import os

app = Flask(__name__)

@app.route('/')
def index():
    return Response("""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Prince Gold Master V4 Elite</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#050507;color:white;font-family:'Inter',sans-serif;overflow-x:hidden}
.phone{max-width:430px;margin:0 auto;min-height:100vh;background:linear-gradient(180deg,#0a0a0f 0%,#000000 100%);position:relative;padding:15px;padding-bottom:100px}
.top-bar{display:flex;justify-content:space-between;align-items:center;padding:10px 5px}
.time{font-weight:800;font-size:18px}
.header-title{font-family:'Orbitron';color:#ff2a2a;text-align:center;font-size:28px;font-weight:800;text-shadow:0 0 15px #ff0000,0 0 30px #ff0000;letter-spacing:2px;margin:5px 0 15px}
.hero-card{border:2px solid #ff2a2a;border-radius:28px;overflow:hidden;box-shadow:0 0 20px rgba(255,0,0,0.5);position:relative;height:340px;background:#000}
.hero-card img{width:100%;height:100%;object-fit:cover}
.bell{position:absolute;top:12px;left:12px;width:46px;height:46px;border-radius:50%;border:2px solid #ff2a2a;background:rgba(0,0,0,0.7);display:flex;align-items:center;justify-content:center;box-shadow:0 0 10px #ff0000;z-index:2}
.notif-panel{margin-top:18px;border:2px solid #ff2a2a;border-radius:28px;padding:20px 15px;background:rgba(10,10,10,0.9);box-shadow:0 0 25px rgba(255,0,0,0.4)}
.notif-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:15px}
.notif-header h2{font-family:'Orbitron';font-size:18px;letter-spacing:1px;text-shadow:0 0 10px #ff0000}
.close-btn{width:44px;height:44px;border-radius:50%;border:2px solid #ff2a2a;background:#000;display:flex;align-items:center;justify-content:center;color:#ff2a2a;font-size:20px;box-shadow:0 0 10px #ff0000;cursor:pointer}
.avatar-wrap{display:flex;justify-content:center;margin:-5px 0 18px}
.avatar{width:82px;height:82px;border-radius:50%;border:3px solid #ff2a2a;overflow:hidden;box-shadow:0 0 20px #ff0000;background:#000}
.avatar img{width:100%;height:100%;object-fit:cover}
.trade-card{border:2px solid #3ab0ff;border-radius:20px;padding:14px 12px;margin-bottom:14px;background:linear-gradient(180deg,rgba(10,20,40,0.8),rgba(5,10,20,0.9));box-shadow:0 0 12px rgba(58,176,255,0.4)}
.trade-card h3{color:#3ab0ff;font-size:17px;font-weight:800;margin-bottom:6px}
.trade-card p{font-size:12.5px;line-height:1.5;color:#d0d0d0}
.fail{color:#ff4d4d;font-weight:700}
.icon-circle{width:52px;height:52px;border-radius:50%;border:2px solid #3ab0ff;display:flex;align-items:center;justify-content:center;float:left;margin-right:10px;margin-top:2px;background:rgba(0,0,0,0.5)}
.bottom-nav{position:fixed;bottom:0;left:0;right:0;max-width:430px;margin:0 auto;background:linear-gradient(180deg,rgba(20,0,0,0.9),rgba(0,0,0,1));border-top:1px solid rgba(255,0,0,0.3);display:flex;justify-content:space-around;align-items:center;padding:12px 10px 18px;box-shadow:0 -10px 30px rgba(255,0,0,0.3);z-index:10}
.nav-item{text-align:center;cursor:pointer}
.nav-circle{width:62px;height:62px;border-radius:50%;border:2px solid #ff2a2a;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:rgba(0,0,0,0.8);box-shadow:0 0 15px rgba(255,0,0,0.5)}
.nav-item.active .nav-circle{background:rgba(255,0,0,0.2);box-shadow:0 0 25px #ff0000;transform:scale(1.1)}
.nav-item span{font-size:10px;color:#ff6b6b;font-weight:700;font-family:'Orbitron'}
.controls{margin-top:15px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}
.btn{padding:14px;border-radius:14px;border:2px solid #ff2a2a;background:#000;color:#ff2a2a;font-family:'Orbitron';font-weight:800;font-size:11px;cursor:pointer;box-shadow:0 0 10px rgba(255,0,0,0.4)}
.btn.active{background:#ff2a2a;color:white}
.status{margin-top:12px;text-align:center;font-family:'Orbitron';font-size:12px;color:#3ab0ff}
.live-dot{display:inline-block;width:8px;height:8px;background:#00ff00;border-radius:50%;box-shadow:0 0 10px #00ff00;margin-right:5px;animation:pulse 1.5s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.3}}
</style>
</head>
<body>
<div class="phone">
<div class="top-bar"><span class="time" id="durbanTime">14:17</span><span>●●● 📶 ⚡ 🔋</span></div>
<div class="header-title">PrinceGold</div>
<div class="hero-card"><div class="bell">🔔</div><img src="/logo.jpg"></div>
<div class="notif-panel">
<div class="notif-header"><h2>NOTIFICATIONS</h2><div class="close-btn">✕</div></div>
<div class="avatar-wrap"><div class="avatar"><img src="/logo.jpg"></div></div>
<div id="tradesContainer">
<div class="trade-card"><div class="icon-circle">↗️</div><h3>System Ready</h3><p>Prince Gold Master V4 Elite initialized<br>MT5 411308190 • Razor Markets<br><span style="color:#00ff88">READY — Waiting for signal</span><br><span id="time1">29/09/2026</span></p></div>
</div>
<div class="controls">
<button class="btn" id="startBtn" onclick="startBot()">START</button>
<button class="btn" id="closeBtn" onclick="closeTrades()">CLOSE</button>
<button class="btn active" id="autoBtn" onclick="toggleAuto()">AUTO ON</button>
</div>
<div class="status"><span class="live-dot"></span><span id="statusText">LIVE • Durban Time • V4 Elite</span></div>
</div>
</div>
<div class="bottom-nav">
<div class="nav-item"><div class="nav-circle">📈</div><span>METATRADER</span></div>
<div class="nav-item active"><div class="nav-circle">🏠</div><span>HOME</span></div>
<div class="nav-item"><div class="nav-circle">⚙️</div><span>SETTINGS</span></div>
</div>
<script>
function updateDurbanTime(){const now=new Date().toLocaleString('en-ZA',{timeZone:'Africa/Johannesburg',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false});document.getElementById('durbanTime').textContent=now;}
setInterval(updateDurbanTime,1000);updateDurbanTime();
let autoOn=true,botRunning=false;
function startBot(){botRunning=true;document.getElementById('startBtn').classList.add('active');document.getElementById('statusText').textContent='RUNNING • Scanning Gold...';addTrade('BUY','XAUUSD.mic','Signal detected');fetch('/start').catch(()=>{});}
function closeTrades(){botRunning=false;document.getElementById('startBtn').classList.remove('active');document.getElementById('statusText').textContent='CLOSED';addTrade('CLOSE','ALL','Closed by user','success');fetch('/close').catch(()=>{});}
function toggleAuto(){autoOn=!autoOn;document.getElementById('autoBtn').textContent=autoOn?'AUTO ON':'AUTO OFF';document.getElementById('autoBtn').classList.toggle('active',autoOn);}
function addTrade(type,symbol,msg,status='failed'){const c=document.getElementById('tradesContainer');const time=new Date().toLocaleString('en-GB',{timeZone:'Africa/Johannesburg'});const card=document.createElement('div');card.className='trade-card';const color=status==='success'?'#00ff88':'#ff4d4d';card.innerHTML=`<div class="icon-circle">${type==='BUY'?'↗️':type==='SELL'?'↘️':'✅'}</div><h3 style="color:${status==='success'?'#00ff88':'#3ab0ff'}">Trade ${status==='success'?'Closed':'Executed'}</h3><p>Prince Gold ${type} ${symbol}<br>0.01 lot • MT5 411308190 • Razor<br><span style="color:${color}">${status==='success'?'SUCCESS':'FAILED'} — ${msg}</span><br>${time}</p>`;c.prepend(card);}
</script>
</body>
</html>""", mimetype='text/html')

@app.route('/logo.jpg')
def logo():
    if os.path.exists('logo.jpg'):
        return send_from_directory('.', 'logo.jpg')
    return '', 302, {'Location': 'https://raw.githubusercontent.com/princendlovu632-jpg/prince-gold/main/logo.jpg'}

@app.route('/start')
def start():
    return 'Bot Started - V4 Elite'

@app.route('/close')
def close():
    return 'Bot Closed'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
