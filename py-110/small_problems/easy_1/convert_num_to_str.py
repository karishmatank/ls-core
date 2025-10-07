"""
Problem (as provided):
In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. 
In this exercise and the next, you're going to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation 
of that integer.

You may not use any of the standard conversion functions available in Python, such as str. Your function should do this 
the old-fashioned way and construct the string by analyzing and manipulating the number.

P:
Input: Integer (non-negative)
Output: String
Rules:
    - Explicit
        - Integer will be non-negative, from 0 upwards
        - Output is the string representation of that integer
        - We can't use str()
    - Implicit
        - Not much I can think of right now

Questions:
    - This might be a reach, but what does it mean to "analyze and manipulate the number"?
    - Can we assume that we'll get a valid integer input?

E:
    - Confirmed understanding that function takes in an integer and returns the string version of that integer
    - Confirmed that the function works for small and larger integers

D:
Integers, as that's the input, as well as strings, as that's the output.

A:
    1. Take an integer as input
    2. Assign a variable 'factor' to the integer 10
    3. Assign a constant variable 'NUM_TO_STR' a dictionary object with keys as digits 0 to 9 
       and values as their string representations
    4. Assign a variable 'str_representation' to an empty string
    5. If the integer starts as 0, simply return '0'
    6. Repeat until the integer is 0:
        a. Take the remainder of the integer after dividing by the factor
        b. Find the string representation of this integer in the NUM_TO_STR dictionary
        c. Append the result from b to the left hand side of the existing str_representation string
        d. Perform integer division to the input integer by the factor
    7. Return str_representation

"""

NUM_TO_STR = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}

def integer_to_string(input_num):
    factor = 10
    str_representation = ''

    if input_num == 0:
        return '0'

    while input_num:
        remainder = input_num % factor
        str_version = NUM_TO_STR[remainder]
        str_representation = str_version + str_representation
        input_num = input_num // factor
    return str_representation

# Test cases
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True