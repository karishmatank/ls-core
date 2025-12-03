"""
P:
Given a number, determine if it is perfect, abundant, or deficient.

Rules:
    - An Aliquot sum is the sum of all positive divisors of the input, including 1 and excluding the number itself
    - Perfect numbers have an Aliquot sum that matches the number
    - Abundant numbers have an Aliquot sum that is > the number
    - Deficient numbers have an Aliquot sum that is < the number
    - The input number must be positive. If it is not, we should raise a ValueError
    - We should create a class called PerfectNumber that has a class method called `classify` that takes the number as
      an argument

E:
13 => prime, only divisor is 1. 1 < 13 => deficient
28 => 1, 2, 14, 4, 7 -> sum is 28 => perfect
12 => 1, 2, 3, 4, 6 -> sum is 16 => abundant

D:
    Input: integer
    Output: string, one of "perfect", "abundant", or "deficient"
    Intermediary:
        - Set: Store unique divisors
        - Range: Loop over all potential divisors to find which ones divide evenly into the number
        - List: Store divisors
        - Integer: Calculate sum of divisors

High-level strategies:
    - Loop over all potential divisors (1 up to input (exclusive)) and detect divisors by testing that there is no remainder
      after input is divided by the divisor. Store divisors in a list and calculate their sum. Classify input by comparing
      sum to input.

A:
    - Class method `classify`
        - If input is <= 0, raise a ValueError
        - Loop over all numbers from 1 to the input, exclusive
            - If the input is divisible evenly by the number, add to a list `divisors`
        - Sum `divisors` => `sum_divisors`
        - If `sum_divisors` = input, number is "perfect"
        - Else if `sum_divisors` > input, number is "abundant"
        - Else, number is "deficient"

"""

class PerfectNumber:
    @classmethod
    def classify(cls, number):
        if number <= 0:
            raise ValueError("Input must be a positive integer")

        sum_divisors = sum(candidate for candidate in range(1, number) if number % candidate == 0)

        if sum_divisors == number:
            return "perfect"
        elif sum_divisors > number:
            return "abundant"
        else:
            return "deficient"