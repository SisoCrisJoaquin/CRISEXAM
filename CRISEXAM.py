import streamlit as st
import base64

# Function to set background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set background
add_bg_from_local("9019808.jpg")

# Title
st.title("📘 Sample Grading System")

# Input fields
name = st.text_input("Student Name")
prelim = st.number_input("Prelim Grade", min_value=0.0, max_value=100.0, step=1.0)
quiz = st.number_input("Quiz Grade", min_value=0.0, max_value=100.0, step=1.0)
recitation = st.number_input("Recitation Grade", min_value=0.0, max_value=100.0, step=1.0)
absences = st.number_input("Number of Absences", min_value=0, step=1)

# Compute button
if st.button("Compute"):
    final_grade = (prelim * 0.4) + (quiz * 0.3) + (recitation * 0.3)

    # Deduct points for absences
    if absences > 3:
        final_grade -= (absences - 3)

    # Pass/Fail
    status = "✅ Passed: Move up" if final_grade >= 60 else "❌ Failed"

    # Show result
    st.subheader(f"🎓 {name}")
    st.write(f"**Final Grade:** {final_grade:.2f}")
    st.write(f"**Status:** {status}")

    # Dean's Lister Reminder
    if final_grade >= 90:
        st.markdown("<h3 style='color:gold;'>⭐ Must be 90% to be a Dean's Lister ⭐</h3>", unsafe_allow_html=True)

    # Return button
    if st.button("🔄 Return"):
        st.experimental_rerun()


