import random
import streamlit as st

st.title("🧪 เกมตอบคำถามชีววิทยา (แนว สอวน.)")
st.write("ทดสอบความรู้ชีววิทยาเตรียมสอบ สอวน. ทายคำศัพท์หรือชื่อโครงสร้างให้ถูกต้อง!")

# คลังข้อสอบชีววิทยา (สามารถเพิ่มข้อสอบเองได้)
quiz_db = [
    {
        "question": "ออร์แกเนลล์ใดทำหน้าที่เกี่ยวกับการสังเคราะห์ลิพิด และกำจัดสารพิษในเซลล์ตับ?",
        "answer": "SER",
        "hint": "ชื่อย่อภาษาอังกฤษ 3 ตัว (Smooth Endoplasmic Reticulum)"
    },
    {
        "question": "การลำเลียงสารเข้าสู่เซลล์โดยการเว้าของเยื่อหุ้มเซลล์เพื่อโอบล้อมสารที่เป็นของแข็ง เรียกว่าอะไร?",
        "answer": "PHAGOCYTOSIS",
        "hint": "ขึ้นต้นด้วยตัว P (Cell eating)"
    },
    {
        "question": "กระบวนการสังเคราะห์แสงในพืช เกิดการคงตัวของคาร์บอน (Carbon fixation) ที่บริเวณใดของคลอโรพลาสต์?",
        "answer": "STROMA",
        "hint": "ของเหลวภายในคลอโรพลาสต์"
    },
    {
        "question": "ระยะใดของการแบ่งเซลล์แบบไมโทซิส (Mitosis) ที่โครโมโซมจะเรียงตัวกันอยู่ตรงกลางเซลล์ชัดเจนที่สุด?",
        "answer": "METAPHASE",
        "hint": "ขึ้นต้นด้วย M"
    },
    {
        "question": "พันธะเคมีที่เชื่อมระหว่างกรดอะมิโนสองโมเลกุลในโครงสร้างของโปรตีน เรียกว่าอะไร?",
        "answer": "PEPTIDE",
        "hint": "พันธะ ... (Peptide bond)"
    }
]

# ระบบจัดการ Session State
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(quiz_db)
    st.session_state.score = 0
    st.session_state.total_played = 0
    st.session_state.show_hint = False

q_data = st.session_state.current_question

# แสดงข้อมูลโจทย์และคะแนน
st.write(f"**คะแนนสะสม:** {st.session_state.score} / {st.session_state.total_played} ข้อ")
st.write("---")
st.subheader(f"คำถาม: {q_data['question']}")

# ปุ่มแสดงคำใบ้
if st.button("💡 ขอคำใบ้"):
    st.session_state.show_hint = True

if st.session_state.show_hint:
    st.info(f"คำใบ้: {q_data['hint']}")

# ช่องกรอกคำตอบ (แปลงเป็นพิมพ์ใหญ่ทั้งหมดเพื่อเช็กผลง่ายขึ้น)
user_answer = st.text_input("พิมพ์คำตอบภาษาอังกฤษ (ตัวพิมพ์เล็กหรือใหญ่ก็ได้):").strip().upper()

# ปุ่มส่งคำตอบ
if st.button("ส่งคำตอบ"):
    if user_answer:
        st.session_state.total_played += 1
        if user_answer == q_data["answer"]:
            st.success("🎉 ถูกต้อง! เก่งมากครับ")
            st.session_state.score += 1
        else:
            st.error(f"❌ ยังไม่ถูกต้อง คำตอบที่ถูกคือ: **{q_data['answer']}**")
    else:
        st.warning("กรุณาพิมพ์คำตอบก่อนกดส่งครับ")

# ปุ่มสุ่มข้อต่อไป
st.write("---")
if st.button("➡️ ไปข้อต่อไป"):
    st.session_state.current_question = random.choice(quiz_db)
    st.session_state.show_hint = False
    st.rerun()

# ปุ่มรีเซ็ตคะแนน
if st.button("🔄 รีเซ็ตคะแนนทั้งหมด"):
    st.session_state.score = 0
    st.session_state.total_played = 0
    st.session_state.current_question = random.choice(quiz_db)
    st.session_state.show_hint = False
    st.rerun()
