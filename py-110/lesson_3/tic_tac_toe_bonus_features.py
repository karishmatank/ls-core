import random
import os
import pdb

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN = 5
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]
]

def prompt(message):
    print(f"==> {message}")

def display_board(board):
    os.system('clear')
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")

    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(lst, delimiter=", ", before_last_element="or"):
    string_output = ""
    before_last_element += " "

    if len(lst) == 1:
        return str(lst[0])
    elif len(lst) == 2:
        string_output = f"{lst[0]} {before_last_element}{lst[1]}"
    else:
        for idx, element in enumerate(lst):
            string_output += str(element)
            if idx != len(lst) - 1:
                string_output += delimiter
            if idx == len(lst) - 2:
                string_output += before_last_element
    
    return string_output

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break
        else:
            prompt("Sorry, that's not a valid choice.")
    
    board[int(square)] = HUMAN_MARKER


def detect_threat_or_opportunity(board):
    """If any two squares in a winning line have the human marker while the other is a space,
       then return the index of the empty space. Otherwise, return None"""
    
    for line in WINNING_LINES:
        existing_choices = [board[idx] for idx in line]

        # If there are two human markers, go on defense
        # Else, if there are two computer markers, go on offense

        # If the computer can go on offense, even if there is a row where it plays defense, it should play offense first
        # Therefore, I put the offense 'and' expression first to short circuit
        if ((existing_choices.count(COMPUTER_MARKER) == 2 and existing_choices.count(INITIAL_MARKER) == 1) or
            (existing_choices.count(HUMAN_MARKER) == 2 and existing_choices.count(INITIAL_MARKER) == 1)):
            # Find the index of the square that is the empty space
            return line[existing_choices.index(INITIAL_MARKER)]
        
    return None

def is_threat(board):
    return bool(detect_threat_or_opportunity(board))

def computer_chooses_square(board):
    if board_full(board):
        return
        
    if is_threat(board):
        # Pick square based on where we see 2 human markers in a winning line
        square = detect_threat_or_opportunity(board)
    elif board[5] == INITIAL_MARKER:
        # Choose square 5 (center) if available
        square = 5
    else:
        square = random.choice(empty_squares(board))
    
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return "Player"
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return "Computer"
    
    return None

def someone_won(board):
    return bool(detect_winner(board))

def choose_first_player():
    # Ask the user to choose who goes first
    while True:
        prompt("Who should go first? Pick between 'player', 'computer', or 'choose': ")
        choice = input().lower().strip()
        if choice in ['player', 'computer', 'choose']:
            break
        prompt("Hmm, that's not a valid choice. Try again!")
    
    if choice == 'choose':
        choice = random.choice(['player', 'computer'])
    
    return choice

def choose_square(board, current_player):
    if current_player == 'player':
        player_chooses_square(board)
    else:
        computer_chooses_square(board)

def alternate_player(current_player):
    if current_player == 'player':
        return 'computer'
    else:
        return 'player'

def play_one_game(board, current_player):
    while True:
        display_board(board)
        choose_square(board, current_player)
        current_player = alternate_player(current_player)
        if someone_won(board) or board_full(board):
            break
    
    display_board(board)

    if someone_won(board):
        prompt(f"{detect_winner(board)} won!")
    else:
        prompt("It's a tie!")

    return detect_winner(board)


def play_again():
    while True:
        prompt("Play again? ('y' or 'n')")
        answer = input().lower().strip()
        if answer in ['y', 'n']:
            break
        prompt("Please enter 'y' or 'n'. ")
    
    return answer == 'y'

def play_tic_tac_toe():
    while True:
        player_wins = 0
        computer_wins = 0

        # Prompt the user for who should go first
        current_player = choose_first_player()

        while (player_wins < GAMES_TO_WIN) and (computer_wins < GAMES_TO_WIN):
            board = initialize_board()
            winner = play_one_game(board, current_player)
            if winner == 'Player':
                player_wins += 1
            elif winner == 'Computer':
                computer_wins += 1

            prompt(f"Player has won {player_wins} time(s), computer has won {computer_wins} time(s).")
        
        if not play_again():
            break
    
    prompt("Thanks for playing Tic Tac Toe!")

play_tic_tac_toe()