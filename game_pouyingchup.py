import random
import streamlit as st

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .status-card {
        background-color: #1e222d;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border: 1px solid #2e3440;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎯 เกมทายตัวเลขปริศนา</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a0a0a0;'>คอมพิวเตอร์สุ่มเลข 1 - 100 ไว้ ลองทายดูซิว่าจะใช้กี่รอบ!</p>", unsafe_allow_html=True)

# Session State
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.write("")

# Form สำหรับรับค่า
with st.form(key="guess_form"):
    guess = st.number_input("ใส่ตัวเลขที่คุณทาย (1-100):", min_value=1, max_value=100, step=1)
    submit_button = st.form_submit_button(label="🎯 ส่งคำตอบ", use_container_width=True)

if submit_button and not st.session_state.game_over:
    st.session_state.attempts += 1
    
    if guess < st.session_state.target_number:
        st.warning(f"💡 น้อยเกินไป! ลองทายตัวเลขที่ **สูงกว่า** {guess}")
    elif guess > st.session_state.target_number:
        st.warning(f"💡 มากเกินไป! ลองทายตัวเลขที่ **ต่ำกว่า** {guess}")
    else:
        st.balloons()
        st.success(f"🎉 ถูกต้องแล้ว! เลขปริศนาคือ **{st.session_state.target_number}**")
        st.info(f"🏆 คุณทายสำเร็จใน **{st.session_state.attempts}** ครั้ง")
        st.session_state.game_over = True

# ปุ่มเริ่มเกมใหม่
st.write("")
if st.button("🔄 เริ่มเกมใหม่", use_container_width=True):
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()
