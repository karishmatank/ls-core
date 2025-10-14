"""
Write a function that returns a list of all palindromic substrings of a string. That is, each 
substring must consist of a sequence of characters that reads the same forward and backward. 
The substrings in the returned list should be sorted by their order of appearance in the input string. 
Duplicate substrings should be included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purpose of this exercise, you should consider all characters and pay attention to case; that is, 
'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, assume that single characters are not palindromes.

P:
Input: String
Output: List of strings
Rules:
    - Explicit
        - The output contains all palindromic substrings of the input string
        - A palindrome is defined as a sequence of characters that reads the same forward and backward
        - The output should have substrings sorted by their order of appearance in the input string
        - Duplicate substrings should be included multiple times
        - Case matters- 'AbcbA' is a palindrome but 'Abcba' is not. Special characters such as "-" matter too
        - Single characters are not palindromes
    - Implicit
        - The substrings in the output should have length 2 or greater
        - An empty input string should return an empty output list
        - Order of appearance means we sort based on the index of the starting character of the substring

E: Confirmed

D: 
We'll use two ranges to iterate through the string, one for starting index, another for ending index
Technically, we do this within our helper functions

A:
    - Assign an empty list to the variable 'palindromes_list'
    - Find all substrings that exist within the input string
    - For each substring:
        - If the substring has length 1, continue to the next substring
        - Check if the substring is a palindrome.
        - If it is, append the substring to the end of 'palindromes_list'
    - Return 'palindromes_list'

Subalgorithm: Check if a string is a palindrome
Input: String
Output: Boolean (True or False)
Algorithm:
    - For a variable 'idx' that ranges from 0 to the length of the input string:
        - Assign a variable 'idx_right_to_left' to the value of -idx - 1
        - If the character at index 'idx' is not equal to the character at index 'idx_right_to_left', return False
    - Return True
    

"""

def leading_substrings(text):
    substrings = []
    for index_end in range(1, len(text) + 1):
        substrings.append(text[:index_end])
    return substrings

def substrings(text):
    substrings = []
    for idx in range(len(text)):
        substr_start_idx = leading_substrings(text[idx:])
        substrings.extend(substr_start_idx)
    return substrings

def check_palindrome(string):
    for idx in range(len(string)):
        idx_right_to_left = -idx - 1
        if string[idx] != string[idx_right_to_left]:
            return False
    return True

def palindromes(text):
    palindromes_list = []
    substrings_list = substrings(text)
    for substr in substrings_list:
        if len(substr) == 1:
            continue
        if check_palindrome(substr):
            palindromes_list.append(substr)
    return palindromes_list


# Test cases
print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True