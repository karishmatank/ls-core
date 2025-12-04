"""
Write a program that can generate the lyrics of the 99 Bottles of Beer song. See the test suite for the entire song.

P:
Given up to two non-negative integer inputs representing starting and ending verse, generate the lyrics for the verses requested.

Rules:
    - If there is one integer input, generate the verse for that number of bottles on the wall
    - If there are two integer inputs, they'll be presented in decreasing order i.e (99, 98) or (2, 0)
    - We should create a class called BeerSong with a few class methods:
        - `verse` -> accepts one integer input
        - `verses` -> accepts two integer inputs
        - `lyrics` -> recites the entire song
    - Tenses in lyrics should change depending on input integer(s)
        - 0 => "No more bottles of beer" + second line says "Go to the store and buy some more", before going back to 99
        - 1 => 1 *bottle* of beer

E:

D:
    Input: 1-2 integers, or none for `lyrics`
    Output: String
    Intermediary:
        - Range: Keep track of which verse numbers we need to print based on inputs
        - List: Store verse lines

High-level strategies:
    - For each verse we need to print, generate lines, keeping in mind changes in tense / lyrics based on verse number. Combine
      verse into one string and return.

A:
    - Constructor (__init__)
        - Create range of verse numbers based on inputs `start` and `end` => instance var `verse_nums`
    - `_generate_verse` instance method
        - Set 'verse_txt' to empty string
        - Start with generate first line of verse
        - if number is 0
            - First line is "No more bottles of beer on the wall, no more bottles of beer.\n"
        - else
            - Set "plural" to False if number is 1, True otherwise
            - Set line text based on verse number + plural
        - Add first line to end of 'verse_txt'

        - Move onto second line of verse
        - Set 'next_num' to result of (verse number - 1) mod 100
        - if next_num is 99
            - Add "Go to the store and buy some more, " to end of 'verse_txt'
        - else
            - Add "Take one down and pass it around, " to end of 'verse_txt'
        
        - if next_num is 0
            - Add "no more bottles of beer on the wall." to end of 'verse_txt'
        - else
            - Add end of second line based on verse number + plural
        - Return 'verse_txt'
    - `verse` class method
        - Input: Integer
        - Algo:
            - Instantiate instance of class, pass in input twice
            -  *_generate_verses*
    - `verses` class method
        - Algo:
            - Instantiate instance of class, pass in both inputs
            - *_generate_verses*
    - `lyrics` class method
        - Algo:
            - Instantiate instance of class, pass in inputs 99 and 0
            - *_generate_verses*

EDIT: A was taking too long, I got frustrated and looked at the hints to then create a Verse class, see code below.
"""

class Verse:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def _is_plural(num):
        return num != 1
    
    def generate(self):
        verse_txt = ""

        # First line
        if self.number == 0:
            first_line = "No more bottles of beer on the wall, no more bottles of beer.\n"
        else:
            add_plural = 's' if self.__class__._is_plural(self.number) else ''
            first_line = (
                f"{self.number} bottle{add_plural} " 
                f"of beer on the wall, {self.number} bottle{add_plural} of beer.\n"
            )
        verse_txt += first_line

        # Second line
        next_num = (self.number - 1) % 100
        if next_num == 99:
            second_line = "Go to the store and buy some more, "
        elif next_num == 0:
            second_line = "Take it down and pass it around, "
        else:
            second_line = "Take one down and pass it around, "
        
        if next_num == 0:
            second_line += "no more bottles of beer on the wall."
        else:
            add_plural = 's' if self.__class__._is_plural(next_num) else ''
            second_line += f"{next_num} bottle{add_plural} of beer on the wall."
        
        verse_txt += second_line + "\n"
        
        return verse_txt


class BeerSong:
    def __init__(self, start, end):
        self.verse_nums = range(start, end - 1, -1)

    @classmethod
    def verse(cls, num):
        return Verse(num).generate()
    
    def _generate_verses(self):
        verses = []
        for verse_num in self.verse_nums:
            verses.append(Verse(verse_num).generate())
        
        return "\n".join(verses)

    @classmethod
    def verses(cls, start=99, end=0):
        song = cls(start, end)
        return song._generate_verses()

    @classmethod
    def lyrics(cls):
        return cls.verses()
