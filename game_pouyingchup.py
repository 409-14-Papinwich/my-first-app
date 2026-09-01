import random
import streamlit as st

st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮", layout="centered")

# Custom CSS ตกแต่ง UI
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2e 0%, #11111b 100%);
    }
    .score-card {
        background-color: #313244;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        border: 1px solid #45475a;
    }
    .score-title {
        font-size: 1rem;
        color: #a6adc8;
        margin-bottom: 5px;
    }
    .score-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: #cdd6f4;
    }
    .choice-box {
        background: #181825;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        color: #cdd6f4;
        border: 1px solid #313244;
    }
    div.stButton > button {
        border-radius: 16px;
        height: 100px;
        font-size: 1.5rem;
        font-weight: bold;
        border: 2px solid #45475a;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        transform: translateY(-5px);
        border-color: #89b4fa;
        box-shadow: 0 10px 20px rgba(137, 180, 250, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# หัวข้อหลัก
st.markdown("<h1 style='text-align: center; color: #cdd6f4;'>⚔️ BATTLE: ROCK PAPER SCISSORS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #bac2de;'>ดวลเป่ายิ้งฉุบกับ AI สมองกล</p>", unsafe_allow_html=True)

st.write("")

# ข้อมูลตัวเลือก
choices = {
    "หิน": {"emoji": "✊", "color": "#f38ba8"},
    "กระดาษ": {"emoji": "✋", "color": "#a6e3a1"},
    "กรรไกร": {"emoji": "✌️", "color": "#89b4fa"}
}

# Session State สำหรับบันทึกคะแนน
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "bot_score" not in st.session_state:
    st.session_state.bot_score = 0

# แสดงการ์ดคะแนน
col_score1, col_score2 = st.columns(2)
with col_score1:
    st.markdown(f"""
        <div class="score-card">
            <div class="score-title">👤 คุณ (You)</div>
            <div class="score-value">{st.session_state.user_score}</div>
        </div>
    """, unsafe_allow_html=True)

with col_score2:
    st.markdown(f"""
        <div class="score-card">
            <div class="score-title">🤖 คอมพิวเตอร์ (BOT)</div>
            <div class="score-value">{st.session_state.bot_score}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ปุ่มเลือกเล่น
st.markdown("<h4 style='text-align: center; color: #a6adc8;'>— เลือกท่าของคุณ —</h4>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

user_choice = None
if col1.button("✊\n\nหิน", use_container_width=True):
    user_choice = "หิน"
if col2.button("✋\n\nกระดาษ", use_container_width=True):
    user_choice = "กระดาษ"
if col3.button("✌️\n\nกรรไกร", use_container_width=True):
    user_choice = "กรรไกร"

# แสดงผลการแข่งขัน
if user_choice:
    bot_choice = random.choice(list(choices.keys()))
    
    st.write("")
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.markdown(f"""
            <div class="choice-box">
                คุณเลือก<br><br>
                <span style="font-size: 3rem;">{choices[user_choice]['emoji']}</span><br><br>
                {user_choice}
            </div>
        """, unsafe_allow_html=True)
        
    with res_col2:
        st.markdown(f"""
            <div class="choice-box">
                บอทเลือก<br><br>
                <span style="font-size: 3rem;">{choices[bot_choice]['emoji']}</span><br><br>
                {bot_choice}
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    
    # คำนวณผลลัพธ์
    if user_choice == bot_choice:
        st.warning("🤝 เสมอกัน! เอาใหม่รอบหน้า")
    elif (
        (user_choice == "หิน" and bot_choice == "กรรไกร")
        or (user_choice == "กระดาษ" and bot_choice == "หิน")
        or (user_choice == "กรรไกร" and bot_choice == "กระดาษ")
    ):
        st.balloons()
        st.success("🎉 ยินดีด้วย! คุณชนะในรอบนี้")
        st.session_state.user_score += 1
    else:
        st.error("💻 เสียใจด้วย! คอมพิวเตอร์ชนะ")
        st.session_state.bot_score += 1

# ปุ่มรีเซ็ต
st.write("")
st.write("")
if st.button("🔄 รีเซ็ตคะแนนทั้งหมด", use_container_width=True):
    st.session_state.user_score = 0
    st.session_state.bot_score = 0
    st.rerun()
