import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
    [data-testid="stAppViewContainer"] { background-color: black !important; }
    [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
    #MainMenu, footer, header { visibility: hidden; }
</style>""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
    <style>
        body, html { margin: 0; padding: 0; height: 100%; width: 100%; overflow: hidden; background: black; }
        .scroll-container { height: 100vh; width: 100vw; overflow-y: auto; scrollbar-width: none; }
        .section { height: 100vh; width: 100vw; display: flex; justify-content: center; align-items: center; color: white; background-size: cover; background-position: center; position: relative; }
        .text-box { text-align: center; background: rgba(0,0,0,0.3); padding: 50px; border-radius: 20px; transition: opacity 1s, transform 1s; opacity: 0; transform: translateY(50px); }
        .text-box.visible { opacity: 1; transform: translateY(0); }
    </style>
</head>
<body>
    <div class="scroll-container" id="container">
        <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp');">
            <div class="text-box"><h1>北海道：仲夏夢之旅</h1><p>2026年7月16日啟程</p></div>
        </div>
        <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp');">
            <div class="text-box"><h1>DAY 1</h1><p>啟程：品嚐在地燒肉，體驗頂級服務。</p></div>
        </div>
    </div>

    <script>
        const container = document.getElementById('container');
        const sections = document.querySelectorAll('.section');
        let isScrolling = false;
        let currentIndex = 0;

        // 平滑滾動邏輯
        container.addEventListener('wheel', (e) => {
            if (isScrolling) return;
            isScrolling = true;

            if (e.deltaY > 0) currentIndex = Math.min(currentIndex + 1, sections.length - 1);
            else currentIndex = Math.max(currentIndex - 1, 0);

            sections[currentIndex].scrollIntoView({ behavior: 'smooth' });
            
            // 觸發文字動畫
            document.querySelectorAll('.text-box').forEach((box, idx) => {
                box.classList.toggle('visible', idx === currentIndex);
            });

            setTimeout(() => { isScrolling = false; }, 1000); // 1秒後才允許下次滾動，避免跳躍
        }, { passive: false });

        // 初始化第一頁動畫
        document.querySelectorAll('.text-box')[0].classList.add('visible');
    </script>
</body>
</html>
""", height=1000)
