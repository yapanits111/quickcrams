import streamlit as st
from notes import notes
from flashcard import flashcard
from quiz import quiz
from login import login

# Home Page
def dashboard():

    # Page Configuration
    st.set_page_config(page_title="QuickCram+", page_icon="📚", layout="wide")

    st.title("QuickCram+ 📚")

    if st.session_state.logged_in:
    # Sidebar for Navigation
        st.sidebar.title("QuickCram+")
        page = st.sidebar.radio(
            "Navigate",
            ["Dashboard", "Notes", "Flashcards", "Quizzes"]
        )

    # Main content based on the selected page
        if page == "Dashboard":
            st.title("Welcome to QuickCram+ 📚")

            st.write("""
            **QuickCram+** is your ultimate study companion, designed to help you manage your study materials effectively.
            - **Notes**: Create and organize your study notes.
            - **Flashcards**: Build and review flashcards for quick revision.
            - **Quizzes**: Test your knowledge with custom quizzes.
            """)

            logout = st.button("Logout")
            if logout:
                st.session_state.logged_in = False
                st.success("Logout successful")
                login() 

        if page == "Notes":
            st.title("Notes")
            notes()
        elif page == "Flashcards":
            st.title("Flashcards")
            flashcard()
        elif page == "Quizzes":
            st.title("Quizzes")
            quiz()

if __name__ == "__main__":
    dashboard()
