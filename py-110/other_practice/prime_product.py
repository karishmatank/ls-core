"""
Write a function that takes a list of integers. 
The function should return a new list containing only the integers that are "prime products". 
A "prime product" is a number that is the product of exactly two distinct prime numbers.

P:
Input: List
Output: New list
Rules:
    - Explicit
        - The input list contains integers
        - The output list is a new list that only contains integers that are "prime products"
        - A "prime product" is defined as a number that is the product of exactly two distinct prime numbers
    - Implicit
        - A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself 
          (2, 3, 5, 7, 11,...)
        - We will only receive positive integers in the input list
        - The prime numbers that make up a prime product do not need to be in the input list
        - If the input list is empty, the output should be an empty list
        - If the input list contains non-integer elements, we should exclude those from the output list
        - If the input has duplicate numbers, and both are prime products, both numbers should be included in the output

D: Lists, ranges to iterate over and figure out what the right prime numbers are to calculate prime products.
Also sets to store the prime numbers that could be divisors for a given number in a list

A:
    - Assign an empty list to the variable 'return_list'
    - For each number in our input list:
        - Get the relevant prime factors, assign to variable 'primes'
        - If the number can be reproduced by multiplying any two integers from 'primes' together, add to 'return_list'
            - If primes has only 2 members and they multiply to the number, the number is a prime product
    - Return 'return_list'

Mini problem: Get the relevant prime numbers less than an input number
Input: Integer
Output: Set of prime numbers less than input integer
Algorithm:
    - Assign an empty set to the variable 'primes'
    - Assign a variable 'factor' to 2
    - While the input is greater than or equal to 'factor' and the input is not equal to 1:
        - If the input is divisible by the factor, add the factor to 'primes' and divide the input by the factor
        - Else, increment factor by 1
    - Return 'primes'
"""

def get_prime_factors(number):
    primes = set()
    factor = 2
    while number >= factor and number != 1:
        if number % factor == 0:
            primes.add(factor)
            number = number // factor
        else:
            factor += 1
    return primes

def find_prime_products(numbers):
    return_list = []

    for num in numbers:
        primes = get_prime_factors(num)
        factors = list(primes)
        if len(primes) == 2 and factors[0] * factors[1] == num:
            return_list.append(num)
    
    return return_list


#
# Test Cases
#

# Basic case with prime products and non-prime products
print(find_prime_products([6, 10, 14, 15, 20, 21]))

# An empty list
print(find_prime_products([]))

# List with no prime products
print(find_prime_products([1, 2, 3, 4, 5, 9, 12]))

# List with duplicates
print(find_prime_products([6, 10, 10, 15, 15, 15]))

# List containing a product of three primes (2*3*5)
print(find_prime_products([10, 15, 30, 35]))

# List containing a square of a prime (5*5)
print(find_prime_products([10, 15, 25, 35]))