"""
Given a list of strings, sort the list based on the highest number of adjacent consonants a string 
contains and return the sorted list. If two strings contain the same highest number of adjacent consonants, 
they should retain their original order in relation to each other. Consonants are considered adjacent 
if they are next to each other in the same word or if there is a space between two consonants in adjacent words. 
Vowels are a, e, i, o, u.

P:
Input: List of strings
Output: List of strings
Rules:
    - Explicit
        - Output should be sorted version of input based on highest # of adjacent consonants a string contains
        - If two strings contain same highest # of adjacent cnosonants, retain their original order in relation to each other
        - Consonants are considered adjacent if they are next to each other in the same word or if there is a space between
          two consonants in adjacent words
        - Vowels are a, e, i, o, u
    - Implicit
        - We should not mutate the input list
        - If a space separates two adjacent consonants, don't count the space as part of the highest # of consonants
        - Assume there are only alphabetical and space characters in the strings in the input list
        - An empty element in the input list means 0 consonants
        - An empty input list means an empty output list
        - Ignore case - "S" is a consonant, as is "s"
        - One standalone consonant character means 0 adjacent consonants
        - Sort from highest to lowest

E: Confirmed

D: We can use intermediary strings to record the longest adjacent consonant string. We can also use lists to separate out
   these longest adjacent substrings.

A:
    - Assign a constant variable VOWELS to 'aeiou'
    - For each word in the input list:
        - Get the length of the longest adjacent consonant subsequence
    - Create a new list that consists of the input list sorted by length of longest adjacent consonant subsequence
    - Return the list created in the prior step

Subproblem: Get the length of the longest adjacent consonant subsequence
Input: String
Output: Integer
Algorithm:
    - Remove the spaces in the string, collapsing the input into one contiguous string of characters
    - Convert the resulting string into lowercase
    - For every vowel present in the remaining string, replace with a space character
    - Split apart the resulting string into a list, with each list consisting of adjacent consonant characters
    - If the resulting list is an empty list, return 0
    - If the longest substring in the list has length 1, return 0
    - Return the length of the longest substring in this list

"""

VOWELS = 'aeiou'

def get_longest_consonant_len(string):
    string = string.replace(" ", "").lower()
    for vowel in VOWELS:
        string = string.replace(vowel, " ")
    consonant_substrings = string.split()
    consonant_substrings.sort(key=len, reverse=True)
    if not consonant_substrings or len(consonant_substrings[0]) == 1:
        return 0
    return len(consonant_substrings[0])

def sort_by_consonant_count(lst):
    return sorted(lst, key=get_longest_consonant_len, reverse=True)
    

# Test cases
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])