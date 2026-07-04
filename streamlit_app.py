import streamlit as st
import streamlit.components.v1 as components

# 確保 Streamlit 配置正確
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>#MainMenu, footer, header { visibility: hidden; } [data-testid='stAppViewContainer']{background:#000;}</style>", unsafe_allow_html=True)

# 為了確保圖片能正常顯示，我們使用固定的背景圖
# 如果你的 image_ae83e1.png 連結失效，請確保該連結是「公開」且「可直接讀取」的
bg_url = "https://share.gemini.google/oIlLoxwynAX3"

components.html(f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ margin: 0; padding: 0; background-color: #000; font-family: sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
        .main-container {{ 
            width: 100%; height: 100vh; 
            background: url('{bg_url}') no-repeat center center fixed; 
            background-size: cover; 
            display: flex; flex-direction: column; align-items: center; justify-content: center;
        }}
        .card {{ 
            background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(10px); 
            padding: 20px; border-radius: 20px; width: 90%; max-width: 400px; text-align: center; border: 1px solid rgba(255,255,255,0.1);
        }}
        .btn {{ 
            display: block; width: 100%; padding: 15px; margin: 10px 0; border-radius: 10px; 
            background: #ffcc00; color: #000; font-weight: bold; cursor: pointer; text-decoration: none;
        }}
        .coming-soon {{ color: #777; background: #222; border-radius: 10px; padding: 15px; margin: 10px 0; }}
        #details {{ display: none; color: #fff; text-align: left; font-size: 14px; margin-top: 15px; }}
    </style>
</head>
<body>
    <div class="main-container">
        <div class="card">
            <h1 style="color:#fff;">發哥旅遊精選</h1>
            <div class="btn" onclick="document.getElementById('details').style.display='block'; this.style.display='none';">
                北海道之旅 ✈️
            </div>
            <div id="details">
                <p>Day 1: 抵達與燒肉之夜 🥩</p>
                <p>Day 2: 富田農場花田、美瑛青池 🌸</p>
                <p>Day 3: 旭山動物園、札幌湯咖哩 🐧</p>
                <p>Day 4: 小樽運河散策 🛶</p>
                <p>Day 5: 北廣島 Outlet 血拼 🛍️</p>
                <p>Day 6: 白色戀人公園 🍪</p>
                <p>Day 7: 狸小路商店街返港 🛫</p>
            </div>
            <div class="coming-soon">行程 2: Coming Soon...</div>
            <div class="coming-soon">行程 3: Coming Soon...</div>
            <div class="coming-soon">行程 4: Coming Soon...</div>
            <div class="coming-soon">行程 5: Coming Soon...</div>
        </div>
    </div>
</body>
</html>
""", height=800)
