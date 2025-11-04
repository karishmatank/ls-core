import random

class Card:
    
    NAMED_VALUES = {
        'Jack': 11,
        'Queen': 12,
        'King': 13,
        'Ace': 14
    }
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    @property
    def value(self):
        if isinstance(self.rank, int):
            return self.rank
        return Card.NAMED_VALUES[self.rank]
        
    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.value < other.value
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.rank == other.rank and self.suit == other.suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    def __init__(self):
        self._initialize_deck()
    
    def _initialize_deck(self):
        self._deck = [Card(rank, suit) for rank in Deck.RANKS 
                                        for suit in Deck.SUITS]
        random.shuffle(self._deck)
    
    def draw(self):
        if not self._deck:
            self._initialize_deck()
        return self._deck.pop()


class PokerHand:
    def __init__(self, deck):
        self._hand = [deck.draw() for _ in range(5)]
        self._counts = self._count_ranks()

    def print(self):
        for card in self._hand:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"
    
    def _count_suits(self):
        suits = [card.suit for card in self._hand]
        return {suit: suits.count(suit) for suit in set(suits)}
    
    def _count_ranks(self):
        ranks = [card.rank for card in self._hand]
        return {rank: ranks.count(rank) for rank in set(ranks)}

    def _is_same_suit(self):
        return len(self._count_suits()) == 1

    def _is_royal_flush(self):
        """A, K, Q, J, 10, all same suit"""
        return (min(self._hand).rank == 10 
                and max(self._hand).rank == 'Ace' 
                and self._is_straight_flush())

    def _is_straight_flush(self):
        """5 cards in consecutive order, all same suit"""
        return (self._is_straight() and self._is_flush())

    def _is_four_of_a_kind(self):
        return any([count == 4 
                    for count in self._counts.values()])

    def _is_full_house(self):
        return all([count == 2 or count == 3 
                    for count in self._counts.values()])

    def _is_flush(self):
        # By the time this is called, we'll have ruled out a royal
        # or straight flush, so we don't need to check the ranks
        return self._is_same_suit()

    def _is_straight(self):
        # We don't need to check suits, as if they had the same suit
        # we would've detected the straight flush
        return (min(self._hand).value == max(self._hand).value - 4 
                and all([count == 1 for count in self._counts.values()]))

    def _is_three_of_a_kind(self):
        return any([count == 3 
                    for count in self._counts.values()])

    def _is_two_pair(self):
        pairs = [count == 2 
                 for count in self._counts.values()]
        return sum(pairs) == 2

    def _is_pair(self):
        return any([count == 2 
                    for count in self._counts.values()])


hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")
