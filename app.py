import os, time, hmac, hashlib, base64
from flask import Flask, Response, request, jsonify
from strategies import get_signal
app=Flask(__name__)
1  import os, time, hmac, hashlib, base64
2  from flask import Flask, Response, request
3  from strategies import get_signal
4  app=Flask(__name__)
5  from flask import jsonify
6  @app.route("/api/signal", methods=["POST"])
7  def signal_api():
8      j=request.get_json() or {}
9      candles=j.get("candles",[{"open":2650,"high":2652,"low":2649,"close":2651}]*30)
10     return jsonify(get_signal(candles))
11
12 LOGO_B64=(




LOGO_B64=(
"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"
"AAA="
)

def gen_license():
    w=int(time.time()//30)
    m=str(w).encode()
    d=hmac.new(MASTER_SECRET.encode(), m, hashlib.sha256).digest()
    c=str(int.from_bytes(d[:4], 'big') % 1000000).zfill(6)
    return c, 30 - int(time.time() % 30)

def check_license(k):
    for w in [int(time.time()//30), int(time.time()//30)-1]:
        m=str(w).encode()
        d=hmac.new(MASTER_SECRET.encode(), m, hashlib.sha256).digest()
        v=str(int.from_bytes(d[:4], 'big') % 1000000).zfill(6)
        if hmac.compare_digest(v, k):
            return True
    return False

@app.route('/logo')
def logo():
    return Response(base64.b64decode(LOGO_B64), mimetype='image/webp')

@app.route('/api/generate-key')
def api_gen():
    s=request.args.get('secret','')
    if s!=MASTER_SECRET:
        return jsonify({"error":"Invalid master secret"}), 403
    c,e=gen_license()
    return jsonify({"license_key":c,"expires_in_sec":e})

@app.route('/api/verify-key', methods=['POST'])
def api_verify():
    d=request.get_json() or {}
    return jsonify({"valid":check_license(d.get('key',''))})

@app.route('/')
def home():
    return '''<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial}body{background:#080c14;color:#c8d2e0}
.top{height:42px;display:flex;justify-content:space-between;align-items:center;padding:0 14px;background:#0d121c;border-bottom:1px solid #1a2535;font-size:11px;color:#5a6d85}
.header{padding:22px 16px 18px;text-align:center;background:radial-gradient(ellipse 80% 70% at 50% 0%,#1c2e45 0%,#121a28 40%,#080c14 100%)}
.lw{width:108px;height:108px;margin:0 auto 14px;border-radius:50%;border:2.5px solid #FFD700;box-shadow:0 0 32px rgba(255,215,0,.9);overflow:hidden;background:#000}
.lw img{width:100%;height:100%;object-fit:cover;border-radius:50%}
.st{color:#FFD700;font-size:9px;letter-spacing:3px;font-weight:700;margin-bottom:6px}.bt{color:#FFD700;font-size:22px;font-weight:900;margin-bottom:5px}.live{color:#7a8da6;font-size:11px}
.card{background:#121a27;border:1px solid #1e2d40;border-radius:12px;margin:10px 12px;padding:14px}
.ch{font-size:9px;color:#5a6f88;letter-spacing:1.6px;font-weight:700;text-transform:uppercase;margin-bottom:6px}.inst{font-size:14px;font-weight:800}.muted{font-size:11px;color:#5a6f88}
.row{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid #1a2535;font-size:12px}.rl{color:#7a8da6}.rv{font-weight:600}
.meta{color:#FFD700;font-size:9px;letter-spacing:1.4px;font-weight:800;margin:14px 0 8px}.inp{background:#0f1825;border:1px solid #1e2d40;border-radius:8px;padding:11px 12px;color:#fff;width:100%;margin:5px 0;font-size:12px}
.btn{background:linear-gradient(90deg,#FFD700,#ffae00);color:#000;border:none;padding:12px;border-radius:8px;width:100%;font-weight:800;margin-top:10px;cursor:pointer}
.lic{background:#1a1500;border:1.5px solid #FFD700;border-radius:10px;padding:12px;margin:10px 0}.off{background:#1f1212;color:#ff5a5a;border:1px solid #3a1a1a;padding:4px 10px;border-radius:14px;font-size:10px;font-weight:700}.on{background:#0f2818;color:#4ade80;border:1px solid #1e4a2a;padding:4px 10px;border-radius:14px;font-size:10px;font-weight:700}
.footer{text-align:center;padding:18px 12px;color:#3a4a5e;font-size:10px}
</style></head><body>
<div class="top"><span>reed.replit.dev</span><span style="color:#ff4d4d">● Dashboard offline</span></div>
<div class="header"><div class="lw"><img src="/logo"></div><div class="st">AUTOMATED MARKET MONITOR</div><div class="bt">Prince Gold Master V1</div><div class="live">XM 411308190 LIVE</div></div>
<div class="card" style="border-color:#FFD700"><div style="color:#FFD700;font-weight:800">🔑 LICENSE - 30 SEC EXPIRY</div><div style="font-size:11px;color:#8aa0b8;margin:6px 0">Enter 6-digit key - only owner can generate</div><div class="lic"><input id="licKey" class="inp" placeholder="Enter license key" style="text-align:center;letter-spacing:4px;font-size:18px;font-weight:800"><button class="btn" onclick="activate()">ACTIVATE LICENSE</button><div id="licStatus" style="margin-top:8px;font-size:11px;color:#ff6b6b">● No license - Bot locked</div><div style="margin-top:6px;font-size:10px;color:#6b7a90">Expires in <span id="timer">--</span>s | Admin: /api/generate-key?secret=YOUR_SECRET</div></div></div>
<div class="card"><div class="ch">LIVE INSTRUMENT</div><div class="inst">XAUUSD</div><div class="muted" style="margin-top:8px">Current bid price</div><div style="color:#FFD700;margin:6px 0">-- --</div><div class="muted">Last update: Waiting for price data</div></div>
<div class="card"><div style="display:flex;justify-content:space-between;align-items:center"><div><div style="font-size:9px;color:#5a6f88;letter-spacing:1.4px;font-weight:700">CONNECTION</div><div style="font-size:16px;font-weight:800;margin-top:2px" id="connText">LOCKED</div></div><div style="width:10px;height:10px;background:#ff3b3b;border-radius:50%;box-shadow:0 0 10px #ff3b3b" id="dot"></div></div><div class="row"><span class="rl">Account</span><span class="rv">XM 411308190</span></div><div class="row"><span class="rl">Status</span><span class="rv" id="statusTxt" style="color:#ff4d4d">NO LICENSE</span></div></div>
<div class="card"><div style="font-weight:700">Bot activity</div><div class="muted">Auto-refreshes every 2 seconds</div></div>
<div class="card"><div style="font-weight:700">Settings</div><div class="meta">METAAPI CONNECTION</div><input class="inp" value="XM 411308190"><input class="inp" value="XAUUSD"><input class="inp" value="****" type="password"><div style="margin-top:8px"><span class="off" id="badge">OFFLINE</span></div><div class="meta" style="margin-top:16px">RISK SETTINGS</div><div class="row"><span class="rl">Lot Size</span><span style="color:#FFD700;font-weight:800" id="lv">0.01</span></div><input type="range" min="0.01" max="1" step="0.01" value="0.01" style="width:100%;accent-color:#FFD700" oninput="document.getElementById('lv').innerText=this.value"><input class="inp" value="300" placeholder="Stop Loss"><input class="inp" value="600" placeholder="Take Profit"><input class="inp" value="50" placeholder="Max Daily Loss"></div>
<div class="footer">Built by Boss Prince | Durban SA | XAUUSD Scalper</div>
<script>
async function activate(){
  const k=document.getElementById('licKey').value.trim();
  if(!k){alert('Enter key');return}
  const r=await fetch('/api/verify-key',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({key:k})});
  const j=await r.json();
  if(j.valid){
    document.getElementById('licStatus').innerHTML='<span style=color:#4ade80>● VALID - Unlocked!</span>';
    document.getElementById('statusTxt').innerText='UNLOCKED';document.getElementById('statusTxt').style.color='#4ade80';
    document.getElementById('connText').innerText='ONLINE';document.getElementById('dot').style.background='#4ade80';
    document.getElementById('badge').innerText='ONLINE';document.getElementById('badge').className='on';
    localStorage.setItem('prince_lic',k);alert('✅ License OK! Bot unlocked!');
  }else{
    document.getElementById('licStatus').innerHTML='<span style=color:#ff4d4d>● INVALID OR EXPIRED</span>';
    alert('❌ Invalid/Expired - Key changes every 30 sec');
  }
}
setInterval(()=>{document.getElementById('timer').innerText=30 - Math.floor(Date.now()/1000 %30)},1000);
</script></body></html>'''

if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",10000)))
    
