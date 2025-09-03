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
    /* Center main content */
    .main-container {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .block-container {{
        max-width: 650px;
        margin: auto;
        padding: 2rem;
        background: rgba(0,0,0,0.6);
        border-radius: 15px;
        color: white;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set background
add_bg_from_local("9019808.jpg")

# Wrap content in a centered container
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="block-container">', unsafe_allow_html=True)

    # Title
    st.title("Sample Grading System")

    # Prelim
    st.subheader("Prelim Grades")
    prelim = st.number_input("Prelim Exam", min_value=0.0, max_value=100.0, step=1.0)
    quiz = st.number_input("Prelim Quiz", min_value=0.0, max_value=100.0, step=1.0)
    recitation = st.number_input("Prelim Recitation", min_value=0.0, max_value=100.0, step=1.0)
    requirement = st.number_input("Prelim Requirement", min_value=0.0, max_value=100.0, step=1.0)
    prelim_absences = st.number_input("Prelim Absences", min_value=0, max_value=5, step=1)

    # Midterm
    st.subheader("Midterm Grades")
    midterm = st.number_input("Midterm Exam", min_value=0.0, max_value=100.0, step=1.0)
    mid_quiz = st.number_input("Midterm Quiz", min_value=0.0, max_value=100.0, step=1.0)
    mid_recitation = st.number_input("Midterm Recitation", min_value=0.0, max_value=100.0, step=1.0)
    mid_requirement = st.number_input("Midterm Requirement", min_value=0.0, max_value=100.0, step=1.0)
    midterm_absences = st.number_input("Midterm Absences", min_value=0, max_value=5, step=1)

    # Finals
    st.subheader("Final Grades")
    final_exam = st.number_input("Final Exam", min_value=0.0, max_value=100.0, step=1.0)
    final_quiz = st.number_input("Final Quiz", min_value=0.0, max_value=100.0, step=1.0)
    final_recitation = st.number_input("Final Recitation", min_value=0.0, max_value=100.0, step=1.0)
    final_requirement = st.number_input("Final Requirement", min_value=0.0, max_value=100.0, step=1.0)
    final_absences = st.number_input("Final Absences", min_value=0, max_value=5, step=1)

    # Compute button
    if st.button("Compute"):
        # Total absences check (auto fail if 5+)
        total_absences = prelim_absences + midterm_absences + final_absences

        if total_absences >= 5:
            st.markdown("---")
            st.subheader("Results")
            st.write(f"**Total Absences:** {total_absences}")
            st.write("**Status:** Failed due to excessive total absences.")
        else:
            # Prelim calculation
            prelim_grade = (prelim * 0.4) + (quiz * 0.25) + (recitation * 0.20) + (requirement * 0.15)

            # Midterm calculation
            midterm_grade = (midterm * 0.4) + (mid_quiz * 0.25) + (mid_recitation * 0.20) + (mid_requirement * 0.15)

            # Final calculation
            finals_grade = (final_exam * 0.4) + (final_quiz * 0.25) + (final_recitation * 0.20) + (final_requirement * 0.15)

            # Final grade = average of prelim + midterm + finals
            final_grade = (prelim_grade + midterm_grade + finals_grade) / 3

            # Pass/Fail
            status = "Passed: Move up" if final_grade >= 60 else "Failed"

            # Show result
            st.markdown("---")
            st.subheader("Results")
            st.write(f"**Prelim Grade:** {prelim_grade:.2f}")
            st.write(f"**Midterm Grade:** {midterm_grade:.2f}")
            st.write(f"**Finals Grade:** {finals_grade:.2f}")
            st.write(f"**Overall Grade:** {final_grade:.2f}")
            st.write(f"**Total Absences:** {total_absences}")
            st.write(f"**Status:** {status}")

            # Dean's Lister Reminder
            if final_grade >= 90:
                st.markdown("<h3 style='color:whitesmoke;'>You qualify for the Dean's List!</h3>", unsafe_allow_html=True)
            elif final_grade >= 60:
                st.markdown("<h4 style='color:whitesmoke;'>Need 90% for Dean's List.</h4>", unsafe_allow_html=True)

        # Return button
        if st.button("Return"):
            st.experimental_rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)




























