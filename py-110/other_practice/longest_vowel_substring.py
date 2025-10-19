"""
Create a function that takes a non-empty string as an argument. The string consists entirely of
lowercase alphabetic characters. The function should return the length of the longest vowel substring. 
The vowels of interest are "a", "e", "i", "o", and "u".

P:
Calculate the length of the longest substring made up entirely of vowels.

Rules:
    - The input string is non-empty
    - The input is also made up of lowercase alphabetic characters
    - Vowels consist of "a", "e", "i", "o", "u"
    - Substrings can be one or more letters
    - Substrings that count for our purposes are made up entirely of vowels
    - Substrings should maintain the order presented in the input string

Data structures:
    - Input: String
    - Output: Integer
    - Intermediary:
        - List: Store all possible substrings for the input, eventually filter to those made up entirely of vowels
        - Range: Iterate through each letter of the input using two ranges to set a start and ending index
        - Boolean: Determine whether a substring consists entirely of vowels
        - Integer: Count the number of letters in a valid substring

High-level strategies:
    - Find all substrings that consist only of vowels and store in a list. Calculate the length of the longest of those 
      substrings
    - MISSED: Iterate through the input string, recording the number of consecutive vowels as we go. Return the length of
      the longest consecutive streak.

A:
    - Create a variable 'VOWELS' with value 'aeiou'
    - Find all substrings made up of all vowels. Store substrings in a list 'valid_substrings'
        - Create a variable 'valid_substrings' with an empty list value
        - For each valid start index and ending index, create a substring from the input
        - If every character in the substring is a vowel, add it to the end of 'valid_substrings'
    - If 'valid_substrings' is empty, return 0
    - Sort 'valid_substrings' from longest to shortest length
    - Calculate the length of the longest substring and return this length

Subalgorithm: Find if every character in a substring is a vowel
Input: String
Output: Boolean
Algorithm:
    - Check each character in the input string
    - If a character is not a, e, i, o, u, return False
    - If all characters are a, e, i, o, u, return True

"""
VOWELS = 'aeiou'

def is_all_vowels(substring):
    for char in substring:
        if char not in VOWELS:
            return False
    return True

def longest_vowel_substring(string):
    valid_substrings = []
    for idx_start in range(len(string)):
        for idx_end in range(idx_start + 1, len(string) + 1):
            substring = string[idx_start:idx_end]
            if is_all_vowels(substring):
                valid_substrings.append(substring)
    
    if not valid_substrings:
        return 0
    
    valid_substrings.sort(key=len, reverse=True)
    return len(valid_substrings[0])

# Test cases
print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
