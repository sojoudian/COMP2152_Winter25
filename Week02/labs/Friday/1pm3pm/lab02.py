import random

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"]
print(elements)


randomElement = round.choice(elements)

attemts = 3

for attemt in range(attemts):
    guess = input(f"Attempt {attemt + 1}/{attemts}: Guess the element: 
                  ").strip()
    if guess.lower() == randomElement.lower():
        print(f"Correct! the element was {randomElement}.")