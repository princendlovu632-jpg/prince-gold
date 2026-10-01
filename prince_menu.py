# PRINCE 3 DOTS MENU - SEPARATE FILE
DOTS_MENU = """
<!-- PRINCE 3 DOTS MENU - TOP RIGHT -->
<div style="position:absolute;top:12px;right:20px;z-index:99999;">
<div onclick="togglePrinceMenu()" style="font-size:36px;color:#FFD700;cursor:pointer;font-weight:bold;">⋮
<div id="prince-menu" style="display:none;position:absolute;right:0;top:45px;background:#0f0f0f;border:2px solid #FFD700;border-radius:12px;min-width:220px;padding:12px;box-shadow:0 0 25px rgba(255,215,0,0.4);">
<!-- EMPTY FOR NOW BOSS -->
</div>
</div>
</div>
<script>
function togglePrinceMenu(){
 var m=document.getElementById('prince-menu');
 m.style.display=(m.style.display==='block'?'none':'block');
}
</script>
"""
