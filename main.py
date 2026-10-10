import streamlit as st 
from services.auth.login_wall import render_login_form
from services.state.session_defaults import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS

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

  workout_started = st.session_state.get("workout_started" , False)

  with st.sidebar:
    st.title("🏋️ AI Fitness Coach")

    if st.session_state.username:
      st.caption(f"👤 Login as {st.session_state.username}")

      st.divider()

    if not workout_started:
      st.selectbox("Exercise" , options=EXERCISE_OPTIONS , key= "plan_exercise")

      st.number_input("Sets" , min_value=0 , max_value=50 , key="plan_sets" , step=1)

      st.number_input("Reps per set" , min_value=0 , max_value=50 , key="plan_reps" , step=1)

      st.markdown("")

      start_session_button = st.button("Start Session" , width="stretch" , key="start_session_button")
      if start_session_button:
        st.session_state["workout_started"] = True
        st.rerun()

      else:
        exercise = st.session_state.get("plan_exercise")
        sets = st.session_state.get("plan_sets")
        reps = st.session_state.get("plan_reps")

        st.info(f"**{exercise}** -- {sets} Sets / {reps} Reps")

        end_session_button = st.button("End Session" , key="end_session_button")

        if end_session_button:
          st.session_state["workout_started"] = False

if __name__ == "__main__":
  main()


st.set_page_config(page_title="Realtime-Fitness-Coach-AI")

