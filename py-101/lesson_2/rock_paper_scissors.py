import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
ABBREVIATIONS = [i[0] if i[0] != 's' else i[:2] for i in VALID_CHOICES]
USER_WIN_SCENARIOS = {
    # User wins with following user choice: computer choice scenarios
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"]
}
MAX_WINS = 3

def prompt(message):
    print(f"==> {message}")

def get_user_choice():
    while True:
        choice = input().lower().strip()
        if choice in VALID_CHOICES:
            break

        # Check if user used an abbreviation
        if choice in ABBREVIATIONS:
            # Transform user choice into full string
            choice = VALID_CHOICES[ABBREVIATIONS.index(choice.lower())]
            break

        prompt("Hmm, that's not a valid choice, please choose again!")
    return choice

def get_computer_choice():
    return random.choice(VALID_CHOICES)

def determine_winner(user, computer):
    if user == computer:
        return None
    if computer in USER_WIN_SCENARIOS[user]:
        return "user"
    return "computer"

def print_round_winner(winner):
    if winner == "user":
        prompt("You win this round!")
    elif winner == "computer":
        prompt("Computer wins this round!")
    else:
        prompt("This round is a tie.")

def print_game_winner(user, computer):
    if user > computer:
        prompt("You win the game!!!")
    elif user < computer:
        prompt("Computer wins the game!!!")
    else:
        prompt("Something went wrong.")

def print_score(user, computer):
    prompt(f"User has {user} wins, computer has {computer} wins.")

def play_game():
    user_wins = 0
    computer_wins = 0

    prompt("We're playing best to 5, let's start!")

    while user_wins < MAX_WINS and computer_wins < MAX_WINS:
        prompt(f"Choose one- {', '.join(VALID_CHOICES)}\n" +
            f"    You may also abbreviate to {', '.join(ABBREVIATIONS)}: ")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        prompt(f"You chose {user_choice}, computer chose {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        print_round_winner(winner)

        if winner == 'user':
            user_wins += 1
        elif winner == 'computer':
            computer_wins += 1

        print_score(user_wins, computer_wins)

    print_game_winner(user_wins, computer_wins)

while True:
    play_game()
    prompt("Play again? Y/N: ")
    if input().lower() in ['n', 'no']:
        break