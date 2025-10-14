"""
Write a function that takes a string of alphabetic characters as an argument. 
The function should find and return the index N where the sum of the alphabetical values of the 
characters to the left of N is equal to the sum of the alphabetical values of the characters to the right of N.

P:
Input: String
Output: Integer
Rules:
    - Explicit
        - The input string will be made up of alphabetical characters
        - The output integer will represent the index N at which the sum of alphabetical values to to left of N == sum
          to the right of N
    - Implicit
        - The "alphabetical value" of a character is its 1-based position in the alphabet (a=1, b=2, ..., z=26)
        - The comparison must be case-insensitive ('a' and 'A' both have a value of 1).
        - The character at the balancing index N is not included in either sum
        - The sum for an empty part of the string (e.g., to the left of index 0 or right of the last index) is 0
        - If no such balance index is found, return -1. This includes an empty input string
        - If there are multiple balance indices, return the smallest one
        - If the input string includes only one character, return the index of that character
            - Balance before index 0 is 0, balance after index 0 is 0, therefore we return index 0

E: Confirmed

D: Ideas:
- We can use a list to store all of the individual characters of the string, or maybe just individual characters per "side"
  (left vs right)
- We can use a range to iterate through the indices of the input string
- We can use a string to store the alphabet, such that the index of a letter in the alphabet corresponds to its numeric value

A:
    - Define a new string called 'lowercase', which is the lowercase version of the input string
    - Define a constant variable ALPHABET, assigned to the string " abcdefghijklmnopqrstuvwxyz"
    - For each index starting from 0 and ending at the length of 'lowercase' (exclusive):
        - Get the characters on the "left side" of the current index from 'lowercase', not including the current index
        - Get the numerical value of the "left side"
        - Get the characters on the "right side" of the current index from 'lowercase', not including the current index
        - Get the numerical value of the "right side"
        - Compare both side values:
            - If they are the same, return the current index we are looping through
    - Return -1

Subproblem: Get the numerical value of a "side"
Input: String
Output: Integer
Algorithm:
    - Assign a variable 'sum' to 0
    - For each character in the input:
        - Get the character's numerical value
        - Add the numerical value to the current value of 'sum'
    - Return 'sum'
        
"""

ALPHABET = " abcdefghijklmnopqrstuvwxyz"

def get_value(substr):
    sum = 0
    for char in substr:
        sum += ALPHABET.index(char)
    return sum

def find_balance_index(text):
    lowercase = text.lower()
    for idx in range(len(lowercase)):
        left_side = lowercase[:idx]
        right_side = lowercase[idx + 1:]
        if get_value(left_side) == get_value(right_side):
            return idx
    return -1

# Test cases
print(find_balance_index("racecar")) # 3
print(find_balance_index("fXae")) # 1
print(find_balance_index("a")) # 0
print(find_balance_index("")) # -1
print(find_balance_index("abCde")) # -1
print(find_balance_index("zZz")) # 1