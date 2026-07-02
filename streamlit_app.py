import streamlit as st

# 設置頁面寬度
st.set_page_config(layout="wide")

# 自訂 CSS 實現毛玻璃效果與 Apple 風格
st.markdown("""
    <style>
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
    }
    .promo-logo {
        width: 150px;
        height: 150px;
        background-color: #ff3b30;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        font-size: 20px;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 頁面內容
st.title("北海道之美：夏日探索")
st.write("---")

# 促銷 Logo
st.markdown('<div class="promo-logo">立即報名<br>-50 HKD</div>', unsafe_allow_html=True)

# 行程卡片
with st.container():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("✈️ 尊享航空體驗")
    st.write("香港國泰航空與北海道國際航空 (AIRDO) 帶給您最頂級的空中禮遇。")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("## 旅程亮點")
# 這裡可以繼續加入更多 Apple 風格的行程區塊...
