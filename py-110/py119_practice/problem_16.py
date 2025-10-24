"""
Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters.

P:
Given a string, return the count of alphanumeric characters that appear more than once in the string, ignoring case.

Rules:
    - The input will only contain alphanumeric characters
    - Ignore case

3141592653589793
42687
 - 3
 - 1
 - 5
 - 9

2718281828459045
790
- 8
- 2
- 1
- 5
- 4


Data structures:
    - Input: string
    - Output: Integer
    - Intermediary:
        - List: 
            - Store each individual char
            - Record chars that occur more than once
        - Dictionary: Count each char, key = char, value = count
        - Set: Get all unique chars, iterate input to count occurrence of each
        - String: Version of input with chars remove as we count them

High-level strategies:
    - Create a dictionary using the lowercased input where key = char and value = count. Return the number of chars where value > 1
    - Create a list out of the input. If we find a char with a count > 1, add to a second list. Return the length of the second list

A:
    - *create_dictionary* -> output: 'char_counts'
    - Get a list of keys whose values are > 1 => 'repeating_chars'
    - Return the length of 'repeating_chars'


*create_dictionary*
Input: String
Output: Dictionary
Algo:
    - Create empty dictionary 'counts'
    - For each char in string:
        - Check if lowercase char in 'counts'
        - If not, add with value 1
        - If so, increment value
    - Return 'counts'

"""

def create_dictionary(text):
    counts = dict()
    for char in text:
        lowercase_char = char.lower()
        counts[lowercase_char] = counts.get(lowercase_char, 0) + 1
    return counts

def distinct_multiples(text):
    char_counts = create_dictionary(text)
    repeating_chars = [key for key, value in char_counts.items()
                            if value > 1]
    return len(repeating_chars)


# print(distinct_multiples('xyz'))
# print(distinct_multiples('3141592653589793'))


# Test cases
print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

"""
Reflection:
Time: 16 min 26 seconds. Straightforward.
"""