import streamlit as st
import requests

BASE_URL = "http://localhost:8080/api"

def register_user(user_data):
    try:
        response = requests.post(f"{BASE_URL}/users/register", json=user_data)
        return response.status_code == 201, response.json().get('message') # 201 indicates successful resource creation
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
        headers = {"Authorization": f"Bearer {st.session_state.get('token', '')}"}
        response = requests.post(f"{BASE_URL}/{endpoint}", json=data, headers=headers)
        if response.status_code == 200:
            return True, response.json()
        return False, f"Failed to save data: {response.status_code}"
    except Exception as e:
        return False, str(e)

def fetch_data(endpoint):
    try:
        headers = {"Authorization": f"Bearer {st.session_state.get('token', '')}"}
        response = requests.get(f"{BASE_URL}/{endpoint}", headers=headers)
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        return []

def delete_data(endpoint):
    try:
        headers = {"Authorization": f"Bearer {st.session_state.get('token', '')}"}
        response = requests.delete(f"{BASE_URL}/{endpoint}", headers=headers)
        return response.status_code == 200, response.json().get('message', '')
    except Exception as e:
        return False, str(e)

def update_data(endpoint, data):
    try:
        headers = {"Authorization": f"Bearer {st.session_state.get('token', '')}"}
        response = requests.put(f"{BASE_URL}/{endpoint}", json=data, headers=headers)
        return response.status_code == 200, response.json()
    except Exception as e:
        return False, str(e)