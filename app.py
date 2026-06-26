"""Streamlit UI for the Number Guessing Game.

All pure logic is in logic_utils.py so it can be tested without Streamlit.
"""
import streamlit as st

from logic_utils import (
    check_guess,
    fresh_game_state,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game — now repaired.")

# --- Sidebar settings ---
st.sidebar.header("Settings")
difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {"Easy": 6, "Normal": 8, "Hard": 10}
attempt_limit = attempt_limit_map[difficulty]
low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# --- Session state init (FIX: attempts starts at 0) ---
for k, v in fresh_game_state(low, high).items():
    if k not in st.session_state:
        st.session_state[k] = v
if "high_score" not in st.session_state:
    st.session_state.high_score = 0
if "difficulty_last" not in st.session_state:
    st.session_state.difficulty_last = difficulty

# FIX: difficulty change triggers full reset with correct range
if st.session_state.difficulty_last != difficulty:
    for k, v in fresh_game_state(low, high).items():
        st.session_state[k] = v
    st.session_state.difficulty_last = difficulty

# --- Main UI ---
st.subheader("Make a guess")
attempts_left = max(0, attempt_limit - st.session_state.attempts)
st.info(f"Guess a number between {low} and {high}. Attempts left: {attempts_left}")

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input("Enter your guess:", key=f"guess_input_{difficulty}")

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

# FIX: new_game now fully resets state and respects current difficulty
if new_game:
    for k, v in fresh_game_state(low, high).items():
        st.session_state[k] = v
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

# FIX: removed the every-other-attempt string cast on secret
if submit:
    ok, guess_int, err = parse_guess(raw_guess)
    if not ok:
        st.error(err)
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            if outcome == "Win":
                st.success(message)
            elif outcome == "Too High":
                st.warning(message)
            else:
                st.info(message)

        st.session_state.score = update_score(
            st.session_state.score, outcome, st.session_state.attempts
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            if st.session_state.score > st.session_state.high_score:
                st.session_state.high_score = st.session_state.score
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.error(
                f"Out of attempts! The secret was {st.session_state.secret}. "
                f"Score: {st.session_state.score}"
            )

# --- Challenge 4: heat map history + high score sidebar ---
st.sidebar.divider()
st.sidebar.metric("🏆 High Score", st.session_state.high_score)

if st.session_state.history:
    st.subheader("Guess History")
    rows = []
    for i, g in enumerate(st.session_state.history, start=1):
        try:
            diff = abs(int(g) - st.session_state.secret)
            if diff == 0:
                heat = "🎯 Hit!"
            elif diff <= 5:
                heat = "🔥 Hot"
            elif diff <= 15:
                heat = "♨️ Warm"
            elif diff <= 30:
                heat = "❄️ Cold"
            else:
                heat = "🧊 Freezing"
        except (ValueError, TypeError):
            heat = "—"
        rows.append({"Attempt": i, "Guess": g, "Heat": heat})
    st.table(rows)

st.divider()
st.caption("Repaired by a human who actually tested the code.")