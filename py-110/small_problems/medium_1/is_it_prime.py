"""
A prime number is a positive number that is evenly divisible only by itself and 1. 
Thus, 23 is prime since its only divisors are 1 and 23. 
However, 24 is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. 
Note that the number 1 is not prime.

Write a function that takes a positive integer as an argument and returns True if the number is prime, 
False if it is not prime.

You may not use any of Python's add-on packages to solve this problem. Your task is to 
programmatically determine whether a number is prime without relying on functions that already do that for you.

P:
Input: Integer
Output: Boolean
Rules:
    - Return True if the number provided is prime, False if not
    - A prime number is only divisible by itself and 1
    - 1 is not a prime number
    - Assume that the argument provided will be a positive integer

D:
    - We can use a set to store factors of the input. If that set doesn't include only 1 and the input integer, number
      is not prime
    - We can also achieve the same as the above with a tuple or list, which may include duplicates if
      duplicate factors exist for a number (i.e. 4 = 2 x 2)
    - We can use a range to iterate through each integer from 2 up to but not including the input number

A:
    - If the input is 1, return False
    - For a 'factor' that ranges from 2 to the input number (exclusive):
        - Find the remainder if we divide the input number by the factor
        - If the remainder is 0, that means that the input is not divisible by just 1 or itself, so it's not prime
            - Therefore, return False
    - If we get to the end of the loop, the number is prime, so return True


"""

def is_prime(number):
    if number == 1:
        return False
    
    # factors = [factor for factor in range(2, number) if number % factor == 0]
    for factor in range(2, number):
        if number % factor == 0:
            return False

    return True


# Test cases
print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True