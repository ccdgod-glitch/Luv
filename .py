import streamlit as st
import datetime

# --- การตั้งค่าหน้าเว็บ ---
st.set_page_config(
    page_title="Our Digital Love Letter ❤️",
    page_icon="💌",
    layout="centered"
)

# --- ใส่ CSS และ JavaScript สำหรับเอฟเฟกต์หัวใจลอยในพื้นหลัง ---
hearts_css_js = """
<style>
/* ตั้งค่าให้พื้นหลังหลักรองรับเอฟเฟกต์ */
.stApp {
    background: linear-gradient(135deg, #fdfbf7 0%, #f4eae1 100%);
    overflow: hidden;
}

/* คอนเทนเนอร์สำหรับหัวใจลอย */
.heart-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

/* สไตล์ของหัวใจแต่ละดวง */
.floating-heart {
    position: absolute;
    bottom: -100px;
    color: rgba(216, 131, 131, 0.35);
    animation: floatUp 8s linear infinite;
    user-select: none;
}

@keyframes floatUp {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 0.8;
    }
    100% {
        transform: translateY(-110vh) rotate(360deg);
        opacity: 0;
    }
}
</style>

<div class="heart-bg" id="heartContainer"></div>

<script>
// ฟังก์ชันสุ่มสร้างหัวใจลอยขึ้นมาเรื่อยๆ
function createHeart() {
    const heartContainer = document.getElementById('heartContainer');
    if (!heartContainer) return;
    
    const heart = document.createElement('div');
    heart.classList.add('floating-heart');
    heart.innerHTML = '♥';
    
    // สุ่มตำแหน่ง ขนาด และความเร็ว
    heart.style.left = Math.random() * 100 + 'vw';
    heart.style.animationDuration = (Math.random() * 4 + 6) + 's';
    heart.style.fontSize = (Math.random() * 18 + 12) + 'px';
    
    heartContainer.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 10000);
}

// สร้างหัวใจทุกๆ 500 มิลลิวินาที
setInterval(createHeart, 500);
</script>
"""

# แสดงผลเอฟเฟกต์หัวใจ
st.markdown(hearts_css_js, unsafe_allow_html=True)


# --- 1. ตั้งค่าข้อมูลส่วนตัว ---
CORRECT_PIN = "1205"  # รหัสผ่าน 4 หลัก
START_DATE = datetime.datetime(2024, 5, 12, 0, 0, 0)

# 🎵 ใส่ ID วิดีโอ YouTube ที่ต้องการ (เอาเฉพาะรหัสหลัง v= หรือหลัง youtu.be/)
# ตัวอย่าง: ลิ้งก์ https://www.youtube.com/watch?v=dQw4w9WgXcQ  -> ID คือ dQw4w9WgXcQ
YOUTUBE_ID = "dQw4w9WgXcQ" 


# --- ตรวจสอบสถานะการปลดล็อก ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- 2. หน้ากรอกรหัสผ่าน ---
if not st.session_state.authenticated:
    st.title("Our Secret Code 🔒")
    st.caption("กรอกวันครบรอบของเราเพื่อเข้าสู่ความทรงจำ (4 หลัก)")
    
    pin_input = st.text_input("Passcode", type="password", max_chars=4, placeholder="••••")
    
    if st.button("ตกลง", use_container_width=True):
        if pin_input == CORRECT_PIN:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("รหัสผ่านไม่ถูกต้อง ลองใหม่อีกครั้งนะ!")

# --- 3. หน้าเนื้อหาหลัก (เมื่อปลดล็อกแล้ว) ---
else:
    # 🎵 เล่นเพลงจาก YouTube อัตโนมัติทันทีที่ผ่านหน้ารหัสผ่านเข้ามา
    autoplay_embed = f"""
        <iframe 
            width="100%" 
            height="200" 
            src="https://www.youtube.com/embed/{YOUTUBE_ID}?autoplay=1&mute=0" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
    """
    st.components.v1.html(autoplay_embed, height=210)

    st.title("ถึงคนพิเศษของฉัน ❤️")
    st.subheader("Digital Love Letter 💌")
    st.write("---")

    # --- ฟีเจอร์ Days Together ---
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

    # --- ฟีเจอร์ข้อความลับ ---
    with st.expander("คลิกเพื่ออ่านข้อความลับเพิ่มเติม 💌"):
        st.write("PS. สัญญาว่าจะพาไปกินของอร่อยๆ และอยู่ซัพพอร์ตกันแบบนี้ตลอดไปเลย รักคุณนะ! 🥰")
