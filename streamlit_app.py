import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
    [data-testid="stAppViewContainer"] { background-color: #000 !important; }
    [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
    #MainMenu, footer, header { visibility: hidden; }
</style>""", unsafe_allow_html=True)

# 多語言轉換輔助函數
def m(zh, en, jp):
    return f'<span class="zh">{zh}</span><span class="en">{en}</span><span class="jp">{jp}</span>'

# 行程資料
itinerary = [
    {
        "title": "DAY 1 🏨", 
        "sub": m("啟程：抵達與燒肉之夜", "Departure: Arrival & Yakiniku Night", "出発：到着と焼肉の夜"),
        "desc": m("香港團隊 (4人) 於 15:20 順利降落新千歲機場(CX580) | 隨即前往 JR 火車月台兌換「富良野地區鐵路週遊券」，並現場辦理特急列車指定席劃位，直達旭川。",
                  "HK Team (4 pax) lands at New Chitose Airport at 15:20 (CX580) | Proceed to JR platform to exchange 'Furano Area Rail Pass' and reserve express train seats to Asahikawa.",
                  "香港チーム（4名）15:20 新千歳空港到着 (CX580) | JR乗り場へ向かい、「富良野エリア鉄道周遊券」を引き換え、特急列車の指定席を予約して旭川へ直行。"),
        "note1": m("【東京隊會合】東京成員 (1人) 則於 18:50 降落旭川機場 ( HD 087 )，搭乘便利的機場巴士前往酒店會合。",
                   "[Tokyo Team Check-in] Tokyo member (1 pax) lands at Asahikawa Airport at 18:50 (HD 087) and takes the airport bus to the hotel.",
                   "【東京チーム合流】東京メンバー（1名）は18:50 旭川空港到着 (HD 087)、便利な空港バスでホテルへ向かい合流。"),
        "note2": m("大隊步行前往旭川烏帕希酒店辦理 Check-in，全家人於酒店溫馨大團圓。",
                   "The group walks to Hotel WBF Asahikawa for check-in. Family reunion at the hotel.",
                   "全員でホテルWBF旭川へ歩いて向かいチェックイン。ホテルで家族の温かい再会。"),
        "note3": m("晚上前往燒肉店品嚐極上成吉思汗羊肉 🥩 | 入住札幌市中心酒店。",
                   "Evening: Enjoy premium mutton at a Genghis Khan  🥩 | Check-in at Sapporo city center hotel.",
                   "夜は焼肉店で極上チンギス・ハンの羊肉 🥩 | 札幌市内のホテルに宿泊。")
    },
    {
        "title": "DAY 2 🌸", 
        "sub": m("【跟團免奔波】專車一日遊", "[Hassle-Free] Private Bus Day Tour", "【貸切バスで楽々】日帰りバスツアー"),
        "desc": m("【跟團免奔波】早上於 JR 旭川站集合上車，參加專車一日遊，長輩中途可在遊覽車上舒適休息。輕鬆遊玩。",
                  "Gather at JR Asahikawa Station in the morning for a private day tour. Elders can rest comfortably on the bus.",
                  "朝、JR旭川駅に集合し貸切バスツアーに参加。ご高齢の方も車内で快適に休憩できます。"),
        "note1": m("【薰衣草滿開】專車直達【富良野富田農場】，飽覽正值大爆發的彩色薰衣草花田與七彩花毯。於美瑛品嚐在地食材午餐。",
                   "[Lavender in Full Bloom] Direct access to Farm Tomita, Furano. Enjoy colorful lavender fields. Local lunch in Biei.",
                   "【ラベンダー満開】ファーム富田（富良野）へ直行。満開のラベンダーを満喫。美瑛で地元食材のランチ。"),
        "note2": m("【網美雙絕景】下午前往夢幻絕景【美瑛青池】與【白金青鬚瀑布】，近距離感受蒂芬妮藍的魔幻水色。傍晚大巴送返 JR 旭川站解散。",
                   "[Stunning Views] Afternoon visit to the magical Biei Blue Pond and Shirahige Waterfall. Evening return to JR Asahikawa.",
                   "【絶景スポット】午後は幻想的な美瑛「青い池」と「白ひげの滝」へ。夕方、バスでJR旭川駅に戻り解散。"),
        "note3": m("【團隊膳食】早餐：酒店內或自理 | 午餐：美瑛在地料理 | 晚餐：旭川醬油拉麵 🍜",
                   "[Meals] Breakfast: Hotel/Own | Lunch: Biei Local Cuisine | Dinner: Asahikawa Soy Sauce Ramen 🍜",
                   "【お食事】朝食：ホテル/各自 | 昼食：美瑛の郷土料理 | 夕食：旭川醤油ラーメン 🍜"),
        "note4": m("【當晚住宿】旭川：經濟酒店 烏帕希 (Hotel WBF Asahikawa) [續住第二晚，行李免搬動]",
                   "[Accommodation] Asahikawa: Hotel WBF Asahikawa [Stay 2nd night, no luggage moving]",
                   "【宿泊】旭川：ホテルWBF旭川 [連泊のため荷物移動なし]")
    },
    {
        "title": "DAY 3 🐧", 
        "sub": m("深度探索：北國秘境", "Deep Exploration: Northern Secrets", "北国の秘境を深く探求"),
        "desc": m("【超萌體驗】上午酒店退房，行李寄存於旭川站。上午9:10前到達旭川站搭乘47專線巴士前往【旭山動物園】觀賞著名的北極熊跳水與企鵝漫步。",
                  "[Cute Experience] Morning check-out, store luggage at Asahikawa Sta. Take bus 47 to Asahiyama Zoo to see diving polar bears & penguins.",
                  "午前チェックアウト、旭川駅に荷物を預ける。47番バスで旭山動物園へ。ホッキョクグマのダイブとペンギンの散歩を見学。"),
        "note1": m("【鐵路移動】下午返回旭川站提取行李，使用週遊券搭乘 JR 特急列車（免費劃指定席對號座）前往札幌（車程約1.5小時）。抵達後入住格蘭貝爾札幌酒店，夜晚漫步【貍小路商店街】。",
                   "[Train Travel] Afternoon return to Asahikawa Sta. Take JR Express (reserved seating) to Sapporo (~1.5h). Check into Granbell Hotel Sapporo. Evening stroll at Tanukikoji.",
                   "【鉄道移動】午後旭川駅に戻る。周遊券でJR特急（指定席）に乗り札幌へ。グランベルホテル札幌にチェックイン。夜は狸小路商店街を散策。"),
        "note2": m("【團隊膳食】早餐：LAWSON/FAMILYMART/7-11 | 午餐：動物園內自理 | 晚餐：札幌特色湯咖哩 🍛",
                   "[Meals] Breakfast: Convenience Store | Lunch: Zoo | Dinner: Sapporo Soup Curry 🍛",
                   "【お食事】朝食：コンビニ | 昼食：動物園内で各自 | 夕食：札幌名物スープカレー 🍛"),
        "note3": m("【當晚住宿】札幌：格蘭貝爾札幌酒店 (Sapporo Hotel by Granbell)",
                   "[Accommodation] Sapporo Hotel by Granbell",
                   "【宿泊】グランベルホテル札幌 (Sapporo Hotel by Granbell)")
    },
    {
        "title": "DAY 4 🛶", 
        "sub": m("文化歷史：小樽運河之旅", "Culture & History: Otaru Canal Tour", "文化と歴史：小樽運河の旅"),
        "desc": m("欣賞煤氣燈夜景、三角市場食海鮮 🦀。", "Enjoy gas lamp night views and fresh seafood at Sankaku Market 🦀.", "ガス灯の夜景と三角市場での新鮮な海鮮を満喫 🦀。"),
        "note1": m("小樽運河散策。", "Otaru Canal stroll.", "小樽運河散策。")
    },
    {
        "title": "DAY 5 🛍️", 
        "sub": m("購物狂熱：北廣島 Outlet", "Shopping Frenzy: Kitahiroshima Outlet", "ショッピング：北広島アウトレット"),
        "desc": m("坐直達大巴去【北廣島三井 Outlet】室內瘋狂血拼。", "Take a direct bus to Mitsui Outlet Park Kitahiroshima for a shopping spree.", "直通バスで三井アウトレットパーク札幌北広島へ。室内でショッピング。"),
        "note1": m("夜晚睇藻岩山新三大夜景 ✨。", "Evening: Enjoy Mt. Moiwa's spectacular night view ✨.", "夜は藻岩山の日本新三大夜景を鑑賞 ✨。")
    },
    {
        "title": "DAY 6 🍫", 
        "sub": m("童趣體驗：白色戀人公園", "Fun Experience: Shiroi Koibito Park", "童心に帰る：白い恋人パーク"),
        "desc": m("札幌市區經典散策、參觀白色戀人朱古力工廠 🍪。", "Classic Sapporo city stroll, visit Shiroi Koibito Chocolate Factory 🍪.", "札幌市内散策と白い恋人チョコレート工場見学 🍪。"),
        "note1": m("完美句點。", "A perfect ending.", "完璧な締めくくり。")
    },
    {
        "title": "DAY 7 🛫", 
        "sub": m("歸途：狸小路商店街", "Return: Tanukikoji Shopping Street", "帰路：狸小路商店街"),
        "desc": m("09:00 札幌市補貨 | 12:00 午餐 | 15:00 前往機場手信街最後衝刺後各自登機返家。", "09:00 Last-minute shopping | 12:00 Lunch | 15:00 Final souvenir shopping at the airport, then board flight home.", "09:00 札幌市内で買い足し | 12:00 昼食 | 15:00 空港のお土産街で最後の買い物の後、帰国の途へ。"),
        "flight": m("CX583 or HD032", "CX583 or HD032", "CX583 または HD032")
    }
]

# 在這裡將第一張圖片替換為你提供的相片連結
imgs = [
    'https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp',
    'https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp', 
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxxCb13giR5qt9ifcOxxgdplCLM4sSXWwNFDMzQzm60jDOBkll5VvMsPs&s=10', 
    'https://images.trvl-media.com/place/6104012/f8fa157e-15a4-4533-84ef-b21cb5b53110.jpg', 
    'https://static.gltjp.com/glt/data/article/21000/20442/20230926_145350_43e48639_w1920.webp', 
    'https://hk.wamazing.com/media/wp-content/uploads/sites/5/2019/07/hokkaidomitsuioutlet_pixta_84488453_M.jpg.webp', 
    'https://d1grca2t3zpuug.cloudfront.net/2025/10/2025shiroikoibitopark1-870x500-1761562254.webp'
]

# 生成 HTML 行程
sections_html = ""
for i, item in enumerate(itinerary):
    notes_html = ""
    for key in ['note1', 'note2', 'note3', 'note4', 'flight']:
        if key in item:
            notes_html += f"<p style='font-size: 14px; color: #ccc; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 8px; margin-top: 8px;'>💡 {item[key]}</p>"
            
    sections_html += f'''
    <div class="v-section" style="background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)), url('{imgs[i]}');">
        <div class="glass-box">
            <h1 style="color:#ffcc00; font-size: 28px; margin-bottom: 5px;">{item['title']}</h1>
            <h3 style="margin-bottom: 12px; font-size: 18px;">{item['sub']}</h3>
            <p style="font-size: 15px; line-height: 1.6; margin-bottom: 15px;">{item['desc']}</p>
            {notes_html}
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
        
        .lang-en .zh, .lang-en .jp {{ display: none !important; }}
        .lang-jp .zh, .lang-jp .en {{ display: none !important; }}
        .lang-zh .en, .lang-zh .jp {{ display: none !important; }}
        
        .lang-btn {{ cursor: pointer; transition: 0.2s; color: #aaa; }}
        .lang-btn:hover {{ color: #fff; }}
        
        .lang-zh .btn-zh {{ color: #ffcc00; font-weight: bold; }}
        .lang-en .btn-en {{ color: #ffcc00; font-weight: bold; }}
        .lang-jp .btn-jp {{ color: #ffcc00; font-weight: bold; }}
        
        .top-bar {{ position: fixed; top: 0; width: 100%; height: 60px; background: rgba(0,0,0,0.8); backdrop-filter: blur(10px); z-index: 1000; display: flex; align-items: center; padding: 0 20px; border-bottom: 1px solid #333; }}
        .main-scroll-container {{ height: 100vh; overflow-y: scroll; scroll-snap-type: y mandatory; scroll-behavior: smooth; }}
        .main-scroll-container::-webkit-scrollbar {{ display: none; }}
        
        .welcome-page {{ height: 100vh; width: 100vw; scroll-snap-align: start; display: flex; flex-direction: column; justify-content: center; background: url('https://i.imgur.com/image_ae83e1.png') no-repeat center/cover; position: relative; }}
        .welcome-page::before {{ content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 1; }}
        
        .h-carousel {{ display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 20px; padding: 0 10vw; width: 100%; position: relative; z-index: 2; margin-top: 30px; }}
        .h-carousel::-webkit-scrollbar {{ display: none; }}
        
        .card {{ flex: 0 0 75%; max-width: 300px; background: rgba(20, 20, 20, 0.85); backdrop-filter: blur(15px); border-radius: 20px; scroll-snap-align: center; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); display: flex; flex-direction: column; }}
        .card img {{ width: 100%; height: 200px; object-fit: cover; }}
        .card-content {{ padding: 20px; text-align: center; flex: 1; display: flex; flex-direction: column; justify-content: center; }}
        .btn-more {{ background: #ffcc00; color: #000; padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold; font-size: 16px; cursor: pointer; display: block; border: none; width: 100%; }}
        
        .v-section {{ height: 100vh; width: 100vw; display: flex; justify-content: center; align-items: center; background-size: cover; background-position: center; scroll-snap-align: start; }}
        .glass-box {{ width: 85%; max-width: 500px; padding: 30px; border-radius: 20px; background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.2); text-align: left; }}
    </style>
</head>
<body class="lang-zh">
    <div class="top-bar">
        <div onclick="document.getElementById('welcome-page').scrollIntoView({{behavior: 'smooth'}})" style="color:#ffcc00; font-weight:bold; font-size:16px; white-space:nowrap; cursor:pointer;">
            {m("發哥旅行社 ✈️", "Fat Gor Travel ✈️", "ファットゴー旅行社 ✈️")}
        </div>
        
        <div style="flex:1; overflow:hidden; margin:0 15px;">
            <marquee direction="left" scrollamount="5" style="color:white; font-size:14px; margin-top: 4px;">
                {m("📢 現正報名：現在加入行程每位減 HKD$50！一齊出發去北海道啦！", 
                   "📢 Special Offer: Join now and save HKD$50 per person! Let's go to Hokkaido!", 
                   "📢 絶賛受付中：今ならお一人様50香港ドル割引！一緒に北海道へ行こう！")}
            </marquee>
        </div>
        
        <div style="font-size:12px; white-space:nowrap;">
            <span class="lang-btn btn-zh" onclick="setLanguage('zh')">繁</span> | 
            <span class="lang-btn btn-en" onclick="setLanguage('en')">EN</span> | 
            <span class="lang-btn btn-jp" onclick="setLanguage('jp')">JP</span>
        </div>
    </div>
    
    <div class="main-scroll-container" id="main-container">
        
        <div class="welcome-page" id="welcome-page">
            <div style="position:relative; z-index:2; text-align:center; margin-bottom:20px; margin-top:40px;">
                <h1 style="color:white; font-size: 28px;">
                    {m("精選行程推介", "Featured Itineraries", "おすすめの旅")}
                </h1>
                <p style="color:#aaa; font-size: 14px;">
                    {m("左右滑動探索更多", "Swipe left/right to explore", "左右にスワイプして探索")}
                </p>
            </div>
            
            <div class="h-carousel">
                <div class="card">
                    <img src="{imgs[0]}" alt="Hokkaido">
                    <div class="card-content">
                        <h2 style="font-size:18px;">
                            {m("北海道仲夏夜如夢之旅 🌸", "Hokkaido Midsummer Dream 🌸", "北海道 真夏の夢の旅 🌸")}
                        </h2>
                        <p style="font-size: 12px; color: #aaa; margin-bottom: 15px;">
                            {m("7天6夜 | 夏日家庭樂", "7 Days 6 Nights | Summer Family Fun", "6泊7日 | 夏の家族旅行")}
                        </p>
                        <button class="btn-more" onclick="document.getElementById('itinerary-start').scrollIntoView({{behavior: 'smooth'}})">
                            {m("了解更多", "Learn More", "詳細を見る")}
                        </button>
                    </div>
                </div>
                
                {''.join([f'''
                <div class="card" style="opacity: 0.7;">
                    <img src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=600&auto=format&fit=crop" style="filter: grayscale(80%);">
                    <div class="card-content">
                        <h2 style="color:#888;">{m("Coming Soon...", "Coming Soon...", "近日公開...")}</h2>
                        <p style="font-size: 12px; color: #666;">{m("敬請期待", "Stay Tuned", "お楽しみに")}</p>
                    </div>
                </div>
                ''' for _ in range(4)])}
            </div>
        </div>

        <div id="itinerary-start"></div>
        {sections_html}
    </div>

    <script>
        function setLanguage(lang) {{
            document.body.className = 'lang-' + lang;
        }}
    </script>
</body>
</html>
""", height=850)
