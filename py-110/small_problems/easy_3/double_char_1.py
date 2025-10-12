"""
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

P:
Input: String
Output: New string
Rules:
    - Explicit
        - The output should double every character in the input string
        - The output should be a new string
    - Implicit
        - "Doubles every character" means that each character repeats twice, with each repeat occurring immediately
          after the character from the original string. I.e "good" turns into "ggoooodd"
        - We'll preserve case, so if a character appears as "H", it is doubled to "HH"
        - An empty string input means an empty string output

E:
    - Confirmed

D:
We may decide to use a range to iterate through the input string.
We'll build the output in a string that we'll constantly reassign

A:
    - Assign an empty string to the variable 'new_string'
    - For each character in the string
        - Create a substring that consists of the character doubled (i.e if char = 'd', the substring will be 'dd')
        - Append the substring to 'new_string'
    - Return 'new_string'

"""

def repeater(text):
    new_string = ''
    for char in text:
        new_string += char * 2
    return new_string

# Test cases
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True