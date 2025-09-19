import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
USER_WIN_SCENARIOS = {
    # User wins with following user choice: computer choice scenarios
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"]
}

def prompt(message):
    print(f"==> {message}")

def get_user_choice():
    while True:
        choice = input()
        if choice.lower() in VALID_CHOICES:
            break
        prompt("Hmm, that's not a valid choice, please choose again!")
    return choice

def get_computer_choice():
    return random.choice(VALID_CHOICES)

def determine_winner(user, computer):
    if user == computer:
        return None
    elif computer in USER_WIN_SCENARIOS[user]:
        return "user"
    else:
        return "computer"
    
def print_winner(winner):
    if winner == "user":
        prompt("You win!")
    elif winner == "computer":
        prompt("Computer wins!")
    else:
        prompt("It's a tie.")

def play_game():
    prompt(f"Choose one- {', '.join(VALID_CHOICES)}: ")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    prompt(f"You chose {user_choice}, computer chose {computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    print_winner(winner)

while True:
    play_game()
    prompt("Play again? Y/N: ")
    if input().lower() in ['n', 'no']:
        break