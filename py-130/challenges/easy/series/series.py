"""
Write a program that will take a string of digits and return all the possible consecutive number series of a 
specified length in that string.

For example, the string "01234" has the following 3-digit series:
- 012
- 123
- 234

Likewise, here are the 4-digit series:
- 0123
- 1234

Finally, if you ask for a 6-digit series from a 5-digit string, you should throw an error.
"""

"""
P:
Given a string of digits and a length, return all lists of consecutive digits of that length.

Rules:
    - Output will be a nested list, where each sublist has elements that are the consecutive integers from the input string
    - Elements of nested lists should be integers
    - Raise a ValueError if the specified length is larger than the length of the string

D:
    Input: String, integer
    Output: List of lists of integers
    Intermediary:
        - Range: Iterate through each possible starting index

High-level ideas:
    - Use a range to find all substrings of the correct length. Convert to lists of integers, append to a master list, and
      return. If specified length > length of the input string, raise a ValueError

A:
    - Constructor
        - Set instance var `numeric_str` to argument passed in
    - `slices` instance method
        - Input: Integer (length)
        - If input > length of self.numeric_str, raise ValueError
        - Create empty list "groups"
        - For a starting index from 0 to len of self.numeric_str - length (inclusive)
            - Get substring from starting index of input length
            - Create a list of integers from substring
            - Append list to end of "groups"
        - Return "groups"

"""

class Series:
    def __init__(self, string):
        self.numeric_str = string

    def slices(self, desired_len):
        if desired_len > len(self.numeric_str):
            raise ValueError
        
        groups = []
        for idx in range(len(self.numeric_str) - desired_len + 1):
            substr = self.numeric_str[idx:idx+desired_len]
            groups.append([int(digit) for digit in substr])
        
        return groups