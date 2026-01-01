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

guess = "".join(selected_letters)

# Guess #1
correct_word = 'death'
wdl.wordle_guess(guess_word=guess,
                 good_letters=['d', 'e'],
                 good_letters_good_placement=[0, 1])
wu.wordle_solver(wordle=wdl)

st.markdown(f"Guess: {guess}")
