"""
P:
Input: String with digits
Output: List of integers
Rules:
- Explicit
    - The input will consist of a string of digits
    - Our output list will contain elements that consist of substrings from the input of strictly increasing digits
    - Our output list elements should be of length 2 or more
    - Our output will have elements as *integers*, not strings
- Implicit
    - All characters in the input string will be digits from '0' to '9'
    - An empty input string should return an empty output list
    - An input string with only one digit should return an empty output list
    - Strictly increasing digits mean that the second digit and beyond in a substring is the next highest digit after the prior digit
        - I.e. '28 would not be considered a valid substring, whereas '23' would
        - i.e. '22' would not be a valid substring either

D:
Lists and strings as part of our output and input. 
I envision using 2 ranges to iterate through the string to give us start and end points for each substring we'll evaluate.
We'll use a list to store each digit of a substring as we evaluate it as well.

A:
- Assign an empty list to variable 'substrings'
- For idx_start from 0 to the second to last digit in the input string:
    - For idx_end from idx_start + 2 to the last digit in the input string:
        - Check if substring from idx_start to idx_end is valid
        - If so, add to the end of 'substrings'
        - If not, break out of the inner loop and move on to the next idx_start
- Coerce each element of 'substrings' into an integer
- Return 'substrings'

Subproblem: Check if substring is valid
Input: String
Output: Boolean
Algorithm:
- Split the substring up into individual digits, store in a list variable 'digits'
- Convert each individual digit into an integer
- For each digit in 'digits' from index 1 to the end of the list:
    - If the digit is not 1 more than the digit at the prior index, return False
- Return True

"""

def check_substring(digit_str):
    digits = [int(substr) for substr in digit_str]
    for idx in range(1, len(digits)):
        if digits[idx] - digits[idx - 1] != 1:
            return False
    return True

def find_increasing_substrings(digits):
    substrings = []
    for idx_start in range(0, len(digits) - 1):
        for idx_end in range(idx_start + 2, len(digits) + 1):
            substring = digits[idx_start:idx_end]
            if check_substring(substring):
                substrings.append(substring)
            else:
                break
    
    return [int(substr) for substr in substrings]



# Test Cases
print(find_increasing_substrings('1234'))      # Expected: [12, 123, 1234, 23, 234, 34]
print(find_increasing_substrings('98712389'))  # Expected: [12, 123, 23, 89]
print(find_increasing_substrings('12234'))     # Expected: [12, 23, 234, 34]
print(find_increasing_substrings('54321'))     # Expected: []
print(find_increasing_substrings('4'))         # Expected: []
print(find_increasing_substrings(''))          # Expected: []