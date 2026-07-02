import streamlit as st
import streamlit.components.v1 as components

# 強制設定頁面寬度，隱藏預設 Streamlit 邊距與 UI
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
    [data-testid="stAppViewContainer"] { background-color: black !important; }
    [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
    #MainMenu, footer, header { visibility: hidden; }
</style>""", unsafe_allow_html=True)

# 定義行程內容
itinerary = [
    ("北海道：仲夏夢之旅", "2026年7月16日 | 香港/東京 飛往北海道", "準備迎接北國的涼爽空氣與大自然饗宴。"),
    ("DAY 1", "啟程：抵達與燒肉之夜", "15:00 抵達新千歲機場 | 18:00 前往燒肉店品嚐極上和牛 | 20:30 入住札幌市中心酒店。"),
    ("DAY 2", "富良野：花海中的漫步", "09:00 出發富良野 | 11:00 富良野花田打卡 | 13:00 當地特色午餐 | 17:00 返回札幌。"),
    ("DAY 3", "深度探索：北國秘境", "10:00 前往郊區風景區 | 12:30 湖畔散策與午茶 | 16:00 體驗在地寧靜生活，感受微風。"),
    ("DAY 4", "文化歷史：小樽運河之旅", "10:30 抵達小樽 | 12:00 運河邊享用海鮮丼 | 15:00 參觀玻璃工藝館與音樂盒堂。"),
    ("DAY 5", "購物狂熱：北廣島 Outlet", "11:00 抵達北廣島 Mitsui Outlet Park | 16:00 盡情選購國際名牌與運動裝備。"),
    ("DAY 6", "童趣體驗：白色戀人公園", "10:00 前往白色戀人公園 | 12:00 參觀巧克力工廠 | 14:00 享受下午茶與製作手工餅乾。"),
    ("DAY 7", "歸途：狸小路商店街", "09:00 狸小路補貨 | 12:00 午餐 | 15:00 前往機場，帶著滿載的回憶返回香港。")
]

imgs = [
    'https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp',
    'https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxxCb13giR5qt9ifcOxxgdplCLM4sSXWwNFDMzQzm60jDOBkll5VvMsPs&s=10',
    'https://images.trvl-media.com/place/6104012/f8fa157e-15a4-4533-84ef-b21cb5b53110.jpg',
    'https://static.gltjp.com/glt/data/article/21000/20442/20230926_145350_43e48639_w1920.webp',
    'https://hk.wamazing.com/media/wp-content/uploads/sites/5/2019/07/hokkaidomitsuioutlet_pixta_84488453_M.jpg.webp',
    'https://d1grca2t3zpuug.cloudfront.net/2025/10/2025shiroikoibitopark1-870x500-1761562254.webp',
    'https://hokkaido.letsgojp.com/archives/381138/'
]

# 產生 HTML 區塊
sections_html = ""
for i in range(len(itinerary)):
    title, sub, desc = itinerary[i]
    sections_html += f"""
        <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('{imgs[i]}');">
            <div class="text-box">
                <h1>{title}</h1>
                <p class="subtitle">{sub}</p>
                <p class="description">{desc}</p>
            </div>
        </div>
    """

# 渲染網頁組件
components.html(f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        /* 重設所有屬性以徹底移除邊框 */
        * {{ margin: 0; padding: 0; box-sizing: border-box; border: none !important; }}
        body, html {{ height: 100%; width: 100%; background: #000; overflow: hidden; }}
        .scroll-container {{ height: 100vh; width: 100vw; overflow-y: auto; scrollbar-width: none; }}
        .section {{ height: 100vh; width: 100vw; display: flex; justify-content: center; align-items: center; color: white; background-size: cover; background-position: center; position: relative; }}
        .text-box {{ text-align: center; padding: 50px; transition: opacity 1s, transform 1s; opacity: 0; transform: translateY(30px); }}
        .text-box.visible {{ opacity: 1; transform: translateY(0); }}
        h1 {{ font-size: 70px; margin: 0; font-weight: 700; }}
        .subtitle {{ font-size: 35px; margin: 15px 0; font-weight: 500; opacity: 0.9; }}
        .description {{ font-size: 24px; max-width: 800px; line-height: 1.6; opacity: 0.8; }}
    </style>
</head>
<body>
    <div class="scroll-container" id="container">
        {sections_html}
    </div>
    <script>
        const container = document.getElementById('container');
        const sections = document.querySelectorAll('.section');
        let isScrolling = false;
        let currentIndex = 0;
        container.addEventListener('wheel', (e) => {{
            if (isScrolling) return;
            isScrolling = true;
            if (e.deltaY > 0) currentIndex = Math.min(currentIndex + 1, sections.length - 1);
            else currentIndex = Math.max(currentIndex - 1, 0);
            sections[currentIndex].scrollIntoView({{ behavior: 'smooth' }});
            document.querySelectorAll('.text-box').forEach((box, idx) => {{
                box.classList.toggle('visible', idx === currentIndex);
            }});
            setTimeout(() => {{ isScrolling = false; }}, 800);
        }}, {{ passive: false }});
        document.querySelectorAll('.text-box')[0].classList.add('visible');
    </script>
</body>
</html>
""", height=1000, scrolling=False)
