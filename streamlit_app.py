import streamlit as st

# 移除 Streamlit 預設的間距
st.markdown("""
    <style>
    /* 確保全螢幕無白邊 */
    .block-container { padding: 0 !important; max-width: 100% !important; }
    
    /* 設定每一頁的區塊 */
    .full-screen-section {
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    
    .text-box { text-align: center; background: rgba(0,0,0,0.3); padding: 20px; }
    </style>
""", unsafe_allow_html=True)

# 定義顯示區塊的函式 (直接使用 CSS background-image)
def show_page(img_url, title, sub):
    st.markdown(f"""
        <div class="full-screen-section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{img_url}');">
            <div class="text-box">
                <h1 style="font-size: 80px;">{title}</h1>
                <p style="font-size: 40px;">{sub}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 顯示內容
show_page('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp', '北海道之仲夏夜', '2026年7月16日啟程')
show_page('https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp', 'DAY 1', '啟程與燒肉之夜')
