"""
Create a function that takes a string as an argument and returns True if the string is a pangram, False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. Note that case is irrelevant.

P:
Given a string, return True if string uses every letter of the alphabet at least once.

Rules:
    - A pangram contains every letter at least once
    - Case is irrelevant - 'A' counts same as 'a'
    - Ignore non alphabetic characters

Data structures:
    - Input: string
    - Output: Boolean
    - Intermediary:
        - Set: Get all unique lowercase characters
        - Dictionary: Count number of unique characters in string
        - String: Store alphabet

High-level strategies:
    - Create a lowercase string from input without any non-alphabetic characters. If a set of these characters matches the length of the alphabet, return True
    - Create a dictionary, counting only lowercased alphabetic characters and their count. If the dictionary has every letter of the alphabet as a key, return True
    - For every lowercased alphabetic character in the input, remove matching character from alphabet. If the alphabet is an empty string, return True

A:
    - Create 'ALPHABET' as 'abcdefghijklmnopqrstuvwxyz'
    - *clean_string* => Input: input string, Output: 'cleaned'
    - Create a set of the letters in 'cleaned'
    - If length of 'cleaned' matches length of ALPHABET:
        - Return True
    - Otherwise return False


*clean_string*: Transform input into a lowercased str w/ only alphabetic characters
Input: String
Output: New string
Algo:
    - Create empty string 'cleaned'
    - For each char in input:
        - If alphabetical:
            - Turn into lowercase
            - Add to the end of 'cleaned'
    - Return 'cleaned'
"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def clean_string(string):
    cleaned = ""
    for char in string:
        if char.isalpha():
            cleaned += char.lower()
    return cleaned

def is_pangram(string):
    cleaned = clean_string(string)
    unique_chars = set(cleaned)
    return len(unique_chars) == len(ALPHABET)



# Test cases
print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard's job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard's task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard's job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

"""
Reflection: 16 min 15 seconds. Seen this one before, so went very smoothly.
"""