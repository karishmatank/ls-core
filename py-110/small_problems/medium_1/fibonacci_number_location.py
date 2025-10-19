"""
As we've seen in the last few exercises, the Fibonacci series is a computationally simple series. 
However, the results grow at an incredibly rapid rate. For example, the 100th Fibonacci number is 
354,224,848,179,261,915,075 -- that's enormous, especially considering that it takes six iterations 
just to find the first 2-digit Fibonacci number.

Write a function that calculates and returns the index of the first Fibonacci number that has the number 
of digits specified by the argument. The first Fibonacci number has an index of 1. 
You may assume that the argument is always an integer greater than or equal to 2.

P:
Input: Integer
Output: Integer
Rules:
    - Input represents a number of digits of a Fibonacci sequence element
    - Output represents the index of the first Fibonacci number with that number of digits
    - The first Fibonacci number has an index of 1
    - Input is >= 2

E: Confirmed

D:
    - Integer: Store the index and number of digits latest Fibonacci number assessed in separate variables
    - List: Store the Fibonacci sequence elements to avoid recalculating them over and over
    - Dictionary: Store the Fibonacci sequence elements using a key as the index number and value as the Fibonacci number

High-level strategies:
    - Keep iterating through index values, starting from 1. Record the Fibonacci number at that index. If its number
      of digits matches the input integer, return the index value. If not, increment the index by 1

A:
    1. Create an index variable with a value of 1
    2. Find the Fibonacci number associated with the current index
    3. Calculate the number of digits of the Fibonacci number
        - Coerce the integer into a string and calculate its length
    4. If the number of digits matches our input integer, return the value of the index
    5. If not, increase index by 1 and go back to step 2

Subproblem: Find the fibonacci number associated with the current index
Input: Integer (index of Fibonacci sequence)
Output: Integer (Fibonacci number)
Algorithm:
    - Create a global list variable initialized to [1, 1]
    - If the index - 1 (b/c of zero indexing) is in the list, return that value
    - Otherwise
        - Find the sum of the n-1 and n-2 Fibonacci numbers
        - Add that value to the list
        - Return the value

"""

import sys
sys.set_int_max_str_digits(50_000)

fibonacci_sequence = [1, 1]

def find_fibonacci_numbers(index):
    if index <= len(fibonacci_sequence):
        return fibonacci_sequence[index - 1]
    value = find_fibonacci_numbers(index - 1) + find_fibonacci_numbers(index - 2)
    fibonacci_sequence.append(value)
    return value

def find_fibonacci_index_by_length(digit_count):
    index = 1
    while True:
        number = find_fibonacci_numbers(index)
        num_digits = len(str(number))
        if num_digits == digit_count:
            break
        index += 1
    return index


# Test cases
# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)