"""
P:
Given a word, compute its Scrabble score.

Rules:
    - We'll be given tile scores, representing the score for each letter
    - A word's score is the sum of each letter's score (tile score)
    - An empty string or None means a score of 0
    - Ignore any non-alpha characters
    - Treat strings as case-insensitive => A and a have same score
    - We should be able to compute scores through initializing Scrabble instance and with score instance method
      as well as with a class method `calculate_score` that takes in an argument

E:
street => all chars have value of 1 => 1 * 6 = 6
quirky => 10 + 1 + 1 + 1 + 5 + 4 = 22

D:
    Input: string
    Output: int
    Intermediary:
        - Dict: tuple of letters as key, score as value
        - String: case-insensitive (lowercase) version of input

A:
    - Set class constant `TILE_SCORES` to dict with chars as keys, scores as values
    - Constructor (__init__)
        - Set instance var `word` to input
    - `score` instance method
        - Compute score of the word -> `calculate_score` class method
        - Return score
    - `calculate_score` class method
        Input: string
        Output: Integer
        Algo:
            - If word is not a string, return 0
            - Set `total_score` to 0
            - For each char in input
                - If char is not alphabetical, continue
                - Find value of lowercased char in `TILE_SCORES`
                - Add value to `total_score`
            - Return `total_score`

"""

class Scrabble:
    TILE_SCORES = {
        'a': 1,
        'b': 3,
        'c': 3,
        'd': 2,
        'e': 1,
        'f': 4,
        'g': 2,
        'h': 4,
        'i': 1,
        'j': 8,
        'k': 5,
        'l': 1,
        'm': 3,
        'n': 1,
        'o': 1,
        'p': 3,
        'q': 10,
        'r': 1,
        's': 1,
        't': 1,
        'u': 1,
        'v': 4,
        'w': 4,
        'x': 8,
        'y': 4,
        'z': 10
    }

    def __init__(self, word):
        self.word = word

    def score(self):
        return self.__class__.calculate_score(self.word)

    @classmethod
    def calculate_score(cls, word):
        if not isinstance(word, str):
            return 0
        
        total_score = 0
        for char in word:
            if not char.isalpha():
                continue

            total_score += cls.TILE_SCORES.get(char.lower(), 0)
        
        return total_score