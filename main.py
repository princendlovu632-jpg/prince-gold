import os
from flask import Flask, request, jsonify, render_template_string
from prince_menu import DOTS_MENU

app = Flask(__name__)

@app.route('/')
def home():
    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>PRINCE GOLD BOT</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="background:#000;color:#FFD700;font-family:Arial;margin:0;padding:20px;position:relative;min-height:100vh;">
{DOTS_MENU}
<h1 style="text-align:center;color:#FFD700;">PRINCE GOLD TRADING SYSTEM</h1>
<p style="text-align:center;">XM 411308190</p>

<div id="bot-content" style="margin-top:50px;">
<!-- YOUR EXISTING BOT CONTENT STAYS HERE -->
<p>Bot is Running...</p>
</div>

<script>
// YOUR EXISTING SCRIPTS HERE
</script>
</body>
</html>
"""
    return render_template_string(html)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
