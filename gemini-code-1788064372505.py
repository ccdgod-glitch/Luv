import streamlit as st
import datetime

# --- การตั้งค่าหน้าเว็บ ---
st.set_page_config(
    page_title=" สุขสันต์วันครบรอบนะ ❤️",
    page_icon="💌",
    layout="centered"
)

# --- ใส่ Pure CSS สำหรับเอฟเฟกต์พื้นหลัง หัวใจลอย และกำหนดสีตัวหนังสือ ---
hearts_css = """
<style>
/* 1. ตั้งค่าสีพื้นหลังโทนพาสเทลโรแมนติก */
.stApp {
    background: linear-gradient(135deg, #fdfbf7 0%, #f4eae1 100%);
}

/* 2. เปลี่ยนสีข้อความทั้งหมดบนหน้าเว็บเป็นสีชมพู */
.stApp, .stApp p, .stApp div, .stApp span, .stApp label {
    color: #d86b88 !important; /* สีชมพูเข้มอ่านง่าย */
}

/* 3. เปลี่ยนสีหัวข้อ (Header) ให้เป็นสีชมพูเข้มโดดเด่น */
h1, h2, h3, h4, h5, h6, .stTitle, .stSubheader {
    color: #c0486b !important; /* สีชมพูอมแดงกุหลาบ */
}

/* 4. เปลี่ยนสีตัวเลขในกล่อง Metric (นับวัน) ให้เป็นสีชมพู */
[data-testid="stMetricValue"] {
    color: #d86b88 !important;
}

[data-testid="stMetricLabel"] {
    color: #e0829d !important;
}

/* 5. เปลี่ยนสีปุ่มและเส้นขอบให้อยู่ในโทนชมพู */
.stButton > button {
    border-color: #e0829d !important;
    color: #c0486b !important;
}

/* คอนเทนเนอร์หัวใจ */
.bg-hearts {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

/* หัวใจดวงต่างๆ สุ่มตำแหน่งและเวลาด้วย CSS */
.heart {
    position: absolute;
    bottom: -100px;
    color: rgba(216, 131, 131, 0.35);
    font-size: 20px;
    animation: floatUp 8s linear infinite;
}

.heart:nth-child(1) { left: 10%; animation-duration: 7s; animation-delay: 0s; font-size: 16px; }
.heart:nth-child(2) { left: 25%; animation-duration: 9s; animation-delay: 2s; font-size: 24px; }
.heart:nth-child(3) { left: 40%; animation-duration: 6s; animation-delay: 4s; font-size: 18px; }
.heart:nth-child(4) { left: 55%; animation-duration: 10s; animation-delay: 1s; font-size: 22px; }
.heart:nth-child(5) { left: 70%; animation-duration: 8s; animation-delay: 3s; font-size: 15px; }
.heart:nth-child(6) { left: 85%; animation-duration: 11s; animation-delay: 5s; font-size: 26px; }
.heart:nth-child(7) { left: 95%; animation-duration: 7s; animation-delay: 2s; font-size: 20px; }

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

<div class="bg-hearts">
    <div class="heart">♥</div>
    <div class="heart">♥</div>
    <div class="heart">♥</div>
    <div class="heart">♥</div>
    <div class="heart">♥</div>
    <div class="heart">♥</div>
    <div class="heart">♥</div>
</div>
"""

# แสดงผลพื้นหลังและเอฟเฟกต์หัวใจ
st.markdown(hearts_css, unsafe_allow_html=True)


# --- 1. ตั้งค่าข้อมูลส่วนตัว ---
CORRECT_PIN = "3008"  # รหัสผ่าน 4 หลัก
START_DATE = datetime.datetime(2023, 4, 30, 0, 0, 0)

# 🎵 เปลี่ยนเป็น YouTube ID ของคุณ
YOUTUBE_ID = "dQw4w9WgXcQ" 

# --- 3. หน้าเนื้อหาหลัก (เมื่อปลดล็อกแล้ว) ---
else:
    # 🎵 เล่นเพลงจาก YouTube อัตโนมัติ (ใส่ mute=1 เพื่อเปิดทางให้นโยบาย Autoplay ของเบราว์เซอร์ผ่านได้)
    autoplay_embed = f"""
        <iframe 
            width="100%" 
            height="200" 
            src="https://www.youtube.com/embed/{YOUTUBE_ID}?autoplay=1&mute=1&enablejsapi=1" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
    """
    st.components.v1.html(autoplay_embed, height=210)


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

    # --- ฟีเจอร์ Days Together (Real-time Counter) ---
    st.markdown("### ⏳ เรารักกันมานานแล้ว...")
    
    # แปลงวันที่เริ่มคบให้อยู่ในรูปแบบ ISO เพื่อส่งเข้า JavaScript
    start_iso = START_DATE.strftime("%Y-%m-%dT%H:%M:%S")

    # กล่องแสดงผลแบบ Real-time ขับเคลื่อนด้วย JavaScript
    realtime_counter_html = f"""
    <div style="
        display: flex; 
        justify-content: space-around; 
        align-items: center; 
        background-color: rgba(255, 255, 255, 0.6); 
        padding: 15px; 
        border-radius: 12px; 
        border: 1px solid #e0829d;
        margin-bottom: 20px;
        font-family: 'Prompt', sans-serif;">
        
        <div style="text-align: center;">
            <div id="rt-days" style="font-size: 26px; font-weight: bold; color: #c0486b;">0</div>
            <div style="font-size: 13px; color: #d86b88;">จำนวนวัน</div>
        </div>
        <div style="text-align: center;">
            <div id="rt-hours" style="font-size: 26px; font-weight: bold; color: #c0486b;">00</div>
            <div style="font-size: 13px; color: #d86b88;">ชั่วโมง</div>
        </div>
        <div style="text-align: center;">
            <div id="rt-mins" style="font-size: 26px; font-weight: bold; color: #c0486b;">00</div>
            <div style="font-size: 13px; color: #d86b88;">นาที</div>
        </div>
        <div style="text-align: center;">
            <div id="rt-secs" style="font-size: 26px; font-weight: bold; color: #c0486b;">00</div>
            <div style="font-size: 13px; color: #d86b88;">วินาที</div>
        </div>
    </div>

    <script>
    const startDate = new Date("{start_iso}").getTime();

    function updateCounter() {{
        const now = new Date().getTime();
        const diff = now - startDate;

        if (diff > 0) {{
            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((diff % (1000 * 60)) / 1000);

            document.getElementById("rt-days").innerText = days;
            document.getElementById("rt-hours").innerText = String(hours).padStart(2, '0');
            document.getElementById("rt-mins").innerText = String(minutes).padStart(2, '0');
            document.getElementById("rt-secs").innerText = String(seconds).padStart(2, '0');
        }}
    }}

    updateCounter();
    setInterval(updateCounter, 1000);
    </script>
    """
    
    # แสดงผลตัวนับเวลา Real-time ผ่าน HTML Component
    st.components.v1.html(realtime_counter_html, height=100)

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
