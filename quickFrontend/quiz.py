import streamlit as st
import requests


API_URL = "http://localhost:8080/api/quiz"  # Make sure this matches your backend port

# Function to fetch quizzes
def fetch_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching quizzes: {e}")
        return []

# Function to post new quiz
def post_data(question, choices, correct_option):
    payload = {
        "question": question,
        "choices": choices,  # `choices` is already a list
        "correctOption": correct_option
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            st.success("Quiz added successfully!")
        else:
            st.error("Failed to add quiz.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error posting quiz: {e}")

# Streamlit UI
def quiz():
    st.title("📝 Quizzes")
    
    # Input for New Quiz Question
    st.subheader("Add a Quiz Question")
    question = st.text_input("Question:")
    option1 = st.text_input("Option 1:")
    option2 = st.text_input("Option 2:")
    option3 = st.text_input("Option 3:")
    option4 = st.text_input("Option 4:")
    correct_option = st.selectbox("Correct Option", [option1, option2, option3, option4])

    if st.button("Add Quiz Question"):
        if question and option1 and option2 and option3 and option4 and correct_option:
            post_data(question, [option1, option2, option3, option4], correct_option)
        else:
            st.warning("Please fill in all fields.")

    # Display quizzes
    st.subheader("Quiz Questions")
    quizzes = fetch_data()
    if quizzes:
        for i, quiz in enumerate(quizzes, 1):
            st.write(f"**Q{i}:** {quiz['question']}")
            for j, option in enumerate(quiz["choices"], 1):
                st.write(f"Option {j}: {option}")
            selected_option = st.selectbox(f"Select your answer for Q{i}", quiz["choices"], key=f"select_{i}")
            if st.button(f"Submit Answer for Q{i}", key=f"submit_{i}"):
                if selected_option == quiz["correctOption"]:
                    st.success("Correct!")
                else:
                    st.error("Incorrect!")
    else:
        st.info("No quiz questions added yet.")

quiz()
