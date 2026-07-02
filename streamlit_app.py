import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    /* 移除所有邊框與玻璃效果 */
    .scroll-container { scroll-snap-type: y mandatory; overflow-y: scroll; height: 100vh; }
    .section { height: 100vh; width: 100%; scroll-snap-align: start; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background-size: cover; background-position: center; color: white; }
    
    /* 專屬字體大小控制 */
    .main-title { font-size: 80px !important; font-weight: bold; margin-bottom: 20px; }
    .sub-title { font-size: 40px !important; margin-bottom: 40px; }
    .day-text { font-size: 60px !important; font-weight: bold; margin-bottom: 20px; }
    .desc-text { font-size: 30px !important; line-height: 1.6; max-width: 800px; }

    /* 背景圖設定 (全部套用黑色濾鏡) */
    #home { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp'); }
    #day1 { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp'); }
    #day2 { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxxCb13giR5qt9ifcOxxgdplCLM4sSXWwNFDMzQzm60jDOBkll5VvMsPs&s=10'); }
    #day3 { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.trvl-media.com/place/6104012/f8fa157e-15a4-4533-84ef-b21cb5b53110.jpg'); }
    #day4 { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://static.gltjp.com/glt/data/article/21000/20442/20230926_145350_43e48639_w1920.webp'); }
    #day5 { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://hk.wamazing.com/media/wp-content/uploads/sites/5/2019/07/hokkaidomitsuioutlet_pixta_84488453_M.jpg.webp'); }
    #day6 { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://d1grca2t3zpuug.cloudfront.net/2025/10/2025shiroikoibitopark1-870x500-1761562254.webp'); }
    #day7 { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://hokkaido.letsgojp.com/archives/381138/'); }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="scroll-container">', unsafe_allow_html=True)

# 首頁 (乾淨的背景與文字)
st.markdown('''
    <div id="home" class="section">
        <div class="main-title">北海道：仲夏夢之旅</div>
        <div class="sub-title">2026 年 7 月 16 日啟程</div>
    </div>
''', unsafe_allow_html=True)

# 7 天行程
days = [
    ("DAY 1", "啟程前往北海道，品嚐當地地道燒肉，入住精選飯店。"),
    ("DAY 2", "富良野花田之旅，感受繽紛夏日花海。"),
    ("DAY 3", "深度探索北國風光，體驗在地寧靜生活。"),
    ("DAY 4", "走訪人文歷史建築，沉浸北海道文化。"),
    ("DAY 5", "北廣島 Outlet 購物，盡享休閒與樂趣。"),
    ("DAY 6", "參訪白色戀人公園，享受浪漫甜蜜時光。"),
    ("DAY 7", "帶著滿載的回憶，準備啟程返回溫暖的家。")
]

for i, (title, desc) in enumerate(days, 1):
    st.markdown(f'''
        <div id="day{i}" class="section">
            <div class="day-text">{title}</div>
            <div class="desc-text">{desc}</div>
        </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
