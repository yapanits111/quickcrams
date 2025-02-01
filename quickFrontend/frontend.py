import streamlit as st
import requests
from login import login
# Backend API Base URL
BASE_URL = "http://localhost:8080/api"  # Update this if your backend is hosted elsewhere

# Page Configuration
st.set_page_config(page_title="QuickCram+", page_icon="📚", layout="wide")

st.title("QuickCram+ 📚")

# Sidebar for Navigation
st.sidebar.title("QuickCram+")
page = st.sidebar.radio(
    "Navigate",
    ["Login", "Sign Up"]
)

# Login Page
if page == "Login":
    login()
        

# Helper Function to Fetch Data from Backend
def fetch_data(endpoint):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch data: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return []

# Helper Function to Post Data to Backend
def post_data(endpoint, data):
    try:
        response = requests.post(f"{BASE_URL}/{endpoint}", json=data)
        if response.status_code == 200 or response.status_code == 201:
            st.success("Data saved successfully!")
        else:
            st.error(f"Failed to save data: {response.status_code}")
    except Exception as e:
        st.error(f"Error saving data: {e}")
