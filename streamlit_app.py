import streamlit as st
import streamlit.components.v1 as components

# 徹底隱藏 Streamlit 的預設 UI 容器
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            [data-testid="stAppViewContainer"] { background-color: black; }
            [data-testid="stMainBlockContainer"] { padding: 0 !important; }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 使用全螢幕 iframe 嵌入，並強制 style 屬性
components.html("""
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body { 
            margin: 0 !important; 
            padding: 0 !important; 
            overflow: hidden; 
            background-color: black;
            width: 100vw;
            height: 100vh;
        }
        .scroll-container {
            height: 100vh;
            width: 100vw;
            overflow-y: scroll;
            scroll-snap-type: y mandatory;
            scrollbar-width: none; /* 隱藏捲軸 */
            -ms-overflow-style: none; /* IE 隱藏捲軸 */
        }
        .scroll-container::-webkit-scrollbar { display: none; } /* Chrome/Safari 隱藏捲軸 */
        
        .section {
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
            position: relative;
        }
        .text-box { 
            text-align: center; 
            background: rgba(0,0,0,0.4); 
            padding: 50px; 
            border-radius: 20px; 
            z-index: 10;
        }
        h1 { font-size: 80px; margin: 0; }
        p { font-size: 30px; margin: 20px 0 0 0; }
    </style>
</head>
<body>
    <div class="scroll-container">
        <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp');">
            <div class="text-box"><h1>北海道：仲夏夢之旅</h1><p>2026年7月16日啟程</p></div>
        </div>
        <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp');">
            <div class="text-box"><h1>DAY 1</h1><p>啟程：飛往北海道，直奔當地燒肉名店享用和牛，入住豪華酒店。</p></div>
        </div>
    </div>
</body>
</html>
""", height=1000)
