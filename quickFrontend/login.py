import streamlit as st
from dashboard import dashboard
from signup import signup



# Function to verify login credentials
def verify_login(email, password):
    #replace with actual logic to verify login credentials
    return email == "user@example.com" and password == "password123"

# Login Form
def login():
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