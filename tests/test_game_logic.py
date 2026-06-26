"""Automated tests for game logic.

Covers each bug fix plus edge cases (Challenge 1).
"""
import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# --- check_guess: verifies the reversed-hint bug is fixed ---
def test_check_guess_win_returns_win():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_check_guess_too_high_tells_player_to_go_lower():
    outcome, msg = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in msg.upper()


def test_check_guess_too_low_tells_player_to_go_higher():
    outcome, msg = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in msg.upper()


def test_check_guess_handles_string_secret():
    # Regression test for the every-other-attempt string-cast bug.
    outcome, _ = check_guess(60, "100")
    assert outcome == "Too Low"


# --- update_score: verifies the wrong-guess-rewards-points bug is fixed ---
def test_wrong_guess_never_rewards_points():
    for attempt in range(1, 11):
        assert update_score(100, "Too High", attempt) == 95
        assert update_score(100, "Too Low", attempt) == 95


def test_win_awards_at_least_10_points():
    assert update_score(0, "Win", 99) >= 10


def test_win_on_attempt_one_awards_full_points():
    assert update_score(0, "Win", 1) == 90


# --- Challenge 1: parse_guess edge cases ---
def test_parse_guess_valid_int():
    ok, value, _ = parse_guess("42")
    assert ok and value == 42


def test_parse_guess_decimal_truncates_to_int():
    ok, value, _ = parse_guess("42.9")
    assert ok and value == 42


def test_parse_guess_negative_number():
    ok, value, _ = parse_guess("-7")
    assert ok and value == -7


def test_parse_guess_empty_string_rejected():
    ok, _, err = parse_guess("")
    assert not ok and err


def test_parse_guess_whitespace_only_rejected():
    ok, _, err = parse_guess("   ")
    assert not ok and err


def test_parse_guess_non_numeric_rejected():
    ok, _, err = parse_guess("seventeen")
    assert not ok and err


def test_parse_guess_huge_number_accepted():
    ok, value, _ = parse_guess("999999999999")
    assert ok and value == 999999999999


def test_parse_guess_none_rejected():
    ok, _, err = parse_guess(None)
    assert not ok and err


# --- get_range_for_difficulty: verifies the inverted Hard range is fixed ---
def test_difficulty_ranges_increase():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high