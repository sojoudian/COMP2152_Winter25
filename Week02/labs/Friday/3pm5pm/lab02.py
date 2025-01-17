

# Define the choices array
choices = ["Rock", "paper", "Scissors"]


def main():
    try:
        user_input = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

        # Validate the user input
        if user_input not in choices:
            raise ValueError("Invalid choice!, Please enter Rock, Paper, Scissors")
        
        # Convert the user input to an index
        player_choice = choices.index(user_input)


    except:


# Run the game through the main function
if __name__ == "__main__":
    main()
