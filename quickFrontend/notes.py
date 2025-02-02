import streamlit as st
import requests
from frontend import *

# Notes Page
def notes():
    st.title("📝 Notes")
    st.write("Create and manage your study notes here.")
    # Add a text area to see created notes
    viewNotes = st.text_area(notes)


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
            if st.button(f"Delete Note {i}", key=f"delete_{i}"):
                requests.delete(f"{BASE_URL}/notes/{note['id']}")
    else:
        st.info("No notes saved yet.")