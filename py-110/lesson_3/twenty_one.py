"""
P:
Input:
    - User will pick cards along the way
Output:
    - Output to the console on who won
Rules:
    - Explicit:
        - Start with a standard 52-card deck consisting of 4 suits (hearts, diamonds, clubs, and spades) and 13 values
          (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)
        - Get as close to the value 21 in your hand without going over
        - The game will have both a player and a dealer
        - The player and dealer are initially dealt a hand of 2 cards each, but the user can only see one of the dealer's cards
        - Card values match the numbers of the cards
            - If card is K, Q, or J, card value is 10. 
            - If card is A, card value is either 1 or 11, depending on the other cards in the hand
            - If the hand's value with the ace worth 11 exceeds 21, then the ace's value turns to 1
            - If there are multiple aces in a hand, one's value can be 11 while the other's value can be 1, etc
        - The player always goes first and can decide to either "hit" or "stay"
            - A "hit" means the player wants to be dealt another card
            - A "bust" means the player's hand exceeds the value 21 and they have lost
            - The player can "hit" as many times as they like
            - The player's turn is over when they either "bust" or "stay"
            - If the player busts, the game is over and the dealer wins
        - The dealer goes second after the player decides to end their turn and "stay"
            - The dealer will hit until the total is at least 17
            - If the dealer busts, the player wins
        - When both the dealer and player stay, the winner is the one with the higher hand value
    - Implicit
        - Decision to hit or stay is based on probability that the player will bust if they choose another card, in addition to
          what we think the dealer is likely going to have to do to try to win
        - It doesn't seem like the suit of the card matters, only the value. We'll store the suit anyway
        - Assume that the human user is the "player" whereas the computer is the "dealer"
        - Assume that there can be a tie, and notify players if that's the case

E:
    - Dealer has ace and unknown card, player has 2 and 8
        - Player should hit. Dealer has an ace, which means they have a high probability of having a 21
        - In addition, our total is currently 10, which means we can't bust with another card
    - Dealer has: 7 and unknown card, player has 10 and 7
        - Player should stay since the chances of the unknown card being an ace are low, which is the only scenario currently
          in which we lose
    - Dealer has: 5 and unknown card, player has J and 6
        - Player should stay. We have 16, so we can try to land a card less than 6, but the dealer is likely going to hit 
          and may bust

D:
    - We'll have to use two lists to store the hands of both the player and the dealer
    - We'll store the cards in a list of 52 elements, where we will remove elements (cards) that are dealt to players
        - Each element of the list will be a list itself, with the first index representing the suit and the second representing
          the value
    - We can store the values of each card in a dictionary, where they key is the card and the value is its numeric value

A:
    1. Initialize deck
    2. Deal cards to player and dealer
    3. Player turn: hit or stay
        - Repeat until bust or stay
    4. If player bust, dealer wins
    5. Dealer turn: hit or stay
        - Repeat until total >= 17
    6. If dealer busts, player wins
    7. Compare cards and declare winner


Subalgorithm 1: Initialize deck
Input: None
Output: Nested list
Algorithm:
    - Assign an empty list to a variable 'deck'
    - For each suit in 'H' (hearts), 'D' (diamonds), 'C' (clubs), 'S' (spades):
        - For each card in 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
            - Create a new list with two elements: the suit and the card
            - Add to the end of 'deck'
    - Return 'deck'

Subalgorithm 2: Deal cards to player and dealer
Input: Nested list representing the current deck, number of cards to deal, the hand that will receive the cards
Output: None, we will mutate the deck and the hand directly
Algorithm:
    - For the number of cards to deal specified:
        - Remove a card at random from the deck
        - Add that card to the hand

Subalgorithm 3: Player turn
Input: 
    - Player hand
    - Dealer hand
    - Current deck
Output: 
    - None
Algorithm:
    - While the user wants to keep playing:
        - Display the user's current hand
        - Display one of the dealer's cards. We will always show the first card (card at index 0)
        - Ask the user what they want to do. Either "hit" or "stay"
            - Basic input validation to make sure they chose one of the two options
        - If they "stay", break out of the loop
        - Deal the user another card
        - If user has busted (value of hand > 21), break out of the loop

Subalgorithm 4: Calculate if a user has busted
Input:
    - Hand of player or dealer, depending on whose turn it is
Output:
    - Boolean (True or False)
Algorithm:
    - Calculate the value of the hand (see next subalgorithm)
    - If the hand value exceeds 21, return True
    - Return False

Subalgorithm 5: Calculate the value of a hand
Input: Hand of the player or dealer, depending on whose turn it is
Output: Integer
Algorithm:
    - Assign a variable 'num_aces' to 0. We'll use this to count the aces that we come across
    - Assign a variable 'total_value' to 0
    - For each card:
        - If the card is an ace, increment 'num_aces' and continue to the next card
        - Get the value from the VALUES dictionary, which has its keys as the card values and values as the numeric
            value of the card
        - Increment 'total_value' by the value of the card
    - For a range starting at 0 and ending at num_aces:
        - If we add 11 to 'total_value' and 'total_value' doesn't go over 21
            - Increment 'total_value' by 11
        - Else
            - Increment 'total_value' by 1
    - Return 'total_value'

Subalgorithm 6: Dealer turn
Input: 
    - Dealer hand
    - Current deck
Output: 
    - None
Algorithm:
    - While the dealer wants to keep playing:
        - If the dealer's hand value < 17
            - Deal the user another card
        - Else
            - break out of the loop

"""

import random

SUITS = ['H', 'D', 'C', 'S']
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': [11, 1]
}
VALUE_MAX = 21
DEALER_HIT_THRESHOLD = 17

def join_and(lst, delimiter=", ", before_last_element="and"):
    string_output = ""
    before_last_element += " "

    if len(lst) == 1:
        string_output = str(lst[0])
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

def card_values_only(hand):
    return [card[1] for card in hand]

def prompt(message):
    print(f"==> {message}")

def initialize_deck():
    return [[suit, card] for suit in SUITS for card in CARDS]

def deal_cards(deck, hand, num_cards):
    for _ in range(0, num_cards):
        card = deck.pop(random.randint(0, len(deck) - 1))
        hand.append(card)

def calculate_hand_value(hand):
    num_aces = 0
    total_value = 0
    for val in [card[1] for card in hand]:
        if val == 'A':
            num_aces += 1
            continue
        total_value += CARD_VALUES[val]
    for _ in range(0, num_aces):
        if (total_value + max(CARD_VALUES['A'])) > VALUE_MAX:
            total_value += min(CARD_VALUES['A'])
        else:
            total_value += max(CARD_VALUES['A'])
    return total_value

def busted(hand):
    return calculate_hand_value(hand) > VALUE_MAX

def player_turn(deck, player_hand, dealer_hand):
    while True:
        # Display user's hand and one of dealer's cards
        prompt(f"Your cards are: {join_and(card_values_only(player_hand))}")
        prompt(f"The dealer's cards are: {dealer_hand[0][1]} and unknown card")

        while True:
            prompt("Player choose - 'hit' or 'stay': ")
            choice = input().lower().strip()
            if choice in ['hit', 'stay']:
                break
            prompt("Hmm, that's not a valid option, try again!")

        if choice == 'stay':
            prompt("You chose to stay!")
            break

        deal_cards(deck, player_hand, 1)

        if busted(player_hand):
            break

def dealer_turn(deck, dealer_hand):
    prompt(f"The dealer's cards are: {join_and(card_values_only(dealer_hand))}")
    # Dealer plays until their card value is > DEALER_HIT_THRESHOLD
    while calculate_hand_value(dealer_hand) < DEALER_HIT_THRESHOLD:
        prompt("Dealer will hit.")
        deal_cards(deck, dealer_hand, 1)
        prompt(f"The dealer's cards are now: {join_and(card_values_only(dealer_hand))}")

def play_game():
    deck = initialize_deck()

    player_hand = []
    dealer_hand = []

    deal_cards(deck, player_hand, 2)
    deal_cards(deck, dealer_hand, 2)

    player_turn(deck, player_hand, dealer_hand)
    prompt(f"Your hand is now {join_and(card_values_only(player_hand))}")
    player_total = calculate_hand_value(player_hand)
    prompt(f"Your total is {player_total}.")

    if busted(player_hand):
        prompt("Your hand is busted :(")
        return "Dealer"

    dealer_turn(deck, dealer_hand)
    prompt(f"Dealer's hand is now {join_and(card_values_only(dealer_hand))}")
    dealer_total = calculate_hand_value(dealer_hand)
    prompt(f"Dealer's total is {dealer_total}.")

    if busted(dealer_hand):
        prompt("Dealer's hand is busted :)")
        return "Player"

    if player_total > dealer_total:
        return "Player"
    if dealer_total > player_total:
        return "Dealer"
    return None

def display_result(result):
    if result:
        prompt(f"{result} wins!")
    else:
        prompt("It was a tie.")

def play_again():
    while True:
        prompt("Do you want to play again? (y or n): ")
        answer = input().lower().strip()
        if answer in ['y', 'n']:
            break
        prompt("Hmm, that wasn't a valid answer. Try again!")
    return answer == 'y'

while True:
    winner = play_game()
    display_result(winner)
    if not play_again():
        break
