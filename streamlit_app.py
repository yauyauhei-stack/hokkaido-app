import streamlit as st

# 自訂 CSS，移除毛玻璃效果，保留黑色濾鏡與白色文字
st.markdown("""
    <style>
    /* 設定全站背景，疊加黑色濾鏡 */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* 強制所有文字元素為白色 */
    h1, h2, h3, p, div {
        color: white !important;
    }
    
    /* 移除毛玻璃，改為純粹的半透明黑色背景 */
    .simple-card {
        background: rgba(0, 0, 0, 0.4); 
        padding: 40px;
        border-radius: 20px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 頁面內容
st.markdown('<div class="simple-card">', unsafe_allow_html=True)
st.title("北海道：夏日家庭之旅")
st.write("體驗國泰航空與 AIRDO 的尊榮飛行服務。")
st.markdown('</div>', unsafe_allow_html=True)
