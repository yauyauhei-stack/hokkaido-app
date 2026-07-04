import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>#MainMenu, footer, header { visibility: hidden; } [data-testid='stAppViewContainer']{background:#000;}</style>", unsafe_html=True)

# 詳細行程內容
hokkaido_details = """
<div style="margin-top:15px; padding:15px; background:rgba(255,255,255,0.05); border-radius:15px; text-align:left; font-size:14px; line-height:1.8;">
    <p><b>Day 1:</b> 啟程：抵達與燒肉之夜 🥩</p>
    <p><b>Day 2:</b> 專車一日遊：富田農場花田、美瑛青池 🌸</p>
    <p><b>Day 3:</b> 旭山動物園、札幌湯咖哩 🐧</p>
    <p><b>Day 4:</b> 小樽運河散策、三角市場海鮮 🛶</p>
    <p><b>Day 5:</b> 北廣島 Outlet 購物、藻岩山夜景 🛍️</p>
    <p><b>Day 6:</b> 白色戀人公園 🍪</p>
    <p><b>Day 7:</b> 狸小路商店街補貨返港 🛫</p>
</div>
"""

components.html(f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ background: #000; color: white; font-family: sans-serif; margin: 0; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }}
        .hero {{ width: 100%; height: 100vh; background: url('https://i.imgur.com/image_ae83e1.png') no-repeat center/cover; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }}
        .glass-card {{ background: rgba(0, 0, 0, 0.6); backdrop-filter: blur(15px); padding: 30px; border-radius: 25px; width: 90%; max-width: 450px; border: 1px solid rgba(255,255,255,0.2); }}
        .trip-btn {{ display: block; width: 100%; padding: 15px; margin: 10px 0; border-radius: 15px; background: #1a1a1a; border: 1px solid #333; cursor: pointer; transition: 0.3s; font-weight: bold; }}
        .trip-btn:hover {{ background: #222; }}
        #hokkaido-content {{ display: none; }}
        .coming-soon {{ color: #555; cursor: default; }}
    </style>
</head>
<body>
    <div class="hero">
        <div class="glass-card">
            <h1 style="margin-bottom:20px;">發哥旅遊精選</h1>
            
            <!-- 北海道行程 (可展開) -->
            <div class="trip-btn" onclick="document.getElementById('hokkaido-content').style.display = (document.getElementById('hokkaido-content').style.display === 'block' ? 'none' : 'block')">
                北海道之旅 ✈️
            </div>
            <div id="hokkaido-content">{hokkaido_details}</div>

            <!-- 其他行程 (Coming Soon) -->
            <div class="trip-btn coming-soon">行程 2: Coming Soon...</div>
            <div class="trip-btn coming-soon">行程 3: Coming Soon...</div>
            <div class="trip-btn coming-soon">行程 4: Coming Soon...</div>
            <div class="trip-btn coming-soon">行程 5: Coming Soon...</div>
        </div>
    </div>
</body>
</html>
""", height=1000)
