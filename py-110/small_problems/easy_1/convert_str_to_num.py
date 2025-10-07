"""
Problem (as provided):
Write a function that takes a string of digits and returns the appropriate number as an integer. 
You may not use any of the standard conversion functions available in Python, such as int. 
Your function should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about invalid characters; 
assume all characters are numeric.

P:
Input: String of digits
Output: Integer
Rules:
    - Explicit
        - Takes a string of digits as input, returns the corresponding number as an integer
        - Can't use standard conversion functions such as int
        - Calculate the result by using the characters in the string
        - Don't worry about leading + or - signs or any other invalid characters
    - Implicit
        - String will only have digits, will assume for now that we won't get an empty string. If we do, we will return 0
        - Will assume that the strings provided won't go out of bounds for the max value of an int in Python

Questions:
    - What is the definition of "appropriate number"? If we get a string "3", does that mean we should return 3?
    - Is there a certain length that this string can be, or can it be a long string?
    - How should we treat empty strings?

E:
    - Confirmed my understanding of "appropriate number" being the integer representation of the string provided

D:
We'll be working with strings, as that's the input, as well as integers, as that's the output.
I'll use a range as well to iterate through the string indices

A:
    1. Take as input a string with numbers only
    2. Assign a counter variable 'factor' to the integer 1
    3. Assign a variable 'rolling_sum' to 0
    4. Moving backwards in the string, we'll start from the right hand side and work to the left most character.
       For each character:
        a. Calculate the ASCII value of the character and subtract from that value the ASCII value of the string '0'
        b. Take the resulting integer and multiply by 'factor'
        c. Add the result of b to 'sum'
        d. Multiply 'factor' by 10
    5. Return 'rolling_sum'
"""

def string_to_integer(numeric_str):
    factor = 1
    rolling_sum = 0
    for idx in range(-1, -(len(numeric_str) + 1), -1):
        num = ord(numeric_str[idx]) - ord('0')
        rolling_sum += num * factor
        factor *= 10
    return rolling_sum

# Test cases
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True