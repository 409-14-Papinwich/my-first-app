import random
import streamlit as st

st.title("เกมทายคำศัพท์ภาษาอังกฤษ")
st.write("ลองทายตัวอักษรเพื่อหาคำศัพท์ปริศนา โดยคุณมีโอกาสทายผิดได้ไม่เกิน 6 ครั้ง")

# รายชื่อคำศัพท์พร้อมคำใบ้
words_db = [
    {"word": "PYTHON", "hint": "ภาษาโปรแกรมมิ่งยอดนิยม"},
    {"word": "STREAMLIT", "hint": "ไลบรารีสำหรับสร้าง Web App"},
    {"word": "COMPUTER", "hint": "อุปกรณ์อิเล็กทรอนิกส์สำหรับคำนวณ"},
    {"word": "INTERNET", "hint": "เครือข่ายคอมพิวเตอร์ที่เชื่อมต่อทั่วโลก"}
]

# ระบบตั้งค่าเริ่มต้น (Session State)
if "secret_info" not in st.session_state:
    st.session_state.secret_info = random.choice(words_db)
    st.session_state.guessed_letters = []
    st.session_state.lives = 6

secret_word = st.session_state.secret_info["word"]
hint = st.session_state.secret_info["hint"]

# แสดงคำใบ้และโอกาสที่เหลือ
st.write("คำใบ้:", hint)
st.write("โอกาสทายผิดที่เหลือ:", st.session_state.lives, "ครั้ง")

# แสดงผลคำศัพท์แบบมีขีดช่องว่าง (เช่น P _ T H O N)
display_word = ""
for letter in secret_word:
    if letter in st.session_state.guessed_letters:
        display_word += letter + " "
    else:
        display_word += "_ "

st.header(display_word)

# ส่วนรับข้อมูลจากผู้ใช้
if st.session_state.lives > 0 and "_" in display_word:
    user_input = st.text_input("พิมพ์ตัวอักษรภาษาอังกฤษ (1 ตัว):", max_chars=1).upper()
    
    if st.button("ส่งคำตอบ"):
        if user_input:
            if user_input in st.session_state.guessed_letters:
                st.warning("คุณเคยทายตัวอักษรนี้ไปแล้ว!")
            else:
                st.session_state.guessed_letters.append(user_input)
                
                # เช็กว่าตัวอักษรที่ทายอยู่ในคำตอบหรือไม่
                if user_input not in secret_word:
                    st.session_state.lives -= 1
                    st.error("ผิด! ไม่มีตัวอักษรนี้")
                else:
                    st.success("ถูกต้อง!")
                st.rerun()

# สรุปผลการแข่งขัน
if "_" not in display_word:
    st.balloons()
    st.success("ยินดีด้วย! คุณทายถูกทั้งหมด")
elif st.session_state.lives <= 0:
    st.error(f"จบเกม! โอกาสหมดแล้ว คำที่ถูกต้องคือ: {secret_word}")

# ปุ่มเริ่มเกมใหม่
st.write("---")
if st.button("เริ่มเกมใหม่ / สุ่มคำใหม่"):
    st.session_state.secret_info = random.choice(words_db)
    st.session_state.guessed_letters = []
    st.session_state.lives = 6
    st.rerun()
