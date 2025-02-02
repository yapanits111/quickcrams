import streamlit as st
from frontend import post_data, fetch_data, delete_data

def flashcard():
    st.title("📇 Flashcards")
    
    if st.button("Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    
    tab1, tab2 = st.tabs(["My Flashcards", "Create Flashcard"])
    
    with tab1:
        st.header("My Flashcards")
        cards = fetch_data("flashcards")
        
        if cards:
            for card in cards:
                with st.expander(f"Flashcard: {card['front']}"):
                    st.write("**Front:**", card['front'])
                    st.write("**Back:**", card['back'])
                    
                    if card['userId'] == st.session_state.user['id']:
                        if st.button("Delete", key=f"delete_{card['cardId']}"):
                            if st.button("Confirm Delete?", key=f"confirm_{card['cardId']}"):
                                success, message = delete_data(f"flashcards/{card['cardId']}")
                                if success:
                                    st.success("Flashcard deleted!")
                                    st.rerun()
                                else:
                                    st.error(message)
        else:
            st.info("No flashcards yet. Create one in the 'Create Flashcard' tab!")

    with tab2:
        st.header("Create New Flashcard")
        with st.form("card_form"):
            front = st.text_input("Front (Question)")
            back = st.text_input("Back (Answer)")
            
            if st.form_submit_button("Save Flashcard"):
                if front and back:
                    card_data = {
                        "front": front,
                        "back": back,
                        "userId": st.session_state.user['id']
                    }
                    success, message = post_data("flashcards", card_data)
                    if success:
                        st.success("Flashcard saved successfully!")
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.error("Please fill in all fields")

if __name__ == "__main__":
    if 'user' not in st.session_state:
        st.error("Please login first!")
        st.session_state.page = "login"
        st.rerun()
    flashcard()