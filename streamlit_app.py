# Local libraries
import Classes.wordle_data as wd
import Tools.streamlit_utils as stu

# Third party packages
import streamlit as st


wdl = wd.Wordle()
wdl.set_data()

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

stu.generate_round_section(rd=1)
stu.run_wordle_solver(rd=1, wdl=wdl)
