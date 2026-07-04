import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
    [data-testid="stAppViewContainer"] { background-color: #050505 !important; }
    #MainMenu, footer, header { visibility: hidden; }
</style>""", unsafe_allow_html=True)

# 行程資料
itinerary = [
    {"title": "DAY 1 🏨", "sub": "啟程：抵達與燒肉之夜", "desc": "香港團隊 (4人) 於 15:20 順利降落新千歲機場(CX580) | 隨即前往 JR 火車月台兌換「富良野地區鐵路週遊券」，並現場辦理特急列車指定席劃位，直達旭川。", "note1": "【東京隊會合】東京成員 (1人) 則於 18:50 降落旭川機場 ( HD 087 )，搭乘便利的機場巴士前往酒店會合。", "note2": "大隊步行前往旭川烏帕希酒店辦理 Check-in，全家人於酒店溫馨大團圓。", "note3": "晚上前往燒肉店品嚐極上和牛 🥩 | 入住札幌市中心酒店。"},
    {"title": "DAY 2 🌸", "sub": "【跟團免奔波】專車一日遊","desc": "【跟團免奔波】早上於 JR 旭川站集合上車，參加專車一日遊，長輩中途可在遊覽車上舒適休息。輕鬆遊玩。","note1": "【薰衣草滿開】專車直達【富良野富田農場】，飽覽正值大爆發的彩色薰衣草花田與七彩花毯。於美瑛品嚐在地食材午餐。", "note2": "【網美雙絕景】下午前往夢幻絕景【美瑛青池】與【白金青鬚瀑布】，近距離感受蒂芬妮藍的魔幻水色。傍晚大巴送返 JR 旭川站解散。","note3": "【團隊膳食】早餐：酒店內或自理 | 午餐：美瑛在地料理 | 晚餐：旭川醬油拉麵 🍜","note4": "【當晚住宿】旭川：經濟酒店 烏帕希 (Hotel WBF Asahikawa) [續住第二晚，行李免搬動]"},
    {"title": "DAY 3 🐧", "sub": "深度探索：北國秘境", "desc": "【超萌體驗】上午酒店退房，行李寄存於旭川站。上午9:10前到達旭川站搭乘47專線巴士前往【旭山動物園】觀賞著名的北極熊跳水與企鵝漫步。","note1":"【鐵路移動】下午返回旭川站提取行李，使用週遊券搭乘 JR 特急列車（免費劃指定席對號座）前往札幌（車程約1.5小時）。抵達後入住格蘭貝爾札幌酒店，夜晚漫步【貍小路商店街】。","note2":"【團隊膳食】早餐：LAWSON/FAMILYMART/7-11 | 午餐：動物園內自理 | 晚餐：札幌特色湯咖哩 🍛","note3":"【當晚住宿】札幌：格蘭貝爾札幌酒店 (Sapporo Hotel by Granbell)"},
    {"title": "DAY 4 🛶", "sub": "文化歷史：小樽運河之旅", "desc": "【小樽散策】Day 4 使用週遊券劃位指定席去【小樽運河】欣賞煤氣燈夜景、三角市場食海鮮 🦀。"},
    {"title": "DAY 5 🛍️", "sub": "購物狂熱：北廣島 Outlet", "desc": "【購物狂歡】Day 5 坐直達大巴去【北廣島三井 Outlet】室內瘋狂血拼，夜晚睇藻岩山新三大夜景 ✨。"},
    {"title": "DAY 6 🍫", "sub": "童趣體驗：白色戀人公園", "desc": "【完美句點】Day 6 札幌市區經典散策、白色戀人朱古力工廠 🍪。"},
    {"title": "DAY 7 🛫", "sub": "歸途：狸小路商店街", "desc": "09:00 札幌市補貨 | 12:00 午餐 | 15:00 前往機場手信街最後衝刺後各自登機返家。", "flight": "CX583 or HD032"}
]

imgs = ['https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxxCb13giR5qt9ifcOxxgdplCLM4sSXWwNFDMzQzm60jDOBkll5VvMsPs&s=10', 'https://images.trvl-media.com/place/6104012/f8fa157e-15a4-4533-84ef-b21cb5b53110.jpg', 'https://static.gltjp.com/glt/data/article/21000/20442/20230926_145350_43e48639_w1920.webp', 'https://hk.wamazing.com/media/wp-content/uploads/sites/5/2019/07/hokkaidomitsuioutlet_pixta_84488453_M.jpg.webp', 'https://d1grca2t3zpuug.cloudfront.net/2025/10/2025shiroikoibitopark1-870x500-1761562254.webp', 'https://hk.wamazing.com/media/wp-content/uploads/sites/5/2019/09/shinchitoseairporttaxfree_pixta_94252250_M.jpg.webp']

sections_html = ""
for i, item in enumerate(itinerary):
    details = "<br><br>".join([f"{v}" for k, v in item.items() if k not in ["title", "sub"]])
    sections_html += f'''
        <div class="section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{imgs[i]}');">
            <div class="text-box">
                <h1>{item['title']}</h1>
                <p class="subtitle">{item['sub']}</p>
                <div class="content">{details}</div>
            </div>
        </div>
    '''

components.html(f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=PingFang+HK:wght@300;500;700&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: #000; color: white; font-family: 'PingFang HK', sans-serif; overflow: hidden; height: 100vh; }}
        
        .top-bar {{ position: fixed; top: 0; width: 100%; height: 60px; background: rgba(0,0,0,0.8); backdrop-filter: blur(10px); z-index: 1000; display: flex; align-items: center; padding: 0 20px; border-bottom: 1px solid #333; }}
        
        .welcome-screen {{ height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; background: url('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp') no-repeat center/cover; }}
        .glass-card {{ background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(20px); border-radius: 30px; padding: 40px; width: 85%; max-width: 400px; text-align: center; border: 1px solid rgba(255,255,255,0.2); }}
        
        .btn {{ display: block; width: 100%; padding: 15px; margin: 10px 0; border-radius: 15px; text-decoration: none; font-weight: bold; cursor: pointer; transition: 0.3s; }}
        .btn-primary {{ background: #ffcc00; color: #000; }}
        .btn-secondary {{ background: rgba(255,255,255,0.2); color: white; }}
        
        .scroll-container {{ height: 100vh; overflow-y: scroll; scroll-snap-type: y mandatory; }}
        .section {{ height: 100vh; display: flex; justify-content: center; align-items: center; background-size: cover; background-position: center; scroll-snap-align: start; }}
        .text-box {{ width: 85%; max-width: 600px; padding: 30px; border-radius: 20px; background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.1); }}
    </style>
</head>
<body>
    <div class="top-bar">
        <div style="color:#ffcc00; font-weight:bold; font-size:16px;">發哥旅行社 ✈️</div>
        <div style="flex:1; overflow:hidden; margin:0 15px;">
            <marquee direction="left" scrollamount="5">📢 現正報名：現在加入行程每位減 HKD$50！一齊出發去北海道啦！</marquee>
        </div>
        <div style="font-size:12px; color:#aaa;">繁 | EN | JP</div>
    </div>

    <div class="welcome-screen">
        <div class="glass-card">
            <h1 style="font-size:28px; margin-bottom:10px;">北海道之旅</h1>
            <p style="opacity:0.8; margin-bottom:20px;">探索北國：夏日家庭樂 | 七月限定</p>
            <div class="btn btn-primary">立即報名 · 每位減 HKD$50</div>
            <div class="btn btn-secondary" onclick="document.getElementById('scroll-target').scrollIntoView()">了解更多</div>
        </div>
    </div>

    <div class="scroll-container" id="scroll-target">
        {sections_html}
    </div>
</body>
</html>
""", height=1000)
