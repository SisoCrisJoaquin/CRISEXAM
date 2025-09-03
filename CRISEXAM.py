import streamlit as st, base64

# Background setup
def add_bg(image):
    with open(image, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{b64}") no-repeat center/cover fixed;
    }}
    .block {{
        max-width: 600px; margin:auto; padding:2rem;
        background:rgba(0,0,0,0.6); border-radius:15px; color:white;
    }}
    </style>
    """, unsafe_allow_html=True)

add_bg("9019808.jpg")

# Content
st.markdown('<div class="block">', unsafe_allow_html=True)
st.title("📘 Grading System")

name = st.text_input("Student Name")

# Inputs
prelim = st.number_input("Prelim Exam", 0.0, 100.0, 0.0)
quiz = st.number_input("Prelim Quiz", 0.0, 100.0, 0.0)
recit = st.number_input("Prelim Recitation", 0.0, 100.0, 0.0)
req = st.number_input("Prelim Requirement", 0.0, 100.0, 0.0)

mid = st.number_input("Midterm Exam", 0.0, 100.0, 0.0)
mquiz = st.number_input("Midterm Quiz", 0.0, 100.0, 0.0)
mrecit = st.number_input("Midterm Recitation", 0.0, 100.0, 0.0)
mreq = st.number_input("Midterm Requirement", 0.0, 100.0, 0.0)

absences = st.number_input("Absences", 0)

# Compute
if st.button("Compute"):
    prelim_g = prelim*0.4 + quiz*0.25 + recit*0.2 + req*0.15
    mid_g = mid*0.4 + mquiz*0.25 + mrecit*0.2 + mreq*0.15
    final = (prelim_g + mid_g)/2 - max(0, absences-3)
    status = "Passed 🎉" if final >= 60 else "Failed ❌"

    st.subheader(f"Results for {name}")
    st.write(f"Prelim: {prelim_g:.2f} | Midterm: {mid_g:.2f}")
    st.write(f"Final Grade: {final:.2f}")
    st.write(f"Status: {status}")
    if final >= 90: st.success("🎓 Dean's Lister!")
    elif final >= 60: st.info("Need 90% for Dean's List")

st.markdown('</div>', unsafe_allow_html=True)













