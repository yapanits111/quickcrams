import streamlit as st
import requests

BASE_URL = "http://localhost:8080/api"

def register_user(user_data):
    try:
        response = requests.post(f"{BASE_URL}/users/register", json=user_data)
        return response.status_code == 201, response.json().get('message', 'Error occurred')
    except Exception as e:
        return False, str(e)

def login_user(credentials):
    try:
        response = requests.post(f"{BASE_URL}/users/login", json=credentials)
        if response.status_code == 200:
            return True, response.json()
        return False, "Invalid credentials"
    except Exception as e:
        return False, str(e)

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
    
def post_quiz(endpoint, data):
    try:
        headers = {"Authorization": f"Bearer {st.session_state.get('token', '')}"}
        response = requests.post(f"{BASE_URL}/{endpoint}", json=data, headers=headers)
        return response.status_code == 200, response.json()
    except Exception as e:
        return False, str(e)

def fetch_quiz(endpoint):
    try:
        headers = {"Authorization": f"Bearer {st.session_state.get('token', '')}"}
        response = requests.get(f"{BASE_URL}/{endpoint}", headers=headers)
        return response.json() if response.status_code == 200 else []
    except Exception as e:
        return []

def delete_quiz(endpoint):
    try:
        headers = {"Authorization": f"Bearer {st.session_state.get('token', '')}"}
        response = requests.delete(f"{BASE_URL}/{endpoint}", headers=headers)
        return response.status_code == 200, response.json().get('message', '')
    except Exception as e:
        return False, str(e)