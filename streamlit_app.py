import streamlit as st
import streamlit.components.v1 as components

# 強制消除 Streamlit 預設邊框
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: black !important; }
    [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
    #MainMenu, footer, header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# 寫入 HTML/CSS/JS
components.html("""
<!DOCTYPE html>
<html>
<head>
    <style>
        body, html { margin: 0; padding: 0; height: 100%; width: 100%; overflow: hidden; background: black; }
        
        .scroll-container {
            height: 100vh;
            width: 100vw;
            overflow-y: scroll;
            scroll-snap-type: y mandatory;
            scrollbar-width: none;
        }
        
        .section {
            height: 100vh;
            width: 100vw;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            background-size: cover;
            background-position: center;
            scroll-snap-align: start;
            position: relative;
        }

        /* 文字進入動畫 */
        .text-box { 
            text-align: center; 
            background: rgba(0,0,0,0.3); 
            padding: 50px; 
            border-radius: 20px;
            animation: fadeIn 1.2s ease-out forwards;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 { font-size: 80px; margin: 0; }
        p { font-size: 30px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="scroll-container" id="container">
        <!-- 每一頁 -->
        <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp');">
            <div class="text-box"><h1>北海道：仲夏夢之旅</h1><p>2026年7月16日啟程</p></div>
        </div>
        <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp');">
            <div class="text-box"><h1>DAY 1</h1><p>啟程：品嚐在地燒肉，體驗頂級服務。</p></div>
        </div>
    </div>
    <script>
        // 強制 iframe 撐滿高度
        document.getElementById('container').style.height = window.innerHeight + 'px';
    </script>
</body>
</html>
""", height=1000)
