import random

#define the choices array
choices = ["Rock", "Paper", "Scissors"]

def main():
    try:
        user_input = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

        # Validate user input
        if user_input not in choices:
            raise ValueError("Invalid choice! Please enter 'Rock', 'Paper, 'Scissors'")

        # Convert the user input to an index
        player_choice = choices.index(user_input)

        # Randomly select the computer choice
        computer_choice = random.randint(0,2)

        print(f"Player chose {choices[player_choice]}")    
        print(f"Computer chose {choices[computer_choice]}")    

        # Determine the winer
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 0 and computer_choice==2) or \
             (player_choice == 1 and computer_choice == 0) or \
             (player_choice == 2 and computer_choice == 1):
            print("Player wins!")
        else:
            print("Computer wins!")  
    except ValueError as e:
        print(f"Error {e}")





# Run the game
if __name__ == "__main__":
    main()