# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The number of attempts were mismatched on the sidebar and the main part of the page and the hints

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| Attempts| Attempts should be 8 |Attempts was 7 | none|
|New Game |Attempts reset to 8 | Attempts did not reset to 8| none |
|Hint |The hint should accurately tell the user if they need to go lower/higher to get secret number | The hint was inaccurate in telling users whether to go lower/higher to get secret number| Telling user to go lower when they need to go higher or vice versa|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used Claude. One example of an AI suggestion that was correct was to fix the number of guesses on the page to match the one on the side panel. There was not an instance where I rejected the AI suggestion in this activity
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided if a bug was fixed by manually refeshing the game and testing it to see if the bug persists. I did not use AI to design or understand any tests 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

In the future I would like to continue to use AI to help me identify and understand the bugs in the code so I can decide how to fix it or ask AI for help if needed. One thing I would do differently in the future is ensuring that my prompts accurately describe what I need the AI to help me with. This project made me have an appreciation for AI assisted coding while enforcing the need for human review to ensure the assistance matches my needs for the task I am completing.