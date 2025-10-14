"""
Create a function called is_valid_parentheses that takes a string containing only the characters 
'(', ')', '{', '}', '[' and ']', and determines if the input string has valid parentheses.

The function should return True if:
•   Open brackets must be closed by the same type of brackets.
•   Open brackets must be closed in the correct order.
•   Every close bracket has a corresponding open bracket of the same type.

P:
Input: String
Output: Boolean
Rules:
    - Explicit
        - The input string will only contain the aforementioned bracket characters
        - Return True if open brackets are closed by the same type of bracket, closed in the correct order, and
          every close bracket has a corresponding open bracket of the same type
    - Implicit
        - An empty string means we return True
        - "Correct order" means that an open bracket must exist before we see a closing bracket, with both types of brackets
          matching
        - The order in which we close open brackets matters. For example, we should close inner brackets first before
          attempting to close outer brackets. "([)]" is invalid because we try to close the outer bracket before the inner one

E: Confirmed

D:
We'll have to keep track of which brackets are open and which we've closed. We can use a list to keep track of this order.
Lists are also a good idea because they are mutable, which means we can remove open brackets that have been closed.
I'm also going to create a dictionary that keeps track of the corresponding open brackets for each closed bracket

A:
    - Assign an empty list to the variable 'outstanding_brackets'
    - Create a dictionary with corresponding open brackets as values to a closed bracket "key", assign to variable 'OPEN_BRACKET'
    - For each character in the input string:
        - If the character is an open bracket, add it to the end of 'outstanding_brackets'
        - If it is a closed bracket, check the last element added to 'outstanding_brackets'
            - If 'outstanding_brackets' is an empty list or the last element of the list is not a corresponding open bracket:
                - Return False
            - Else:
                - Remove the last element from 'outstanding_brackets'
    - If the length of 'outstanding_brackets' is 0
        - Return True
    - Else
        - Return False

Subalgorithm: Check if a character is a corresponding open bracket:
Input: String (closed bracket character)
Output: String (open bracket character)
Algorithm:
    - Return the value associated with the key passed in as input

"""

OPEN_BRACKET = {
    ']': "[",
    '}': "{",
    ")": "("
}

def get_open_bracket(closed_bracket):
    return OPEN_BRACKET[closed_bracket]

def is_valid_parentheses(text):
    outstanding_brackets = []

    for char in text:
        if char in "({[":
            outstanding_brackets.append(char)
        elif not outstanding_brackets or get_open_bracket(char) != outstanding_brackets[-1]:
            return False
        else:
            outstanding_brackets.pop()
    
    return len(outstanding_brackets) == 0




# Test cases
print(is_valid_parentheses("()"))           # True
print(is_valid_parentheses("()[]{}"))       # True
print(is_valid_parentheses("(]"))           # False
print(is_valid_parentheses("([)]"))         # False
print(is_valid_parentheses("{[]}"))         # True
print(is_valid_parentheses(""))             # True
print(is_valid_parentheses("]"))            # False