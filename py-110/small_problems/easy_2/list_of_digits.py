"""
Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

P:
Input: Positive integer
Output: List
Rules:
    - Explicit
        - Input will always be a positive integer
        - Output will be a list that consists of the digits in the number
    - Implicit
        - Assume the input will always be of type integers, and not a string representation of an integer or any other
          data type
        - Assume there will always be an input, and that the function won't be invoke with no argument

Questions:
    - Can the input be a string representation of a positive integer, which may include other characters besides numbers?
    - Should an empty argument return an empty list?

E:
    - Confirmed understanding

D:
I'll use a string to work with each digit individually. List will be returned

A:
    - Coerce the input into a string, assign to variable "input_str"
    - Create a new list that turns each character in 'input_str' into a separate element in the list
    - Coerce each element of the list into an integer
    - Return the list
 
"""

def digit_list(number):
    input_str = str(number)
    return_list = list(input_str)
    return [int(num) for num in return_list]

# Test cases
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True