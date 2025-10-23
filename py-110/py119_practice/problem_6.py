"""
Create a function that takes a string argument and returns a dict object in which the keys represent the lowercase letters in the string, and the values represent how often the corresponding letter occurs in the string.

P:
Given a list, create a dictionary with lowercase keys as characters and values as counts.

Rules:
    - Keys are lowercase letters in the string
    - Values are their counts, how often they occur
    - Only include alphabetical characters
    - Ignore uppercase characters as well
    - Empty input = empty output dict

Data structures:
    - Input: string
    - Output: dictionary
    - Intermediary:
        - [ ]

High-level strategies:
    - Iterate through the characters. If a lowercase characters is not in the dict, add it. Increment a character's value by 1 whenever we see it. Return the dictionary
    - Create a list of only lowercase characters from the string. Create a dictionary of counts using this list. Return the dictionary

A:
    - Create empty dict 'char_counts'
    - For each char in the input:
        - If char is not alphabetical or if not lowercase
            - Continue to next iteration
        - Check if char is in 'char_counts'. If not, add it
        - Increment char's value in 'char_counts' by 1
    - Return 'char_counts'

"""

def count_letters(text):
    char_counts = {}
    for char in text:
        if not char.isalpha() or not char.islower():
            continue
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


# Test cases
expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})

"""
Reflection:
Time: 12 min 51 seconds. Probably easier than the ones I should expect on the assessment. 
"""