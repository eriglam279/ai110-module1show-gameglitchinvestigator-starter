# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and the game was unplayable.

- You couldn't win.
- The hints lied to you.
- The secret number had commitment issues.

This repo is the **repaired** version.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`
3. Run the tests: `pytest -v`

## 🐛 Bugs Found & Fixes Applied

**Game purpose:** A Streamlit number-guessing game where the player tries to guess a secret number within a limited number of attempts, with a score that rewards faster wins.

**Bugs found in the starter code:**
1. Hints were reversed — `check_guess` returned "Go HIGHER" when the guess was already too high.
2. Every other attempt, the secret was cast to a string in `app.py`, breaking comparisons.
3. `update_score` rewarded +5 for "Too High" on even attempts instead of penalizing.
4. `attempts` initialized to 1, making "Attempts left" off by one.
5. "New Game" didn't reset score, status, or history, and ignored the current difficulty.

**Fixes applied:**
- Refactored all game logic into `logic_utils.py` so it can be tested without Streamlit.
- Swapped the reversed hint messages in `check_guess` and added `int()` coercion to handle any stray string inputs.
- Removed the every-other-attempt string cast from the submit handler in `app.py`.
- Rewrote `update_score` so wrong guesses always cost 5 points and wins award `max(10, 100 - 10 * attempt)`.
- Added a `fresh_game_state(low, high)` helper used by both startup and the "New Game" button so resets always respect the current difficulty.
- Added 16 pytest cases covering each fix plus edge cases for `parse_guess`.

## 📸 Demo Walkthrough

1. Open the app at http://localhost:8501. Select "Normal" in the sidebar.
2. Expand "Developer Debug Info" to see the secret (e.g., 73).
3. Enter `40` → game shows "📈 Go HIGHER!" and Attempts left: 7.
4. Enter `90` → game shows "📉 Go LOWER!" and Attempts left: 6. Score is now -10 (two wrong guesses, -5 each).
5. Enter `73` → balloons, "🎉 Correct!", and final score 80.
6. The Guess History table shows each attempt with a heat indicator (🔥 Hot / ♨️ Warm / ❄️ Cold / 🎯 Hit).
7. Click "New Game 🔁" → state fully resets, secret is re-drawn from the current difficulty range.

## 🧪 Test Results

======================== test session starts ========================

collected 16 items
tests/test_game_logic.py ................                      [100%]
======================== 16 passed in 0.08s =========================

## 🚀 Stretch Features

- **Challenge 1 — Advanced Edge-Case Testing.** Added 8 pytest cases for `parse_guess` covering empty strings, whitespace, None, negatives, decimals, large numbers, and non-numeric input. See `tests/test_game_logic.py` and `ai_interactions.md`.
- **Challenge 3 — Professional Documentation & PEP 8.** All functions in `logic_utils.py` have docstrings. `flake8 logic_utils.py` reports no issues (see `lint_results.txt`). See `ai_interactions.md` for prompts.
- **Challenge 4 — Enhanced Game UI.** Added a Guess History table with Hot/Warm/Cold/Freezing heat indicators (computed by absolute distance to the secret), a 🏆 High Score sidebar metric, and color-coded hint banners (success/warning/info). All UI changes live in the bottom of `app.py`.