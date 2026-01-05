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

st.divider()

state = stu.generate_round_section(rd=1)
stu.run_wordle_solver(state=state, wdl=wdl)

# st.write("")  # Linebreak
#
# # Run simulation
# run_button = st.button("Run Wordle Solver")
#
# if run_button:
#     st.subheader("Wordle Solver Results")
#
#     with st.spinner("Running Wordle Solver..."):
#
#         good_letters = []
#         good_letters_good_placement = []
#         good_letters_bad_placement = []
#
#         for i, letter_info in enumerate(state["letters"]):
#             # Good letters, bad placement
#             if letter_info["color"] == "lightyellow":
#                 good_letters.append(letter_info["letter"])
#                 good_letters_bad_placement.append(i)
#                 good_letters_good_placement.append(None)
#
#             # Good letters, good placement
#             elif letter_info["color"] == "green":
#                 good_letters.append(letter_info["letter"])
#                 good_letters_bad_placement.append(None)
#                 good_letters_good_placement.append(i)
#
#         if not good_letters:
#             good_letters = None
#
#         if not good_letters_good_placement:
#             good_letters_good_placement = None
#
#         if not good_letters_bad_placement:
#             good_letters_bad_placement = None
#
#         wdl.wordle_guess(guess_word=state["guess"],
#                          good_letters=good_letters,
#                          good_letters_good_placement=good_letters_good_placement,
#                          good_letters_bad_placement=good_letters_bad_placement,
#                          debug=False)
#         results = wu.wordle_solver(wordle=wdl, print_wiki_words=False)
#
#         st.markdown(f"### Guess: {state["guess"]}")
#         st.markdown(results.replace("\n", "  \n"))  # Replace newlines with streamlit-friendly newlines
