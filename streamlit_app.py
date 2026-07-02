import streamlit as st

# 網頁設定
st.set_page_config(layout="wide")

st.markdown("""
    <style>
    /* 1. 全站背景設定 (已加入你的圖片連結與黑色濾鏡) */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* 2. 強制所有文字為白色 */
    h1, h2, h3, p, div {
        color: white !important;
    }
    
    /* 3. 個別調教文字大小的區塊 (你可以自由修改 px 數值) */
    .title-size { font-size: 72px !important; font-weight: bold; margin-bottom: 40px; }/title
    .subtitle-size { font-size: 50px !important; margin-bottom: 15px; }/second
    .content-size { font-size: 50px !important; line-height: 1.8; margin-bottom: 10px; }/thrid
    
    /* 4. 移除所有玻璃效果，確保背景乾淨 */
    .clean-box {
        background: transparent;
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 網頁排版內容
st.markdown('<div class="clean-box">', unsafe_allow_html=True)

# 你可以在這裡自由呼叫不同的 class 來調整每一段的大小
st.markdown('<div class="title-size">北海道之仲夏夜如夢之旅</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-size">尊享頂級航空服務體驗</div>', unsafe_allow_html=True)
st.markdown('<div class="content-size">透過香港國泰航空與北海道國際航空 (AIRDO)，為您的家庭打造一場難忘的冒險。</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
