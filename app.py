import os,time,hmac,hashlib,base64
from flask import Flask,Response,request,jsonify
app=Flask(__name__)
MASTER="PRINCE-GOLD-XM411308190-DURBAN-2026"
LOGO="[STRIPPED 844 bytes]"

# ===== YOUR 3 STRATEGIES ADDED ONLY - NO OTHER CHANGE =====
def ema(data, period):
    if len(data) < period:
        return [data[-1]] if data else [0]
    k=2/(period+1)
    vals=[data[0]]
    for p in data[1:]:
        vals.append(p*k + vals[-1]*(1-k))
    return vals

def rsi_calc(data, period=14):
    if len(data) < period+1:
        return 50
    gains=0;losses=0
    for i in range(1,period+1):
        diff=data[-i]-data[-i-1]
        if diff>0:
            gains+=diff
        else:
            losses+=abs(diff)
    if losses==0:
        return 100
    rs=gains/losses
    return 100-(100/(1+rs))

def strategy_1(candles):
    if len(candles)<25:
        return {"signal":"HOLD"}
    closes=[c["close"] for c in candles]
    e9=ema(closes,9)[-1]
    e21=ema(closes,21)[-1]
    e9p=ema(closes[:-1],9)[-1]
    e21p=ema(closes[:-1],21)[-1]
    rsi=rsi_calc(closes,14)
    if e9>e21 and e9p<=e21p and 45<rsi<68:
        return {"signal":"BUY","sl":closes[-1]-2,"tp":closes[-1]+4,"name":"SAFE_SCALP"}
    if e9<e21 and e9p>=e21p and 32<rsi<55:
        return {"signal":"SELL","sl":closes[-1]+2,"tp":closes[-1]-4,"name":"SAFE_SCALP"}
    return {"signal":"HOLD"}

def strategy_2(candles):
    if len(candles)<20:
        return {"signal":"HOLD"}
    closes=[c["close"] for c in candles]
    sma=sum(closes[-20:])/20
    std=(sum([(c-sma)**2 for c in closes[-20:]])/20)**0.5
    upper=sma+std*2
    lower=sma-std*2
    rsi=rsi_calc(closes,14)
    if closes[-1]<=lower and rsi<32:
        return {"signal":"BUY","sl":closes[-1]-2.5,"tp":sma,"name":"RANGE_BOUNCE"}
    if closes[-1]>=upper and rsi>68:
        return {"signal":"SELL","sl":closes[-1]+2.5,"tp":sma,"name":"RANGE_BOUNCE"}
    return {"signal":"HOLD"}

def strategy_3(candles):
    if len(candles)<25:
        return {"signal":"HOLD"}
    highs=[c["high"] for c in candles]
    lows=[c["low"] for c in candles]
    closes=[c["close"] for c in candles]
    prev_high=max(highs[-20:-1])
    prev_low=min(lows[-20:-1])
    rsi=rsi_calc(closes,14)
    if highs[-1]>prev_high+0.6 and closes[-1]<prev_high and rsi>70:
        return {"signal":"SELL","sl":highs[-1]+1.2,"tp":closes[-1]-6,"name":"LIQUIDITY_GUARD"}
    if lows[-1]<prev_low-0.6 and closes[-1]>prev_low and rsi<30:
        return {"signal":"BUY","sl":lows[-1]-1.2,"tp":closes[-1]+6,"name":"LIQUIDITY_GUARD"}
    return {"signal":"HOLD"}

def master_signal(candles):
    s1=strategy_1(candles)
    s2=strategy_2(candles)
    s3=strategy_3(candles)
    buys=[r for r in [s1,s2,s3] if r["signal"]=="BUY"]
    sells=[r for r in [s1,s2,s3] if r["signal"]=="SELL"]
    if len(buys)>=2:
        return buys[0]
    if len(sells)>=2:
        return sells[0]
    high=[r for r in [s1,s2,s3] if r["signal"]!="HOLD" and r.get("name")=="LIQUIDITY_GUARD"]
    if high:
        return high[0]
    return {"signal":"HOLD"}

# ===== END OF 3 STRATEGIES - REST IS SAME AS BEFORE =====

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

@app.route("/
