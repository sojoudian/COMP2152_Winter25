import random

#define the choices array
choices = ["Rock", "Paper", "Scissors"]

def main():
    user_input = input("Enter your choice (Rock, Paper, Scissors)").capitalize()

    # Validate user input
    if user_input not in choices:
        raise ValueError("Invalid choice! Please enter 'Rock', 'Paper, 'Scissors'")
    
    # Convert the user input to an index
    player_choice = choices.index(user_input)

    
    return True

# Run the game
if __name__ == "main":
    main()