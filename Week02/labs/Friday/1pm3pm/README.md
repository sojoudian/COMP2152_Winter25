
# **Lab Week 3: Animal Guessing Game**

In the lab session, we will code the starter `main.py` together. After the lab, complete the following:

---

### **Problem Requirements**

1. **Define Animal Options:**
   - Create an array called `animals` that contains the following options: `"Lion"`, `"Elephant"`, `"Dolphin"`, `"Eagle"`, `"Cheetah"`, `"Kangaroo"`.  

2. **Simulate a Guessing Round:**
   - Use a random number generator to select an animal from the array. Save the selected animal in a variable called `correctAnimal`.  
   - Allow the player to make a guess by typing the name of an animal (e.g., `"Lion"`). Save the guess in a variable called `playerGuess`.  

3. **Determine the Result:**
   - Compare the `playerGuess` to the `correctAnimal`. Print one of the following messages based on the outcome:
     - If the guess is correct: `"Congratulations! You guessed it right: It's a {correctAnimal}!"`
     - If the guess is incorrect: `"Sorry, wrong guess! The correct answer was {correctAnimal}."`  

4. **Optional Challenges:**
   - Provide a hint if the guess is incorrect, such as:
     - `"Hint: The correct animal is faster than your guess."`
     - `"Hint: The correct animal lives in the water."`  
   - Modify the program to give the player 3 chances to guess correctly. Keep track of the number of attempts using a variable `attempts`. After 3 incorrect guesses, reveal the correct animal and end the program.

5. **Input Validation:**
   - Ensure the `playerGuess` is a valid string and matches one of the animal options. If an invalid input is detected, print an error message like:
     `"Invalid input! Please guess from the following options: Lion, Elephant, Dolphin, Eagle, Cheetah, Kangaroo."`

---

**Starter Code (main.py):**

```python

# Define the animal options

# Randomly select the correct animal

# Placeholder for player's guess

# TODO: Add logic to compare playerGuess to correctAnimal

# Example of initial output
```

---

**Lab Session Goals:**
- Understand the use of string arrays and random selections.  
- Learn how to handle and compare string inputs in Python.  
- Add error handling and validate user inputs.

**Post-Lab Tasks:**
- Implement the guessing logic and optional challenges.  
- Test your program to ensure it handles various cases correctly.

---

This problem focuses on strings, arrays, conditionals, and error handling, making it suitable for exploring core programming concepts while avoiding number-based logic.
