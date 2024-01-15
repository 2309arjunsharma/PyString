import random

def basic_ai(player_choice):
    choices = ['rock', 'paper', 'scissors']

    # AI makes a random choice
    ai_choice = random.choice(choices)

    # Determine the winner
    winner = determine_winner(player_choice, ai_choice)

    # Display the choices and winner
    print(f"Player choice: {player_choice}")
    print(f"AI choice: {ai_choice}")
    print(f"Winner: {winner}")

def determine_winner(player_choice, ai_choice):
    # Define the rules
    rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

    if player_choice == ai_choice:
        return "It's a tie!"
    elif rules[player_choice] == ai_choice:
        return "Player wins!"
    else:
        return "AI wins!"

# Main game loop
while True:
    # Get player input
    player_input = input("Enter your choice (rock/paper/scissors) or 'exit' to quit: ").lower()

    # Check if the player wants to exit
    if player_input == 'exit':
        break

    # Check if the player's input is valid
    if player_input in ['rock', 'paper', 'scissors']:
        # Call the AI function
        basic_ai(player_input)
    else:
        print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'exit'.")
