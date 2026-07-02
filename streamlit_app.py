import streamlit as st

# 自訂 CSS，重點在於 background 的 linear-gradient
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    h1, h2, h3, p, div {
        color: white !important;
    }
    .content-card {
        background: rgba(255, 255, 255, 0.05); /* 更薄的毛玻璃 */
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 顯示內容
st.markdown('<div class="content-card">', unsafe_allow_html=True)
st.title("北海道：探索之旅")
st.write("這是一場為家庭量身打造的夏日冒險。")
st.markdown('</div>', unsafe_allow_html=True)
