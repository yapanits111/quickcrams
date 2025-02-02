import streamlit as st
from frontend import *

def quiz():
    st.title("📝 Quiz Application")
    
    if st.button("Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    
    tab1, tab2 = st.tabs(["Available Quizzes", "Create Quiz"])
    
    with tab1:
        st.header("Available Quizzes")
        quizzes = fetch_data("quiz")
        
        if quizzes:
            for quiz in quizzes:
                with st.expander(f"Quiz: {quiz['title']}"):
                    total_score = 0
                    user_answers = {}
                    
                    # Display all questions
                    for idx, question in enumerate(quiz['questions']):
                        st.subheader(f"Question {idx + 1}")
                        st.write(question['question'])
                        answer = st.radio(
                            "Select your answer:", 
                            question['choices'],
                            key=f"quiz_{quiz['quizId']}_q{idx}"
                        )
                        user_answers[idx] = answer
                    
                    # Submit button for all answers
                    if st.button("Submit Quiz", key=f"submit_{quiz['quizId']}"):
                        for idx, question in enumerate(quiz['questions']):
                            if user_answers[idx] == question['correctOption']:
                                total_score += 1
                                
                        score_percentage = (total_score / len(quiz['questions'])) * 100
                        st.success(f"Your score: {total_score}/{len(quiz['questions'])} ({score_percentage:.1f}%)")
                        
                        # Save quiz result
                        result = post_data("quiz/results", {
                            "quizId": quiz['quizId'],
                            "userId": st.session_state.user['id'],
                            "score": total_score
                        })
                    
                    # Delete option for quiz owner
                    if 'user' in st.session_state and quiz['userId'] == st.session_state.user['id']:
                        if st.button("Delete Quiz", key=f"delete_{quiz['quizId']}"):
                            if st.button("Confirm Delete?", key=f"confirm_{quiz['quizId']}"):
                                success, message = delete_data(f"quiz/{quiz['quizId']}")
                                if success:
                                    st.success("Quiz deleted successfully!")
                                    st.rerun()
                                else:
                                    st.error(f"Failed to delete quiz: {message}")
        else:
            st.info("No quizzes available. Create one in the 'Create Quiz' tab!")

    with tab2:
        st.header("Create New Quiz")
        
        # Initialize session state for questions
        if 'num_questions' not in st.session_state:
            st.session_state.num_questions = 1

        # Quiz title
        title = st.text_input("Quiz Title")
        
        # Add/remove question buttons
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("Add Question"):
                st.session_state.num_questions += 1
        with col2:
            if st.button("Remove Question") and st.session_state.num_questions > 1:
                st.session_state.num_questions -= 1

        # Create form for multiple questions
        questions_data = []
        with st.form("quiz_form"):
            for q in range(st.session_state.num_questions):
                st.subheader(f"Question {q + 1}")
                question = st.text_input(f"Question", key=f"q{q}")
                choice1 = st.text_input(f"Choice 1", key=f"q{q}c1")
                choice2 = st.text_input(f"Choice 2", key=f"q{q}c2")
                choice3 = st.text_input(f"Choice 3", key=f"q{q}c3")
                choice4 = st.text_input(f"Choice 4", key=f"q{q}c4")
                
                choices = [choice1, choice2, choice3, choice4]
                correct_option = st.selectbox(
                    "Correct Answer", 
                    choices,
                    key=f"q{q}correct"
                )
                
                questions_data.append({
                    "question": question,
                    "choices": choices,
                    "correctOption": correct_option
                })
            
            submitted = st.form_submit_button("Create Quiz")
            if submitted:
                if title and all(q["question"] and all(q["choices"]) for q in questions_data):
                    quiz_data = {
                        "title": title,
                        "questions": questions_data,
                        "userId": st.session_state.user['id']
                    }
                    success, message = post_data("quiz", quiz_data)
                    if success:
                        st.success("Quiz created successfully!")
                        st.session_state.num_questions = 1  # Reset question count
                        st.rerun()
                    else:
                        st.error(f"Failed to create quiz: {message}")
                else:
                    st.error("Please fill in all fields")

if __name__ == "__main__":
    if 'user' not in st.session_state:
        st.error("Please login first!")
        st.session_state.page = "login"
        st.rerun()
    quiz()