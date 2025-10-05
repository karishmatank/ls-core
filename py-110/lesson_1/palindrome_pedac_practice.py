"""
PROBLEM (from lesson):

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.


input: string
output: list of strings
rules:
    - Explicit requirements:
        - Substrings must be palindromes
        - Substrings must be of length 2 or more
        - Palindromes are case sensitive: "aA" is not a palindrome while "aa" is
    - Implicit requirements:
        - If input is an empty string, return empty list

Data structure: list

Algorithm (adapted from lesson):
    - Create an empty list and assign to variable 'result'
    - Create a list of all substrings at least 2 characters long:
        - Create an empty list and assign to variable 'substrings'
        - For each index from 0 to length of string - 2:
            - For each substr_len from 2 (min length of substring) to length of string - index:
                - Slice string with start index = index and end index = index + substr_len
                - Append to 'substrings'
        - Return 'substrings'
    - For each substring, determine if palindrome.
        - Reverse the substring and assign to varialble 'reversed'
        - If substring value == 'reversed' value:
            - Return true
        - Else:
            - Return false
    - If string is a palindrome, add to 'result'
    - Return 'result'
"""

MIN_SUBSTR_LEN = 2

def get_substrings(string):
    substrings = []
    for idx in range(0, len(string) - MIN_SUBSTR_LEN + 1):
        for substr_len in range(MIN_SUBSTR_LEN, len(string) - idx + 1):
            index_start = idx
            index_end = idx + substr_len
            substr = string[index_start:index_end]
            substrings.append(substr)

    return substrings

def is_palindrome(string):
    return string == string[::-1]

def palindrome_substrings(string):
    result = []
    substrings = get_substrings(string)
    for substring in substrings:
        if is_palindrome(substring):
            result.append(substring)
    return result


# Test cases:

# Comments show expected return values
print(palindrome_substrings("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings(""))           # []
print(palindrome_substrings("repaper"))    # ['repaper', 'epape', 'pap']
print(palindrome_substrings("supercalifragilisticexpialidocious")) # ["ili"]