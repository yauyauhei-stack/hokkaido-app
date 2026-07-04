import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
    [data-testid="stAppViewContainer"] { background-color: #000 !important; }
    [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
    #MainMenu, footer, header { visibility: hidden; }
</style>""", unsafe_allow_html=True)

# 完整行程資料
itinerary = [
    {"title": "DAY 1 🏨", "sub": "啟程：抵達與燒肉之夜", "desc": "香港團隊 (4人) 於 15:20 順利降落新千歲機場(CX580) | 隨即前往 JR 火車月台兌換「富良野地區鐵路週遊券」，並現場辦理特急列車指定席劃位，直達旭川。", "note": "晚上前往燒肉店品嚐極上和牛 🥩 | 入住札幌市中心酒店。"},
    {"title": "DAY 2 🌸", "sub": "【跟團免奔波】專車一日遊", "desc": "【薰衣草滿開】專車直達【富良野富田農場】，飽覽正值大爆發的彩色薰衣草花田與七彩花毯。", "note": "下午前往夢幻絕景【美瑛青池】與【白金青鬚瀑布】。"},
    {"title": "DAY 3 🐧", "sub": "深度探索：北國秘境", "desc": "上午9:10前到達旭川站搭乘47專線巴士前往【旭山動物園】觀賞著名的北極熊跳水與企鵝漫步。", "note": "下午搭乘 JR 特急列車前往札幌。入住格蘭貝爾札幌酒店，夜晚漫步【貍小路商店街】。"},
    {"title": "DAY 4 🛶", "sub": "文化歷史：小樽運河之旅", "desc": "使用週遊券搭乘 JR 前往【小樽】，漫步小樽運河欣賞煤氣燈夜景。", "note": "於三角市場品嚐新鮮海鮮 🦀。"},
    {"title": "DAY 5 🛍️", "sub": "購物狂熱：北廣島 Outlet", "desc": "坐直達大巴去【北廣島三井 Outlet】室內瘋狂血拼。", "note": "夜晚睇藻岩山新三大夜景 ✨。"},
    {"title": "DAY 6 🍫", "sub": "童趣體驗：白色戀人公園", "desc": "札幌市區經典散策、參觀白色戀人朱古力工廠 🍪。", "note": "完美句點。"},
    {"title": "DAY 7 🛫", "sub": "歸途：狸小路商店街", "desc": "09:00 札幌市補貨 | 12:00 午餐 | 15:00 前往機場手信街最後衝刺後各自登機返家。", "note": "搭乘 CX583 返港。"}
]

# 圖片資料
imgs = [
    'https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp', # 北海道封面 / Day 1
    'https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp', # Day 2
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxxCb13giR5qt9ifcOxxgdplCLM4sSXWwNFDMzQzm60jDOBkll5VvMsPs&s=10', # Day 3
    'https://images.trvl-media.com/place/6104012/f8fa157e-15a4-4533-84ef-b21cb5b53110.jpg', # Day 4
    'https://static.gltjp.com/glt/data/article/21000/20442/20230926_145350_43e48639_w1920.webp', # Day 5
    'https://hk.wamazing.com/media/wp-content/uploads/sites/5/2019/07/hokkaidomitsuioutlet_pixta_84488453_M.jpg.webp', # Day 6
    'https://d1grca2t3zpuug.cloudfront.net/2025/10/2025shiroikoibitopark1-870x500-1761562254.webp'  # Day 7
]

# 生成 Day 1 到 Day 7 的全螢幕滑動區塊 (第三次風格)
sections_html = "".join([f'''
    <div class="v-section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.7)), url('{imgs[i]}');">
        <div class="glass-box">
            <h1 style="color:#ffcc00; font-size: 32px; margin-bottom: 10px;">{item['title']}</h1>
            <h3 style="margin-bottom: 15px;">{item['sub']}</h3>
            <p style="font-size: 16px; line-height: 1.6; margin-bottom: 15px;">{item['desc']}</p>
            <p style="font-size: 14px; color: #ccc; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 10px;">💡 {item['note']}</p>
        </div>
    </div>
''' for i, item in enumerate(itinerary)])

# 生成 HTML，加入左右滑動卡片 UI
components.html(f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=PingFang+HK:wght@300;500;700&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: #000; color: white; font-family: 'PingFang HK', sans-serif; overflow: hidden; height: 100vh; }}
        
        /* 頂部導航列 (保持第三次風格) */
        .top-bar {{ position: fixed; top: 0; width: 100%; height: 60px; background: rgba(0,0,0,0.8); backdrop-filter: blur(10px); z-index: 1000; display: flex; align-items: center; padding: 0 20px; border-bottom: 1px solid #333; }}
        
        /* 主垂直滾動容器 */
        .main-scroll-container {{ height: 100vh; overflow-y: scroll; scroll-snap-type: y mandatory; scroll-behavior: smooth; }}
        .main-scroll-container::-webkit-scrollbar {{ display: none; }}
        
        /* 歡迎頁 - 佔滿首屏 */
        .welcome-page {{ height: 100vh; width: 100vw; scroll-snap-align: start; display: flex; flex-direction: column; justify-content: center; background: url('https://i.imgur.com/image_ae83e1.png') no-repeat center/cover; position: relative; }}
        .welcome-page::before {{ content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 1; }}
        
        /* 橫向滑動卡片容器 (手機 App UI) */
        .h-carousel {{ display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 20px; padding: 0 10vw; width: 100%; position: relative; z-index: 2; margin-top: 30px; }}
        .h-carousel::-webkit-scrollbar {{ display: none; }}
        
        /* 獨立卡片設計 */
        .card {{ flex: 0 0 75%; max-width: 300px; background: rgba(20, 20, 20, 0.85); backdrop-filter: blur(15px); border-radius: 20px; scroll-snap-align: center; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); display: flex; flex-direction: column; }}
        .card img {{ width: 100%; height: 200px; object-fit: cover; }}
        .card-content {{ padding: 20px; text-align: center; flex: 1; display: flex; flex-direction: column; justify-content: center; }}
        .card-content h2 {{ font-size: 20px; margin-bottom: 15px; }}
        
        /* 按鈕設計 */
        .btn-more {{ background: #ffcc00; color: #000; padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold; font-size: 16px; cursor: pointer; display: block; border: none; width: 100%; }}
        .btn-none {{ display: none; }} /* 隱藏其他卡片的按鈕 */
        
        /* 垂直行程區塊 (Day 1-7) */
        .v-section {{ height: 100vh; width: 100vw; display: flex; justify-content: center; align-items: center; background-size: cover; background-position: center; scroll-snap-align: start; }}
        .glass-box {{ width: 85%; max-width: 500px; padding: 30px; border-radius: 20px; background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.1); text-align: left; }}
        
    </style>
</head>
<body>
    <div class="top-bar">
        <div style="color:#ffcc00; font-weight:bold; font-size:16px; white-space:nowrap;">發哥旅行社 ✈️</div>
        <div style="flex:1; overflow:hidden; margin:0 15px;">
            <marquee direction="left" scrollamount="5" style="color:white; font-size:14px; margin-top: 4px;">📢 現正報名：現在加入行程每位減 HKD$50！一齊出發去北海道啦！</marquee>
        </div>
    </div>
    
    <div class="main-scroll-container" id="main-container">
        
        <!-- 首頁：打橫滑動的 5 個選項 -->
        <div class="welcome-page">
            <div style="position:relative; z-index:2; text-align:center; margin-bottom:20px; margin-top:40px;">
                <h1 style="color:white; font-size: 28px;">精選行程推介</h1>
                <p style="color:#aaa; font-size: 14px;">左右滑動探索更多</p>
            </div>
            
            <div class="h-carousel">
                <!-- 選項 1: 北海道 (有了解更多掣) -->
                <div class="card">
                    <img src="{imgs[0]}" alt="北海道">
                    <div class="card-content">
                        <h2>北海道仲夏之旅 🌸</h2>
                        <p style="font-size: 12px; color: #aaa; margin-bottom: 15px;">7天6夜 | 夏日家庭樂</p>
                        <button class="btn-more" onclick="document.getElementById('itinerary-start').scrollIntoView({{behavior: 'smooth'}})">了解更多</button>
                    </div>
                </div>
                
                <!-- 選項 2: Coming Soon (冇掣) -->
                <div class="card" style="opacity: 0.7;">
                    <img src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=600&auto=format&fit=crop" style="filter: grayscale(80%);">
                    <div class="card-content">
                        <h2 style="color:#888;">Coming Soon...</h2>
                        <p style="font-size: 12px; color: #666;">敬請期待</p>
                    </div>
                </div>
                
                <!-- 選項 3: Coming Soon (冇掣) -->
                <div class="card" style="opacity: 0.7;">
                    <img src="https://images.unsplash.com/photo-1518684079-3c830dcef090?q=80&w=600&auto=format&fit=crop" style="filter: grayscale(80%);">
                    <div class="card-content">
                        <h2 style="color:#888;">Coming Soon...</h2>
                        <p style="font-size: 12px; color: #666;">敬請期待</p>
                    </div>
                </div>
                
                <!-- 選項 4: Coming Soon (冇掣) -->
                <div class="card" style="opacity: 0.7;">
                    <img src="https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=600&auto=format&fit=crop" style="filter: grayscale(80%);">
                    <div class="card-content">
                        <h2 style="color:#888;">Coming Soon...</h2>
                        <p style="font-size: 12px; color: #666;">敬請期待</p>
                    </div>
                </div>
                
                <!-- 選項 5: Coming Soon (冇掣) -->
                <div class="card" style="opacity: 0.7;">
                    <img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=600&auto=format&fit=crop" style="filter: grayscale(80%);">
                    <div class="card-content">
                        <h2 style="color:#888;">Coming Soon...</h2>
                        <p style="font-size: 12px; color: #666;">敬請期待</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- 錨點：按了解更多後滑動到這裡 -->
        <div id="itinerary-start"></div>
        
        <!-- Day 1 至 Day 7 的詳細行程 (第三次風格的全螢幕滾動) -->
        {sections_html}
        
    </div>
</body>
</html>
""", height=850)
