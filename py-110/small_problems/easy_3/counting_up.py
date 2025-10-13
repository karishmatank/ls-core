"""
Write a function that takes an integer argument and returns a list containing all integers between 1 and 
the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

P:
Input: Integer
Output: List of integers
Rules:
    - Explicit
        - The output list contains all integers between 1 and the argument **inclusive** and in ascending order
        - Assume the argument will always be a positive integer
    - Implicit
        - Assume the argument will never be < 1

E:
    - Confirmed understanding

D:
    - We can use a range to iterate through the numbers we need

A:
    - Assign a variable 'list_num' to an empty list
    - For a range of numbers starting from 1 and going up to the provided integer + 1 (exclusive):
        - Add the number to 'list_num'
    - Return 'list_num'
"""

def sequence(num):
    return [idx for idx in range(1, num + 1)]

# Test cases
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True