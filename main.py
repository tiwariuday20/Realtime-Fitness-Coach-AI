import streamlit as st 
from services.auth.login_wall import render_login_form
from services.state.session_defaults import initial_session_defaults


def main():
  st.set_page_config(
    page_icon="🏋️",
    page_title="AI Real-time Fitness Coach",
    initial_sidebar_state="expanded",
    layout="centered"
  )

  if not render_login_form():
    return 

  initial_session_defaults()

  with st.sidebar:
    st.title("🏋️ AI Fitness Coach")

    if st.session_state.username:
      st.caption(f"👤 Login as {st.session_state.username}")

      st.divider()

if __name__ == "__main__":
  main()


st.set_page_config(page_title="Realtime-Fitness-Coach-AI")

