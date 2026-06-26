# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

*Didn't attempt this one.*

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

 Had AI generate pytest cases for `parse_guess` covering weird stuff users do (empty strings, whitespace, None, negatives, decimals, huge numbers, gibberish) all 8 tests passed on first run.

**Prompt used:**

> "Generate pytest cases for `parse_guess(raw)` in logic_utils.py that cover edge cases: empty string, whitespace-only, None, negative numbers, decimal strings, very large numbers, and non-numeric input. Each test should be a single assertion and not depend on Streamlit."

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Empty string | See prompt above | `test_parse_guess_empty_string_rejected` | Y | Hits Submit without typing anything. |
| Whitespace only | See prompt above | `test_parse_guess_whitespace_only_rejected` | Y | Accidental space tap, starter only checked for `""`. |
| None | See prompt above | `test_parse_guess_none_rejected` | Y | In case stale state passes None through. |
| Negative number | See prompt above | `test_parse_guess_negative_number` | Y | Outside game range, but parser shouldn't crash. |
| Decimal string | See prompt above | `test_parse_guess_decimal_truncates_to_int` | Y | Text input accepts decimals; game uses ints. |
| Huge number | See prompt above | `test_parse_guess_huge_number_accepted` | Y | Confirm nothing blows up on `999999999999`. |
| Non-numeric | See prompt above | `test_parse_guess_non_numeric_rejected` | Y | Typos like "fifty" should fail. |
| Valid int | See prompt above | `test_parse_guess_valid_int` | Y | Sanity check happy path still works. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Add Google-style docstrings to every function in logic_utils.py.
Then check the file for PEP 8 issues.
```

**Linting output before:**

```
logic_utils.py:84:6: W292 no newline at end of file
logic_utils.py:85:1: W293 blank line contains whitespace
```

**Changes applied:**

AI assisted in the implementation of docstrings for five functions in `logic_utils.py`. `flake8` flagged missing newline at the end of file, which I cleaned up

 AI suggested me to split `check_guess` into three smaller functions for "single responsibility." I said no as function does one thing (compare two numbers, retur result), splitting would just spread that one job around without making anything clearer.

---

## Model Comparison (SF11)

*Didn't attempt this one.*