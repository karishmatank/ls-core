"""
Write a program that takes a word and a list of possible anagrams and selects the correct sub-list that 
contains the anagrams of the word.

For example, given the word "listen" and a list of candidates like "enlists", "google", "inlets", and "banana", 
the program should return a list containing "inlets". Please read the test suite for the exact rules of anagrams.
"""

"""
P:
Given a word and a list of words, return a sub-list of anagrams.

Rules:
    - An anagram of the input word is a string in the list that has the same letters and frequency of letters as the input
      word
    - We should create a class called Anagram whose constructor takes in a string and who has an instance method `match`
      that takes in the list of strings
    - Anagrams are case-insensitive
    - Repeats of the word itself do not count as anagrams!

E:
diaper vs ["hello", "world", "zombies", "pants"] => No anagrams
ant vs ["tan", "stand", "at"] => "tan" is the only anagram
corn vs ["corn", "dark", "Corn", "rank", "CORN", "cron", "park"] => "corn", "Corn", "CORN" do not count!, cron only

D:
    Input: Word, list of words
    Output: List
    Intermediary:
        - String: Sorted strings to detect anagrams
        - Dictionary: Count frequency of each letter in a word, compare to input word's dict

High-level strategies:
    - For each word in the list, if case-insensitive word is not identical to case-insensitive input word, check if they 
      are anagrams by using sorted strings. If so, add word to a sub-list and return sub-list

A:
    - Constructor (__init__)
        - Set instance variable `word` to value of argument
    - `match` method
        - Set "sorted_word" to sorted list of chars in self.word, all lower
        - For each candidate in input list
            - Move to next word if self.word matches candidate exactly (case-insensitive)
            - Sort + lowercase => "sorted_candidate" (list of chars)
            - Create new list of all candidates where "sorted_candidate" = "sorted_word"
        - Return sub-list
"""

class Anagram:
    def __init__(self, word):
        self.word = word

    def _is_anagram(self, candidate):
        lower_word = self.word.lower()
        lower_candidate = candidate.lower()

        if lower_word == lower_candidate:
            return False
        
        sorted_word = sorted(lower_word)
        sorted_candidate = sorted(lower_candidate)
        return sorted_word == sorted_candidate
    
    def match(self, words):
        return list(filter(self._is_anagram, words))