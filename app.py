@app.route("/")
def home():
    html = f"""
    <html><head><title>Prince Gold</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    .top-bar{{display:flex;justify-content:space-between;align-items:center;padding:10px 20px;}}
    .dots{{font-size:28px;color:#FFD700;cursor:pointer;user-select:none;position:relative}}
    .dropdown{{display:none;position:absolute;right:0;top:35px;background:#111;border:1px solid #FFD700;border-radius:8px;min-width:160px;z-index:999}}
    .dropdown a{{display:block;padding:12px;color:#FFD700;text-decoration:none;font-size:14px;border-bottom:1px solid #333}}
    .dropdown a:hover{{background:#222}}
    .show{{display:block}}
    </style>
    </head>
    <body style="background:#000;color:#FFD700;text-align:center;font-family:Arial;margin:0;padding:0">
    
    <div class="top-bar">
        <div></div>
        <div class="dots" onclick="toggleMenu()">⋮
            <div id="menu" class="dropdown">
                <!-- EMPTY FOR NOW BOSS - YOU WILL TELL ME WHAT TO PUT -->
            </div>
        </div>
    </div>

    <img src="data:image/png;base64,{LOGO_B64[1:-1] if len(LOGO_B64)>1 else LOGO_B64}" style="width:150px"/>
    <h1>PRINCE GOLD BOT</h1>
    <h2>XM: 411308190</h2>
    <p>3 Strategies: SAFE SCALP (78%) + RANGE BOUNCE (82%) + LIQUIDITY GUARD (90%)</p>
    <p>Master needs 2 to agree = SAFE</p>
    <p style="color:lime">STATUS: ONLINE ✅</p>
    
    <script>
    function toggleMenu(){{
        document.getElementById("menu").classList.toggle("show");
    }}
    window.onclick = function(e){{
        if (!e.target.matches('.dots')){{
            var m=document.getElementById("menu");
            if(m.classList.contains('show')) m.classList.remove('show');
        }}
    }}
    </script>
    </body></html>
    """
    return Response(html, mimetype='text/html')
