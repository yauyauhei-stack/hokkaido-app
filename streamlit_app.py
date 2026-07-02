import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    /* 移除所有預設的外邊距，確保沒空白 */
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    /* 設定每一個行程的區域 */
    .section {
        height: 100vh;
        width: 100%;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }

    /* 圖片設定：使用 position: sticky 讓圖片在滑動時產生視覺黏貼效果 */
    .bg-img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-size: cover;
        background-position: center;
        z-index: -1; /* 圖片在最底層 */
        filter: brightness(0.6); /* 黑色濾鏡 */
    }

    /* 文字樣式 */
    .text-container {
        text-align: center;
        color: white;
        z-index: 1;
    }
    
    .title-size { font-size: 90px !important; font-weight: bold; }
    .subtitle-size { font-size: 50px !important; }
    .content-size { font-size: 30px !important; line-height: 1.8; }
    </style>
""", unsafe_allow_html=True)

# 函式：產生每一頁
def create_section(img_url, title, sub, content):
    st.markdown(f'''
        <div class="section">
            <div class="bg-img" style="background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{img_url}');"></div>
            <div class="text-container">
                <div class="title-size">{title}</div>
                <div class="subtitle-size">{sub}</div>
                <div class="content-size">{content}</div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# 頁面內容
create_section('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp', '北海道之仲夏夜', '2026年7月16日', '尊享頂級航空服務體驗')
create_section('https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp', 'DAY 1', '啟程', '前往北海道，品嚐當地地道燒肉')
# 你可以繼續用 create_section 加入後續的 Day 2 ~ Day 7
