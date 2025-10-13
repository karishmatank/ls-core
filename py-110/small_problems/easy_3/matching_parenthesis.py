"""
Write a function that takes a string as an argument and returns True if all parentheses in the string
are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

Note that balanced pairs must start with a (, not a ).

P:
Input: String
Output: Boolean (True or False)
Rules:
    - Explicit
        - Return True if the parenthese are balanced
        - Balanced is defined as parentheses existing in matching '(' and ')' pairs
        - Balanced pairs must start with a '(', not ')'
    - Implicit
        - Not only does the number of ( need to match to ), but every ) must have at least one ( come before it
        - If the input string does not have any parentheses at all, we'll return True

E:
Confirmed

D: No intermediary data structures for now

A:
    - Assign a variable 'open_count' to 0
    - For each character in the input string:
        - If the character == '(':
            - Increment 'open_count' by 1
        - Else if the character == ')':
            - If 'open_count' == 0:
                - Return False, as we are not supposed to allow closed parentheses before any open
            - Decrement 'open_count' by 1
    - If 'open_count' == 0
        - Return True
    - Else:
        - Return False
        
"""

def is_balanced(text):
    open_count = 0
    for char in text:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count == 0:
                return False
            open_count -= 1
    
    return open_count == 0

# Test cases
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True