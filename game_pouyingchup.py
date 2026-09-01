import random
import streamlit as st

st.title("เกมสล็อตหมุนดวง")
st.write("กดปุ่มเพื่อหมุน ถ้าได้รูปเหมือนกัน 3 อันจะชนะ!")

# กำหนดสัญลักษณ์
symbols = ["🍎", "🍌", "🍒", "🍇"]

# สร้าง Session State เก็บเงิน
if "money" not in st.session_state:
    st.session_state.money = 100

st.write("เงินคงเหลือ:", st.session_state.money, "บาท")

# ปุ่มกดหมุน
if st.button("หมุนสล็อต (ครั้งละ 10 บาท)"):
    if st.session_state.money >= 10:
        st.session_state.money -= 10

        # สุ่มรูป 3 ช่อง
        slot1 = random.choice(symbols)
        slot2 = random.choice(symbols)
        slot3 = random.choice(symbols)

        # แสดงผล
        st.write("ผลการหมุน:")
        st.header(f"{slot1} | {slot2} | {slot3}")

        # เช็กผลแพ้ชนะ
        if slot1 == slot2 == slot3:
            st.success("คุณชนะ! ได้รับ 50 บาท")
            st.session_state.money += 50
        else:
            st.info("เสียใจด้วย คุณไม่ถูกรางวัล")
    else:
        st.error("เงินของคุณหมดแล้ว!")

# ปุ่มเติมเงิน
if st.button("เริ่มใหม่ / เติมเงิน"):
    st.session_state.money = 100
    st.rerun()
