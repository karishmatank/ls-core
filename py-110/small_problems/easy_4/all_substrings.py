"""
Write a function that returns a list of all substrings of a string. Order the returned list by where 
in the string the substring begins. This means that all substrings that start at index position 0 should come first, 
then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each position, 
return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:

P:
Input: String
Output: List of strings
Rules:
    - Explicit
        - The output list should have all substrings of the input string
        - The output should be ordered by where in the string the substring begins
            - All substrings that start at index position 0 should come first, followed by index 1, etc
        - For the substrings that start at the same index position, order those substrings from shortest to longest
    - Implicit
        - An empty input string should lead to an empty input list
        - A substring is any contiguous string that has a length of 1 or more

E: Confirmed

D:
    - I'll use intermediary lists to maintain order per starting index as I find substrings

A:
    - Assign an empty list to the variable 'substrings'
    - For an variable 'idx' that ranges from 0 to the length of the input string:
        - Find all substrings that begin with the character at index 'idx' in the input string (we'll use our prior
          function to do this)
        - Add each resulting substring to the end of 'substrings', maintaining the same order
    - Return 'substrings'

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


# Test cases
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True