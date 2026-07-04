import streamlit as st
import streamlit.components.v1 as components

# 設定頁面無邊框
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>#MainMenu, footer, header { visibility: hidden; } [data-testid='stAppViewContainer']{background:#000;}</style>", unsafe_allow_html=True)

# 詳細行程資料
itinerary_data = [
    {"day": "DAY 1", "sub": "抵達與燒肉之夜", "desc": "香港團隊(4人)抵達新千歲，JR直達旭川，全家人酒店會合，晚餐享用極上和牛。"},
    {"day": "DAY 2", "sub": "專車遊：富良野與美瑛", "desc": "薰衣草花田與七彩花毯，下午前往夢幻絕景美瑛青池與白金青鬚瀑布。"},
    {"day": "DAY 3", "sub": "旭山動物園與移動", "desc": "觀賞北極熊跳水，下午搭乘特急列車前往札幌，體驗貍小路商店街。"},
    {"day": "DAY 4", "sub": "小樽運河與海鮮", "desc": "欣賞小樽煤氣燈夜景，於三角市場品嚐新鮮海鮮。"},
    {"day": "DAY 5", "sub": "北廣島購物與夜景", "desc": "三井Outlet室內購物，晚上欣賞藻岩山新三大夜景。"},
    {"day": "DAY 6", "sub": "白色戀人公園", "desc": "札幌市區漫步，參觀白色戀人朱古力工廠。"},
    {"day": "DAY 7", "sub": "歸途補貨", "desc": "機場手信街最後衝刺，登機返家。"}
]

imgs = [
    'https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp',
    'https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxxCb13giR5qt9ifcOxxgdplCLM4sSXWwNFDMzQzm60jDOBkll5VvMsPs&s=10',
    'https://images.trvl-media.com/place/6104012/f8fa157e-15a4-4533-84ef-b21cb5b53110.jpg',
    'https://static.gltjp.com/glt/data/article/21000/20442/20230926_145350_43e48639_w1920.webp',
    'https://hk.wamazing.com/media/wp-content/uploads/sites/5/2019/07/hokkaidomitsuioutlet_pixta_84488453_M.jpg.webp',
    'https://d1grca2t3zpuug.cloudfront.net/2025/10/2025shiroikoibitopark1-870x500-1761562254.webp'
]

# 生成詳細行程的 HTML
expanded_html = "".join([f'''
    <div style="background:rgba(255,255,255,0.05); margin-bottom:15px; padding:15px; border-radius:15px; border:1px solid #444;">
        <img src="{imgs[i]}" style="width:100%; border-radius:10px; margin-bottom:10px;">
        <h3 style="color:#ffcc00; margin:0;">{item['day']} - {item['sub']}</h3>
        <p style="font-size:14px; margin-top:5px; color:#ddd;">{item['desc']}</p>
    </div>
''' for i, item in enumerate(itinerary_data)])

components.html(f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ margin: 0; background: #000; color: white; font-family: sans-serif; }}
        .bg {{ width: 100vw; min-height: 100vh; background: url('https://i.imgur.com/image_ae83e1.png') no-repeat center center/cover; padding: 20px; display: flex; justify-content: center; }}
        .card {{ background: rgba(0,0,0,0.8); backdrop-filter: blur(20px); padding: 30px; border-radius: 30px; width: 100%; max-width: 450px; border: 1px solid #333; }}
        .btn {{ width: 100%; padding: 18px; margin: 10px 0; border-radius: 15px; border: none; font-weight: bold; cursor: pointer; transition: 0.3s; text-align: center; }}
        .active {{ background: #ffcc00; color: #000; }}
        .soon {{ background: #1a1a1a; color: #666; }}
        #itinerary-details {{ display: none; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="bg">
        <div class="card">
            <h1 style="text-align:center; margin-bottom:30px;">選擇行程</h1>
            <div class="btn active" onclick="document.getElementById('itinerary-details').style.display = (document.getElementById('itinerary-details').style.display === 'block' ? 'none' : 'block')">
                北海道之旅 ✈️
            </div>
            <div id="itinerary-details">{expanded_html}</div>
            
            <div class="btn soon">行程 2: Coming Soon...</div>
            <div class="btn soon">行程 3: Coming Soon...</div>
            <div class="btn soon">行程 4: Coming Soon...</div>
            <div class="btn soon">行程 5: Coming Soon...</div>
        </div>
    </div>
</body>
</html>
""", height=1000)
