import random

# Function to determine the winner
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    choices = ["rock", "paper", "scissors"]
    while True:
        player_choice = input("Choose your weapon (rock/paper/scissors): ").lower()
        if player_choice in choices:
            break
        else:
            print("Invalid choice. Please try again.")

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}\n")

    result = get_winner(player_choice, computer_choice)
    print(result)

# Start the game
play_game()
