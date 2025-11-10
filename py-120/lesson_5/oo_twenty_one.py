import random
import os

def clear_screen():
    os.system('clear')

class Card:
    MAX_ACE_VALUE = 11
    MIN_ACE_VALUE = 1

    FACE_CARD_VALUES = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': MAX_ACE_VALUE
    }

    def __init__(self, rank, suit):
        # What attributes does a card need? Rank? Suit?
        #   Points?
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    def value(self):
        if isinstance(self.rank, int):
            return self.rank
        
        return Card.FACE_CARD_VALUES[self.rank]
        

class Deck:
    SUITS = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    def __init__(self):
        # What attributes does a deck need? A collection of
        #   52 cards?
        # Some data structure, like a list or dictionary,
        #   might be required.
        self.reset()
        
    def reset(self):
        self.cards = [Card(rank, suit) for rank in Deck.RANKS 
                                       for suit in Deck.SUITS]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        # Does the dealer or the deck deal the cards?
        cards = []

        for _ in range(num_cards):
            card = self.cards.pop()
            cards.append(card)

        return cards

class Participant:
    MAX_HAND_VALUE = 21

    def __init__(self):
        # STUB
        # What attributes does a participant require? Score?
        #   Hand? Betting balance?
        # What else goes here? all the redundant behaviors
        #   from Player and Dealer?
        self.reset_hand()

    @property
    def hand(self):
        return self._hand
    
    @property
    def hand_value(self):
        return self._hand_value

    def hit(self, cards):
        for card in cards:
            self._hand.append(card)
            self.update_hand_value()

    def is_busted(self):
        return self.hand_value > Participant.MAX_HAND_VALUE
    
    def update_hand_value(self):
        num_aces = 0
        total_value = 0
        for card in self.hand:
            if card.rank == 'A':
                num_aces += 1
            total_value += card.value()

        for _ in range(0, num_aces):
            if total_value > Participant.MAX_HAND_VALUE:
                total_value -= (Card.MAX_ACE_VALUE - Card.MIN_ACE_VALUE)
        
        self._hand_value = total_value
    
    def reset_hand(self):
        self._hand = []
        self._hand_value = 0

class Player(Participant):
    def __init__(self):
        # STUB
        # What additional attributes might a player need?
        # Score? Hand? Amount of money available?
        super().__init__()
        self.balance = 5

    def stay(self):
        print("You chose to stay!")

    def show_cards(self):
        print(f"Player's cards are: {', '.join([str(card) for card in self.hand])}")

    def display_hand_value(self):
        print(f"Player's hand value is {self.hand_value}")
        

class Dealer(Participant):
    HIT_THRESHOLD = 17

    def __init__(self):
        # STUB
        # Very similar to a Player; do we need this?
        super().__init__()

    def stay(self):
        print("Computer chose to stay!")

    def show_cards(self):
        if self.hide_cards:
            self.hide()
        else:
            self.reveal()

    def hide(self):
        print(f"Dealer's cards are: {self.hand[0]} and unknown card")

    def reveal(self):
        print(f"Dealer's cards are: {', '.join([str(card) for card in self.hand])}")

    def display_hand_value(self):
        print(f"Dealer's hand value is {self.hand_value}")
    
    def reset_hand(self):
        super().reset_hand()
        self.hide_cards = True

    # def deal(self):
    #     # STUB
    #     # Does the dealer or the deck deal?
    #     pass

class TwentyOneGame:
    def __init__(self):
        # STUB
        # What attributes does the game need? A deck? Two
        #   participants?
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        clear_screen()
        self._display_welcome_message()

        while True:
            self._play_one_game()
            self._display_balance()
            if self.player.balance <= 0:
                self._display_broke_message()
                break

            if self.player.balance >= 10:
                self._display_rich_message()
                break

            if not self._is_continuing():
                break

        self._display_goodbye_message()

    def _display_balance(self):
        print(f"Your balance is ${self.player.balance}.")

    def _display_broke_message(self):
        print("You are broke!")

    def _display_rich_message(self):
        print("You are rich!")
    
    def _is_continuing(self):
        while True:
            play_again = input("Play again? (y/n): ").lower().strip()
            if play_again in ['y', 'n']:
                break
            print("Hmm, that's not a valid response. y/n only.")

        return play_again == 'y'

    def _play_one_game(self):
        self.reset()

        self.deal_cards()
        self.show_cards()

        self.player_turn()
        if not self.player.is_busted():
            self.dealer.hide_cards = False
            self.dealer_turn()

        print()

        winner = self._determine_winner()
        if winner:
            self._adjust_player_balance(winner)

        self._display_busted_result()
        self.display_result(winner)

    def reset(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck.reset()

    def deal_cards(self):
        """Deal two cards to each participant"""
        self.player.hit(self.deck.deal(2))
        self.dealer.hit(self.deck.deal(2))
        
    def show_cards(self):
        self.player.show_cards()
        self.dealer.show_cards()

    def player_turn(self):
        while True:
            choice = self._player_choice()
            if choice == 'stay':
                clear_screen()
                self.player.stay()
                break

            self.player.hit(self.deck.deal(1))
            clear_screen()
            self.show_cards()
            self.player.display_hand_value()

            if self.player.is_busted():
                break

    def _player_choice(self):
        while True:
            choice = input("Player choose - 'hit' or 'stay': ").lower().strip()
            if choice in ['hit', 'stay']:
                break
            print("Hmm, that's not a valid option, try again!")
        
        return choice

    def dealer_turn(self):
        while self.dealer.hand_value < Dealer.HIT_THRESHOLD:
            print("Dealer will hit.")
            self.dealer.hit(self.deck.deal(1))
            self.dealer.show_cards()
            self.dealer.display_hand_value()

    @staticmethod
    def _display_welcome_message():
        print("Welcome to Twenty-One!")
    
    @staticmethod
    def _display_goodbye_message():
        print("Thanks for playing Twenty-One!")

    def _determine_winner(self):
        if self.player.is_busted():
            return self.dealer
        
        if self.dealer.is_busted():
            return self.player
        
        # Then check for value comparisions
        if self.dealer.hand_value > self.player.hand_value:
            return self.dealer
        elif self.player.hand_value > self.dealer.hand_value:
            return self.player
        else:
            return None
    
    def _display_busted_result(self):
        if self.player.is_busted():
            print("You busted :/ Dealer wins!")
        elif self.dealer.is_busted():
            print("Dealer busted, you win!") 

    def display_result(self, winner):
        # Display hands for a final time
        self.show_cards()

        if winner == self.player:
            print("You win!")
        elif winner == self.dealer:
            print("Dealer wins!")
        else:
            print("It was a tie.")

    def _adjust_player_balance(self, winner):
        if winner == self.player:
            self.player.balance += 1
        else:
            self.player.balance -= 1
    



game = TwentyOneGame()
game.start()