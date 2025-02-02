import streamlit as st
from frontend import post_data, fetch_data

# Flashcards Page
def flashcard():
    st.title("📇 Flashcards")
    st.write("Create and review flashcards for quick revision.")

    # Input for New Flashcard
    col1, col2 = st.columns(2)
    with col1:
        front = st.text_input("Front (Question):")
    with col2:
        back = st.text_input("Back (Answer):")

    if st.button("Add Flashcard"):
        if front and back:
            post_data("flashcards", {"front": front, "back": back})
        else:
            st.warning("Please fill in both the front and back of the flashcard.")

    # Display Flashcards
    st.subheader("Your Flashcards")
    flashcards = fetch_data("flashcards")
    if flashcards:
        for i, card in enumerate(flashcards, 1):
            st.write(f"**Card {i}**")
            st.write(f"**Q:** {card['front']}")
            st.write(f"**A:** {card['back']}")

    else:
        st.info("No flashcards created yet.")
