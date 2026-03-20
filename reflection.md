# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  
  While the game UI looks user-friendly and easy to understand, when running it for the first time, it let me enter numbers that are out of the specified range and did not dispaly any error message. Some of the bugs that I found and the what should happen are list below.

   -When changing the level of difficulty, the range is not setting correctly in the main window, and the secret is not changing within the the range of integers specified in the difficulty level
  - requirement: The main window should display the correct information based on level of difficulty,and the secret should be within the the range of integers specified in the difficulty level

   - Hints does not help the user to get closer to secret number to win the game. Hints mislead the user
  - requirement: Hints are supposed to help the user to get closer the required target

- bug: The "New Game" does not reset the window to paly a new game
  - requirement: The "New Game" button should reset all the variables in the game. It should reset the state of the game.

  - bug: "Attempts allowed" The sidebar is one point higher than "Attempts left" in the main area.
  - requirement. The sidebar and main window should display the same number of attempts at all levels of diffukty

 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  AI suggestion : Hint always says "1 to 100" regardless of difficulty
  This is what AI specifically stated about this bug 
  ```
  st.info(
    f"Guess a number between 1 and 100. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
  )
  ```
  The string "1 and 100" is hardcoded. It never uses the low and high variables that were already computed just above it at app.py:87:

  low, high = get_range_for_difficulty(difficulty)

  How I verified:  You can easily verify this. When the user change the level of difficuly , the main window does not show the correct range of numbers for the user to enter.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  There is this AI suggesstion"Bug: **Hard's range (1–50) is smaller than Normal's (1–100), yet Hard gets fewer attempts (5 vs 8).** That's actually harder. But the hint UI always says "Guess between 1 and 100" regardless of difficulty (line 110)."
  While AI is correctly distinguish harder range and Nomral range. However, AI suggest that Harder range should have more attempts than nomral range. While I do not have access to specific user requirements of this app, I assume that having fewer range for the level 'Hard' than that for the 'Normal' range is by design by the development team.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
