"""
Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase alphabetic characters. The function should return the length of the longest vowel substring. The vowels of interest are "a", "e", "i", "o", and "u".

P:
Given a string, return the length of the "longest vowel substring", which is any substring of length 1 or greater made up entirely of vowels.

Rules:
    - Input is non-empty and entirely lowercase alphabetic characters
    - A substring is of length 1 or greater
    - Vowels are a, e, i, o, u
    - Substring means consecutive characters, maintaining order from original string

'launchschoolstudents'
- 'au'
- 'oo'
- 'u'
- 'e' => Longest is 2

Data structures:
    - Input: string
    - Output: integer
    - Intermediary:
        - Strings: Keep track of current longest substring as we iterate through characters
        - Range: Iterate through characters
        - List: List of all substrings
        - Boolean: Is a substring made up entirely of vowels? Yes/no
        - Integer: Keep track of both current and longest substring length

High-level strategies:
    - Iterate through each character. If character is a vowel, add 1 to a counter. If character is not vowel, if latest substring length is longest so far, record as such. Return length of that longest substring
    - Create a list of all substrings. Count substrings that are made up entirely of vowels. Return the count
    - Replace non-vowel characters with spaces. Split the remaining string into substrings, separated by one or more spaces. Count the number of substrings

A:
    - Set variable 'VOWELS' to 'aeiou'
    - Set variable 'longest_len' to 0
    - Set variable 'current_len' to 0
    - For each character in input string:
        - If character is a vowel, increment 'current_len' by 1
        - If character is a consonant:
            - Set 'longest_len' to the larger of 'longest_len' and 'current_len'
            - Reset 'current_len' to 0
    - Set 'longest_len' to the larger of 'longest_len' and 'current_len'
    - Return 'longest_len'

"""

VOWELS = 'aeiou'

def longest_vowel_substring(string):
    longest_len = 0
    current_len = 0
    for char in string:
        if char in VOWELS:
            current_len += 1
        else:
            longest_len = max(longest_len, current_len)
            current_len = 0
    longest_len = max(longest_len, current_len)
    return longest_len


# Test cases
print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)


"""
Reflection: 15 min 57 seconds. Went very smoothly. Liked the multiple ideas I had. 
Could have also moved the max() logic out of the if-else and reassigned `longest_len` after every iteration of the loop,
instead of only when we reach a consonant. That would avoid us from having to use max() outside of the for loop altogether
i.e.:

VOWELS = 'aeiou'

def longest_vowel_substring_alt(string):
    longest_len = 0
    current_len = 0
    for char in string:
        if char in VOWELS:
            current_len += 1
        else:
            # When a consonant is found, reset the current count
            current_len = 0

        # After every character, check if the current streak is the new max
        longest_len = max(longest_len, current_len)

    return longest_len
"""