"""
Write a function that takes a list of strings and returns a list of the same string values, 
but with all vowels (a, e, i, o, u) removed.

P:
Input: List of strings
Output: List of strings
Rules:
    - Explicit
        - The output list is the same length as the input list, but with all strings in the output having their vowels
          removed
        - Vowels include a, e, i, o, u
    - Implicit
        - An empty input list means an empty output list
        - If a string within the list has no vowels, we should return an output at that index that matches the input
        - Maintain case. In addition, upper case A, E, I, O, U should be dropped
        - If a string in the list consists of all vowels, the output at that index should have an empty string

E: Confirmed

D: We can use either:
    - A list to store each character, dropping characters that are vowels, and then stitching the list back into a string
    - A variable that points to a string, that we continuously reassign as we add on characters to the end

A:
    - Assign an empty list to the variable 'return_list'
    - For each string in the input list:
        - Assign an empty string to a variable 'reconstructed'
        - For each character in the string:
            - If the lowercase version of the character is not a, e, i, o, or u, append to 'reconstructed'
        - Add 'reconstructed' to the end of 'return_list'
    - Return 'return_list'

"""

def remove_vowels(input_list):
    return_list = []
    for string in input_list:
        reconstructed = ''
        for char in string:
            if char.lower() not in 'aeiou':
                reconstructed += char
        return_list.append(reconstructed)
    return return_list

# Test cases
# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True