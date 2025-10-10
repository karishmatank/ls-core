"""
Problem:
Build a single player Tic Tac Toe game where a user can play against a computer.

P:
Input: 
    - User will input their square choices along the way
    - User will decide whether they want to keep playing
    - Computer will have input as well on computer-made decisions
Output:
    - Board printed to the console
    - Winner or tie decision printed to the console
Rules:
    - Explicit:
        - Tic Tac Toe is to be played on a 3x3 grid
        - Each player will take turns and mark a square on the board
        - The first player to get 3 squares in a row, whether horizontally, vertically, or diagonally, wins
        - If all 9 squares are filled and neither player has 3 in a row, the game ends in a tie
    - Implicit:
        - The player's choices will be denoted with an X, and the computer's choices will be denoted with O
        - The game will continue as long as there is no winner yet and there are still empty squares on the board
        - A player can't target a square that's already been filled
        - The game will end immediately when either the player or computer wins
        - Board resets when we start a new game

E:
- Don't have test cases yet

D:
We'll likely want to use lists, as we want to maintain order but preserve mutability for when a user selects a square
- Idea 1: We'll have nested lists, where we'll have an outer list representing the entire board, and then 3 nested lists 
  representing each row of the board. Each element of the nested list represents each of the 3 columns that intersect with that row.
- Idea 2: Just use one long list of 9 elements, which we'll split up before we display the board. The split will only be for
  display purposes, whereas we'll use the 9-element list while updating the board

We can also use a dictionary to store descriptors for the squares, such that users can choose the square that they want to based
on our descriptor (i.e. "top left", "bottom right", etc)

A (adapted from what the assignment gave):
    1. Display the empty initial 3x3 board
    2. Ask the user to mark a square on the board
    3. Check if the user won. If so:
        a. Display the updated board
        b. Display the user as the winner
        c. Go to step 9
    4. Check if the board is full after the user's move. If so, display a tie.
    5. The computer will subsequently mark a different square on the board
    6. Check if the computer won. If so:
        a. Display the updated board
        b. Display the user as the winner
        c. Go to step 9
    7. Display the updated board
    8. If the board is full, display a tie
    9. If there is no winner and the board is not full, go back to step 2
    10. Ask the user if they want to play again.
    11. If they do, go back to step 1
    12. Return

    

Subprocess 1: Display the board
Input: Any squares that have been selected and by who (in other words, the current board) in the form of a list
Output: Print the board to the console
Rules:
    - Explicit
        - We'll take in information related to who has selected which square of the board
        - We'll output the formatted board
    - Implicit
        - Empty squares will be represented using a single space character
        - Squares that the user has selected will be represented with the string 'X'
        - Squares that the computer has selected will be represented with the string 'O'
        - Each row will be printed on its own line, with 3 rows printed in succession
        - Output will be formatted such that columns across rows line up neatly
Data structures: We'll use nested lists, where we will split the input list into 3 equally sized sublists   
Algorithm:
    - Split the board into 3 rows, each row with 3 elements
    - For each row in the board provided:
        - Print each element, with a space before, a space after, and each element separated by a | character
        - If we just printed the first or second row, print a series of dashes to signal a new row below
    - Return

Subprocess 1a: Initialize the board
Input: None
Output: A list representing the components of an empty board
Algorithm:
    - Create a list of 9 elements, all empty strings
    - Return list

    

Subprocess 2: Player and computer turn
Input: The current board
Output: None
Rules:
    - Explicit
        - We need to ask the human player to choose an available square on the board
        - The computer will choose an available square on the board thereafter
    - Implicit
        - A user or computer can only select from available squares
        - The program should output a list of available indices for the user to choose from,
          alongside a visual representation of which indices correspond to which squares 
        - If the user chooses an invalid index, they will be reprompted to choose again
        - Valid indices range from 0 to 8 inclusive
Algorithm:
    - Display current board
    - Get choice from user
    - Get choice from computer

Subprocess 2a: Get available indices
Input: The current board
Output: List of integers representing indices
Algorithm:
    - Check the board for which elements are not already equal to 'X' or 'O'
    - Return a list of indices based on the elements identified in the prior step

Subprocess 2b: Display the available indices
Input: List of available indices
Output: Text to the console
Algorithm:
    - Assign a global variable to a dictionary that links each index as a key to a descriptor message as a value
    - For each index in the available_indices, print the index followed by the descriptor. 
    - Return

Subprocess 2c: Get choice from user
Input: The current board
Output: None, mutate board to reflect user's choice
Algorithm:
    - Get available indices
    - Display the available indices
    - Prompt the user to choose an index
    - If the choice is invalid (out of bounds or square not available), prompt them again
    - Record the user's choice in the board using an X

Subprocess 2d: Get choice from computer
Input: The current board
Output: None, mutate board to reflect computer's choice
Algorithm:
    - Get available indices
    - Computer picks at random from the available indices
    - Record the computer's choice in the board using an O



Subprocess 3: Determine if there is a winner
Input: The current board
Output: A string detailing the winner
Rules:
    - Explicit
        - If the user wins, return a string 'user'
        - If the computer wins, return a string 'computer'
        - If there is not yet a winner, return an empty string
    - Implicit
        - A user wins if there are 3 Xs in a row, column, or diagonally
        - A computer wins if there are 3 Os in a row, column or diagonally
        - Row win means 3 Xs or Os in either (0, 1, 2), (3, 4, 5), or (6, 7, 8)
        - Column win means 3 Xs or Os in either (0, 3, 6), (1, 4, 7) or (2, 5, 8)
        - Diagonal win means 3 Xs or Os in either (0, 4, 8) or (2, 4, 6)
        - Check if the user won first, as they will go first when playing
Data structures: We can use a list of tuples perhaps, where each tuple is a combination of 3 integers as detailed above.
A:
    1. Assign a constant variable 'WINNING_COMBOS' to a list of tuples, with each tuple being a 3 integer combination of
       indexes that must match in symbol for either the user or computer to have won
    2. Check if the user won:
        a. For each combination in WINNING_COMBOS:
            i. If the board at each of the indices in the combination has a value of 'X', return the string 'user'
            ii. Otherwise keep going
    3. If the user hasn't won, check if the computer won:
        a. For each combination in  WINNING_COMBOS:
            i. If the board at each of the indices in the combination has a value of 'O', return the string 'computer'
            ii. Otherwise keep going
    4. Return an empty string as no one has won if we reach this point


"""

import random

INITIAL_MARKER = ''
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
SQUARE_DESCRIPTIONS = {
    0: "Top left",
    1: "Top middle",
    2: "Top right",
    3: "Middle left",
    4: "Center",
    5: "Middle right",
    6: "Bottom left",
    7: "Bottom middle",
    8: "Bottom right"
}
WINNING_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def prompt(message):
    return f"==> {message}"

def initialize_board():
    return [INITIAL_MARKER] * 9

def split_board(board):
    row_1 = board[:3]
    row_2 = board[3:6]
    row_3 = board[6:]
    return [row_1, row_2, row_3]

def display_board(board):
    board = split_board(board)
    for idx_row, row in enumerate(board):
        for idx, element in enumerate(row):
            print(f" {element if element else ' '} {'|' if idx != 2 else ''}", end='')

        print()

        if idx_row != 2:
            print("-----------")

def get_available_indices(board):
    return [idx for idx, value in enumerate(board) if value == INITIAL_MARKER]

def display_available_indices(index_list):
    for idx in index_list:
        print(f"{idx}: {SQUARE_DESCRIPTIONS[idx]}")

def player_choose_square(board):
    available_indices = get_available_indices(board)
    display_available_indices(available_indices)

    while True:
        user_choice = input(prompt("Choose a square: ")).strip()
        try:
            user_choice = int(user_choice)
            if user_choice in available_indices:
                break
            print(prompt("Hmm, that's not an available choice. Try again!"))
        except ValueError:
            print(prompt("Hmm, that choice isn't an integer. Try again!"))

    board[user_choice] = HUMAN_MARKER

def computer_choose_square(board):
    available_indices = get_available_indices(board)
    computer_choice = random.choice(available_indices)
    board[computer_choice] = COMPUTER_MARKER

def determine_winner(board):
    for combo in WINNING_COMBOS:
        if all([board[idx] == HUMAN_MARKER for idx in combo]):
            return 'user'
    
    for combo in WINNING_COMBOS:
        if all([board[idx] == COMPUTER_MARKER for idx in combo]):
            return 'computer'
    
    return ''

def board_full(board):
    return len(get_available_indices(board)) == 0
    
def play_game():
    while True:
        board = initialize_board()
        display_board(board)

        while True:
            player_choose_square(board)
            winner = determine_winner(board)
            if winner:
                display_board(board)
                print(prompt(f"{winner.title()} wins!"))
                break
            if board_full(board):
                print(prompt("Tie."))
                break

            computer_choose_square(board)
            winner = determine_winner(board)
            if winner:
                display_board(board)
                print(prompt(f"{winner.title()} wins!"))
                break

            display_board(board)    
            if board_full(board):
                print(prompt("Tie."))
                break

        play_again = input(prompt("Play again? Y/N: "))
        if play_again.lower() != 'y':
            break

play_game()