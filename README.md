# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

AI built number guessing game in Streamlit and it broken. You can't win, hints lied, secret number won't stay put. This repo fixed that.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`
3. Run the tests: `pytest -v`

## 🐛 Bugs Found & Fixes Applied

It a Streamlit number guessing game: pick number in range, get hot/cold hints, score go up for fast wins and down for misses.

**What was broken:**
1. Hints backwards. Guess too high, told you go higher.
2. Every other turn, game swapped secret to string, so comparisons don't work.
3. Wrong guesses on even turns gave +5 points instead of taking 5
4.  Attempts counter start at 1 instead of 0, Normal mode show "7 left" before done anything.
5. New Game didn't reset score and game over state.

**What I changed:**
- Pulled game logic out `app.py` into `logic_utils.py` so can be tested by itself.
- Flipped swapped hint messages in `check_guess`, made sure it always works with ints
- Deleted line in `app.py` that caused secret to string every other turn.
- Rewrote `update_score` so misses always cost 5 and wins scale with how fast you got it.
- Made single `fresh_game_state` helper that both startup and New Game button use, so resets matches current difficulty.
- Added 16 pytest cases covering every fix and bunch of weird `parse_guess` inputs.

## 📸 Demo Walkthrough

1. Open the app and pick "Normal" in sidebar.
2. Expand "Developer Debug Info" to look at secret 
3. Say it's 73.
4. Guess 40 = "Go HIGHER!" 7 attempts left.
5. Guess 90 = "Go LOWER!" 6 attempts left. Score sits at -10 from two misses.
6. Guess 73 = balloons, "Correct!", final score 80.
7. Guess History table marks each guess as Hot, Warm,  Cold, Hit based on how close it was.
8. Hit "New Game", everything resets with new secret based on current difficulty.

## 🧪 Test Results

```
======================== test session starts ========================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
collected 16 items                                                   

tests/test_game_logic.py::test_check_guess_win_returns_win PASSED                       [  6%]
tests/test_game_logic.py::test_check_guess_too_high_tells_player_to_go_lower PASSED     [ 12%]
tests/test_game_logic.py::test_check_guess_too_low_tells_player_to_go_higher PASSED     [ 18%]
tests/test_game_logic.py::test_check_guess_handles_string_secret PASSED                 [ 25%]
tests/test_game_logic.py::test_wrong_guess_never_rewards_points PASSED                  [ 31%]
tests/test_game_logic.py::test_win_awards_at_least_10_points PASSED                     [ 37%]
tests/test_game_logic.py::test_win_on_attempt_one_awards_full_points PASSED             [ 43%]
tests/test_game_logic.py::test_parse_guess_valid_int PASSED                             [ 50%]
tests/test_game_logic.py::test_parse_guess_decimal_truncates_to_int PASSED              [ 56%]
tests/test_game_logic.py::test_parse_guess_negative_number PASSED                       [ 62%]
tests/test_game_logic.py::test_parse_guess_empty_string_rejected PASSED                 [ 68%]
tests/test_game_logic.py::test_parse_guess_whitespace_only_rejected PASSED              [ 75%]
tests/test_game_logic.py::test_parse_guess_non_numeric_rejected PASSED                  [ 81%]
tests/test_game_logic.py::test_parse_guess_huge_number_accepted PASSED                  [ 87%]
tests/test_game_logic.py::test_parse_guess_none_rejected PASSED                         [ 93%]
tests/test_game_logic.py::test_difficulty_ranges_increase PASSED                        [100%]

======================== 16 passed in 0.08s =========================
```

## 🚀 Stretch Features

- **Challenge 1: Edge-Case Testing:** 8 extra pytest cases throw weird inputs at `parse_guess` (empty strings, just whitespace, None, negatives, decimals, huge numbers, gibberish) 

All in `tests/test_game_logic.py`.

- **Challenge 3: Docstrings & PEP 8:** Every function in `logic_utils.py` has docstring, `flake8` runs clean. Prompts and notes in `ai_interactions.md`.

- **Challenge 4: Better UI:** Added Guess History table with Hot/Warm/Cold indicators, 🏆 High Score in sidebar, color coded hint banners so wins, misses, "wrong direction" look different
