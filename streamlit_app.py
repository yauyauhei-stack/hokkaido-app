import streamlit as st

st.title("北海道家族之旅 ✈️")
st.subheader("發哥旅行社：專屬行程對帳系統")

# 互動功能：計算費用
st.write("### 成員費用計算器")
member_type = st.radio("選擇您的身分：", ("香港成員", "日本成員"))

if member_type == "香港成員":
    st.success("您的應付總額為: HK$ 9,412.38")
    st.write("- 包含：機票、分攤酒店、巴士、景點及 4 人份 JR Pass")
else:
    st.warning("您的應付總額為: HK$ 6,529.41")
    st.write("- 包含：AirDo 機票、分攤酒店、巴士、景點及當地交通")

st.info("如有疑問，請聯絡發哥旅行社：87235839")
