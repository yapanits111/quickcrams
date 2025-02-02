import streamlit as st
from frontend import register_user
from login import login
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def signup():
    st.title("Sign Up")
    
    with st.form("signup_form"):
        firstName = st.text_input("First Name")
        lastName = st.text_input("Last Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        repassword = st.text_input("Re-enter Password", type="password")
        
        submitted = st.form_submit_button("Sign Up")
        if submitted:
            if not all([firstName, lastName, email, password, repassword]):
                st.error("Please fill in all fields")
            elif not is_valid_email(email):
                st.error("Please enter a valid email address")
            elif password != repassword:
                st.error("Passwords do not match")
            else:
                success, message = register_user({
                    "firstName": firstName,
                    "lastName": lastName,
                    "email": email,
                    "password": password
                })
                
                if success:
                    st.success("Registration successful! Please login.")
                    st.session_state.page = "login"
                    st.rerun()
                else:
                    st.error(message or "Email already exists")

    st.write("Already have an account?")
    if st.button("Login"):
        st.session_state.page = "login"
        st.rerun()

if __name__ == "__main__":
    signup()