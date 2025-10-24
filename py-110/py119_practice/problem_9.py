"""
Create a function that takes two string arguments and returns the number of times that the second string occurs in the first string. Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.

P:
Given two strings, return the number of unique (non-overlapping) times that the second occurs in the first.

Rules:
    - Non-overlapping means that 'babab' contains 1 instance of 'bab', with 'ab' left over. 'babbab' contains 2 instances of 'bab'
    - Second string will never be empty
    - First string can be empty => we would output 0
    - Strings will only have lowercase alphabetical characters

Data structures:
    - Input: 2 strings
    - Output: Integer (count of 2nd input in first)
    - Intermediary:
        - String: Keep track of substrings within the first input

High-level strategies:
    - Iterate through the first input, creating intermediary string in the process. If character sequence matches up with letters of the second, increment a counter by 1 and reset intermediary string. Return number of occurrences.
    - Create a new string from the first input. Replace occurrences of second input with a space character. Return the number of spaces.

A:
    - Create a new string that replaces occurrences of second input in first input with a space
    - Count the number of spaces in the new string
    - Return the count

"""

def count_substrings(str1, str2):
    leftover_chars = str1.replace(str2, " ")
    return leftover_chars.count(" ")


# Test cases
print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)


"""
Reflection:
Time: 14 min 15 sec
"""