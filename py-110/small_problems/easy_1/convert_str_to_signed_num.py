"""
Problem (as provided):
In the previous exercise, you developed a function that converts simple numeric strings to integers. 
In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer. 
The string may have a leading + or - sign; 
if the first character is a +, your function should return a positive number; 
if it is a -, your function should return a negative number. 
If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, such as int. 
You may, however, use the string_to_integer function from the previous exercise.

P: 
Input: String of digits
Output: Integer
Rules:
    - Explicit
        - Takes a string of digits
        - Returns the "appropriate number" as an integer
        - There may or may not be a leading + or - sign
        - If '+' or no sign, return a positive number
        - If '-', return a negative number
        - You can't use the int() function but can use the previous string_to_integer function
        - The string will always contain a valid number
    - Implicit
        - Appropriate number means the numeric representation of the string i.e. "3" returns 3
        - Assume there will only be one + or -, if it is present at all
        - Assume there will be no other special characters besides + or -

Questions:
    - Can we expect a + or - to be the only other characters besides numeric characters?
    - Will + or - always be at the start of the string? Assume so as problem states "leading"
    - Should we expect only one + or - character, if it is present?

E: 
    - Confirmed my understanding on leading + or -, only see one + or - or none

D:
We'll be working with strings and integers, as the input is a string and the output will be an integer.

A:
    1. Take as input a string
    2. Separate out a leading + or -, if it exists.
    3. Call our previous string_to_integer function on the string that step 2 returns
    4. If we have a leading "-", multiply the integer returned from step 3 by -1
    5. Return the resulting integer

"""
from convert_str_to_num import string_to_integer

def string_to_signed_integer(numeric_signed_str):
    if numeric_signed_str.startswith("+") or numeric_signed_str.startswith("-"):
        # symbol, *numeric_str = numeric_signed_str

        # THE ABOVE RETURNS A LIST FOR numeric_str, KEEP AS A STRING FOR THIS EXERCISE!!!
        # In this case, with our string_to_integer function, it happened to work
        symbol = numeric_signed_str[0]
        numeric_str = numeric_signed_str[1:]
    else:
        symbol = ""
        numeric_str = numeric_signed_str
    
    num = string_to_integer(numeric_str)

    if symbol == "-":
        num *= -1
    
    return num

# Test cases
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
