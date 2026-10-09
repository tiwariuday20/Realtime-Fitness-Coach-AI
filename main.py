import streamlit as st 
from services.auth.login_wall import render_login_form


def main():
  st.set_page_config(
    page_icon="🏋️",
    page_title="AI Real-time Fitness Coach",
    initial_sidebar_state="expanded",
    layout="centered"
  )

  if not render_login_form():
    return 

  st.write("Hello")

if __name__ == "__main__":
  main()


st.set_page_config(page_title="Realtime-Fitness-Coach-AI")

