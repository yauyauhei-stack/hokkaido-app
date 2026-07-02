import streamlit as st

st.set_page_config(layout="wide", page_title="北海道之仲夏夢")

st.markdown("""
    <style>
    /* 強制清除所有邊框與空白 */
    [data-testid="stAppViewContainer"] { padding: 0 !important; margin: 0 !important; background: black; }
    [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
    
    .scroll-container { height: 100vh; width: 100vw; overflow-y: scroll; scroll-snap-type: y mandatory; scrollbar-width: none; }
    .full-screen-section { height: 100vh; width: 100vw; display: flex; flex-direction: column; justify-content: center; align-items: center; color: white; background-size: cover; background-position: center; scroll-snap-align: start; scroll-snap-stop: always; }
    
    .text-box { text-align: center; background: rgba(0,0,0,0.4); padding: 50px; border-radius: 30px; backdrop-filter: blur(5px); }
    .title-text { font-size: 80px !important; font-weight: bold; margin-bottom: 20px; }
    .desc-text { font-size: 32px !important; line-height: 1.5; max-width: 900px; }
    </style>
""", unsafe_allow_html=True)

# 定義你的 7 天詳細行程資料 (對應你的圖片)
itinerary = [
    ("北海道：仲夏夢之旅", "2026年7月16日 | 香港/東京 飛往北海道", 'https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp'),
    ("DAY 1", "啟程：抵達後直奔當地燒肉名店，享用頂級和牛，入住市中心豪華酒店。", 'https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp'),
    ("DAY 2", "富良野花田：漫步在色彩斑斕的花海中，欣賞大自然調色盤。", 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxxCb13giR5qt9ifcOxxgdplCLM4sSXWwNFDMzQzm60jDOBkll5VvMsPs&s=10'),
    ("DAY 3", "寧靜時光：深入北海道的秘境角落，遠離都市煩囂，享受北國的清風。", 'https://images.trvl-media.com/place/6104012/f8fa157e-15a4-4533-84ef-b21cb5b53110.jpg'),
    ("DAY 4", "文化探索：造訪小樽運河與歷史建築群，體驗古典的北國風情。", 'https://static.gltjp.com/glt/data/article/21000/20442/20230926_145350_43e48639_w1920.webp'),
    ("DAY 5", "購物狂熱：前往北廣島 Outlet，盡情選購國際品牌與日系精品。", 'https://hk.wamazing.com/media/wp-content/uploads/sites/5/2019/07/hokkaidomitsuioutlet_pixta_84488453_M.jpg.webp'),
    ("DAY 6", "甜蜜回憶：前往白色戀人公園，參觀巧克力工廠並享受甜點時光。", 'https://d1grca2t3zpuug.cloudfront.net/2025/10/2025shiroikoibitopark1-870x500-1761562254.webp'),
    ("DAY 7", "圓滿歸途：在狸小路商店街購買伴手禮，帶著滿滿回憶飛往香港。", 'https://hokkaido.letsgojp.com/archives/381138/')
]

st.markdown('<div class="scroll-container">', unsafe_allow_html=True)

for title, desc, img in itinerary:
    st.markdown(f'''
        <div class="full-screen-section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{img}');">
            <div class="text-box">
                <div class="title-text">{title}</div>
                <div class="desc-text">{desc}</div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
