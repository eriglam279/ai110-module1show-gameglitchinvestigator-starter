"""Game logic utilities for the Number Guessing Game.

All pure logic lives here so it can be unit-tested without Streamlit.
"""
import random


def get_range_for_difficulty(difficulty: str):
    """Return the inclusive (low, high) range for the given difficulty.

    FIX: starter returned 1-50 for Hard, which was smaller than Normal.
    Hard should give a wider range, making it harder to guess.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw):
    """Parse a raw user input string into an integer guess.

    Returns a tuple (ok, value, error_message).
    Accepts plain ints and decimals ("42.7" -> 42).
    """
    if raw is None or str(raw).strip() == "":
        return False, None, "Enter a guess."
    raw = str(raw).strip()
    try:
        value = int(float(raw)) if "." in raw else int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number."
    return True, value, None


def check_guess(guess, secret):
    """Compare a guess to the secret number.

    Returns (outcome, message) where outcome is one of
    'Win', 'Too High', or 'Too Low'.

    FIX: starter had hints reversed and cast secret to a string
    on even attempts, causing wrong comparisons. We now coerce
    both sides to int and return the correct direction.
    """
    # FIX: AI suggested adding more try/except here â€” rejected.
    # Root cause was the string cast upstream, not this function.
    guess = int(guess)
    secret = int(secret)
    if guess == secret:
        return "Win", "ðŸŽ‰ Correct!"
    if guess > secret:
        return "Too High", "ðŸ“‰ Go LOWER!"
    return "Too Low", "ðŸ“ˆ Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Update the running score based on the outcome of a guess.

    - Wins award (100 - 10 * attempt_number), minimum 10 points.
    - Wrong guesses always cost 5 points.

    FIX: starter rewarded Too High on even attempts. Wrong guesses
    should never give points.
    """
    if outcome == "Win":
        return current_score + max(10, 100 - 10 * attempt_number)
    if outcome in ("Too High", "Too Low"):
        return current_score - 5
    return current_score


def fresh_game_state(low: int, high: int) -> dict:
    """Return a dict representing a brand-new game's session state."""
    return {
        "secret": random.randint(low, high),
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }
