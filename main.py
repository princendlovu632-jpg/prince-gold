from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>Prince Gold Bot</title></head>
    <body style="background:#000;color:gold;text-align:center;padding:50px;font-family:Arial">
    <h1>👑 PRINCE GOLD BOT 👑</h1>
    <h2 style="color:white">Status: LIVE ✅</h2>
    <p>Gold Trading Dashboard is Running</p>
    <div style="border:2px solid gold;padding:20px;margin:20px">
    <h3>XAUUSD Signals</h3>
    <p>Waiting for market...</p>
    <p style="color:lime">BOT ACTIVE</p>
    </div>
    <p>by PrinceNdlovu</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
