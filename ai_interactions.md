AI Interactions Log

Test Generation:

I asked my AI assistant to generate pytest cases for parse_guess covering edge cases like empty strings, whitespace, None, negative numbers, decimals, huge numbers, and non-numeric input. It produced 8 tests, all of which passed. I included them in tests/test_game_logic.py.

The edge cases matter because:
- Empty string: user hits Submit without typing
- Whitespace: user types a space by accident
- None: defensive coding
- Negative numbers: outside game range but should parse
- Decimals: text input allows them
- Huge numbers: confirm no crash
- Non-numeric: typos like "fifty" should fail gracefully
- Valid int: sanity check

Linting and Style:

I asked the AI to add docstrings to every function in logic_utils.py and check for PEP 8 issues. It added docstrings to all five functions. flake8 flagged a missing newline at the end of the file, which I fixed. After the fix, flake8 reports no issues.

The AI also suggested splitting check_guess into three smaller functions. I rejected that suggestion because the function does one thing (compare two numbers) and splitting it would add noise without making the code clearer.    