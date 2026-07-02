import streamlit as st

# 設定全螢幕與無邊距
st.set_page_config(layout="wide")

st.markdown("""
    <style>
    /* 移除 Streamlit 預設的 Padding */
    .stApp { padding: 0 !important; }
    
    /* 滾動容器設定：強制對齊 */
    .scroll-container {
        height: 100vh;
        overflow-y: scroll;
        scroll-snap-type: y mandatory; /* 這就是關鍵：強制滾動鎖定 */
    }
    
    /* 每一頁的設定 */
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
        scroll-snap-align: start; /* 每一頁都鎖定在起點 */
        scroll-snap-stop: always;  /* 強制每一頁都要停頓 */
    }
    
    .text-box { text-align: center; background: rgba(0,0,0,0.3); padding: 20px; }
    </style>
""", unsafe_allow_html=True)

# 顯示容器開始
st.markdown('<div class="scroll-container">', unsafe_allow_html=True)

# 定義顯示區塊函式
def show_page(img_url, title, sub):
    st.markdown(f"""
        <div class="full-screen-section" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{img_url}');">
            <div class="text-box">
                <h1 style="font-size: 80px;">{title}</h1>
                <p style="font-size: 40px;">{sub}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 放入你的圖片與內容
show_page('https://static.gltjp.com/glt/data/article/21000/20526/20231120_140429_94a4429a_w1920.webp', '北海道之仲夏夜', '2026年7月16日啟程')
show_page('https://ak-d.tripcdn.com/images/0222n12000l3pxclpD02D_W_600_0_R5.webp', 'DAY 1', '啟程與燒肉之夜')

# 結束容器
st.markdown('</div>', unsafe_allow_html=True)
