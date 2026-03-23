def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""    
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
           value = float(raw)
           return False, value, "No decimals allowed. The guess must be an integer."
        else:
            value = int(raw)
            if value <= 0:
                return False, None, "zero and negative numbers are not allowed.The guess must be a positive integer .."
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret): #FIX: Refactored logic into logic_utils.py using claude code 
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    else:##FIX: Updated the return values for "Too High" and "Too Low" outcomes to provide clearer feedback to the user on whether they should guess higher or lower, and to ensure consistency in the feedback messages.
        if guess > secret:
            return "Too High", "📈 Go LOWER!" #fixed the return value
        else:
            return "Too Low", "📉 Go HIGHER!" #fixed the return value
    # except TypeError:## FIXME: Added error handling for type errors that may occur if guess or secret are not comparable types, such as if the user inputs a non-numeric value that was not properly parsed, to prevent the application from crashing and to provide a user-friendly error message.
    #     g = str(guess)
    #     if g == secret:
    #         return "Win", "🎉 Correct!"
    #     if g > secret:
    #         return "Too High", "📈 Go LOWER!" #fixed the return value
    #     return "Too Low", "📉 Go HIGHER!" #fixed the return value


def update_score(current_score: int, outcome: str, attempt_number: int):  #FIX: Refactored logic into logic_utils.py using claude code 
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        # if points < 10:
        #     points = 10
        return current_score + points

    if outcome == "Too High":
        ##removed the attempt number condition to simplify the logic and 
        # ensure consistent scoring for "Too High" outcomes regardless of attempt number.
        # if attempt_number % 2 == 0: 
        #     return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score