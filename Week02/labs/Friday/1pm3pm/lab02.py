import random
from random import choice

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"]
print(elements)


randomElement = random.choice(elements)

attempts = 3

for attempt in range(attempts):
    guess = input(f"Attempt {attempt + 1}/{attempts}: Guess the element: ").strip()
    if guess.lower() == randomElement.lower():
        print(f"Correct! the element was {randomElement}.")
    else:
        if attempt < attempts - 1:
                        print(f"Wrong! Hint: The element starts with '{randomElement[0]}'. Try again!")
        else:
            print(f"Wrong guess! The element was {randomElement}")    