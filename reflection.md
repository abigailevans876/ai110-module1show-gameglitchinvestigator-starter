# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game it looked like it was working until I started guessing. The first bug I saw was the number of attempts were mismatched on the sidebar and the main part of the page and the second bug was that if I guessed high, the hint told me to go higher

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Cause in Code |
|-------|-------------------|-----------------|------------------------|---------------|
| Start a new game on Normal | "Attempts left: 8" to match the sidebar | "Attempts left: 7" | none | `st.session_state.attempts` started at `1` instead of `0` |
| Guess 63 when the secret is 53 | "Go LOWER!" | "Go HIGHER!" | none | The messages in `check_guess` were swapped |
| Guess 9 twice when the secret is 50 | "Go HIGHER!" both times | Attempt 1: "Go HIGHER!", attempt 2: "Go LOWER!" | none | On even attempts the secret was turned into a string, so `"9" > "50"` was compared as text |
| Keep guessing after winning | "You already won. Start a new game to play again." | The game kept accepting guesses (attempt 4: "Go HIGHER!") | none | `st.session_state.status = "playing"` ran on every rerun, and the New Game handler was missing |

**Game trace (starter code, before fixes)**

```
Secret: 53 | Guess a number between 1 and 100. Attempts left: 7
attempts=2: guessed 63 -> ['Go HIGHER!']          <- wrong, 63 is too high
attempts=3: guessed 53 -> ['Correct!', 'You won! The secret was 53. Final score: 65']
```

**Game trace (after the hint fix, before the remaining fixes)**

```
Secret set to 50
attempts=1: guessed 9 -> ['Go HIGHER!']           status=playing
attempts=2: guessed 9 -> ['Go LOWER!']            status=playing   <- same guess, opposite hint
attempts=3: guessed 50 -> ['Correct!', 'You won! The secret was 50. Final score: 60'] status=won
attempts=4: guessed 20 -> ['Go HIGHER!']          status=playing   <- game kept going after the win
```

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used Claude. One example of an AI suggestion that was correct was when I accepted the attempts fix. I confirmed it, by checking that "Attempts left" showed 8, matching the sidebar. Claude also explained that Streamlit reruns the whole script on every click, so 'st.session_state.status = "playing"' at the top of the file wiped out a win right after it happened.
A suggestion I didn't accept as written was that I rejected Claude's edits to app.py twice and asked to be guided step by step first because I wanted to understand why the change was suggested.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided if a bug was fixed by manually refeshing the game and testing it to see if the bug persists. For example, I also used pytest to exammine if test_guess_too_high checks that a guess of 60 against a secret of 50 returns "Too High" with a "LOWER" message. The original tests failed at first because check_guess returns two values (the outcome and the message), not just one. I use AI to design tests as Claude suggested and wrote the edge-case tests (empty input, "abc", -5, 3.7). This helped me to understand how the current code handles irregular inputs and how it is handled.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

In Streamlit, every time a button is clicked or a box is typed into, the Python program runs again from top to bottom. Without session state, the secret number would regenerate on every click because the code at the top would execute repeatedly. However, Streamlit provides `st.session_state` as a persistent memory between reruns, acting like a sticky note that preserves data, so checking `if "secret" not in st.session_state` ensures the secret is only chosen once at the start of the game. Without properly scoping that state, top-level assignments like `st.session_state.status = "playing"` run on every rerun and immediately wipe out a player's win.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

In the future I would like to continue to use AI to help me identify and understand the bugs in the code so I can decide how to fix it or ask AI for help if needed. One thing I would do differently in the future is ensuring that my prompts accurately describe what I need the AI to help me with. This project made me have an appreciation for AI assisted coding while enforcing the need for human review to ensure the assistance matches my needs for the task I am completing.