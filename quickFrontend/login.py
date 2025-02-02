import streamlit as st
from dashboard import dashboard
from signup import signup

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if st.session_state.logged_in:
    dashboard()

# Function to verify login credentials
def verify_login(email, password):
    #replace with actual logic to verify login credentials
    return email == "user@example.com" and password == "password123"

# Login Form
def login():
    # Page Configuration
    st.set_page_config(page_title="QuickCram+", page_icon="📚", layout="wide")

    st.title("QuickCram+ 📚")
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if verify_login(email, password):
            st.session_state.logged_in = True
            st.success("Login successful")
            dashboard()
        else:
            st.error("Invalid email or password")
    
    st.write("Don't have an account?")
    if st.button("Sign Up"):
        signup()