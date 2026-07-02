import streamlit as st

# 自訂 CSS：純粹的黑色濾鏡背景，無毛玻璃，文字全白
st.markdown("""
    <style>
    /* 設定全站背景，疊加黑色濾鏡 */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* 強制所有文字元素為白色 */
    h1, h2, h3, p, div {
        color: white !important;
    }
    
    /* 移除所有玻璃效果，改為純粹的不透明色塊（若需要）或乾淨排版 */
    .content-box {
        background: transparent;
        padding: 40px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 頁面內容
st.markdown('<div class="content-box">', unsafe_allow_html=True)
st.title("北海道：夏日探索")
st.write("精選頂級航空服務與絕美行程體驗。")
st.markdown('</div>', unsafe_allow_html=True)
