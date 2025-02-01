import streamlit as st
from frontend import post_data, fetch_data

# Notes Page
def notes():
    st.title("📝 Notes")
    st.write("Create and manage your study notes here.")

    # Input for New Note
    new_note = st.text_area("Add a new note:")
    if st.button("Save Note"):
        if new_note:
            post_data("notes", {"content": new_note})
        else:
            st.warning("Please enter a note before saving.")

    # Display Saved Notes
    st.subheader("Your Notes")
    notes = fetch_data("notes")
    if notes:
        for i, note in enumerate(notes, 1):
            st.write(f"{i}. {note['content']}")
    else:
        st.info("No notes saved yet.")