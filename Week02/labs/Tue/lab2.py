import random

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
print("Elements: ", elements)
#  git add . && git commit -m "add elements array" && git push

# def funct_name():
#     return True
# def say_greeting(name, message="hi"):
#     print(f" {message}, {name}")
# say_greeting("Maziar")
# say_greeting("Maziar", "Hello")

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer!")
            continue
try:
    elements_selected = get_valid_int_input("Enter the index of the element you like: ")
    # Roll dice
    elementRoll = random.randint(1, 6)
    totalNum = elements_selected + elementRoll

    # Print the result based on the totalNum
    if elementRoll <= 2:
        print("You rolled a weak element, friend.")
    elif elementRoll <= 4:
        print("Yor element is moderate.")
    else:
        print("Nice element.")
except IndexError:
    print("Error: Invalid element index!")        
except Exception as e:
    print(f"An unexpected error occurred: {e}")    