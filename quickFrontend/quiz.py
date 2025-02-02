import streamlit as st
from frontend import *
import requests

# Quizzes Page
def quiz():
    st.title("📝 Quizzes")
    st.write("Create and take quizzes to test your knowledge.")

    # Input for New Quiz Question
    st.subheader("Add a Quiz Question")
    question = st.text_input("Question:")
    option1 = st.text_input("Option 1:")
    option2 = st.text_input("Option 2:")
    option3 = st.text_input("Option 3:")
    option4 = st.text_input("Option 4:")
    correct_option = st.selectbox("Correct Option", ["Option 1", "Option 2", "Option 3", "Option 4"])

    # Create quiz
    if st.button("Add Quiz Question"):
        if question and option1 and option2 and option3 and option4 and correct_option:
            post_data("quiz", {
                "question": question,
                "option1": option1,
                "option2": option2,
                "option3": option3,
                "option4": option4,
                "correct_option": correct_option
            })
        else:
            st.warning("Please fill in all fields.")

    # Take Quiz
    st.subheader("Your Quiz Questions")
    quizzes = fetch_data("quiz")
    if quizzes:
        for i, quiz in enumerate(quizzes, 1):
            st.write(f"**Q{i}:** {quiz['question']}")
            for j, option in enumerate([quiz['option1'], quiz['option2'], quiz['option3'], quiz['option4']], 1):
                st.write(f"Option {j}: {option}")
            if st.button(f"Submit Answer for Q{i}", key=f"submit_{i}"):
                selected_option = st.selectbox(f"Select your answer for Q{i}", [quiz['option1'], quiz['option2'], quiz['option3'], quiz['option4']], key=f"select_{i}")
                correct_option = quiz['correct_option']
                if selected_option == correct_option:
                    st.success("Correct!")
                else:
                    st.error("Incorrect!")
    else:
        st.info("No quiz questions added yet.")

quiz()