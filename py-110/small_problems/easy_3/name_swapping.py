"""
Write a function that takes a string argument consisting of a first name, a space, and a last name. 
The function should return a new string consisting of the last name, a comma, a space, and the first name.

You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").

P:
Input: String
Output: New string
Rules:
    - Explicit
        - The input string consists of two words, where a word is defined as a continuous group of characters
          that doesn't include a space. These words consist of a first and last name
        - The output string should reverse the order of these words (names)
        - The output should add a comma after the new first word (last name)
        - Assume the string does not contain middle names, initials, or suffixes
    - Implicit
        - An empty string should return an empty output string

E:
    - Confirmed understanding

D:
We can use a list to store each word.

A:
    - Separate the input string into two words, forming a list. Assign to a variable 'names'
    - Reverse the order of the strings in 'names'
    - Combine the strings in 'names' together by starting with the string at index 0, followed by a ", ", followed by the string
      at index 1
    - Return the result from the last step
"""

def swap_name(name_str):
    names = name_str.split()
    names.reverse()
    return ", ".join(names)

# Test cases
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True