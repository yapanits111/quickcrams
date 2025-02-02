import streamlit as st
from frontend import post_data, fetch_data

def quiz():
    st.title("📝 Quiz Application")
    
    tab1, tab2 = st.tabs(["Take Quiz", "Create Quiz"])
    
    with tab1:
        st.header("Take Quiz")
        quizzes = fetch_data("quiz")
        
        if quizzes:
            for quiz in quizzes:
                st.subheader(quiz['question'])
                answer = st.radio("Select your answer:", quiz['choices'], key=f"quiz_{quiz['quizId']}")
                
                if st.button("Submit Answer", key=f"submit_{quiz['quizId']}"):
                    if answer == quiz['correctOption']:
                        st.success("Correct! 🎉")
                        # Save quiz result
                        result = {
                            "quizId": quiz['quizId'],
                            "userId": 1,  # Replace with actual user ID after authentication
                            "score": 1
                        }
                        post_data("quiz/results", result)
                    else:
                        st.error("Incorrect! Try again.")
                st.divider()
        else:
            st.info("No quizzes available.")

    with tab2:
        st.header("Create New Quiz")
        with st.form("quiz_form"):
            question = st.text_input("Question")
            choice1 = st.text_input("Choice 1")
            choice2 = st.text_input("Choice 2")
            choice3 = st.text_input("Choice 3")
            choice4 = st.text_input("Choice 4")
            
            choices = [choice1, choice2, choice3, choice4]
            correct_option = st.selectbox("Correct Answer", choices)
            
            submitted = st.form_submit_button("Create Quiz")
            if submitted:
                if question and all(choices) and correct_option:
                    quiz_data = {
                        "question": question,
                        "choices": choices,
                        "correctOption": correct_option
                    }
                    if post_data("quiz", quiz_data):
                        st.success("Quiz created successfully!")
                else:
                    st.error("Please fill in all fields.")

        # Show created quizzes with delete option
        st.header("Manage Quizzes")
        quizzes = fetch_data("quiz")
        if quizzes:
            for quiz in quizzes:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**Q:** {quiz['question']}")
                with col2:
                    if st.button("Delete", key=f"delete_{quiz['quizId']}"):
                        response = requests.delete(f"{BASE_URL}/quiz/{quiz['quizId']}")
                        if response.status_code == 200:
                            st.success("Quiz deleted successfully!")
                            st.rerun()
                st.divider()

if __name__ == "__main__":
    quiz()