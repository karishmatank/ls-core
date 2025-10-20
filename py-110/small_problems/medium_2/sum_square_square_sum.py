"""
Write a function that computes the difference between the square of the sum of the first count positive integers and the sum of the squares of the first count positive integers.

P:
Given an integer, calculate the difference between 1) the square of the sum of each positive integer from 1 to the input integer and 2) the sum of the squares of each positive integer from 1 to the input.

Rules:
    - We'll subtract the sum of the squares from the square of the sum
    - Within our calcs, we should include the input integer
    - If our input is <= 1, return 0

Data structures:
    - Input: integer
    - Output: integer (result from the difference)
    - Intermediary
        - Range: Iterate from 1 to the input number (inclusive)
        - List: Store these values and conduct transformations, including finding the squares or summing all numbers
        - Integer: Record the sums as we iterate through each number

High-level ideas:
    - Create a list of numbers ranging from 1 to input. Find the square of the sum of all numbers. Subtract the sum of the squares of the individual numbers. Return the result
    - Create variables for both sums and calculate the sums as we iterate through each number. Return the result of the difference

A:
    - If the input number is <= 1, return 0
    - Create a range that starts from 1 and ends at the input number (inclusive). Store this in a list 'numbers'
    - Calculate the square of the sum of all the numbers. Assign to variable 'square_of_sum'
    - Calculate the square of each number in the list and find the sum. Assign to variable 'sum_of_squares'
    - Return the value of 'square_of_sum' - 'sum_of_squares'

"""

def sum_square_difference(number):
    if number <= 1:
        return 0

    numbers = list(range(1, number + 1))
    square_of_sum = sum(numbers) ** 2
    sum_of_squares = sum([num ** 2 for num in numbers])
    return square_of_sum - sum_of_squares
    

# Test cases
print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

"""
Reflection. Around 15 and a half minutes. Great job speaking through everything and testing as you go.
"""