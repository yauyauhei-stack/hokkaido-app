import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>#MainMenu, footer, header { visibility: hidden; } [data-testid='stAppViewContainer']{background:#000;}</style>", unsafe_allow_html=True)

# 準備所有詳細行程內容 (包含了你那7張圖和所有詳細資訊)
itinerary_data = [
    {"day": "DAY 1 🏨", "sub": "啟程：抵達與燒肉之夜", "desc": "香港團隊 (4人) 於 15:20 降落新千歲機場(CX580) | 隨即前往 JR 火車月台兌換「富良野地區鐵路週遊券」。", "note": "晚上前往燒肉店品嚐極上和牛 🥩 | 入住札幌市中心酒店。"},
    {"day": "DAY 2 🌸", "sub": "【跟團免奔波】專車一日遊", "desc": "【薰衣草滿開】專車直達【富良野富田農場】，飽覽薰衣草花田與七彩花毯。", "note": "下午前往夢幻絕景【美瑛青池】與【白金青鬚瀑布】。"},
    {"day": "DAY 3 🐧", "sub": "深度探索：北國秘境", "desc": "前往【旭山動物園】觀賞著名的北極熊跳水與企鵝漫步。", "note": "傍晚搭乘 JR 前往札幌，漫步【貍小路商店街】。"},
    {"day": "DAY 4 🛶", "sub": "文化歷史：小樽運河之旅", "desc": "使用週遊券劃位指定席去【小樽運河】欣賞煤氣燈夜景、三角市場食海鮮 🦀。", "note": "小樽運河散策。"},
    {"day": "DAY 5 🛍️", "sub": "購物狂熱：北廣島 Outlet", "desc": "坐直達大巴去【北廣島三井 Outlet】室內瘋狂血拼，夜晚睇藻岩山新三大夜景 ✨。", "note": "購物狂歡。"},
    {"day": "DAY 6 🍫", "sub": "童趣體驗：白色戀人公園", "desc": "札幌市區經典散策、參觀白色戀人朱古力工廠 🍪。", "note": "完美句點。"},
    {"day": "DAY 7 🛫", "sub": "歸途：狸小路商店街", "desc": "09:00 札幌市補貨 | 12:00 午餐 | 15:00 前往機場手信街最後衝刺後各自登機返家。", "note": "返港。"}
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

# 生成展開後的 HTML
expanded_html = "".join([f'''
    <div style="background: rgba(30,30,30,0.8); margin: 10px 0; padding: 15px; border-radius: 15px; border-left: 4px solid #ffcc00;">
        <img src="{imgs[i]}" style="width:100%; border-radius:10px; margin-bottom:10px;">
        <h4 style="color:#ffcc00; margin:0;">{item['day']} - {item['sub']}</h4>
        <p style="font-size:13px; margin:5px 0;">{item['desc']}</p>
        <p style="font-size:12px; color:#aaa;">{item['note']}</p>
    </div>
''' for i, item in enumerate(itinerary_data)])

components.html(f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ margin: 0; background: #000; color: white; font-family: sans-serif; overflow-x: hidden; }}
        .bg {{ width: 100vw; min-height: 100vh; background: url('https://i.imgur.com/image_ae83e1.png') no-repeat center center/cover; display: flex; justify-content: center; align-items: center; padding: 20px; }}
        .card {{ background: rgba(0,0,0,0.7); backdrop-filter: blur(15px); padding: 30px; border-radius: 25px; width: 100%; max-width: 400px; text-align: center; border: 1px solid #444; }}
        .trip-btn {{ display: block; width: 100%; padding: 15px; margin: 10px 0; border-radius: 15px; background: #ffcc00; color: #000; font-weight: bold; cursor: pointer; }}
        .soon-btn {{ display: block; width: 100%; padding: 15px; margin: 10px 0; border-radius: 15px; background: #222; color: #666; font-weight: bold; }}
        #itinerary-details {{ display: none; margin-top: 15px; text-align: left; max-height: 400px; overflow-y: auto; }}
        #itinerary-details::-webkit-scrollbar {{ display: none; }}
    </style>
</head>
<body>
    <div class="bg">
        <div class="card">
            <h1>發哥旅遊精選</h1>
            <div class="trip-btn" onclick="document.getElementById('itinerary-details').style.display = (document.getElementById('itinerary-details').style.display === 'block' ? 'none' : 'block')">
                北海道之旅 ✈️
            </div>
            <div id="itinerary-details">{expanded_html}</div>
            
            <div class="soon-btn">行程 2: Coming Soon...</div>
            <div class="soon-btn">行程 3: Coming Soon...</div>
            <div class="soon-btn">行程 4: Coming Soon...</div>
            <div class="soon-btn">行程 5: Coming Soon...</div>
        </div>
    </div>
</body>
</html>
""", height=900)
