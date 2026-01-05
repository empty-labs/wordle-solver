# Local libraries
import Tools.wordle_utils as wu

# Third party packages
import streamlit as st
import string


uppercase_letters = string.ascii_uppercase
letters = [l for l in uppercase_letters]
colors = ["gray", "lightyellow", "green"]
color_cycle = {colors[0]: colors[1], colors[1]: colors[2], colors[2]: colors[0]}

def generate_round_section(rd: int):

    st.divider()

    # Initialize state
    if "round" not in st.session_state:
        st.session_state["round"] = {}

    round_key = f"Round {rd}"
    st.header(round_key)

    # Initialize section state
    if round_key not in st.session_state.round:
        st.session_state.round[round_key] = {}
        st.markdown(f"{rd} {round_key}")

    state = st.session_state.round[round_key]

    choice_cols = st.columns(5)

    state["choice_cols"] = []
    state["selected_letters"] = []

    for i, col in enumerate(choice_cols):
        state["choice_cols"].append(col)

        with col:
            state["selected_letters"].append(st.selectbox(
                f"Letter #{rd}-{i+1}:",
                letters,
                index=0
            ))

    # Initialize state
    state["letters"] = [{"letter": "", "color": colors[0]} for letter in state["selected_letters"]]

    # Create columns for each letter
    state_cols = st.columns(5)

    state["state_cols"] = []

    for col in state_cols:
        state["state_cols"].append(col)

    for i, col in enumerate(state["state_cols"]):
        letter_info = state["letters"][i]
        letter_info["letter"] = state["selected_letters"][i]

        # Add a unique key for each button to avoid StreamlitDuplicateElementId
        if col.button("Change State", key=f"letter_btn_{rd}_{i}"):
            # Cycle the color
            letter_info["color"] = color_cycle[letter_info["color"]]

        # Show the letter with its background color
        col.markdown(
            f"<div style='background-color:{letter_info['color']}; color:black; padding:20px; text-align:center; font-weight:bold; font-size:20px;'>{letter_info['letter']}</div>",
            unsafe_allow_html=True
        )

    # Current guess
    state["guess"] = "".join(state["selected_letters"])


def run_wordle_solver(rd: int, wdl):

    round_key = f"Round {rd}"
    state = st.session_state.round[round_key]

    st.write("")  # Linebreak

    # Run simulation
    run_button = st.button("Run Wordle Solver", key=f"run_btn_{rd}")

    if run_button:
        st.subheader("Wordle Solver Results")

        with st.spinner("Running Wordle Solver..."):

            good_letters = []
            good_letters_good_placement = []
            good_letters_bad_placement = []

            for i, letter_info in enumerate(state["letters"]):
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

            wdl.wordle_guess(guess_word=state["guess"],
                             good_letters=good_letters,
                             good_letters_good_placement=good_letters_good_placement,
                             good_letters_bad_placement=good_letters_bad_placement,
                             debug=False)
            results = wu.wordle_solver(wordle=wdl, print_wiki_words=False)

            st.markdown(f"### Guess: {state["guess"]}")
            st.markdown(results.replace("\n", "  \n"))  # Replace newlines with streamlit-friendly newlines

            state['wdl'] = wdl

            if rd < 5:
                generate_round_section(rd=rd+1)
                run_wordle_solver(rd=rd+1, wdl=wdl)
