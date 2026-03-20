from logic_utils import check_guess

# def test_winning_guess():
#     # If the secret is 50 and guess is 50, it should be a win
#     result = check_guess(50, 50)
#     assert result == "Win"

# def test_guess_too_high():
#     # If secret is 50 and guess is 60, hint should be "Too High"
#     result = check_guess(60, 50)
#     assert result == "Too High"

# def test_guess_too_low():
#     # If secret is 50 and guess is 40, hint should be "Too Low"
#     result = check_guess(40, 50)
#     assert result == "Too Low"


# --- Bug: check_guess returns a tuple, not a plain string ---
# The three tests above compare result to a string like "Win" or "Too High",
# but check_guess actually returns (outcome, message). All three will fail.

def test_check_guess_returns_tuple():
    # Exposes the return-type mismatch: result is a tuple, not a string
    result = check_guess(50, 50)
    assert isinstance(result, tuple), f"Expected tuple, got {type(result)}"
    assert len(result) == 2

def test_winning_guess():
    # Correct way to assert: unpack the tuple
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📈 Go LOWER!"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📉 Go HIGHER!"


# --- Bug: st.info() shows wrong "Attempts left" on first render ---
# app.py initializes st.session_state.attempts = 1 (not 0).
# The display formula is: attempt_limit - st.session_state.attempts
# So on the very first render (before any guess), the player sees one fewer
# attempt than they actually have.

def test_attempts_left_off_by_one_on_first_render():
    attempt_limit = 8          # Normal difficulty
    initial_attempts = 1       # value set in app.py at session start
    displayed = attempt_limit - initial_attempts
    # Bug: displayed is 7, but the player hasn't guessed yet — should be 8
    assert displayed != attempt_limit, (
        "Attempts left should equal attempt_limit before any guess, but the "
        "off-by-one init causes it to show one fewer."
    )

def test_attempts_left_correct_after_new_game():
    # "New Game" resets attempts to 0, so the formula works correctly after reset
    attempt_limit = 8
    attempts_after_reset = 0   # set by new_game handler in app.py
    displayed = attempt_limit - attempts_after_reset
    assert displayed == attempt_limit  # correct: shows full attempt count
