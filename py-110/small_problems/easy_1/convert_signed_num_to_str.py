"""
Problem (as provided):
In the previous exercise, you developed a function that converts non-negative numbers to strings. 
In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string representation.

You may not use any of the standard conversion functions available in Python, such as str. 
You may, however, use integer_to_string from the previous exercise.

P:
Input: Integer
Output: String
Rules:
    - Explicit
        - The integer input can now be negative
        - If the integer is negative, it'll have a - sign
    - Implicit
        - Integers are represented as base 10 numbers
        - Output related to negative integers should include a "-" character at the start of the string
        - Output related to positive integers will include a "+" character at the start of the string
        - 0 should return "0"

Questions:
    - Should output strings include a "+" character if the number is positive? Answer is yes

E:
    - Answered my question on the "+" character
    - Confirmed my other understandings on what the string representation is

D:
We'll be using strings as the outputs are strings, along with integers given the input is an integer

A:
    1. Take as input an integer
    2. Assign a variable symbol:
        a. If the integer > 0: to "+"
        b. If the integer < 0: to "-"
    3. If the integer < 0, we need to multiply the number by -1 to prepare it for our integer_to_string function,
       which only takes positive integers
    4. Call our prior integer_to_string function on the input integer
    5. Add the symbol to the front of the result from 4
    6. Return the result from 5

"""

from convert_num_to_str import integer_to_string

def signed_integer_to_string(num):
    if num > 0:
        symbol = "+"
    elif num < 0:
        symbol = "-"
        num *= -1
    else:
        symbol = ""
    
    return symbol + integer_to_string(num)


# Test cases
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True