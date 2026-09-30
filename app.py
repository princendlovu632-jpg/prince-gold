import os, time, hmac, hashlib, base64, json
from flask import Flask, Response, request, jsonify
app=Flask(__name__)

MASTER_SECRET="PRINCE-GOLD-XM411308190-DURBAN-2026"
# Luxury pricing
PRICES={"weekly":700, "monthly":2500, "yearly":25000}

LOGO_B64=(
"[STRIPPED 80 bytes]"
"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"
"HNeA3v1sgBel1AgHyV5LgIxgAAA="
)

def gen_license(plan="weekly"):
    window=int(time.time()//30)
    msg=f"{window}:{plan}".encode()
    dig=hmac.new(MASTER_SECRET.encode(), msg, hashlib.sha256).digest()
    code=str(int.from_bytes(dig[:4], 'big') % 1000000).zfill(6)
    return code, 30 - int(time.time() % 30)

def check_license(k, plan="weekly"):
    for w in [int(time.time()//30), int(time.time()//30)-1]:
        for p in ["weekly","monthly","yearly","demo"]:
            m=f"{w}:{p}".encode()
            d=hmac.new(MASTER_SECRET.encode(), m, hashlib.sha256).digest()
            v=str(int.from_bytes(d[:4], 'big') % 1000000).zfill(6)
            if hmac.compare_digest(v, k):
                return True, p
    return False, None

@app.route('/logo')
def logo():
    return Response(base64.b64decode(LOGO_B64), mimetype='image/webp')

@app.route('/
