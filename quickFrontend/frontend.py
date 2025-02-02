import streamlit as st
import requests

import streamlit as st
import requests

BASE_URL = "http://localhost:8080/api"

def post_data(endpoint, data):
    try:
        response = requests.post(f"{BASE_URL}/{endpoint}", json=data)
        if response.status_code == 200:
            st.success("Data saved successfully!")
            return response.json()
        else:
            st.error(f"Failed to save data: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error saving data: {e}")
        return None

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