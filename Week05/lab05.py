# Question 1: Prompt the user for a Hero's name (in two words) and validate input.
while True:
    hero_input = input("Enter your Hero's name (in two words): ").strip()
    
    if condition:
        
        # Create short_name: first two characters of the first word and first character of the second word.
        
        break
    else:
        print("Invalid input. Please enter exactly two words using only letters.")

# Question 2: Display the hero's stars using short_name.
stars_display = "***"  # Example stars display


# Import the required functions from functions_lab05.py.
from functions_lab05 import collect_loot, use_loot

# Question 3: Collect loot by calling the collect_loot() function.
belt = []
loot_options = ["Health Potion", "Poison Potion", "Leather Boots", "Gold Coin"]


# Question 4: Use loot by calling the use_loot() function.
health_points = 10  # Starting health points


# Question 5: Roll a dice to determine who strikes first.
import random


if condition:
    print("Hero attacks first!")
    # Simulate the hero attacking followed by the monster counter-attacking.
    print("Hero attacks the monster!")
    print("Monster counter-attacks!")
else:
    print("Monster attacks first!")
    # Simulate the monster attacking followed by the hero counter-attacking.
    print("Monster attacks the hero!")
    print("Hero counter-attacks!")

# Question 6: Define the inception_dream() function using recursion.
def inception_dream():
    answer = input("Do you want to dive deeper into the dream? (yes/no): ")
    if condition:
        # Recursive case: add 1 and dive deeper.
        return 1
    else:
        # Base case: return 2.
        return 2

crazy_level = inception_dream()
# After the dream, reduce health points by 1 and increase hero's combat strength by crazy_level.
health_points -= 1
hero_combat_strength = 5 + crazy_level  # Assuming a base combat strength of 5.
print("After the dream:")
print("Health Points:", health_points)
print("Hero Combat Strength:", hero_combat_strength)
