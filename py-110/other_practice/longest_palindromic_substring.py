"""
Implement a function that finds the longest palindromic substring in a given string. 
A palindrome is a string that reads the same backward as forward.

P:
Input: String
Output: String
Rules:
    - Explicit
        - The output should be the longest palindromic substring within the input
        - A palindrome is a string that reads the same backwards as forwards
    - Implicit
        - An empty input string should yield an empty output string
        - Single characters are palindromes. In this case, assume that the function would return the first instance of
          a single character palindrome that it comes across
            - First implies a substring that starts at a lower index value vs another substring
        - If there is only one character in the input string, we should return that character

E: Confirmed

D: I'll use intermediary strings to store substrings as we loop through. I'll use two ranges, one for a starting index and one
   as an ending index to create those substrings. I'll use a list to store all substrings for the input string.

A:
    - Assign a variable 'longest_palindrome' to an empty string
    - Find all substrings for the input string
    - For each substring:
        - Check if it is a palindrome
        - If so, and if the length of the substring is longer than the length of 'longest_palindrome':
            - Reassign 'longest_palindrome' to be the substring we are looping over
    - Return 'longest_palindrome'
    
Subproblem: Find all substrings
Input: String
Output: List of strings
Algorithm:
    - Assign a variable 'substrings' to an empty list
    - For an 'idx_start' that ranges from 0 to the length of the string:
        - For an 'idx_end' that ranges from idx_start + 1 to the length of the string + 1:
            - Create a substring starting from 'idx_start' to 'idx_end'
            - Add this substring to the end of 'substrings'
    - Return 'substrings'

Subproblem: Check if a string is a palindrome
Input: String
Output: Boolean
Algorithm:
    - Return true if the input matches the value of the input reversed

"""

def get_all_substrings(string):
    substrings = []
    for idx_start in range(len(string)):
        for idx_end in range(idx_start + 1, len(string) + 1):
            substrings.append(string[idx_start:idx_end])
    return substrings

def is_palindrome(string):
    return string == string[::-1]


def longest_palindromic_substring(text):
    longest_palindrome = ''
    substrings = get_all_substrings(text)
    for substring in substrings:
        if is_palindrome(substring) and len(substring) > len(longest_palindrome):
            longest_palindrome = substring
    return longest_palindrome

# Test cases
print(longest_palindromic_substring("babad") == "bab") # "aba" would also be valid
print(longest_palindromic_substring("cbbd") == "bb")
print(longest_palindromic_substring("a") == "a")
print(longest_palindromic_substring("ac") == "a") # Single characters are palindromes
print(longest_palindromic_substring("racecar") == "racecar")
print(longest_palindromic_substring("abcdefgfedcba") == "abcdefgfedcba")