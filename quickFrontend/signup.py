import streamlit as st
import login as login

def signup():
    st.title("Sign Up")
    firstName = st.text_input("First Name")
    lastName = st.text_input("Last Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    repassword = st.text_input("Re-enter Password", type="password")
    
    if st.button("Sign Up"):
        if password != repassword:
            st.error("Passwords do not match")
        if email == "e" and password == "p":
            st.success("Sign Up Successful")
            login.login()
        else:
           # try:
                #insert logic to save user data in database
                st.error("Email already used")

    st.write("Already have an account?")
    if st.button("Login"):
        login.login()  # This will refresh the page, you can replace it with actual login page redirection

signup()