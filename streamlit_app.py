# Local libraries
import Tools.streamlit_utils as stu

# Third party packages
import streamlit as st


# Page config
st.set_page_config(
    page_title="Wordle Solver",
    layout="centered"
)

st.title("🔤 Wordle Solver")
st.header("How to Use")
st.caption("Use this tool as a companion to the Wordle puzzle game.")

st.subheader("Option #1:")
st.markdown("Hit 'Run Solver' now to get a list of the top 10 commonly-used words.")

st.subheader("Option #2:")
st.markdown("1. Complete the 1st round in your Wordle app.")
st.markdown("2. Enter your letter guesses here, change the state of each letter (gray, yellow, green).")
st.markdown("3. Hit 'Run Solver' to get top 10 commonly-used words based on these choices.")
st.markdown("4. Repeat for subsequent rounds.")

st.header("States")
st.markdown("Gray = letter not found")
st.markdown("Yellow = good letter, wrong position")
st.markdown("Green = good letter, correct position")

if "active_rounds" not in st.session_state:
    st.session_state.active_rounds = 1

# for rd in range(1, st.session_state.active_rounds + 1):
#
#     stu.generate_round_section(rd)
#     stu.run_wordle_solver(rd)
#
#     if 'round' in st.session_state:
#         round_key = f"round_{rd}"
#         state = st.session_state.round[round_key]
#
#         if state.get("solver_ran"):
#             st.subheader("Wordle Solver Results")
#             st.markdown(f"### Guess: {state['solver_guess']}")
#             st.markdown(state["solver_results"].replace("\n", "  \n"))

rd = 1
stu.generate_round_section(rd)
stu.run_wordle_solver(rd)

if 'round' in st.session_state:
    round_key = f"round_{rd}"
    state = st.session_state.round[round_key]

    if state.get("solver_ran"):
        st.subheader("Wordle Solver Results")
        st.markdown(f"### Guess: {state['guess']}")
        st.markdown(state["results"].replace("\n", "  \n"))