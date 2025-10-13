"""
Create a function that takes two integers as arguments. The first argument is a count, and the second is 
the starting number of a sequence that your function will create. 
The function should return a list containing the same number of elements as the count argument. 
The value of each element should be a multiple of the starting number.

You may assume that count will always be an integer greater than or equal to 0. The starting number can be any integer. 
If the count is 0, the function should return an empty list.

P:
Input: Two integers
Output: List
Rules:
    - Explicit
        - The first argument is a count, the second is the starting number of the output list
        - The output list will contain the same number of elements as the first argument specifies
        - The value of each element in the output should be a multiple of the starting number
        - The first argument will always be >= 0. The starting number doesn't have to be
        - If the first argument is 0, the function should return an empty list
    - Implicit
        - "Multiple" seems to be defined as the starting number * 2, then starting number * 3, etc.
        - If the starting number is negative, it makes sense that all other numbers in the sequence will be negative
        - If the starting number is 0, all numbers in the sequence will be zero

Questions:
    - What is the definition of "multiple"? By what factor should we be multiplying?

E: Confirmed

D:
We can use a range to iterate through all of the indices we need for the output list.

A:
    - Assign an empty list to a variable 'multiples'
    - For a range starting at 1 and ending at the value of the first argument (inclusive):
        - Multiply the starting number by the current value we are iterating over
        - Add that result to the end of 'multiples'
    - Return 'multiples'
"""

def sequence(count, starting_num):
    multiples = []
    for factor in range(1, count + 1):
        multiples.append(starting_num * factor)
    return multiples

# Test cases
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True