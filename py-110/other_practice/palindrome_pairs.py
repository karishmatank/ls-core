"""
Given a list of unique words, write a function that finds all pairs of distinct indices (i, j) in the list, such that the concatenation of the two words, words[i] + words[j], is a palindrome. The function should return a list of these pairs.

P:
Given a list of words, return a list of indices (nested list) where the words at the indices specified combine to form a palindrome.

Rules:
    - Words in input list will be unique
    - List can have empty strings as elements
    - A single character letter is considered a palindrome


["bat", "tab", "cat"]
"battab" => [0, 1]
"batcat"
"tabbat" => [1, 0]
"tabcat"
"catbat"
"cattab"

Data structures:
    - Input: List of strings
    - Output: Nested lists of integers (indices)
    - Intermediary:
        - String: Create new strings based on concat
        - Boolean: Is a string a palindrome? Yes/no
        - Range: Iterate through the list twice

High-level ideas:
    - Use 2 ranges to iterate through input list, getting first and second parts. Concatenate both parts into one string. Test whether string is palindrome. If so, add their indices into a new list and add that list into our output list. Return output list.

A:
    - Create empty list 'indices'
    - For a 'start_idx' from 0 to last string of input:
        - For an 'end_idx' from 0 to last string of input:
            - If start and end index match, continue
            - Create 'candidate' by adding element at 'start_idx' with element at 'end_idx'
            - *is_palindrome* => If 'candidate' is palindrome:
                - Create new list of indices [start_idx, end_idx]
                - Add new list to end of 'indices'
    - Return 'indices'

*is_palindrome*
    Input: String
    Output: Boolean
    Algo:
        - Create reversed version of input => 'reversed_str'
        - Return True if 'reversed_str' is same as input string, False otherwise

"""

def is_palindrome(string):
    reversed_str = string[::-1]
    return reversed_str == string

def palindrome_pairs(str_list):
    indices = []
    for start_idx in range(len(str_list)):
        for end_idx in range(len(str_list)):
            if start_idx == end_idx:
                continue
            candidate = str_list[start_idx] + str_list[end_idx]
            if is_palindrome(candidate):
                indices.append([start_idx, end_idx])
    return indices


# # Test cases
print(palindrome_pairs(["bat", "tab", "cat"]))
# Expected: [[0, 1], [1, 0]]

print(palindrome_pairs(["dog", "cow", "cat"]))
# # Expected: []

print(palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]))
# # Expected: [[0, 1], [1, 0], [2, 4], [3, 2]]

print(palindrome_pairs(["a", ""]))
# # Expected: [[0, 1], [1, 0]]