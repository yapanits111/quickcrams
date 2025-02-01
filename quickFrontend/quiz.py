import streamlit as st
from frontend import post_data, fetch_data

# Quizzes Page
def quiz():
    st.title("📝 Quizzes")
    st.write("Create and take quizzes to test your knowledge.")

    # Input for New Quiz Question
    st.subheader("Add a Quiz Question")
    question = st.text_input("Question:")
    answer = st.text_input("Answer:")

    #Create quiz
    if st.button("Add Quiz Question"):
        if question and answer:
            post_data("quizzes", {"question": question, "answer": answer})
        else:
            st.warning("Please fill in both the question and answer.")

    # Take Quiz
    st.subheader("Your Quiz Questions")
    quizzes = fetch_data("quizzes")
    # if quizzes:
    #     # for i, quiz in enumerate(quizzes, i):
    #     #     st.write(f"**Q{i}:** {quiz['question']}")
    #     #     st.write(f"**A:** {quiz['answer']}")
    #     #     st.write(f"**B:**"{quiz['answer']})
    #     #     st.write(f"**C:**"{quiz['answer']})
    #     #     st.write(f"**D:**"{quiz['answer']})
    # else:
    #   st.info("No quiz questions added yet.")