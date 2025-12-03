"""
P:
Given an octal number, convert to an integer in base 10.

Rules:
    - To convert an octal to decimal, multiply the nth digit from the right by 8^(n-1) and sum the results per digit
    - Invalid inputs include non-numeric strings or strings that have any digit above 7
        - If input is invalid, return 0
    - The only valid digits in an octal are 0 to 7 inclusive
    - We should define a class called Octal that is initialized with the input string. The method `to_decimal` will
      give the output

E:
"10" => 1 * (8^2-1) + 0 * (8^1-1) = 8
"17" => 1 * (8^1) + 7 * (8^0) = 8 + 7 = 15
"130" => 1 * (8^2) + 3 * (8^1) + 0 = 64 + 24 = 88

D:
    - Input: String of digits
    - Output: Integer
    - Intermediary:
        - List: Store each digit of input
        - Range: Iterate through digits to multiply by proper 8^(n-1) factor

High-level strategies:
    - Turn input into a list of digits. Iterate through digits, multiplying by 8^factor, setting factor based on index
      of element. Return the sum of results

A:
    to_decimal method:
    - If input is not all digits, return 0
    - Split into list `digits`, turn digits to ints
    - If any digit in `digits` is > 7, return 0
    - Set `total_sum` to 0
    - For each digit in `digits`
        - Set factor as the length of `digits` - digit index - 1
        - Multiply digit by 8^factor, add to `total_sum`
    - Return `total_sum`

"""

class Octal:
    def __init__(self, octal_num):
        self.octal_num = octal_num
    
    def to_decimal(self):
        if not self.octal_num.isdigit():
            return 0
        
        digits = [int(digit) for digit in self.octal_num]
        if any([digit > 7 for digit in digits]):
            return 0
    
        total_sum = 0
        for idx, digit in enumerate(digits):
            factor = len(digits) - idx - 1
            total_sum += digit * (8 ** factor)
        
        return total_sum