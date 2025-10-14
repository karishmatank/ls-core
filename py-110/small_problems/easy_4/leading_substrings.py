"""
Write a function that takes a string argument and returns a list of substrings of that string. 
Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.

P:
Input: String
Output: List of strings
Rules:
    - Explicit
        - Output list is a list of substrings from the input string
        - Each substring in the output should begin with the first letter of the input string
        - The substrings should be ordered from shortest to longest
    - Implicit
        - An empty input string means an empty output list
        - Assume that the input string will be one contiguous string of characters, such that we don't have to watch
          out for any special characters

E: Confirmed

D: We'll use a range to iterate through the input string to find substrings of varying lengths

A:
    - Assign an empty list to a variable 'substrings'
    - For an 'index_end' that starts at value 1 and ends at the length of the string (inclusive):
        - Get the substring that starts at index 0 and ends at the current value of 'index_end'
    - Just in case 'substrings' is not already sorted, we'll sort 'substrings' by the length of each substring
    - Return 'substrings'

"""

def leading_substrings(text):
    substrings = []
    for index_end in range(1, len(text) + 1):
        substrings.append(text[0:index_end])
    substrings.sort(key=len)
    return substrings


# Test cases
# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])