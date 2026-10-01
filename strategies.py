# strategies.py - 3 SAFE STRATEGIES - ADD ONLY
def ema(data, p):
    if len(data)<p: return [data[-1]] if data else [0]
    k=2/(p+1); vals=[data[0]]
    for x in data[1:]: vals.append(x*k+vals[-1]*(1-k))
    return vals

def rsi_calc(data, per=14):
    if len(data)<per+1: return 50
    g=0; l=0
    for i in range(1,per+1):
        d=data[-i]-data[-i-1]
        if d>0: g+=d
        else: l+=abs(d)
    if l==0: return 100
    return 100-(100/(1+g/l))

def get_signal(candles):
    if len(candles)<25: return {"signal":"HOLD"}
    closes=[c["close"] for c in candles]
    e9=ema(closes,9)[-1]; e21=ema(closes,21)[-1]
    e9p=ema(closes[:-1],9)[-1]; e21p=ema(closes[:-1],21)[-1]
    rsi=rsi_calc(closes,14)
    s1="HOLD"
    if e9>e21 and e9p<=e21p and 45<rsi<68: s1="BUY"
    elif e9<e21 and e9p>=e21p and 32<rsi<55: s1="SELL"
    sma=sum(closes[-20:])/20
    std=(sum([(c-sma)**2 for c in closes[-20:]])/20)**0.5
    up=sma+std*2; low=sma-std*2
    s2="HOLD"
    if closes[-1]<=low and rsi<32: s2="BUY"
    elif closes[-1]>=up and rsi>68: s2="SELL"
    highs=[c["high"] for c in candles]; lows=[c["low"] for c in candles]
    ph=max(highs[-20:-1]); pl=min(lows[-20:-1])
    s3="HOLD"
    if highs[-1]>ph+0.6 and closes[-1]<ph and rsi>70: s3="SELL"
    elif lows[-1]<pl-0.6 and closes[-1]>pl and rsi<30: s3="BUY"
    if [s1,s2,s3].count("BUY")>=2: return {"signal":"BUY","strategies":[s1,s2,s3]}
    if [s1,s2,s3].count("SELL")>=2: return {"signal":"SELL","strategies":[s1,s2,s3]}
    return {"signal":"HOLD","strategies":[s1,s2,s3]}
