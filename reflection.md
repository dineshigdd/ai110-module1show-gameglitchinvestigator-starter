# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  While the game UI looks user-friendly and easy to understand, when running it for the first time, it let me enter numbers that are out of the specified range and did not dispaly any error message. Some of the bugs that I found and the what should happen are list below.

  - bug: "Attempts allowed" The sidebar is one point higher than "Attempts left" in the main area.
  - requirement. The sidebar and main window should display the same number of attempts at all levels of diffukty

  - bug: The "New Game" does not reset the window to paly a new game
  - requirement: The "New Game" button should reset all the variables in the game. It should reset the state of the game.

  - when changing the level of difficulty, the range is not setting correctly in the main window
  - requirement: The main window should display the correct information based on level of difficulty

  - Hints does not help the user to get closer to secret number to win the game. Hints mislead the user
  - requirement: Hints are supposed to help the user to get closer the required target



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

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
