## 1. What was broken when you started?

### Bugs Observed

1. Hints were reversed — guessing 0 against a secret of 35 showed
   "Go LOWER" instead of "Go HIGHER."
2. On even-numbered attempts, the secret was cast to a string, causing
   comparisons to break and history to log corrupted values like 0 and -1.
3. Wrong guesses sometimes increased the score instead of decreasing it.
4. Attempts left showed 7 before the first guess on Normal (should be 8).
5. New Game button didn't reset score or status after a loss.

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|---|---|---|---|
| Guess 0, secret 35 (Normal) | "Go HIGHER" hint | "Go LOWER" displayed | none |
| Guess on attempt #2 | Normal hint + guess logged | History shows 0 or -1 | none |
| Wrong guess on even attempt | Score decreases by 5 | Score increased by 5 | none |
| Fresh Normal game, no guesses yet | "Attempts left: 8" | "Attempts left: 7" | none |
| Click New Game after losing | Full reset | Score/status unchanged | none |

## 2. How did you use AI as a teammate?

### Correct AI suggestion
When I asked my AI assistant to walk through `check_guess` step-by-step
for `guess=80, secret=50`, it correctly identified that the function
returned "Go HIGHER!" when the player should be told to go lower, and
pointed at the swapped message strings on the two return lines.
I verified this by checking the source — the message strings were indeed
attached to the wrong branches — and by running the game with the debug
expander open: guess=80 against secret=50 produced "📈 Go HIGHER!" before
the fix, and "📉 Go LOWER!" after.

### Misleading AI suggestion
When I asked the assistant how to fix the every-other-attempt string-cast
issue, it proposed wrapping `check_guess` in additional `try/except`
blocks and adding a `str(secret) == str(guess)` fallback. That hides the
symptom instead of removing the cause. The actual bug was a stray
`if attempts % 2 == 0: secret = str(...)` block in `app.py`'s submit
handler. I rejected the suggestion, deleted the bad cast entirely, and
added `test_check_guess_handles_string_secret` as a regression test so
the cleaner fix is verified going forward.

## 3. Debugging and testing your fixes

I verified each fix two ways:

1. **Manual play** with the Developer Debug Info expander open, so I could
   see the secret and confirm hint direction. Guessing 0 against a secret
   of 35 now correctly says "📈 Go HIGHER!" instead of "Go LOWER."
2. **`pytest -v`** — 16 tests pass, including a regression test for the
   string-secret bug and 8 edge-case tests for `parse_guess` (empty
   string, whitespace, None, negatives, decimals, huge numbers, non-numeric
   strings, valid int).

The full pytest output is in `test_results.txt` and pasted in the README.

## 4. What surprised you about working with AI on this project?

The most surprising thing was how confidently the AI suggested fixes that
addressed symptoms instead of root causes. When I described the broken
hint behavior, it was quick to wrap things in `try/except` rather than
look upstream at the `app.py` submit handler where the actual string
cast lived. That made me realize that reviewing the diff line-by-line
matters more than reading the AI's explanation — the explanation often
sounds reasonable even when the fix is wrong.

## 5. If you had more time, what would you improve?

I would add a persistent high-score file (saved to disk between
sessions), difficulty-aware scoring (Hard wins worth more), and a
visual chart of guesses vs the secret in the Guess History panel. I'd
also add property-based tests with Hypothesis to catch edge cases I
didn't think of, and wire up GitHub Actions to run pytest on every push.