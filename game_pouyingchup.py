import random
import streamlit as st

st.title("🧪 สอวน. ชีววิทยา Challenge")
st.write("ทายคำศัพท์และแนวคิดสำคัญทางชีววิทยา เพื่อเตรียมความพร้อมสอบ สอวน.")

# คลังข้อสอบชีววิทยา สอวน. แบบเจาะจง (รองรับหลายคำตอบ)
quiz_db = [
    {
        "question": "พันธะโควาเลนต์ที่เชื่อมระหว่างหมู่คาร์บอกซิลของกรดอะมิโนตัวหนึ่ง กับหมู่อะมิโนของกรดอะมิโนอีกตัวหนึ่ง เรียกว่าอะไร?",
        "answers": ["PEPTIDE", "PEPTIDE BOND", "พันธะเปปไทด์"],
        "hint": "คำศัพท์ภาษาอังกฤษขึ้นต้นด้วยตัว P หรือตอบภาษาไทยก็ได้"
    },
    {
        "question": "ออร์แกเนลล์ที่มีโครงสร้างแบบ เยื่อหุ้มสองชั้น (Double membrane) และมี DNA เป็นของตัวเอง คืออะไรบ้าง? (ระบุมา 1 ชื่อ)",
        "answers": ["MITOCHONDRIA", "CHLOROPLAST", "NUCLEUS", "ไมโทคอนเดรีย", "คลอโรพลาสต์", "นิวเคลียส"],
        "hint": "ตอบชื่อใดชื่อหนึ่ง เช่น ไมโทคอนเดรีย หรือ คลอโรพลาสต์"
    },
    {
        "question": "กระบวนการเปลี่ยนกลูโคส 1 โมเลกุลให้เป็นไพรูเวต 2 โมเลกุล ซึ่งเกิดขึ้นที่ไซโทพลาซึม เรียกว่ากระบวนการอะไร?",
        "answers": ["GLYCOLYSIS", "ไกลโคลิซิส", "ไกลโคไลซิส"],
        "hint": "ขั้นตอนแรกสุดของการหายใจระดับเซลล์ (Cellular respiration)"
    },
    {
        "question": "สารที่เป็นตัวรับอิเล็กตรอนตัวสุดท้าย (Final electron acceptor) ในกระบวนการหายใจระดับเซลล์แบบใช้ออกซิเจน คืออะไร?",
        "answers": ["OXYGEN", "O2", "ออกซิเจน", "แก๊สออกซิเจน"],
        "hint": "เป็นแก๊สที่สิ่งมีชีวิตใชัในการหายใจ"
    },
    {
        "question": "เอนไซม์ชนิดใดทำหน้าที่ตัดสายสเปกตรัมพันธะไฮโดรเจน เพื่อคลายเกลียวคู่ออกเป็นสายเดี่ยวในกระบวนการจำลอง DNA (DNA Replication)?",
        "answers": ["HELICASE", "DNA HELICASE", "เฮลิเคส"],
        "hint": "ขึ้นต้นด้วยตัว H (Unzip DNA)"
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

# ช่องกรอกคำตอบ
user_answer = st.text_input("พิมพ์คำตอบของคุณ (ภาษาไทย หรือ ภาษาอังกฤษ):").strip().upper()

# ปุ่มส่งคำตอบ
if st.button("ส่งคำตอบ"):
    if user_answer:
        st.session_state.total_played += 1
        
        # ตรวจสอบว่าคำตอบที่พิมพ์ เข้าเงื่อนไขคำตอบใดคำตอบหนึ่งใน List หรือไม่
        accepted_answers = [ans.upper() for ans in q_data["answers"]]
        
        if user_answer in accepted_answers:
            st.success("🎉 ถูกต้อง! เก่งมากครับ")
            st.session_state.score += 1
        else:
            main_ans = q_data['answers'][0]
            st.error(f"❌ ยังไม่ถูกต้อง คำตอบที่ถูกต้องคือ: **{main_ans}** (หรือคำใกล้เคียง)")
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
