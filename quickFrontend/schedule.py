import streamlit as st
from frontend import post_data, fetch_data

# Study Schedule Page
def schedule():
    st.title("📅 Study Schedule")
    st.write("Plan your study sessions here.")

    # Input for New Study Task
    task = st.text_input("Add a new study task:")
    date = st.date_input("Select a date:")
    time = st.time_input("Select a time:")

    if st.button("Add Task"):
        if task:
            post_data("study-schedule", {"task": task, "date": str(date), "time": str(time)})
        else:
            st.warning("Please enter a task before saving.")

    # Display Study Schedule
    st.subheader("Your Study Schedule")
    study_schedule = fetch_data("study-schedule")
    if study_schedule:
        for i, task in enumerate(study_schedule, 1):
            st.write(f"**Task {i}:** {task['task']}")
            st.write(f"**Date:** {task['date']} | **Time:** {task['time']}")
            st.write("---")
    else:
        st.info("No tasks added to the study schedule yet.")