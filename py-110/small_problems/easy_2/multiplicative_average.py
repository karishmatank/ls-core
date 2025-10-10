"""
Write a function that takes a list of positive integers as input, multiplies all of the integers together, 
divides the result by the number of entries in the list, and returns the result as a string 
with the value rounded to three decimal places.

P:
Input: List of positive integers
Output: String representation of 3 decimal place float
Rules:
    - Explicit
        - Input list has positive integers
        - Output string is the result after multiplying all integers together and dividing by list length
        - Output to be rounded to 3 decimal places
    - Implicit
        - Even if the output evaluates to fewer than 3 decimal places, we'll pad the end with zeros
        - Assume that the input list will always be populated
        - Assume that the input list will always include integers only
        - Integers can appear more than once in the input list

Questions
    - How should we treat empty lists?
    - Are all integers always expected to be positive?
    - Will all elements be integers, or should we expect elements of varying types?

E:
    - Confirmed understanding from the test cases

D:
Lists and strings as input and output, not really using any intermediary data structures

A:
    - Assign a variable 'product' to 1
    - For each element in the input list:
        - Multiply the current value of 'product' by the value of the element
    - Divide 'product' by the length of the list, assign to variable 'result'
    - Round 'result' to 3 decimal places
    - Coerce 'result' to a string
    - Return the string representation of 'result'

"""

def multiplicative_average(numbers):
    product = 1
    for num in numbers:
        product *= num
    result = product / len(numbers)

    return f"{result:.3f}"
    

# Test cases
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")