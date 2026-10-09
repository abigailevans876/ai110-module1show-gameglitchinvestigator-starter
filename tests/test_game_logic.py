from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_empty_input():
    # Clicking Submit with an empty box should be rejected
    ok, value, err = parse_guess("")
    assert ok is False and err == "Enter a guess."

def test_non_numeric_input():
    # Letters should be rejected instead of crashing
    ok, value, err = parse_guess("abc")
    assert ok is False and err == "That is not a number."

def test_negative_number():
    # Negative numbers parse as ints
    ok, value, err = parse_guess("-5")
    assert ok is True and value == -5

def test_decimal_is_truncated():
    # Decimals are cut down to a whole number
    ok, value, err = parse_guess("3.7")
    assert ok is True and value == 3
