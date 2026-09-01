import random
import streamlit as st

st.title("🧪 ชีววิทยา Challenge")
st.write("ทายคำศัพท์และแนวคิดสำคัญทางชีววิทยา ")

# คลังข้อสอบชีววิทยา 
quiz_db = [
    {
        "question": "พันธะโควาเลนต์ที่เชื่อมระหว่างหมู่คาร์บอกซิลของกรดอะมิโนตัวหนึ่ง กับหมู่อะมิโนของกรดอะมิโนอีกตัวหนึ่ง เรียกว่าอะไร?",
        "answers": ["PEPTIDE", "PEPTIDE BOND", "พันธะเปปไทด์"],
        "hint": "ขึ้นต้นด้วยตัว P หรือตอบภาษาไทยว่า พันธะ..."
    },
    {
        "question": "ออร์แกเนลล์ที่มีโครงสร้างแบบ เยื่อหุ้มสองชั้น (Double membrane) และมี DNA เป็นของตัวเอง คืออะไรบ้าง? (ระบุมา 1 ชื่อ)",
        "answers": ["MITOCHONDRIA", "CHLOROPLAST", "NUCLEUS", "ไมโทคอนเดรีย", "คลอโรพลาสต์", "นิวเคลียส"],
        "hint": "เช่น ไมโทคอนเดรีย หรือ คลอโรพลาสต์"
    },
    {
        "question": "น้ำตาลโมเลกุลเดี่ยวชนิดใดที่เป็นแหล่งพลังงานหลักของเซลล์ และเป็นสารตั้งต้นในกระบวนการหายใจระดับเซลล์?",
        "answers": ["GLUCOSE", "กลูโคส", "น้ำตาลกลูโคส"],
        "hint": "น้ำตาลสายเดี่ยวที่พบมากในเลือด (ขึ้นต้นด้วยตัว G)"
    },
    {
        "question": "แก๊สชนิดใดที่สิ่งมีชีวิตจำเป็นต้องใช้ในกระบวนการหายใจระดับเซลล์เพื่อสร้างพลังงาน ATP?",
        "answers": ["OXYGEN", "O2", "ออกซิเจน", "แก๊สออกซิเจน"],
        "hint": "แก๊สที่เราสูดหายใจเข้าผ่านปอด"
    },
    {
        "question": "เบสชนิดใดในโมเลกุล DNA ที่จะจับคู่กับ อะดีนีน (Adenine : A) เสมอ?",
        "answers": ["THYMINE", "T", "ไทมีน", "เบสไทมีน"],
        "hint": "ขึ้นต้นด้วยตัว T (การจับคู่เบสสมเคมี A กับ...)"
    }
]

# ฟังก์ชันสำหรับเริ่มต้นเกมใหม่
def reset_game():
    st.session_state.questions_queue = list(range(len(quiz_db)))
    random.shuffle(st.session_state.questions_queue)  # สุ่มสลับลำดับข้อสอบไม่ให้ซ้ำ
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.show_hint = False
    st.session_state.answered_current = False

# ระบบจัดการ Session State
if "questions_queue" not in st.session_state:
    reset_game()

total_questions = len(quiz_db)
current_step = st.session_state.current_index

# --- หน้าสรุปคะแนนเมื่อทำครบทุกข้อ ---
if current_step >= total_questions:
    st.balloons()
    st.header("🏆 สรุปผลการทดสอบ")
    
    score = st.session_state.score
    percentage = (score / total_questions) * 100
    
    st.write(f"คุณตอบถูกทั้งหมด: **{score}** จาก **{total_questions}** ข้อ")
    st.write(f"คิดเป็น: **{percentage:.1f}%**")
    
    if percentage == 100:
        st.success("🥇 สุดยอดมาก! คุณได้คะแนนเต็ม ตึงเปรี๊ยะ ตึงเปรี๊ยะ")
    elif percentage >= 60:
        st.info("🥈 ทำได้ดีมาก! ลองทบทวนจุดที่ผิดอีกนิดรับรองเป๊ะขึ้นแน่นอน")
    else:
        st.warning("🥉 พยายามได้ดีแล้ว! ลองกดเริ่มใหม่เพื่อฝึกฝนอีกรอบนะ")

    if st.button("🔄 เริ่มทำแบบทดสอบใหม่อีกครั้ง"):
        reset_game()
        st.rerun()

# --- หน้าทำแบบทดสอบ ---
else:
    q_index = st.session_state.questions_queue[current_step]
    q_data = quiz_db[q_index]

    # แสดงสถานะความคืบหน้า
    st.write(f"**ข้อที่ {current_step + 1} / {total_questions}** | คะแนนสะสม: {st.session_state.score}")
    st.progress((current_step) / total_questions)
    st.write("---")
    
    st.subheader(f"คำถาม: {q_data['question']}")

    # ปุ่มแสดงคำใบ้
    if st.button("💡 ขอคำใบ้"):
        st.session_state.show_hint = True

    if st.session_state.show_hint:
        st.info(f"คำใบ้: {q_data['hint']}")

    # ช่องกรอกคำตอบ
    user_answer = st.text_input("พิมพ์คำตอบของคุณ (ภาษาไทย หรือ ภาษาอังกฤษ):", key=f"input_{current_step}").strip().upper()

    # ปุ่มส่งคำตอบ
    if st.button("ส่งคำตอบ") and not st.session_state.answered_current:
        if user_answer:
            st.session_state.answered_current = True
            accepted_answers = [ans.upper() for ans in q_data["answers"]]
            
            if user_answer in accepted_answers:
                st.success("🎉 ถูกต้อง! เก่งมากครับ")
                st.session_state.score += 1
            else:
                main_ans = q_data['answers'][0]
                st.error(f"❌ ยังไม่ถูกต้อง คำตอบที่ถูกต้องคือ: **{main_ans}**")
        else:
            st.warning("กรุณาพิมพ์คำตอบก่อนกดส่งครับ")

    # ปุ่มไปข้อถัดไป
    if st.session_state.answered_current:
        st.write("---")
        if st.button("➡️ ไปข้อต่อไป"):
            st.session_state.current_index += 1
            st.session_state.show_hint = False
            st.session_state.answered_current = False
            st.rerun()
