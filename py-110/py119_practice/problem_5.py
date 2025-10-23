"""
Create a function that takes a string argument and returns the character that occurs most often in the string. If there are multiple characters with the same greatest frequency, return the one that appears first in the string. When counting characters, consider uppercase and lowercase versions to be the same.

P:
Given a string, return the most frequent character. Return the first character that appears if multiple match the same frequency.

Rules:
    - Case-insensitive = 'A' is the same as 'a'
    - Appearing first means having a lower index value
    - Most often means highest count
    - The output character is lowercase
    - Output is alphabetical (no spaces)

E:
'Mississippi' => 4 's', 4 'i', return 'i' as it appears first

Data structures:
    - Input: string
    - Output: string (one character)
    - Intermediary:
        - Dictionary: Key is char, value is count, maintains insertion order
        - List: Get keys from dictionary sorted by value

High-level strategies:
    - Create a dictionary which keeps track of count of lowercase alphabetical characters. Return the character with the highest count and appears first, if multiple have same count. 

A:
    - Create empty dict 'char_counts'
    - For each char in input string:
        - If char is not alphabetical, continue to next iteration
        - Set 'lower' to lowercase char
        - Increment value of key 'lower' in dictionary, or add if not there
    - Get keys of the dictionary
    - Sort keys based on respective values, from largest to smallest
    - Return first element of keys list

"""

def most_common_char(text):
    char_counts = dict()
    for char in text:
        if not char.isalpha():
            continue
        lower = char.lower()
        char_counts[lower] = char_counts.get(lower, 0) + 1

    letters = list(char_counts.keys())
    letters.sort(key=lambda key: char_counts[key], reverse=True)
    return letters[0]

# Test cases
print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')


"""
Reflection
Time: 19 min 27 seconds. Caught a small error in my algorithm that I then corrected. This one went quite well.
"""