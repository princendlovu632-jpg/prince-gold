import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return """<html><body style="background:#000;color:gold;text-align:center;padding:50px"><h1>👑 PRINCE GOLD MASTER V1 👑</h1><h2 style="color:white">XAUUSD ELITE</h2><h3 style="color:#00ff88">$4158 - STRONG BUY</h3><button style="background:gold;color:black;padding:20px 50px;font-size:24px;border:none;border-radius:12px;font-weight:bold">V1 LIVE</button></body></html>"""
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",10000)))
