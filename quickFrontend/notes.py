import streamlit as st
from frontend import post_data, fetch_data, delete_data

def notes():
    st.title("📝 Notes")
    
    if st.button("Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    
    tab1, tab2 = st.tabs(["My Notes", "Create Note"])
    
    with tab1:
        st.header("My Notes")
        notes = fetch_data("notes")
        
        if notes:
            for note in notes:
                with st.expander(f"Note: {note['title']}"):
                    st.write(note['content'])
                    if note['userId'] == st.session_state.user['id']:
                        if st.button("Delete", key=f"delete_{note['noteId']}"):
                            if st.button("Confirm Delete?", key=f"confirm_{note['noteId']}"):
                                success, message = delete_data(f"notes/{note['noteId']}")
                                if success:
                                    st.success("Note deleted!")
                                    st.rerun()
                                else:
                                    st.error(message)
        else:
            st.info("No notes yet. Create one in the 'Create Note' tab!")

    with tab2:
        st.header("Create New Note")
        with st.form("note_form"):
            title = st.text_input("Title")
            content = st.text_area("Content")
            
            if st.form_submit_button("Save Note"):
                if title and content:
                    note_data = {
                        "title": title,
                        "content": content,
                        "userId": st.session_state.user['id']
                    }
                    success, message = post_data("notes", note_data)
                    if success:
                        st.success("Note saved successfully!")
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
    notes()