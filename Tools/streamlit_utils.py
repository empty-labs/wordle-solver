# Local libraries
import Classes.wordle_data as wd
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

    round_key = f"round_{rd}"
    st.header(f"Round {rd}")

    # Initialize section state
    if round_key not in st.session_state.round:
        st.session_state.round[round_key] = {}
        st.markdown(f"{rd} {round_key}")

    state = st.session_state.round[round_key]

    choice_cols = st.columns(5)
    selected_letters = []

    for i, col in enumerate(choice_cols):

        with col:
            selected_letters.append(st.selectbox(
                f"Letter #{rd}:",
                letters,
                key=f"round_{rd}_letter_{i}",
                index=0
            ))

    # Initialize state
    if "letters" not in state:
        state["letters"] = [{"letter": "", "color": colors[0]} for _ in range(5)]

    # Create columns for each letter
    state_cols = st.columns(5)

    for i, col in enumerate(state_cols):
        letter_info = state["letters"][i]
        letter_info["letter"] = selected_letters[i]

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
    state["guess"] = "".join(selected_letters)


def run_wordle_solver(rd: int):

    round_key = f"round_{rd}"
    state = st.session_state.round[round_key]

    if 'wdl' not in st.session_state:
        wdl = wd.Wordle()
        wdl.set_data()
        st.session_state['wdl'] = wdl

    st.write("")  # Linebreak

    # Run simulation
    run_button = st.button("Run Wordle Solver", key=f"run_btn_{rd}")

    if run_button:

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

            st.session_state['wdl'].wordle_guess(
                guess_word=state["guess"],
                good_letters=good_letters,
                good_letters_good_placement=good_letters_good_placement,
                good_letters_bad_placement=good_letters_bad_placement,
                debug=False)
            state["results"] = wu.wordle_solver(
                wordle=st.session_state['wdl'],
                print_wiki_words=False)

            state["solver_ran"] = True

            # if rd < 1 and st.session_state.active_rounds == rd:
            #     st.session_state.active_rounds += 1
            #
            # st.rerun()
