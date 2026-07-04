import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>#MainMenu, footer, header { visibility: hidden; } [data-testid='stAppViewContainer']{background:#000;}</style>", unsafe_allow_html=True)

# 完整行程資料 (對應你的 7 張圖片)
itinerary = [
    {"title": "DAY 1 🏨", "sub": "啟程：抵達與燒肉之夜", "desc": "香港團隊 (4人) 於 15:20 順利降落新千歲機場(CX580) | 隨即前往 JR 火車月台兌換「富良野地區鐵路週遊券」。", "note": "晚上前往燒肉店品嚐極上和牛 🥩"},
    {"title": "DAY 2 🌸", "sub": "【跟團免奔波】專車一日遊", "desc": "專車直達【富良野富田農場】，飽覽彩色薰衣草花田與七彩花毯。", "note": "下午前往【美瑛青池】與【白金青鬚瀑布】。"},
    {"title": "DAY 3 🐧", "sub": "深度探索：北國秘境", "desc": "前往【旭山動物園】觀賞北極熊跳水與企鵝漫步。", "note": "晚上漫步【貍小路商店街】，晚餐：札幌湯咖哩 🍛"},
    {"title": "DAY 4 🛶", "sub": "文化歷史：小樽運河之旅", "desc": "欣賞煤氣燈夜景、三角市場食海鮮 🦀。", "note": "小樽運河散策。"},
    {"title": "DAY 5 🛍️", "sub": "購物狂熱：北廣島 Outlet", "desc": "坐直達大巴去【北廣島三井 Outlet】室內瘋狂血拼。", "note": "夜晚睇藻岩山新三大夜景 ✨。"},
    {"title": "DAY 6 🍫", "sub": "童趣體驗：白色戀人公園", "desc": "札幌市區經典散策、白色戀人朱古力工廠 🍪。", "note": "完美句點。"},
    {"title": "DAY 7 🛫", "sub": "歸途：狸小路商店街", "desc": "09:00 札幌市補貨 | 12:00 午餐 | 15:00 前往機場手信街最後衝刺。", "note": "登機返家。"}
]

# 你的 7 張圖片
imgs = [
    'https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp',
    'https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxxCb13giR5qt9ifcOxxgdplCLM4sSXWwNFDMzQzm60jDOBkll5VvMsPs&s=10',
    'https://images.trvl-media.com/place/6104012/f8fa157e-15a4-4533-84ef-b21cb5b53110.jpg',
    'https://static.gltjp.com/glt/data/article/21000/20442/20230926_145350_43e48639_w1920.webp',
    'https://hk.wamazing.com/media/wp-content/uploads/sites/5/2019/07/hokkaidomitsuioutlet_pixta_84488453_M.jpg.webp',
    'https://d1grca2t3zpuug.cloudfront.net/2025/10/2025shiroikoibitopark1-870x500-1761562254.webp'
]

# 生成行程 HTML
sections_html = "".join([f'''
    <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{imgs[i]}');">
        <div class="text-box">
            <h1>{item['title']}</h1>
            <p style="font-size:18px; margin-bottom:10px;">{item['sub']}</p>
            <p>{item['desc']}</p><br><p style="color:#ffcc00;">{item['note']}</p>
        </div>
    </div>
''' for i, item in enumerate(itinerary)])

components.html(f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: #000; color: white; font-family: 'PingFang HK', sans-serif; overflow: hidden; }}
        .top-bar {{ position: fixed; top: 0; width: 100%; height: 60px; background: rgba(0,0,0,0.8); backdrop-filter: blur(10px); z-index: 1000; display: flex; align-items: center; padding: 0 20px; border-bottom: 1px solid #333; }}
        .scroll-container {{ height: 100vh; overflow-y: scroll; scroll-snap-type: y mandatory; }}
        .scroll-container::-webkit-scrollbar {{ display: none; }}
        .welcome-screen {{ height: 100vh; display: flex; align-items: center; justify-content: center; background: url('{imgs[0]}') no-repeat center/cover; scroll-snap-align: start; }}
        .glass-card {{ background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(20px); border-radius: 30px; padding: 40px; width: 85%; max-width: 400px; text-align: center; border: 1px solid rgba(255,255,255,0.2); }}
        .btn {{ display: block; width: 100%; padding: 15px; margin: 10px 0; border-radius: 15px; font-weight: bold; cursor: pointer; border: none; }}
        .section {{ height: 100vh; display: flex; justify-content: center; align-items: center; background-size: cover; background-position: center; scroll-snap-align: start; }}
        .text-box {{ width: 85%; max-width: 600px; padding: 30px; border-radius: 20px; background: rgba(0,0,0,0.7); backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.1); }}
    </style>
</head>
<body>
    <div class="top-bar">
        <div style="color:#ffcc00; font-weight:bold; font-size:16px; margin-right:20px;">發哥旅行社 ✈️</div>
        <marquee style="flex:1; font-size:14px;">📢 現正報名：現在加入行程每位減 HKD$50！一齊出發去北海道啦！</marquee>
        <div style="font-size:12px; margin-left:20px;">繁 | EN | JP</div>
    </div>
    <div class="scroll-container">
        <div class="welcome-screen">
            <div class="glass-card">
                <h1>北海道之旅</h1>
                <p style="margin: 10px 0;">探索北國：夏日家庭樂 | 七月限定</p>
                <button class="btn" style="background:#ffcc00;" onclick="document.getElementById('first-day').scrollIntoView()">了解更多</button>
            </div>
        </div>
        <div id="first-day"></div>
        {sections_html}
    </div>
</body>
</html>
""", height=1000)
