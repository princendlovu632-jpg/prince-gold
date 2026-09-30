import os,time,hmac,hashlib,base64
from flask import Flask,Response,request,jsonify
app=Flask(__name__)
MASTER="PRINCE-GOLD-XM411308190-DURBAN-2026"
LOGO="UklGRnACAABXRUJQVlA4IGQCAAAwDwCdASpkAGQAPrVUn0unJSKhrRQJYOAWiWcA02MwzgPpAmbv8CCcrHYoUg0Qll8FmnSSut3gCzFp8ALCR4yCSGXPGy+AdAPNBMXfkPr7PNjSX2Wkz4upLiyvFiBZGA8YK2XQOmDuIDypN7qZyhuripLOKhObFvXEDk/1iG9HgPgAAP74ULOgiJFo1vqTklCgjbOwpu5s/uvIEICREXbJjBDlIz7mpoUSHAsLUIVe+RHLfmuk4uDQ/LoyUQ3x7MiVhg9JQf/7hISOvTwxDugADvcG8Qxvnaa/P+YWq2QLxsPWOYNgRCqgk5z0VsdvrHFa0qeNhLcuOxtKzw6GKn+ivE4+5+z6v9AK8NxRhHkXeR3KCXFlQO42ZQ1KuzSDWSmBHLGQ6TamHrbV3tr/n+yKQm+tLW28T6T/X8KmVvN3ibpCywS2qqkEf0Sc1YUvZ6cSU/nhgtMRNouTSPYtpJ6/B6cgj0jzoeKC0hMSfO4AB7XhTrDQEGI/TElh7jqrq3pBH+aH1dbj9yJ912FBcjBejCdA6S7fVjo5ob7PMfn56YB9S6VygiuFNmyAPdrfxdVKZBbDW9oPl+zp5ZPKBJS6tOr8bL0TnFva4ad85BJAvFVHJhT+mAAOsC21O8PvLtytqm8hnN+nDeoZQpDLcHPLCtXqx7hTKztdAFZ5RayFlcbXXPjuAIbbKVDleyfkfF9r05rGvzPsSaFn0o9Ic0gq+XT/cbWCnh+eQySe02DOva1YYYm7heR/ES61yhe9XLooIDfZ4bFphU7ShFeZumqG0vY9tZl12mYqkOOvi2s41NAAAAA="

def gen(p):
    w=int(time.time()//30)
    d=hmac.new(MASTER.encode(),f"{w}:{p}".encode(),hashlib.sha256).digest()
    return str(int.from_bytes(d[:4],"big")%1000000).zfill(6),30-int(time.time()%30)

def check(k):
    for w in [int(time.time()//30),int(time.time()//30)-1]:
        for p in ["weekly","monthly","yearly","demo"]:
            d=hmac.new(MASTER.encode(),f"{w}:{p}".encode(),hashlib.sha256).digest()
            v=str(int.from_bytes(d[:4],"big")%1000000).zfill(6)
            if hmac.compare_digest(v,k):
                return True,p
    return False,None

@app.route("/logo")
def logo():
    return Response(base64.b64decode(LOGO),mimetype="image/webp")

@app.route("/api/generate-key")
def genkey():
    s=request.args.get("secret","")
    p=request.args.get("plan","weekly")
    if s!=MASTER:
        return jsonify({"error":"Invalid"}),403
    c,e=gen(p)
    price={"weekly":700,"monthly":2500,"yearly":25000}.get(p,700)
    return jsonify({"license_key":c,"plan":p,"price":price,"expires_in":e})

@app.route("/api/verify-key",methods=["POST"])
def verify():
    j=request.get_json() or {}
    ok,pl=check(j.get("key",""))
    return jsonify({"valid":ok,"plan":pl})

@app.route("/")
def home():
    return '<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style>*{margin:0;padding:0;box-sizing:border-box;font-family:Arial}body{background:#080c14;color:#c8d2e0}.top{height:42px;display:flex;justify-content:space-between;align-items:center;padding:0 14px;background:#0d121c;border-bottom:1px solid #1a2535;font-size:11px;color:#5a6d85}.header{padding:24px 16px;text-align:center;background:radial-gradient(ellipse 80% 70% at 50% 0%,#1c2e45 0%,#121a28 40%,#080c14 100%)}.lw{width:108px;height:108px;margin:0 auto 14px;border-radius:50%;border:2.5px solid #FFD700;box-shadow:0 0 32px rgba(255,215,0,.9);overflow:hidden;background:#000}.lw img{width:100%;height:100%;object-fit:cover;border-radius:50%}.st{color:#FFD700;font-size:9px;letter-spacing:3px;font-weight:700}.bt{color:#FFD700;font-size:22px;font-weight:900}.live{color:#7a8da6;font-size:11px}.card{background:#121a27;border:1px solid #1e2d40;border-radius:12px;margin:10px 12px;padding:14px}.lux{border:1.5px solid #FFD700;background:linear-gradient(145deg,#1a1600 0%,#121a27 100%);box-shadow:0 0 25px rgba(255,215,0,.15)}.price{border:1px solid #1e2d40;border-radius:10px;padding:12px;margin:8px 0;display:flex;justify-content:space-between;align-items:center;cursor:pointer}.price.pop{border-color:#FFD700;background:linear-gradient(145deg,#1a1600 0%,#121a27 100%)}.badge{background:linear-gradient(90deg,#FFD700,#ffae00);color:#000;font-size:8px;font-weight:900;padding:3px 8px;border-radius:4px}.inp{background:#0f1825;border:1px solid #1e2d40;border-radius:8px;padding:11px;color:#fff;width:100%;margin:5px 0}.btn{background:linear-gradient(90deg,#FFD700,#ffae00);color:#000;border:none;padding:12px;border-radius:8px;width:100%;font-weight:900;margin-top:10px;cursor:pointer}.off{background:#1f1212;color:#ff5a5a;padding:4px 10px;border-radius:14px;font-size:10px}.on{background:#0f2818;color:#4ade80;padding:4px 10px;border-radius:14px;font-size:10px}.footer{text-align:center;padding:18px;color:#3a4a5e;font-size:10px}</style></head><body><div class="top"><span>prince-gold.onrender.com</span><span style="color:#ff4d4d">● Dashboard offline</span></div><div class="header"><div class="lw"><img src="/logo"></div><div class="st">AUTOMATED MARKET MONITOR</div><div class="bt">Prince Gold Master V1</div><div class="live">XM 411308190 LIVE</div></div><div class="card lux"><div style="text-align:center;color:#FFD700;font-weight:900;letter-spacing:2px">◆ PRINCE GOLD ELITE ◆</div><div style="text-align:center;color:#8aa0b8;font-size:10px;margin:4px 0 12px">Luxury XAUUSD Scalper • Built for Kings</div><div class="price" onclick="sel(&quot;weekly&quot;)"><div><div style="font-weight:800">WEEKLY ELITE</div><div style="font-size:10px;color:#6b7f99">7 days full access</div></div><div style="text-align:right"><div style="color:#FFD700;font-weight:900;font-size:18px">R700</div><div style="font-size:10px;color:#6b7f99">/ week</div></div></div><div class="price pop" onclick="sel(&quot;monthly&quot;)"><div><div style="font-weight:800">MONTHLY ROYAL <span class="badge">MOST POPULAR</span></div><div style="font-size:10px;color:#6b7f99">30 days • Premium • Priority</div></div><div style="text-align:right"><div style="color:#FFD700;font-weight:900;font-size:18px">R2,500</div><div style="font-size:10px;color:#6b7f99">/ month</div></div></div><div class="price" onclick="sel(&quot;yearly&quot;)"><div><div style="font-weight:800">YEARLY LEGACY</div><div style="font-size:10px;color:#6b7f99">365 days • Lifetime</div></div><div style="text-align:right"><div style="color:#FFD700;font-weight:900;font-size:18px">R25,000</div><div style="font-size:10px;color:#6b7f99">/ year</div></div></div></div><div class="card lux"><div style="color:#FFD700;font-weight:900">🔑 LICENSE - 30 SEC DEMO</div><div style="font-size:11px;color:#8aa0b8;margin:6px 0">Enter 6-digit key - only owner can generate</div><div style="background:#1a1500;border:1.5px solid #FFD700;border-radius:10px;padding:12px;margin:10px 0"><input id="licKey" class="inp" placeholder="Enter license key" style="text-align:center;letter-spacing:4px;font-size:18px;font-weight:800"><button class="btn" onclick="activate()">✦ ACTIVATE LUXURY ACCESS ✦</button><div id="licStatus" style="margin-top:8px;font-size:11px;color:#ff6b6b">● No license - Locked</div><div style="margin-top:6px;font-size:10px;color:#6b7a90">Expires in <span id="timer" style="color:#FFD700;font-weight:800">--</span>s | Plan: <span id="planSel" style="color:#FFD700">Monthly R2500</span></div></div><div style="font-size:9px;color:#4a5a6e">Admin: /api/generate-key?secret=YOUR_SECRET&plan=monthly</div></div><div class="card"><div style="font-size:9px;color:#5a6f88;letter-spacing:1.6px;font-weight:700">LIVE INSTRUMENT</div><div style="font-weight:800">XAUUSD • Gold Spot</div><div style="font-size:11px;color:#5a6f88;margin-top:8px">Current bid price</div><div style="color:#FFD700;margin:6px 0">◆◆ -- -- ◆◆</div><div style="font-size:11px;color:#5a6f88">Waiting for elite feed</div></div><div class="footer">◆ Built by Boss Prince | Durban SA | Luxury XAUUSD Scalper ◆<br><span style="color:#FFD700;font-weight:700">Weekly R700 • Monthly R2500 • Yearly R25000</span><br>Elite only</div><script>let cur="monthly";function sel(p){cur=p;document.getElementById("planSel").innerText=p+" - R"+(p=="weekly"?700:p=="monthly"?"2,500":"25,000")}async function activate(){const k=document.getElementById("licKey").value.trim();if(!k){alert("Enter key");return}const r=await fetch("/api/verify-key",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({key:k})});const j=await r.json();if(j.valid){document.getElementById("licStatus").innerHTML="<span style=color:#4ade80>● VALID - "+j.plan.toUpperCase()+" UNLOCKED! 👑</span>";alert("👑 ELITE ACCESS GRANTED! "+j.plan)}else{document.getElementById("licStatus").innerHTML="<span style=color:#ff4d4d>● INVALID OR EXPIRED</span>";alert("❌ Invalid/Expired - Key changes every 30 sec")}}setInterval(()=>{document.getElementById("timer").innerText=30-Math.floor(Date.now()/1000%30)},1000);</script></body></html>'

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",10000)))
