"""
Write a function that checks if any permutation of a given string can form a palindrome. The check must be case-insensitive and should ignore any non-alphanumeric characters (spaces, punctuation, etc.).

P:
Given a string, return True if any other order of the same letters would be a palindrome. Ignore non-alphanumeric characters.

Rules:
    - Ignore non-alpha characters
    - Case insensitive
    - Palindrome means that all letters repeat even number of times, in some cases there may be one letter that repeats odd number of times
    - A single letter input is considered a palindrome.


"Tact Coa"
"tactcoa" => "tacocat" is palindrome, "tactoca" is not, etc.

"aabb" => "abba" is palindrome

"aabbcd" => "abcdba" is not palindrome, neither is "abdcba"

"A man, a plan, a canal, Panama"
    - "a" = 10
    - "m" = 2
    - "n" = 4
    - "p" = 2
    - "l" = 2
    - "c" = 1


Data structures:
    - Input: string
    - Output: Boolean
    - Intermediate:
        - Dictionary: Key = char, value = count
        - String: Lowercased + without non alpha chars
        - Set: Get all unique chars

High-level idea:
    - Create a dictionary out of a lowercased string with only alphas. For each key in dictionary, check how many values are even vs odd. If none or one odd values, return True. Otherwise, return False

A:
    - If input only has one char, return True
    - Create a cleaned string => *clean_string*
    - *get_value_counts* => Get chars and their counts, output => 'counts'
    - Set variable 'num_odd' to 0
    - For char in 'counts'
        - If value associated w/ char is odd, increment 'num_odd' by 1
    - Return True if num_odd <= 1, otherwise return False


*clean_string*
    Input: String
    Output: String
    Algo:
        - Create empty string "cleaned"
        - For each char of input:
            - If alpha, convert to lowercase and add to "cleaned"
        - Return "cleaned"

*get_value_counts*
    Input: String
    Output: Dict
    Algo:
        - Create empty dict 'counts'
        - For each char in input:
            - If char not in 'counts', add it
            - Increment value of char by 1
        - Return 'counts'

"""

def clean_string(string):
    cleaned = ""
    for char in string:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned

def get_value_counts(string):
    counts = dict()
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    return counts

def can_form_palindrome(string):
    if len(string) == 1:
        return True
    
    cleaned_str = clean_string(string)
    counts = get_value_counts(cleaned_str)
    
    num_odd = 0
    for value in counts.values():
        if value % 2 == 1:
            num_odd += 1
    
    return num_odd <= 1

# print(get_value_counts("tactcoa"))

# # Test cases
print(can_form_palindrome("Tact Coa"))  # Expected: True (permutations include "taco cat", "atco cta", etc.)
print(can_form_palindrome("aabbc"))    # Expected: True ("abcba")
print(can_form_palindrome("aabbcd"))   # Expected: False
print(can_form_palindrome("a"))        # Expected: True
print(can_form_palindrome("A man, a plan, a canal, Panama")) # Expected: True
print(can_form_palindrome("Hello World")) # Expected: False