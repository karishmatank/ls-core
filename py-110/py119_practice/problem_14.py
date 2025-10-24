"""
Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

If the argument is negative, return 0.

P:
Given an integer, find all unique positive numbers less than the integer that are multiples of 7 or 11. Calculate their sum and return.

Rules:
    - We want all positive numbers less than the input that are multiples of 7 or 11
    - If a number is a multiple of both 7 and 11, count just once
    - If input is negative or 0, return 0
    - If the input itself is divisible by 7 or 11, don't count it - we want #s *less than* the input

Data structures:
    - Input: integer
    - Output integer (sum)
    - Intermediary:
        - Range: Iterate through numbers from 1 (inclusive) to integer (exclusive)
        - Integer: Update our sum with every number
        - Boolean: Check if the number is divisible by 7 or 11 (yes/no)
        - List: Store numbers divisible by 7 or 11

High-level strategies:
    - Iterate through a range starting from 1 and ending at input (exclusive). Check if number is divisible by 7 or 11. If so, add to a sum variable. Return the sum variable.
    - Create a list of numbers less than input that are divisible by 7 or 11. Return the sum of those numbers

A:
    - *get_divisible_nums* => Input: input integer, Output: 'numbers'
    - If 'numbers' is empty:
        - Return 0
    - Return the sum of 'numbers'


*get_divisible_nums*
Input: Integer
Output: List
Algo:
    - Find all numbers from 1 to the input (exclusive) that are either divisible by 7 or 11
    - Return that list


"""

def get_divisible_nums(number):
    return [num for num in range(1, number) if num % 7 == 0 or 
                                               num % 11 == 0]


def seven_eleven(number):
    numbers = get_divisible_nums(number)
    return sum(numbers)


# Test cases
print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)


"""
Reflection: 
Time: 14 min 38 seconds. Probably too easy for what will be on the interview.
"""