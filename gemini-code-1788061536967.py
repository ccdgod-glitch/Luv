import streamlit as st
import datetime
import time

# --- การตั้งค่าหน้าเว็บ ---
st.set_page_config(
    page_title="Our Digital Love Letter ❤️",
    page_icon="💌",
    layout="centered"
)

# --- 1. ตั้งค่าข้อมูลส่วนตัว ---
CORRECT_PIN = "1205"  # รหัสผ่าน 4 หลัก (เช่น วันครบรอบ)
START_DATE = datetime.datetime(2024, 5, 12, 0, 0, 0)  # ปี, เดือน, วัน, ชม, นาที, วินาที ที่เริ่มรักกัน
SONG_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"  # เปลี่ยนเป็นลิงก์เพลง MP3 ที่ต้องการ

# --- ตรวจสอบสถานะการปลดล็อก (Session State) ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- 2. หน้ากรอกรหัสผ่าน (Passcode Protection) ---
if not st.session_state.authenticated:
    st.title(" Our Secret Code 🔒")
    st.caption("กรอกวันครบรอบของเราเพื่อเข้าสู่ความทรงจำ (4 หลัก)")
    
    pin_input = st.text_input("Passcode", type="password", max_chars=4, placeholder="••••")
    
    if st.button("ตกลง", use_container_width=True):
        if pin_input == CORRECT_PIN:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("รหัสผ่านไม่ถูกต้อง ลองใหม่อีกครั้งนะ!")

# --- 3. หน้าเนื้อหาหลัก (เมื่อปลดล็อกสำเร็จ) ---
else:
    # เล่นเพลง Background Music
    st.audio(SONG_URL, format="audio/mp3", autoplay=True)
    
    st.title("ถึงคนพิเศษของฉัน ❤️")
    st.subheader("Digital Love Letter 💌")
    st.write("---")

    # --- ฟีเจอร์ Countdown / Days Together ---
    now = datetime.datetime.now()
    diff = now - START_DATE
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    st.markdown("### ⏳ เรารักกันมานานแล้ว...")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("จำนวนวัน", f"{days} วัน")
    col2.metric("ชั่วโมง", f"{hours:02d}")
    col3.metric("นาที", f"{minutes:02d}")
    col4.metric("วินาที", f"{seconds:02d}")

    st.write("---")

    # --- ฟีเจอร์ Digital Love Letter ---
    st.markdown("""
    ขอบคุณนะที่เข้ามาเป็นเรื่องราวดีๆ ในทุกๆ วัน  
    ตั้งแต่วันแรกที่ได้รู้จักกัน จนถึงวันนี้ รอยยิ้มของคุณยังคงเป็นสิ่งที่ทำให้โลกของเราสดใสขึ้นเสมอ ✨

    ขอบคุณสำหรับความเข้าใจ ความหวังดี และทุกช่วงเวลาที่เราได้เรียนรู้ร่วมกัน  
    ไม่ว่าจะวันไหนๆ ก็อยากให้อยู่ข้างๆ กันแบบนี้ไปนานๆ นะครับ 💕
    """)

    # --- ฟีเจอร์ข้อความลับเพิ่มเติม ---
    with st.expander("คลิกเพื่ออ่านข้อความลับเพิ่มเติม 💌"):
        st.write("PS. สัญญาว่าจะพาไปกินของอร่อยๆ และอยู่ซัพพอร์ตกันแบบนี้ตลอดไปเลย รักคุณนะ! 🥰")