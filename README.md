# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Purpose

Glitchy Guesser is a Streamlit number guessing game. You pick a difficulty (Easy, Normal, or Hard). The game picks a secret number in that range, and you get a limited number of attempts to guess it. After each guess, a hint tells you whether to go higher or lower, and your score changes depending on how quickly you win.

### Bugs found

| # | Bug | Cause in code |
|---|-----|---------------|
| 1 | "Attempts left" showed 7 on Normal while the sidebar said 8 | `st.session_state.attempts` started at `1` instead of `0` |
| 2 | Hints pointed the wrong way (guessing too high said "Go HIGHER") | The two messages in `check_guess` were swapped |
| 3 | The same guess got opposite hints on different attempts | On even attempts the secret was turned into a string with `str(...)`, so the comparison was done as text (`"9" > "50"` is `True`) |
| 4 | After winning or losing you could keep guessing, and New Game did nothing | `st.session_state.status = "playing"` ran on every rerun, and the `if new_game:` handler was missing |
| 5 | The instructions always said "between 1 and 100", whatever the difficulty | The range was hard-coded in the `st.info` message |

### Fixes applied

1. **Attempts counter:** it now starts at `0`, so `attempt_limit - attempts` matches the sidebar.
2. **Hints:** the messages in `check_guess` were swapped back, so "Too High" says "📉 Go LOWER!" and "Too Low" says "📈 Go HIGHER!".
3. **String secret:** `app.py` always passes the integer `st.session_state.secret` to `check_guess`. The comparison is now numeric on every attempt.
4. **Game over and New Game:** the status reset was moved inside an `if new_game:` block. That block also resets attempts and history and picks a new secret in the current difficulty's range. Streamlit reruns the whole script on every click, so the reset only belongs inside the button's branch.
5. **Range message:** the instructions now use `{low}` and `{high}` from `get_range_for_difficulty`.
6. **Refactor:** `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` moved to `logic_utils.py` so they can be tested with pytest.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py` and keep the default "Normal" difficulty. The info box says "Guess a number between 1 and 100. Attempts left: 8", which matches the sidebar.
2. Open "Developer Debug Info". The secret is 32.
3. Guess 42. The hint is "📉 Go LOWER!" and the score drops to -5.
4. Guess 31. The hint is "📈 Go HIGHER!". This is attempt 2, an even attempt, and the hint is still correct.
5. Guess 32. Balloons appear, then "You won! The secret was 32. Final score: 50".
6. Guess again. The game blocks it with "You already won. Start a new game to play again."
7. Click "New Game 🔁". Status is back to playing, attempts are 0, history is empty, and there's a new secret.

Session output from the fixed app:

```
Difficulty: Normal | Secret (from debug panel): 32 | Guess a number between 1 and 100. Attempts left: 8
Attempt 1: guessed 42 -> ['📉 Go LOWER!'] | score=-5
Attempt 2: guessed 31 -> ['📈 Go HIGHER!'] | score=-10
Attempt 3: guessed 32 -> ['🎉 Correct!', 'You won! The secret was 32. Final score: 50'] | score=50
Status: won
Guess after winning -> ['You already won. Start a new game to play again.'] | attempts still 3
New Game -> status: playing | attempts: 0 | history: [] | new secret: 43
```

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest -v
============================= test session starts ==============================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0
collected 7 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 42%]
tests/test_game_logic.py::test_empty_input PASSED                        [ 57%]
tests/test_game_logic.py::test_non_numeric_input PASSED                  [ 71%]
tests/test_game_logic.py::test_negative_number PASSED                    [ 85%]
tests/test_game_logic.py::test_decimal_is_truncated PASSED               [100%]

============================== 7 passed in 0.02s ===============================
```

## 🚀 Stretch Features

- **Advanced Edge-Case Testing:** `tests/test_game_logic.py` has four `parse_guess` edge-case tests: empty input, non-numeric text, a negative number, and a decimal. All of them pass (see Test Results above). The prompts and reasoning are in `ai_interactions.md`.
