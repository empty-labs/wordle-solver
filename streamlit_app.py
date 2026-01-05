# Local libraries
import Classes.wordle_data as wd
import Tools.wordle_utils as wu

# Third party packages
import streamlit as st
import string


uppercase_letters = string.ascii_uppercase
letters = [l for l in uppercase_letters]

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

st.header("Round #1")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    selected_letter_1 = st.selectbox(
        "Letter #1:",
        letters,
        index=0
    )

with col2:
    selected_letter_2 = st.selectbox(
        "Letter #2:",
        letters,
        index=0
    )

with col3:
    selected_letter_3 = st.selectbox(
        "Letter #3:",
        letters,
        index=0
    )

with col4:
    selected_letter_4 = st.selectbox(
        "Letter #4:",
        letters,
        index=0
    )

with col5:
    selected_letter_5 = st.selectbox(
        "Letter #5:",
        letters,
        index=0
    )

selected_letters = [selected_letter_1, selected_letter_2, selected_letter_3, selected_letter_4, selected_letter_5]

# Initialize state
if "letters" not in st.session_state:
    st.session_state.letters = [{"letter": "", "color": "gray"} for letter in selected_letters]

# Color cycle
color_cycle = {"gray": "lightyellow", "lightyellow": "green", "green": "gray"}

# Create columns for each letter
cols = st.columns(5)

for i, col in enumerate(cols):
    letter_info = st.session_state.letters[i]
    letter_info["letter"] = selected_letters[i]

    # Add a unique key for each button to avoid StreamlitDuplicateElementId
    if col.button("Change State", key=f"letter_btn_{i}"):
        # Cycle the color
        letter_info["color"] = color_cycle[letter_info["color"]]

    # Show the letter with its background color
    col.markdown(
        f"<div style='background-color:{letter_info['color']}; color:black; padding:20px; text-align:center; font-weight:bold; font-size:20px;'>{letter_info['letter']}</div>",
        unsafe_allow_html=True
    )

# Current guess
guess = "".join(selected_letters)

st.write("")  # Linebreak

# Run simulation
run_button = st.button("Run Wordle Solver")

if run_button:
    st.subheader("Wordle Solver Results")

    with st.spinner("Running Wordle Solver..."):

        good_letters = []
        good_letters_good_placement = []
        good_letters_bad_placement = []

        for i, letter_info in enumerate(st.session_state.letters):
            # Good letters, bad placement
            if letter_info["color"] == "lightyellow":
                good_letters.append(letter_info["letter"])
                good_letters_bad_placement.append(i)
                good_letters_good_placement.append(None)

            # Good letters, good placement
            elif letter_info["color"] == "green":
                good_letters.append(letter_info["letter"])
                good_letters_bad_placement.append(None)
                good_letters_good_placement.append(i)

        if not good_letters:
            good_letters = None

        if not good_letters_good_placement:
            good_letters_good_placement = None

        if not good_letters_bad_placement:
            good_letters_bad_placement = None

        wdl.wordle_guess(guess_word=guess,
                         good_letters=good_letters,
                         good_letters_good_placement=good_letters_good_placement,
                         good_letters_bad_placement=good_letters_bad_placement,
                         debug=False)
        results = wu.wordle_solver(wordle=wdl, print_wiki_words=False)

        st.markdown(f"### Guess: {guess}")
        st.markdown(results.replace("\n", "  \n"))  # Replace newlines with streamlit-friendly newlines
