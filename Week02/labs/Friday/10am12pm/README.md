
# Lab Week 3: Number Guessing Game Coding Problem  

In the lab session, we will code the starter `main.py` together. After the lab, complete the following:

---

### **Problem Requirements**

1. **Define a Target Number:**  
   - Use a random number generator to select a secret target number between 1 and 100 (inclusive).  
   - Save the target number in a variable called `targetNumber`.

2. **User Input:**  
   - Prompt the user to guess the target number.  
   - Save their guess in a variable called `userGuess`.  
   - Ensure the user's input is a valid integer.

3. **Provide Feedback:**  
   - Compare the user's guess to the target number.  
   - Print one of the following messages based on the comparison:  
     - `"Too low! Try again."` if the guess is lower than the target number.  
     - `"Too high! Try again."` if the guess is higher than the target number.  
     - `"Congratulations! You've guessed it!"` if the guess matches the target number.

4. **Loop Until Correct:**  
   - Continue prompting the user for guesses until they correctly guess the target number.  
   - Keep track of the number of attempts and display it when the user guesses correctly.

5. **Optional Challenges:**  
   - Limit the number of attempts to 10. If the user exceeds this limit without guessing correctly, print:  
     `"Game over! The target number was [targetNumber]."`  
   - Provide hints like `"You're very close!"` if the guess is within 5 numbers of the target.

6. **Input Validation:**  
   - Add error handling to ensure the user enters a valid integer.  
   - If the input is invalid, print: `"Invalid input! Please enter a number between 1 and 100."`

7. **Enhance User Interaction:**  
   - Before the game starts, ask the user if they'd like to play. Accept `"yes"` or `"no"` (case-insensitive) as responses.  
   - If the user chooses `"no"`, print: `"Maybe next time!"` and exit the program gracefully.

---

**Starter Code (main.py):**

```python

# Generate the target number

# Ask the user if they want to play

# Placeholder for user interaction (to be completed)

# Initialize variables
```

---

**Lab Session Goals:**  
- Understand loops, conditionals, and user input validation.  
- Implement feedback mechanisms to enhance interactivity.  

**Post-Lab Tasks:**  
- Add optional challenges and input validation described above.  

---

This problem builds on essential programming concepts, while providing opportunities to practice loops, conditionals, and user interaction in Python.
