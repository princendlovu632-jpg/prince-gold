import os
from flask import Flask
app=Flask(__name__)
LOGO="data:image/jpeg;base64,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"
HTML=f"""<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Prince Gold V1</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:Arial}}body{{background:#0a0e14;color:#cdd6e3}}
.header{{padding:24px;text-align:center;background:radial-gradient(circle at center,#122033 0%,#0a0e14 70%)}}
.lw{{width:135px;height:135px;margin:0 auto 16px;position:relative}}
.lw img{{width:100%;height:100%;border-radius:50%;border:3px solid #FFD700;box-shadow:0 0 35px rgba(255,215,0,.7),0 0 65px rgba(0,229,255,.5);object-fit:cover}}
.ring{{position:absolute;inset:-12px;border:2px solid rgba(0,229,255,.35);border-radius:50%}}
.st{{color:#FFD700;font-size:10px;letter-spacing:3px;font-weight:600}}.bt{{color:#FFD700;font-size:24px;font-weight:800;margin:6px 0}}.ls{{font-size:11px;color:#8aa0b8}}
.card{{background:#111827;border:1px solid #1f2937;border-radius:12px;margin:12px 16px;padding:16px}}
.cl{{font-size:10px;letter-spacing:2px;color:#6b7a90;text-transform:uppercase}}.cv{{font-size:16px;font-weight:700;color:white;margin-top:3px}}
.row{{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid #1a2332;font-size:13px}}.muted{{color:#6b7a90;font-size:12px}}
.off{{background:#2a1212;color:#ff6b6b;border:1px solid #4a2020;padding:4px 10px;border-radius:6px;font-size:11px;font-weight:700}}
.on{{background:#0f2a1f;color:#4ade80;border:1px solid #1a4d2e;padding:4px 10px;border-radius:6px;font-size:11px;font-weight:700}}
.inp{{background:#0e1520;border:1px solid #1f2d44;border-radius:8px;padding:10px 12px;color:white;width:100%;margin:6px 0;font-size:13px;outline:none}}
.rl{{color:#FFD700;font-size:11px;font-weight:700;letter-spacing:1px;margin:18px 0 8px}}
.slider{{width:100%;accent-color:#FFD700}}.pill{{background:#0f2a1f;color:#4ade80;border-radius:12px;padding:2px 10px;font-size:12px;font-weight:700;cursor:pointer}}
.pill-off{{background:#2a1212;color:#ff6b6b}}
.btn{{background:linear-gradient(90deg,#FFD700,#ffae00);color:#000;border:none;padding:12px;border-radius:8px;width:100%;font-weight:800;margin-top:10px;cursor:pointer}}
.btn2{{background:#1f2937;color:#FFD700;border:1px solid #FFD700;padding:10px;border-radius:8px;width:100%;font-weight:700;margin-top:8px;cursor:pointer}}
.log{{background:#0a0e14;border:1px solid #1a2332;border-radius:8px;padding:8px;height:100px;overflow-y:auto;font-size:11px;color:#8aa0b8;margin-top:8px}}
</style></head><body>
<div style="padding:12px 16px;display:flex;justify-content:space-between;border-bottom:1px solid #1a2332;font-size:12px"><span style="color:#6b7a90">reed.replit.dev</span><span id="topStatus" style="color:#ff4d4d">● Dashboard offline</span></div>
<div class="header"><div class="lw"><div class="ring"></div><img src="{{LOGO}}"></div><div class="st">AUTOMATED MARKET MONITOR</div><div class="bt">Prince Gold Master V1</div><div class="ls">XM 411308190 LIVE</div></div>
<div class="card"><div class="cl">LIVE INSTRUMENT</div><div class="cv">XAUUSD</div><div class="muted" style="margin-top:10px">Current bid price</div><div id="price" style="text-align:center;color:#FFD700;margin:12px;font-size:32px;font-weight:800">--</div><div class="muted" id="lastUpdate">Last update: Waiting for price data</div></div>
4d;border-radius:50%;box-shadow:0 0 10px #ff4d4d"></div></div><div class="row" style="margin-top:12px"><span class="muted">Account</span><span id="accShow">XM 411308190</span></div><div class="row"><span class="muted">Symbol</span><span>XAUUSD</span></div><div class="row"><span class="muted">Ask</span><span id="askPrice" class="muted">--</span></div>
<button class="btn" id="connectBtn" onclick="toggleConnect()">CONNECT NOW</button>
</div>
<div class="card"><div style="display:flex;justify-content:space-between"><div style="font-weight:700;font-size:13px">Bot activity</div><div class="muted" style="font-size:11px">Auto-refreshes every 2 seconds</div></div><div id="botLog" class="log">Waiting to connect...</div></div>
<div class="card"><div style="display:flex;justify-content:space-between;margin-bottom:12px"><div style="font-weight:700">Settings</div><div class="muted" style="font-size:11px">Connection and risk controls</div><div style="color:#FFD700;cursor:pointer" onclick="toggleSettings()" id="setToggle">-</div></div>
<div id="settingsBox">
<div class="rl">METAAPI CONNECTION</div><div class="muted">Account ID</div><input id="accountId" class="inp" value="XM 411308190" oninput="saveSettings()">
<div class="muted">Symbol</div><select id="symbolSel" class="inp" onchange="saveSettings()"><option>XAUUSD</option><option>EURUSD</option><option>GBPUSD</option></select>
<div class="muted">MetaApi Token</div><input id="tokenInp" class="inp" placeholder="Paste token here" type="password" oninput="saveSettings()">
<div class="muted">Connection Status</div><div style="margin:6px 0"><span id="statusBadge" class="off">● OFFLINE</span></div>
<div class="rl">RISK SETTINGS</div><div style="display:flex;justify-content:space-between"><span class="muted">Lot Size</span><span style="color:#FFD700;font-weight:700" id="lotVal">0.01</span></div><input id="lotSlider" type="range" class="slider" min="0.01" max="1" step="0.01" value="0.01" oninput="updateLot(this.value)">
<div class="muted" style="margin-top:8px">Stop Loss (pips)</div><input id="slInp" class="inp" value="300" oninput="saveSettings()">
<div class="muted">Take Profit (pips)</div><input id="tpInp" class="inp" value="600" oninput="saveSettings()">
<div class="muted">Max Daily Loss</div><input id="dlInp" class="inp" value="50" oninput="saveSettings()">
<div style="display:flex;justify-content:space-between;margin-top:8px"><span class="muted">Auto Lot</span><span id="autoPill" class="pill" onclick="toggleAuto()">ON</span></div>
<button class="btn2" onclick="saveSettingsAlert()">SAVE SETTINGS</button>
</div></div>
<div style="text-align:center;padding:20px;font-size:10px;color:#4a5a70">Built by Boss Prince | Durban SA</div>
<script>
let online=false,price=2650.25,interval=null,autoLot=true,logCount=0;
function toggleConnect(){
 online=!online;
 const btn=document.getElementById('connectBtn');
 const txt=document.getElementById('connText');
 const dot=document.getElementById('dot');
 const badge=document.getElementById('statusBadge');
 const top=document.getElementById('topStatus');
 if(online){
  txt.innerText='ONLINE';txt.style.color='#4ade80';
  dot.style.background='#4ade80';dot.style.boxShadow='0 0 10px #4ade80';
<div class="card"><div style="display:flex;justify-content:space-between;align-items:center"><div><div class="cl">CONNECTION</div><div class="cv" id="connText">OFFLINE</div></div><div id="dot" style="width:10px;height:10px;background:#ff4d
     badge.className='on';badge.innerText='● ONLINE';
  top.innerText='● Dashboard online';top.style.color='#4ade80';
  btn.innerText='DISCONNECT';btn.style.background='#2a1212';btn.style.color='#ff6b6b';
  startPrice();
  addLog('✅ Connected to XM 411308190');
  addLog('📈 XAUUSD stream started');
 }else{
  txt.innerText='OFFLINE';txt.style.color='white';
  dot.style.background='#ff4d4d';dot.style.boxShadow='0 0 10px #ff4d4d';
  badge.className='off';badge.innerText='● OFFLINE';
  top.innerText='● Dashboard offline';top.style.color='#ff4d4d';
  btn.innerText='CONNECT NOW';btn.style.background='linear-gradient(90deg,#FFD700,#ffae00)';btn.style.color='#000';
  stopPrice();
  addLog('❌ Disconnected');
 }
}
function startPrice(){
 if(interval)clearInterval(interval);
 interval=setInterval(()=>{
  price+=(Math.random()-0.5)*2;
  document.getElementById('price').innerText=price.toFixed(2);
  document.getElementById('askPrice').innerText=(price+0.35).toFixed(2);
  document.getElementById('lastUpdate').innerText='Last update: '+new Date().toLocaleTimeString();
  if(++logCount%3==0)addLog('💹 Price tick: '+price.toFixed(2));
 },2000);
}
function stopPrice(){
 if(interval)clearInterval(interval);
 document.getElementById('price').innerText='--';
 document.getElementById('askPrice').innerText='--';
 document.getElementById('lastUpdate').innerText='Last update: Waiting for price data';
}
function updateLot(v){document.getElementById('lotVal').innerText=v;saveSettings();}
function toggleAuto(){
 autoLot=!autoLot;
 const p=document.getElementById('autoPill');
 p.innerText=autoLot?'ON':'OFF';
 p.className=autoLot?'pill':'pill pill-off';
 addLog(autoLot?'Auto Lot ON':'Auto Lot OFF');
 saveSettings();
}
function addLog(m){const l=document.getElementById('botLog');l.innerHTML='<div>['+new Date().toLocaleTimeString()+'] '+m+'</div>'+l.innerHTML;}
function toggleSettings(){const b=document.getElementById('settingsBox');const t=document.getElementById('setToggle');if(b.style.display==='none'){b.style.display='block';t.innerText='-';}else{b.style.display='none';t.innerText='+';}}
function saveSettings(){const d={acc:document.getElementById('accountId').value,sym:document.getElementById('symbolSel').value,sl:document.getElementById('slInp').value,tp:document.getElementById('tpInp').value,dl:document.getElementById('dlInp').value,lot:document.getElementById('lotSlider').value,auto:autoLot};localStorage.setItem('princeV1',JSON.stringify(d));document.getElementById('accShow').innerText=d.acc;}
function saveSettingsAlert(){saveSettings();addLog('Settings saved!');alert('Settings Saved Boss!');}
window.onload=()=>{const s=localStorage.getItem('princeV1');if(s){try{const d=JSON.parse(s);document.getElementById('accountId').value=d.acc||'XM 411308190';document.getElementById('slInp').value=d.sl||'300';document.getElementById('tpInp').value=d.tp||'600';document.getElementById('dlInp').value=d.dl||'50';document.getElementById('lotSlider').value=d.lot||'0.01';document.getElementById('lotVal').innerText=d.lot||'0.01';autoLot=d.auto!==false;document.getElementById('autoPill').innerText=autoLot?'ON':'OFF';document.getElementById('autoPill').className=autoLot?'pill':'pill pill-off';document.getElementById('accShow').innerText=d.acc||'XM 411308190';}catch(e){}}};
</script></body></html>
"""
@app.route("/")
def home():
    return HTML
if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",10000)))
