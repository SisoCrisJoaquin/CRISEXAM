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

st.subheader("Prelim Grades")
prelim = st.number_input("Prelim Exam", min_value=0.0, max_value=100.0, step=1.0)
quiz = st.number_input("Prelim Quiz", min_value=0.0, max_value=100.0, step=1.0)
recitation = st.number_input("Prelim Recitation", min_value=0.0, max_value=100.0, step=1.0)

st.subheader("Midterm Grades")
midterm = st.number_input("Midterm Exam", min_value=0.0, max_value=100.0, step=1.0)
mid_quiz = st.number_input("Midterm Quiz", min_value=0.0, max_value=100.0, step=1.0)
mid_recitation = st.number_input("Midterm Recitation", min_value=0.0, max_value=100.0, step=1.0)

absences = st.number_input("Number of Absences", min_value=0, step=1)

# Compute button
if st.button("Compute"):
    # Prelim calculation
    prelim_grade = (prelim * 0.4) + (quiz * 0.3) + (recitation * 0.3)

    # Midterm calculation
    midterm_grade = (midterm * 0.4) + (mid_quiz * 0.3) + (mid_recitation * 0.3)

    # Final grade = average of prelim + midterm
    final_grade = (prelim_grade + midterm_grade) / 2

    # Deduct points for absences
    if absences > 3:
        final_grade -= (absences - 3)

    # Pass/Fail
    status = "✅ Passed: Move up" if final_grade >= 60 else "❌ Failed"

    # Show result
    st.markdown("---")
    st.subheader(f"Results for {name}")
    st.write(f"**Prelim Grade:** {prelim_grade:.2f}")
    st.write(f"**Midterm Grade:** {midterm_grade:.2f}")
    st.write(f"**Final Grade:** {final_grade:.2f}")
    st.write(f"**Status:** {status}")

    # Dean's Lister Reminder
    if final_grade >= 90:
        st.markdown("<h3 style='color:gold;'>🎉 Congratulations! You qualify for the Dean's List!</h3>", unsafe_allow_html=True)
    elif final_grade >= 60:
        st.markdown("<h4 style='color:whitesmoke;'>Keep aiming higher! Need 90% for Dean's List.</h4>", unsafe_allow_html=True)

    # Return button
    if st.button("🔄 Return"):
        st.experimental_rerun()






