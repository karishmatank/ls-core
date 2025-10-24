"""
Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

P:
Given a string of digits, return the number of substrings that end in an even digit.

Rules:
    - Even-numbered refers to the last digit in the substring representing an even number
    - If a substring occurs more than once, count as separate occurrences
    - A substring is one or more digits
    - Substrings preserve order from the input
    - Input string will only have numeric characters


'3145926'
- '3145926'
- '314'
- '14'
- '4'
- '314592'
- '14592'
- '4592'
- '592'
- '92'
- '2'
- '145926'
- '45926'
- '5926'
- '926'
- '26'
- '6'

Data structures:
    - Input: string
    - Output: Integer
    - Intermediary:
        - Strings in a list- Finding and storing substrings
        - Boolean- Does the substring end in an even number? Yes/no

High-level strategies:
    - Find all substrings from input. Count the number that end in an even digit. Return the count.
    - Iterate through the input string. If the digit is even, count the number of characters to its left, including itself. Return the total count.

A:
    - Set variable 'total_count' to 0
    - For each index and char in string:
        - Coerce char into an int
        - Check if the int is even.
        - If so
            - Set 'count_substr' to index + 1 (tracks # of chars thus far in the string, incl current char)
            - Increment 'total_count' by 'count_substr'
    - Return 'total_count'

"""

def even_substrings(digit_str):
    total_count = 0
    for idx, char in enumerate(digit_str):
        if int(char) % 2 == 0:
            count_substr = idx + 1
            total_count += count_substr
    return total_count



# Test cases
print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

"""
Reflection:
Time: 17 min 41 seconds
"""