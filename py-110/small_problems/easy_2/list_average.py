"""
Write a function that takes one argument, a list of integers, and returns the average 
of all the integers in the list, rounded down to the integer component of the average. 
The list will never be empty, and the numbers will always be positive integers.

P:
Input: List of integers
Output: Integer
Rules:
    - Explicit
        - Input is a list of integers
        - Output is the average of all integers in the list, rounded down to the nearest integer. Output is thus
          an integer
        - List will never be empty
        - List will always be positive integers
    - Implicit
        - Average is the sum of all elements in the list, divided by the number of elements in the list
        - A list with one element should just return the value of that element

Questions:
    - Can the input list have negative integers? How should those be treated, if so? (Answered in problem, never mind)

E:
    - Confirmed understanding

D:
We'll be working with the input *list*. I don't anticipate needing any other intermediary data structures

A:
    - Sum all elements of the input list
    - Calculate the average by dividing the sum by the length of the list
    - Round down to the nearest integer
    - Return that rounded down integer
"""

def average(numbers):
    return sum(numbers) // len(numbers)

# Test cases
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True