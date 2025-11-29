import streamlit as st
import os
import google.generativeai as genai
import datetime

st.set_page_config(page_title="Daily Planner", layout="wide")

api_key = os.getenv("GOOGLE_API_KEY") 
if not api_key:
    api_key = 'ENTER_API_KEY'

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    st.error(f"API Error: {e}")
    st.stop()

if "generated_plan" not in st.session_state:
    st.session_state.generated_plan = ""
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.header("Settings")
    name = st.text_input("Your Name", "Pratyush")
    start_time = st.time_input("Start Day At", datetime.time(6, 0))
    end_time = st.time_input("End Day At", datetime.time(17, 0))
    
    st.markdown("---")
    st.write(f"Welcome, {name}.")
    
    if st.button("Clear Planner"):
        st.session_state.generated_plan = ""
        st.session_state.chat_history = []
        st.rerun()

st.title("Daily Planner and Coach")
st.write("Turn your task list into a structured timeline.")

tab1, tab2 = st.tabs(["Plan My Day", "Productivity Coach"])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("1. Task Input")
        user_tasks = st.text_area(
            "List your tasks for today:",
            placeholder="Example: Reply to emails, study python, gym, meeting at 2pm",
            height=200
        )
        
        priority = st.selectbox("Focus Mode", ["Balanced", "Deep Work", "Easy Wins"])

        if st.button("Generate Schedule"):
            if user_tasks.strip():
                with st.spinner("Processing..."):
                    prompt = (
                        f"Act as a professional productivity planner. "
                        f"The user {name} wants to work from {start_time} to {end_time}. "
                        f"Tasks: {user_tasks}. "
                        f"Focus Strategy: {priority}. "
                        f"Create a strict Markdown Table with columns: Time, Task, Duration, and Energy Level. "
                        f"Be realistic."
                    )
                    
                    response = model.generate_content(prompt)
                    st.session_state.generated_plan = response.text
            else:
                st.warning("Please enter tasks.")

    with col2:
        st.subheader("2. Your Schedule")
        if st.session_state.generated_plan:
            st.markdown(st.session_state.generated_plan)
        else:
            st.info("Schedule will appear here.")

with tab2:
    st.subheader("Productivity Advice")
    
    for role, text in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(text)

    user_query = st.chat_input("Ask for advice...")
    
    if user_query:
        st.session_state.chat_history.append(("user", user_query))
        with st.chat_message("user"):
            st.write(user_query)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                coach_prompt = f"You are a strict productivity coach. Give short advice for: {user_query}"
                response = model.generate_content(coach_prompt)
                st.write(response.text)
                st.session_state.chat_history.append(("assistant", response.text))