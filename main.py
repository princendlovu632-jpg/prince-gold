import os
from flask import Flask, Response
import base64

LOGO = (
"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"
"HNeA3v1sgBel1AgHyV5LgIxgAAA="
)

app=Flask(__name__)

@app.route('/logo')
def logo():
    return Response(base64.b64decode(LOGO), mimetype='image/webp')

@app.route('/')
def home():
    return '''<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1"><style>
*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Arial}
body{background:#070b12;color:#d0d9e6;min-height:100vh}
.topbar{padding:10px 14px;display:flex;justify-content:space-between;align-items:center;background:#0a0f1a;border-bottom:1px solid #151d2a;font-size:11px;color:#6b7a90}
.live-dot{width:6px;height:6px;background:#ff3b3b;border-radius:50%;display:inline-block;margin-right:6px;box-shadow:0 0 8px #ff3b3b}
.header{padding:18px 16px 20px;text-align:center;background:radial-gradient(ellipse at center top,#1a2a3a 0%,#0e1520 45%,#070b12 80%);position:relative;overflow:hidden;border-bottom:1px solid #1a2332}
.header::before{content:"";position:absolute;top:0;left:0;right:0;bottom:0;background:repeating-linear-gradient(90deg,transparent,transparent 80px,rgba(255,215,0,0.02) 80px,rgba(255,215,0,0.02) 81px);pointer-events:none}
.lw{width:110px;height:110px;margin:8px auto 14px;border-radius:50%;border:2.5px solid #FFD700;box-shadow:0 0 35px rgba(255,215,0,0.85),0 0 15px rgba(255,215,0,0.5),inset 0 0 20px rgba(0,0,0,0.8);overflow:hidden;background:#000;position:relative;z-index:1}
.lw img{width:100%;height:100%;object-fit:cover;border-radius:50%}
.offline-badge{position:absolute;top:14px;right:14px;background:rgba(0,0,0,0.6);border:1px solid #2a1a1a;color:#ff6b6b;padding:4px 8px;border-radius:12px;font-size:9px;display:flex;align-items:center;gap:5px;backdrop-filter:blur(4px);z-index:2}
.st{color:#FFD700;font-size:9px;letter-spacing:3.2px;font-weight:700;margin-bottom:6px;opacity:0.9;position:relative;z-index:1}
.bt{color:#FFD700;font-size:22px;font-weight:900;margin:4px 0 4px;letter-spacing:0.3px;position:relative;z-index:1;text-shadow:0 0 20px rgba(255,215,0,0.4)}
.live{color:#8aa0b8;font-size:11px;font-weight:500;position:relative;z-index:1}
.card{background:#121a27;border:1px solid #1e2a3a;border-radius:12px;margin:10px 12px;padding:14px;position:relative}
.card-title{font-size:9px;color:#6b7a90;letter-spacing:1.8px;font-weight:700;text-transform:uppercase;margin-bottom:8px}
.instrument{font-size:15px;font-weight:800;color:#e8eef7;letter-spacing:0.2px}
.bid-row{display:flex;justify-content:space-between;align-items:center;margin:14px 0 8px}
.bid-label{font-size:11px;color:#8aa0b8}
.bid-dots{display:flex;gap:4px}
.bid-dot{width:10px;height:4px;background:#FFD700;border-radius:2px;display:inline-block}
.muted{color:#6b7a90;font-size:11px}
.conn-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
.conn-title{font-size:9px;color:#6b7a90;letter-spacing:1.5px;font-weight:700}
.conn-value{font-size:16px;font-weight:800;color:#fff;margin-top:2px}
.red-dot{width:10px;height:10px;background:#ff3b3b;border-radius:50%;box-shadow:0 0 10px #ff3b3b}
.row{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid #1a2535;font-size:12px}
.row:last-child{border-bottom:none}
.row-label{color:#8aa0b8;font-size:12px}
.row-value{font-weight:600;color:#e8eef7;font-size:12px}
.bot-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.bot-title{font-weight:700;font-size:13px}
.bot-sub{font-size:10px;color:#6b7a90}
.settings-header{display:flex;justify-content:space-between;align-items:center;cursor:pointer}
.settings-title{font-weight:700;font-size:13px}
.settings-sub{font-size:10px;color:#6b7a90}
.meta-label{color:#FFD700;font-size:9px;letter-spacing:1.5px;font-weight:800;margin:14px 0 8px;text-transform:uppercase}
.inp{background:#0e1622;border:1px solid #1f2d42;border-radius:8px;padding:11px 12px;color:#a0aec0;width:100%;margin:6px 0;font-size:12px;outline:none}
.inp:focus{border-color:#FFD700}
.select{appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' fill='%236b7a90' viewBox='0 0 16 16'%3E%3Cpath d='M8 11L3 6h10z'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 12px center}
.conn-status{display:flex;align-items:center;gap:6px;margin:8px 0}
.status-off{background:#2a1212;color:#ff6b6b;border:1px solid #4a1f1f;padding:4px 10px;border-radius:12px;font-size:10px;font-weight:700;display:inline-flex;align-items:center;gap:5px}
.risk-title{color:#FFD700;font-size:9px;letter-spacing:1.5px;font-weight:800;margin:18px 0 12px;text-transform:uppercase}
.lot-row{display:flex;justify-content:space-between;align-items:center;margin:6px 0 8px}
.lot-label{font-size:12px;color:#8aa0b8}
.lot-value{color:#FFD700;font-weight:800;font-size:13px}
.slider{width:100%;accent-color:#FFD700;height:4px;margin:8px 0 14px;background:#1a2535;border-radius:2px}
.pill{background:#0f2a1f;color:#4ade80;border:1px solid #1f4a2f;border-radius:12px;padding:3px 10px;font-size:10px;font-weight:800;display:inline-block}
.pill-on{background:#0f2a1f;color:#4ade80}
.pill-off{background:#2a1212;color:#ff6b6b;border-color:#4a1f1f}
.footer{text-align:center;padding:16px;color:#4b5a6f;font-size:10px;margin-top:8px}
</style></head><body>
<div class="topbar"><span>reed.replit.dev</span><span style="color:#ff6b6b;display:flex;align-items:center"><span class="live-dot"></span>Dashboard offline</span></div>
<div class="header"><div class="offline-badge"><span style="width:6px;height:6px;background:#ff3b3b;border-radius:50%;display:inline-block"></span>Dashboard offline</div><div class="lw"><img src="/logo" alt="Prince"></div><div class="st">AUTOMATED MARKET MONITOR</div><div class="bt">Prince Gold Master V1</div><div class="live">XM 411308190 LIVE</div></div>
<div class="card"><div class="card-title">LIVE INSTRUMENT</div><div class="instrument">XAUUSD</div><div class="bid-row"><div class="bid-dots"><span class="bid-dot"></span><span class="bid-dot"></span></div></div><div style="font-size:12px;color:#8aa0b8;margin:6px 0 4px">Current bid price</div><div style="height:22px"></div><div class="muted">Last update: Waiting for price data</div></div>
<div class="card"><div class="conn-header"><div><div class="conn-title">CONNECTION</div><div class="conn-value">OFFLINE</div></div><div class="red-dot"></div></div><div class="row"><span class="row-label">Account</span><span class="row-value">XM 411308190</span></div><div class="row"><span class="row-label">Symbol</span><span class="row-value">XAUUSD</span></div><div class="row"><span class="row-label">Ask</span><span class="row-value">--</span></div></div>
<div class="card"><div class="bot-header"><div class="bot-title">Bot activity</div><div class="bot-sub">Auto-refreshes every 2 seconds</div></div><div style="height:60px;background:#0a0f1a;border-radius:8px;border:1px solid #1a2535"></div></div>
<div class="card"><div class="settings-header"><div><div class="settings-title">Settings</div><div class="settings-sub">Connection and risk controls</div></div><div style="color:#FFD700">−</div></div><div class="meta-label">MetaApi Connection</div><div style="font-size:11px;color:#8aa0b8;margin-bottom:4px">Account ID</div><input class="inp" value="XM 411308190" readonly><div style="font-size:11px;color:#8aa0b8;margin:8px 0 4px">Symbol</div><select class="inp select"><option>XAUUSD</option><option>EURUSD</option><option>GBPUSD</option></select><div style="font-size:11px;color:#8aa0b8;margin:8px 0 4px">MetaApi Token</div><input class="inp" value="****" type="password" readonly><div style="font-size:11px;color:#8aa0b8;margin:8px 0 4px">Connection Status</div><div class="conn-status"><span class="status-off"><span style="width:6px;height:6px;background:#ff3b3b;border-radius:50%;display:inline-block"></span>OFFLINE</span></div><div class="risk-title">Risk Settings</div><div class="lot-row"><span class="lot-label">Lot Size</span><span class="lot-value">0.01</span></div><input type="range" class="slider" min="0.01" max="1" step="0.01" value="0.01"><div style="font-size:11px;color:#8aa0b8;margin:8px 0 4px">Stop Loss (pips)</div><input class="inp" value="300"><div style="font-size:11px;color:#8aa0b8;margin:8px 0 4px">Take Profit (pips)</div><input class="inp" value="600"><div style="font-size:11px;color:#8aa0b8;margin:8px 0 4px">Max Daily Loss</div><input class="inp" value="50"><div style="display:flex;justify-content:space-between;align-items:center;margin-top:14px"><span style="font-size:12px;color:#8aa0b8">Auto Lot</span><span class="pill pill-on">ON</span></div></div>
<div class="footer">Built by Boss Prince | Durban SA | XAUUSD Scalper</div>
</body></html>'''

if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",10000)))
