"""
Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

P:
Input: Positive integer
Output: Positive integer
Rules:
    - Explicit
        - The output integer is the input integer with the numbers reversed
    - Implicit
        - Assume the input will not contain other characters (i.e. be a float that includes a period, etc.)
        - If the input has trailing zeros, those will not be reflected in the output integer
        - Assume we won't receive an empty input (no argument)
        - If the input only has one digit, we can return the input as the output

E:
    - Confirmed

D:
Two ideas:
- We'll use a string to parse through each digit individually
- We can split the integer into individual digits by using a list

Both of these will maintain order while allowing us to sort the digits in the way we want.

A:
    - Turn the input integer into a list of digits.
        - We'll turn the input into a string so that we can easily separate out the digits
        - Assign to a variable 'num_list'
    - Reverse 'num_list', such that the last digit is now first and the first is last, and so on
    - Combine the elements of the reversed 'num_list' into one string
    - Coerce the resulting string into an integer and return
"""

def reverse_number(num):
    num_list = list(str(num))
    num_list.reverse()
    num_str = ''.join(num_list)
    return int(num_str)

# Test cases
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True