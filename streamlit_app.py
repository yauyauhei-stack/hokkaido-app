import streamlit as st

# 設定頁面為寬屏且隱藏側邊欄
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# 這裡我們利用 st.components.v1.html 建立一個完全獨立的沙盒
import streamlit.components.v1 as components

components.html(f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ overflow: hidden; }} /* 禁止原本的滾動 */
        
        .scroll-container {{
            height: 100vh;
            width: 100vw;
            overflow-y: scroll;
            scroll-snap-type: y mandatory;
            scrollbar-width: none;
        }}
        .section {{
            height: 100vh;
            width: 100vw;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            background-size: cover;
            background-position: center;
            scroll-snap-align: start;
            scroll-snap-stop: always;
        }}
        .text-box {{ text-align: center; background: rgba(0,0,0,0.5); padding: 50px; border-radius: 20px; }}
    </style>
</head>
<body>
    <div class="scroll-container">
        <!-- 每一頁內容 -->
        <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp');">
            <div class="text-box"><h1>北海道：仲夏夢之旅</h1><p>2026年7月16日啟程</p></div>
        </div>
        <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp');">
            <div class="text-box"><h1>DAY 1</h1><p>啟程：抵達後直奔當地燒肉名店，享用頂級和牛，入住市中心豪華酒店。</p></div>
        </div>
        <!-- 你可以繼續在這裡添加剩下的 Day 2-7 -->
    </div>
</body>
</html>
""", height=800)
