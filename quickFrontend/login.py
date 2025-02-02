import streamlit as st
from dashboard import dashboard
from signup import signup
from frontend import login_user

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.set_page_config(page_title="QuickCram+", page_icon="📚", layout="wide")
    
    if st.session_state.logged_in:
        dashboard()
        return

    st.title("QuickCram+ 📚")
    st.title("Login")
    
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            success, response = login_user({"email": email, "password": password})
            if success:
                st.session_state.logged_in = True
                st.session_state.user = response["user"]
                st.session_state.token = response["token"]
                st.success("Login successful!")
                st.rerun()
            else:
                st.error(response)
    
    st.write("Don't have an account?")
    if st.button("Sign Up"):
        st.session_state.page = "signup"
        st.rerun()

if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = "login"
    login()