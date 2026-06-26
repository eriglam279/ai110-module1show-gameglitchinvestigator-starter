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