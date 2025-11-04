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
        self._cards = [Card(rank, suit) for rank in Deck.RANKS 
                                        for suit in Deck.SUITS]
        random.shuffle(self._cards)
    
    def draw(self):
        if not self._cards:
            self._initialize_deck()
        return self._cards.pop()

deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).