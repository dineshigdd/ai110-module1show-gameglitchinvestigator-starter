# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  
  While the game UI looks user-friendly and easy to understand, during the first run, it allowed me to enter numbers outside the specified range without displaying an error message. Below are the bugs I found and the corresponding requirements:

  1. Bug: When changing the difficulty level, the range in the main window does not update correctly, and the secret number does not stay within the range specified by the difficulty level.

  **Requirement:** The main window should display correct information based on the difficulty level, and the secret must be within the specified integer range.

  2. Bug: Hints do not help the user get closer to the secret number; instead, they are misleading.

  **Requirement:** Hints must assist the user in narrowing down the target number.

  3. Bug: The 'New Game' button does not reset the window to play a new game.

  **Requirement:** The 'New Game' button should reset all game variables and the game state.

  4. Bug: The 'Attempts allowed' in the sidebar is one point higher than the 'Attempts left' in the main area.

  **Requirement:** The sidebar and main window should display the same number of attempts across all difficulty levels.

  5. Bug: The number of attempts does not decrease with every guess.
  **Requirement:** The number of attempts should decrease by one after each guess.
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

  How I verified: This can be easily verified: when the user changes the difficulty level, the main window fails to update and show the correct range of numbers for the user to enter.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  There is a AI suggestion  : "Bug: **Hard's range (1–50) is smaller than Normal's (1–100), yet Hard gets fewer attempts (5 vs 8).** That's actually harder. But the hint UI always says "Guess between 1 and 100" regardless of difficulty (line 110)."

  The AI correctly distinguishes between the 'Hard' and 'Normal' ranges; however, it suggests that the 'Hard' level should have more attempts than the 'Normal' level. While I do not have access to the specific user requirements for this app, I am assuming that a smaller range for the 'Hard' level compared to the 'Normal' level is an intentional design choice by the development team."
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  First, I manually checked the output of the functions I debugged. Then, I decided to generate test cases for the two bugs I fixed. Finally, I ran pytest using the command `python -m pytest tests/test_game_logic.py`. I discovered that the existing test cases contained errors because they were comparing the output of the check_guess function to a string, even though the function returns a tuple. Therefore, I commented out the existing test cases and utilized AI-generated ones instead.
  
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  The value of the secret was being cast as a string during even-numbered attempts. Since the guess value was an integer and we require an integer comparison, this string casting was removed. Additionally, the output strings within the tuples were corrected for consistency. These changes were verified using newly generated test cases: test_winning_guess(), test_guess_too_high(), and test_guess_too_low().
    
- Did AI help you design or understand any tests? How?
  I used AI to generate test cases, as I had no prior knowledge of pytest. I used AI to learn about the framework and how to run the test commands. When I first executed the test files, they produced errors because the existing test cases were comparing tuples to strings. AI helped me understand these errors within the existing test code

  Note: I also used AI to change minor functionality of the game, such as disabling the difficulty selection box after a win or loss until a new game starts.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  I learned that Streamlit is a tool designed for those who want to share data science projects as web apps. It is, therefore, engineered for those who do not have knowledge of JS, HTML, and CSS, but want to quickly share their data science projects.

  Streamlit maintains persistent data in session variables; it reruns the entire program whenever a user changes the state. However, the data stored in the session variables remains unaffected by these reruns. 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  You can manage these reruns using the st.rerun() and st.stop() functions.

  st.rerun(): This is used to force an immediate restart of the script from the very top. It is useful when you change a session variable and want the UI to reflect that change instantly without waiting for the next user interaction.

  st.stop(): This does not "manage" a rerun in the sense of starting over. Instead, it halts execution immediately. Anything written in your code after st.stop() will not be executed or displayed. This is useful for stopping the app if an error occurs or after a specific condition is met (like a "Game Over" screen where you don't want the rest of the page to load).

- What change did you make that finally gave the game a stable secret number?
  The secret remains stable until the user starts a new game. The randomly generated secret is stored in the session state and is reassigned to the secret variable during every rerun. This ensures that the secret stays consistent throughout the session. When a new game is started, a new secret is generated and stored in the session
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? 
- This could be a testing habit, a prompting strategy, or a way you used Git.
  While I used AI in this project, the most critical lesson I learned is that as a developer or engineer, I must have a deep understanding of the codebase I am developing. If you rely totally on AI without understanding the logic or the code behind your application, it can be very challenging to debug and fix errors. In summary, you must be the master and use AI only as an assistant. 

- What is one thing you would do differently next time you work with AI on a coding task?
  While I believe I used AI reasonably well in this project, next time I will make sure to provide better documentation for debugging and increase the number of test cases. When it comes to version control, I should have made more frequent commits.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  AI-generated code is fairly useful; however, it is not without flaws. Your prompt is critical, and you often need more than one prompt to refine the AI-generated code. This is where your understanding of the codebase is essential.