## 1. What was broken when you started?

### Bugs Observed

1. Hints were backwards. I guessed 0 when secret is 35, game say go lower.
2. Every other guess, history show weird value like 0 or -1 instead of what I typed
3. Some wrong guess made score go up instead of down
4. Before even guessed once, Normal mode said 7 attempts left, when it supposed be 8.
5. New Game button didn't reset anything after lost

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|---|---|---|---|
| Guess 0, secret 35 (Normal) | "Go HIGHER" hint | "Go LOWER" displayed | none |
| Guess on attempt #2 | Normal hint + guess logged | History shows 0 or -1 | none |
| Wrong guess on even attempt | Score decreases by 5 | Score increased by 5 | none |
| Fresh Normal game, no guesses yet | "Attempts left: 8" | "Attempts left: 7" | none |
| Click New Game after losing | Full reset | Score/status unchanged | none |

## 2. How did you use AI as a teammate?

### A time AI got it right
Asked AI walk through what `check_guess` does when guess 80 and secret is 50. Spotted "Go HIGHER" and "Go LOWER" messages were attached to wrong branches. I checked code and confirmed they were swapped. Once I flipped them, the hints finally matched the debug panel.

### A time AI got it wrong
For bug where hints lied every other turn, AI suggested add more `try/except` around `check_guess` and compare things as strings. That would've just hidden the problem since real cause was a line in `app.py` that secretly convert secret to string on even attempts. I deleted that line instead, and added test to make sure bug never comes back.

## 3. Debugging and testing your fixes

I checked everything two ways:

1. Played game with debug panel open so could see  secret and confirm hint pointed me the right direction. Guess 0 with secret of 35 now correctly says "Go HIGHER."
2. Ran `pytest -v`, got 16 passing tests, including regression test for string bug and 8 tests for weird `parse_guess` inputs

full test output in `test_results.txt` and README.

## 4. What surprised you about working with AI on this project?

AI confident when it wrong. Kept suggesting band-aids, wrapping things in `try/except`, adding fallbacks, instead of looking at where bug actually started. Explanations just sounded smart, it would've been easy to just trust them and move on. That part surprised me since I read actual code changes carefully, not just  AI's reasoning.

## 5. If you had more time, what would you improve?

I save high score to file so sticks around after closing app, make Hard mode wins worth more points,  add little chart in Guess History showing how close each guess was. I also set up GitHub Actions so tests run automatically every time I push.