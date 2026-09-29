from flask import Flask, request, jsonify, render_template_string
import os, random, datetime

app = Flask(__name__)
VERIFY_TOKEN = "prince123"
users = set()

def get_gold_signal():
    price = round(random.uniform(2640, 2680), 2)
    change = round(random.uniform(-5, 5), 2)
    trend = "BUY" if change > 0 else "SELL"
    strength = random.choice(["STRONG", "MODERATE"])
    return price, change, trend, strength

HTML = """
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prince Gold</title>
<style>
body{background:#0a0a0a;color:#fff;font-family:Arial;padding:15px}
.card{background:#1a1a1a;border:1px solid #d4af37;border-radius:15px;padding:20px;margin:15px 0}
.gold{color:#d4af37;font-size:36px;font-weight:bold}
.buy{color:#00ff88;font-size:26px}.sell{color:#ff4444;font-size:26px}
.btn{background:#d4af37;color:#000;padding:12px 20px;border-radius:20px;text-decoration:none;font-weight:bold}
</style>
</head>
<body>
<h1>PRINCE GOLD BOT</h1>
<p>LIVE Trading Bot</p>
<div class="card">
<h3>XAUUSD / GOLD</h3>
<div class="gold">${{price}}</div>
<p>Change: {{change}} | {{trend}} {{strength}}</p>
<div class="{{'buy' if trend=='BUY' else 'sell'}}">{{trend}} SIGNAL</div>
<p>{{time}}</p>
</div>
<div class="card">
<p>Status: <b style="color:#0f8">LIVE</b></p>
<p>Users: {{users}} | Webhook: /webhook Ready</p>
</div>
<div class="card">
<h3>WhatsApp Commands</h3>
<p>GOLD = Signal<br>PRICE = Price<br>HELP = Menu</p>
</div>
<script>setTimeout(()=>location.reload(),30000)</script>
</body>
</html>
"""

@app.route('/')
def home():
    return "Prince Gold Bot is Live
