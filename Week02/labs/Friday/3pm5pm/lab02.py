import random

# Define the choices array
choices = ["Rock", "Paper", "Scissors"]


def main():
    try:
        user_input = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

        # Validate the user input
        if user_input not in choices:
            raise ValueError("Invalid choice!, Please enter Rock, Paper, Scissors")
        
        # Convert the user input to an index
        playerChoice = choices.index(user_input)

        computerChoice = random.randint(0, 2)

        print(f"Player choice {choices[playerChoice]}")
        print(f"Computer choice {choices[computerChoice]}")


        # Determine the winer
        #Atklass: UFNA
        if playerChoice == computerChoice:
            print("It's a tie!")
        elif (playerChoice == 0 and computerChoice == 2) or \
            (playerChoice == 1 and computerChoice == 0) or \
            (playerChoice == 2 and computerChoice == 1):
            print("Player wins")
        else:
            print("Computer wins!")
    except ValueError as e:
        print(f"Error {e}")


# Run the game through the main function
if __name__ == "__main__":
    main()
