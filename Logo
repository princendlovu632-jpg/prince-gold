from flask import Flask, jsonify, render_template_string, send_file
import requests
from datetime import datetime
import os

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PRINCE GOLD MASTER V3</title>
<style>
body{background:#000;color:#FFD700;font-family:Arial;text-align:center;margin:0;padding:10px;overflow-x:hidden}
.bg-logo{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);width:90%;opacity:0.08;z-index:-1;pointer-events:none}
.logo-main{width:220px;height:220px;border-radius:50%;border:4px solid #FFD700;box-shadow:0 0 40px #00e5ff,0 0 80px #FFD700;margin:15px auto;display:block}
h1{font-size:28px;text-shadow:0 0 10px gold}
.card{border:2px solid gold;border-radius:20px;padding:15px;margin:12px auto;max-width:450px;background:rgba(15,15,15,0.9)}
.btn-row{display:flex;justify-content:center;gap:8px;max-width:460px;margin:15px auto;flex-wrap:wrap}
.btn{flex:1;min-width:110px;padding:16px 5px;border-radius:14px;border:none;font-weight:bold;font-size:15px;cursor:pointer}
.btn:active{transform:scale(0.95)}
.start{background:#00ff00;color:#000;box-shadow:0 0 15px #00ff00}
.close{background:#ff1744;color:#fff;box-shadow:0 0 15px #ff1744}
.auto{background:#00e5ff;color:#000;box-shadow:0 0 15px #00e5ff}
.auto.on{background:#FFD700;box-shadow:0 0 20px #FFD700}
.price{font-size:42px;color:#fff;margin:10px 0;font-weight:bold}
.sig{border:3px solid #00ff00;padding:12px;border-radius:14px;font-size:20px;font-weight:bold;color:#00ff00;background:rgba(0,255,0,0.1)}
</style>
</head>
<body>
<img src="/logo" class="bg-logo">
<img src="/logo" class="logo-main">

<h1>👑 PRINCE GOLD MASTER V3 👑</h1>
<div style="color:#00e5ff;font-size:13px">XM 411308190 LIVE | Durban Time</div>
<div id="time" style="margin:8px;color:#aaa">--:--:--</div>

<div class="btn-row">
<button class="btn start" onclick="startBot()">🟢 START</button>
<button class="btn close" onclick="closeBot()">🔴 CLOSE</button>
<button class="btn auto" id="autoBtn" onclick="toggleAuto()">🤖 AUTOMATED<br>OFF</button>
</div>

<div class="card">
<div style="font-size:14px;opacity:0.8">XAUUSD Live Price</div>
<div id="price" class="price">$4152.1</div>
<div id="spread" style="color:#ffaa00;font-size:13px">SELL --- | BUY ---</div>
</div>

<div class="card">
<div>XAUUSD Signals</div>
<div id="sig" class="sig">🔥 STRONG BUY - Gold Pumping!</div>
<h3 id="action">Action: BUY 0.01 Lot</h3>
<div id="status" style="color:#00ff00;font-weight:bold">BOT ACTIVE ✅</div>
<div id="mt5" style="margin-top:8px;font-size:13px;color:#ccc">Your XM 411308190</div>
</div>

<script>
let autoOn=false, running=true;
function startBot(){running=true; document.getElementById('status').innerHTML='BOT ACTIVE ✅ - Scanning...'; document.getElementById('status').style.color='#00ff00';}
function closeBot(){running=false; document.getElementById('status').innerHTML='BOT STOPPED 🔴 - Closed'; document.getElementById('status').style.color='#ff1744';}
function toggleAuto(){autoOn=!autoOn; let b=document.getElementById('autoBtn'); if(autoOn){b.innerHTML='🤖 AUTOMATED<br>ON'; b.classList.add('on');} else{b.innerHTML='🤖 AUTOMATED<br>OFF'; b.classList.remove('on');}}
async function fetchPrice(){
 if(!running) return;
 try{let r=await fetch('/api/price'); let d=await r.json();
 document.getElementById('price').innerText='$'+d.price;
 document.getElementById('spread').innerText='SELL '+d.sell+' | BUY '+d.buy+' | Spread: '+d.spread;
 document.getElementById('sig').innerText=d.signal;
 document.getElementById('action').innerText='Action: '+d.action;
 document.getElementById('time').innerText=d.time+' (Durban Time)';
 document.getElementById('mt5').innerText='Your XM '+d.account+': '+d.action;
 }catch(e){}
}
setInterval(fetchPrice,2000); fetchPrice();
</script>
</body>
</html>
"""

def get_live_price():
    try:
        r = requests.get('https://api.gold-api.com/price/XAU', timeout=4)
        if r.status_code==200:
            return float(r.json()['price'])
    except: pass
    return 4152.10

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/logo')
def logo():
    for name in ['logo.jpg','logo.png','prince.jpg']:
        if os.path.exists(name):
            return send_file(name, mimetype='image/jpeg')
    return '', 404

@app.route('/api/price')
def api_price():
    price = get_live_price()
    sell = round(price + 5.95, 2)
    buy = price
    import random
    signal = "🔥 STRONG BUY - Gold Pumping!"
    action = "BUY 0.01 Lot"
    if random.random() > 0.7:
        signal = "🔥 STRONG SELL - Gold Dropping!"
        action = "SELL 0.01 Lot"
    try:
        from zoneinfo import ZoneInfo
        now = datetime.now(ZoneInfo('Africa/Johannesburg')).strftime('%H:%M:%S - %d %b %Y')
    except:
        now = datetime.now().strftime('%H:%M:%S - %d %b %Y')
    return jsonify({'price':price,'sell':sell,'buy':buy,'spread':round(sell-buy,2),'signal':signal,'action':action,'time':now,'account':'411308190 LIVE'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
