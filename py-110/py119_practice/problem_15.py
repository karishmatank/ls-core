"""
Create a function that takes a string argument that consists entirely of numeric digits and computes the greatest product of four consecutive digits in the string. The argument will always have more than 4 digits.

P:
Given a string of digits, compute the largest product of 4 consecutive digits.

Rules:
    - The input will always have more than 4 digits
    - The input will be entirely numeric digits
    - Consecutive means we maintain the order of the digits as given

Data structures:
    - Input: string
    - Output: Integer
    - Intermediary:
        - List: Substrings of 4 chars or more, maintaining order of the original string
        - Integer: Tracks largest product thus far
        - Range: Iterate through the list

High-level strategies:
    - Get all substrings of length 4. For each, compute the product of the digits. Return the largest product.
    - Iterate through digits of the string, starting at the first digit and ending at the 4th to last digit (inclusive). Get the 4 digits starting at the current digit. Record largest product as we iterate. Return the largest product.

A:
    - Set variable 'SUBSTRING_LEN' to 4
    - Set variable 'largest_product' to 0
    - For an index ranging from start of input to the 4th to last digit (inclusive):
        - Get the 4 consecutive ints starting at the index => 'substr'
        - *calculate_product* input: 'substr', output: 'current_product'
        - Set 'largest_product' to the larger of current value and 'current_product'
    - Return 'largest_product'

*calculate_product* - Calculate the product of digits
Input: String (digits)
Output: Integer (product)
Algo:
    - Create a list out of the input
    - Turn each element into an integer
    - Set variable 'product' to 1
    - Iterate through list and multiply 'product' by each digit
    - Return 'product'

"""
SUBSTRING_LEN = 4

def calculate_product(digits_str):
    digits = [int(digit) for digit in list(digits_str)]
    product = 1
    for digit in digits:
        product *= digit
    return product

def greatest_product(digits_str):
    largest_product = 0
    for idx in range(len(digits_str) - SUBSTRING_LEN + 1):
        substr = digits_str[idx:idx + 4]
        current_product = calculate_product(substr)
        largest_product = max(largest_product, current_product)
    return largest_product


# print(calculate_product('2345'))

# # Test cases
print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6


"""
Reflection:
Time: 18 min 55 seconds. Pretty straightforward.
"""