import random
import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="เกมเป่ายิ้งฉุบ", page_icon="✊")

st.title("✊ ✋ ✌️ เกมเป่ายิ้งฉุบ")
st.write("เลือกตัวเลือกของคุณเพื่อแข่งกับคอมพิวเตอร์!")

# กำหนดตัวเลือกและอีโมจิ
choices = {"หิน": "✊", "กระดาษ": "✋", "กรรไกร": "✌️"}

# ระบบบันทึกคะแนน (Session State)
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "bot_score" not in st.session_state:
    st.session_state.bot_score = 0

# แสดงคะแนนปัจจุบัน
col_score1, col_score2 = st.columns(2)
col_score1.metric("คะแนนของคุณ", st.session_state.user_score)
col_score2.metric("คะแนนคอมพิวเตอร์", st.session_state.bot_score)

st.divider()

# ปุ่มเลือกเล่น
st.subheader("เลือกตัวเลือกของคุณ:")
col1, col2, col3 = st.columns(3)

user_choice = None
if col1.button("✊ หิน", use_container_width=True):
    user_choice = "หิน"
if col2.button("✋ กระดาษ", use_container_width=True):
    user_choice = "กระดาษ"
if col3.button("✌️ กรรไกร", use_container_width=True):
    user_choice = "กรรไกร"

# ลอจิกการตัดสินผลแพ้ชนะ
if user_choice:
    bot_choice = random.choice(list(choices.keys()))

    st.write("---")
    res_col1, res_col2 = st.columns(2)
    res_col1.info(f"คุณเลือก: **{user_choice}** {choices[user_choice]}")
    res_col2.info(f"คอมพิวเตอร์เลือก: **{bot_choice}** {choices[bot_choice]}")

    # ตรวจสอบผลลัพธ์
    if user_choice == bot_choice:
        st.warning("🤝 ผลลัพธ์: เสมอกัน!")
    elif (
        (user_choice == "หิน" and bot_choice == "กรรไกร")
        or (user_choice == "กระดาษ" and bot_choice == "หิน")
        or (user_choice == "กรรไกร" and bot_choice == "กระดาษ")
    ):
        st.success("🎉 ผลลัพธ์: คุณชนะ!")
        st.session_state.user_score += 1
    else:
        st.error("💻 ผลลัพธ์: คอมพิวเตอร์ชนะ!")
        st.session_state.bot_score += 1

# ปุ่มรีเซ็ตคะแนน
st.divider()
if st.button("🔄 รีเซ็ตคะแนนทั้งหมด"):
    st.session_state.user_score = 0
    st.session_state.bot_score = 0
    st.rerun()
