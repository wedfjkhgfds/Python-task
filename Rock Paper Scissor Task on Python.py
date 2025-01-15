import random

def get_user_choice():
    """Get the user's choice."""
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice, please choose 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Get the computer's choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Function to play the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Get user's and computer's choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        #  display the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
