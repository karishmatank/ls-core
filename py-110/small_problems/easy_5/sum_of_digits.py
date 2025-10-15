"""
Write a function that takes one argument, a positive integer, and returns the sum of its digits.

P:
Input: Positive integer
Output: Integer
Rules:
    - Explicit
        - The output is the sum of the digits of the input integer
    - Implicit
        - Assume we will always have an input argument
        - Digits go from 0 to 9 inclusive
        - Assume no negative digits / integers

E: Confirmed

D: We can use a string to iterate through each digit individually. 

A:
    - Assign a variable 'total_sum' to the value 0
    - Coerce the input integer into a string. Assign the return value to the variable 'integer_str'
    - For each digit in 'integer_str'
        - Coerce the digit back to an integer and add to the current value of 'total_sum'
    - Return 'total_sum'

"""

def sum_digits(number):
    total_sum = 0
    integer_str = str(number)
    for digit in integer_str:
        total_sum += int(digit)
    return total_sum

# Test cases
print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True