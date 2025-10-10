"""
Problem:
Build a single player Tic Tac Toe game where a user can play against a computer.

P:
Input: 
    - User will input their square choices along the way + whether they want to keep playing
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
        - The player will input X for their choice, and the computer will input O
        - The game will continue as long as there is no winner yet and there are still empty squares on the board
        - A player can't target a square that's already been filled
        - The game will end immediately when either the player or computer wins
        - Board resets when we start a new game

E:
- Don't have test cases yet

D:
We'll likely want to use lists, as we want to maintain order but preserve mutability for when a user selects a square
We'll have nested lists, where we'll have an outer list representing the entire board, and then 3 nested lists representing
each row of the board. Each element of the nested list represents each of the 3 columns that intersect with that row.

A (adapted from what the assignment gave):
    1. Display the empty initial 3x3 board
    2. Ask the user to mark a square on the board
    3. The computer will subsequently mark a different square on the board
    4. Display the updated board
    5. If there is a winner, display the winner
    6. If the board is full, display a tie
    7. If there is no winner and the board is not full, go back to step 2
    8. Ask the user if they want to play again.
    9. If they do, go back to step 1
    10. Return

    

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
Data structures: We'll use nested lists   
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
Input: An integer representing a space on the board
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
    - Get available indices
    - Display the available indices
    - Prompt the user to choose an index
    - If the choice is invalid (out of bounds or square not available), prompt them again
    - Record the user's choice in the board using an X
    - Get choice from computer, record choice using an O
        - Computer should choose randomly from a given list of available indices

Subprocess 2a: Get available indices
Input: None
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



"""

import random

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


def prompt(message):
    return f"==> {message}"

def initialize_board():
    return ['', '', '', '', '', '', '', '', '']

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

def get_available_indices():
    return [idx for idx, value in enumerate(board) if value == '']

def display_available_indices(index_list):
    for idx in index_list:
        print(f"{idx}: {SQUARE_DESCRIPTIONS[idx]}")

def player_choose_square():
    available_indices = get_available_indices()
    display_available_indices(available_indices)

    while True:
        user_choice = input(prompt("Choose a square: "))
        try:
            user_choice = int(user_choice)
            if user_choice in available_indices:
                break
            print(prompt("Hmm, that's not an available choice. Try again!"))
        except ValueError:
            print(prompt("Hmm, that choice isn't an integer. Try again!"))

    board[user_choice] = 'X'

def computer_choose_square():
    available_indices = get_available_indices()
    computer_choice = random.choice(available_indices)
    board[computer_choice] = 'O'

    

board = initialize_board()
display_board(board)
player_choose_square()
print(get_available_indices())