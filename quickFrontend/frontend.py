import streamlit as st
import requests

BASE_URL = "http://localhost:8080"  # Use the backend port


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