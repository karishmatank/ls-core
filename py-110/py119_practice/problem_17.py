"""
Create a function that takes a list of integers as an argument. The function should determine the minimum integer value that can be appended to the list so the sum of all the elements equals the closest prime number that is greater than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

Notes:

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.


P:
Given a list of numbers, return the smallest integer that should be added such that the new sum of the numbers is equal to the prime number closest to the current sum (next highest).

Rules:
    - List will always have at least 2 ints
    - All values in the list will be positive
    - List can have duplicate values
    - If current list sums to prime number, need to still check for next largest prime (can't append a 0)
    - Prime number is a num > 1, that can only be divided by 1 and itself

[5, 2]
- Sums to 7, which is prime (doesn't matter)
- Next largest is 11
- 11 - 7 = 4


Data structures:
    - Input: List of ints
    - Output: Integer
    - Intermediary:
        - Boolean: Is a number prime? Yes/no
        - Integer: 
            - Sum of the current list
            - Iterate through integers > current sum to find next prime
            - Iterate through factors to determine whether a number is prime

High-level strategies:
    - Calculate the sum of the input. Find the number that is the next highest prime (greater than the sum). Return the difference between the next highest prime and the current sum.

A:
    - Create variable 'current_sum', sum of input digits
    - *get_next_prime* => Input: 'current_sum', Output: 'next_highest_prime'
    - Return 'next_highest_prime' - 'current_sum'


*get_next_prime*: Get next highest prime number
Input: Integer
Output: Integer (next highest prime)
Algo:
    - Create variable 'candidate_prime' => input + 1
    - Repeat until we get a prime number:
        - Test if 'candiate_prime' is prime => *is_prime*
        - If so, return 'candidate_prime'
        - Else, increment 'candidate_prime' by 1

*is_prime*: Check if number is prime
Input: Integer
Output: Boolean
Algo:
    - For a 'factor' ranging from 2 to the input (exclusive):
        - Divide input by 'factor'
        - If there is no remainder, return False
    - Return True

"""

def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True

def get_next_prime(num):
    candidate_prime = num + 1
    while True:
        if is_prime(candidate_prime):
            break
        candidate_prime += 1
    return candidate_prime

def nearest_prime_sum(numbers_list):
    current_sum = sum(numbers_list)
    next_highest_prime = get_next_prime(current_sum)
    return next_highest_prime - current_sum


# # Test cases
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

"""
Reflection:
Time: 18 min 26 seconds. Went pretty smoothly. Accidentally had an infinite loop in my algo, which I caught when coding, then
corrected algo. Otherwise very smooth.
"""