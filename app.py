import os
from flask import Flask, Response

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prince Gold Master V4 Elite</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#070709;color:#fff;font-family:Inter,sans-serif;text-align:center}
.header{padding:30px;background:#0e0e10;border-bottom:2px solid #FFD700}
h1{font-family:Orbitron,sans-serif;font-size:38px;color:#FFD700;letter-spacing:3px}
h1 span{color:#fff}
.badge{margin-top:10px;display:inline-block;border:1px solid #FFD700;padding:5px 14px;border-radius:20px;font-size:11px;letter-spacing:2px;color:#FFD700}
.hero{padding:20px}
.hero img{width:100%;max-width:900px;border-radius:18px;border:2px solid #FFD700;box-shadow:0 0 30px rgba(255,215,0,.3)}
.card{max-width:680px;margin:30px auto;background:#121214;border:1px solid #222;border-radius:18px;padding:28px}
.dot{color:#00ff88;font-weight:700}
.price{font-family:Orbitron;font-size:42px;color:#FFD700;margin:15px 0}
.btn{display:block;width:100%;padding:18px;margin:12px 0;border-radius:12px;font-weight:800;text-decoration:none;font-size:16px}
.btn-gold{background:linear-gradient(90deg,#FFD700,#FFA500);color:#000}
.btn-dark{background:#1e1e20;color:#FFD700;border:1px solid #FFD700}
.small{color:#777;font-size:11px;margin-top:15px}
</style>
</head>
<body>
<div class="header">
<h1>PRINCE<span>GOLD</span></h1>
<div class="badge">V4 ELITE • LIVE • MT5 READY</div>
</div>
<div class="hero">
<img src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1200" alt="Gold">
</div>
<div class="card">
<div class="dot">● BOT ACTIVE — V4 ELITE</div>
<div class="price">GOLD BOT</div>
<p style="color:#bbb">Professional Gold Trading AI<br>Scalper + H1 Swing + News Filter + MT5 Bridge</p>
<a class="btn btn-gold" href="#">START TRADING - V4</a>
<a class="btn btn-dark" href="/health">CHECK STATUS</a>
<p class="small">prince-gold.onrender.com • Render • 2026<br>Build: V4 Elite Master</p>
</div>
</body>
</html>
