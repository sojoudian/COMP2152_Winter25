
# Lab Week 2: Periodic Table Guessing Game  

In this lab session, we will collaboratively work on the starter `main.py` file. After the lab, you are expected to complete the tasks below.

---

### **Problem Requirements**

1. **Define Elements:**  
   Create an array called `elements` that contains the names of the first 10 elements of the periodic table:  
   `["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"]`.

2. **Random Element Selection:**  
   - Use a random number generator to select a random element from the `elements` array. Save the selection in a variable called `randomElement`.  
   - Print a message such as: "A random element has been chosen."

3. **Guess the Element:**  
   - Prompt the user to guess the randomly chosen element by typing its name (e.g., "Oxygen").  
   - Compare the user's guess to `randomElement` and determine if it matches.  

4. **Provide Feedback:**  
   - If the user guesses correctly, print: "Correct! The element was {randomElement}."  
   - If the user guesses incorrectly, print: "Wrong! The correct element was {randomElement}."

5. **Optional Challenges:**  
   - If the user's guess is partially correct (e.g., different casing or extra spaces), strip unnecessary spaces and ignore case when comparing.  
   - After revealing the correct answer, print an additional message about the element. For example:  
     - "Hydrogen is the lightest element in the universe."  
     - "Helium is commonly used in balloons."  

6. **Enhance User Interaction:**  
   - Allow the user to guess up to 3 times. If the user still fails after 3 attempts, reveal the correct element and end the program.  
   - After each incorrect guess, print a hint such as: "Try again! The element starts with '{first_letter}'."  

7. **Input Validation:**  
   - Ensure the user's input is a string. If it’s not valid (e.g., an empty input or a number), print an error message and prompt them again.  

---

**Starter Code (main.py):**

```python

# Define the elements array

# Randomly select an element

# Prompt the user to guess (to be completed)

# Compare guess to the random element (to be completed)
```

---

**Lab Session Goals:**  
- Understand the use of arrays for storing and accessing data.  
- Practice conditionals for comparing user input with predefined values.  
- Work with string manipulation to handle case-insensitive comparisons.  

**Post-Lab Tasks:**  
- Complete the enhancements to the program as described above.  
- Test your program with different inputs to ensure all conditions are met.  

---

This problem introduces core programming concepts like arrays, user input, conditionals, and string manipulation while adding an educational twist about chemistry elements.
