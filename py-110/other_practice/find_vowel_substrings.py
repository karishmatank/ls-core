"""
Write a function named find_vowel_substrings that takes a single string as an argument. 
The function should identify all substrings that start and end with a vowel (a, e, i, o, u). 
It should then return a new list containing these substrings, sorted by their length in descending order. 
If two substrings have the same length, their original order of appearance should be preserved in the sorted list.

P:
Input: String
Output: List of strings
Rules:
- Explicit
    - Our function should identify all substrings that start and end with a vowel
    - Our output list should include all valid substrings
    - Our output list should sort these substrings by length in descending order
    - If two substrings have the same length, preserve their order of appearance
- Implicit
    - Overlapping substrings are considered separate. I.e. if our input is ‘aeiou’, we would count both ‘ae’ and ‘aei’, among others
    - Order of finding substrings matters, even though we are sorting them in the end
        - We should find substrings based on holding constant a starting index while iterating the ending index
    - A single character that is a vowel counts as a substring
    - An empty string as input should return an empty list as output
    - Characters between the start and end characters can be anything- they don’t have to be vowels
    - Case insensitive - ‘Apple’ is considered a valid substring, but the output would include ‘apple’, not ‘Apple’

E:
    - Confirmed + added on to implicit arguments

D: 
Input is string, output is list of strings.
We can use a list to hold the substrings, as well as to sort them
We'll use ranges to iterate over the list and provide start and end indices
I'll use a string to hold the valid vowel characters

A:
    - Create a lowercase version of the input string
    - Assign a variable 'substrings' to an empty list
    - For a starting index ranging from 0 to the last character in the input string:
        - For an ending index ranging from the starting index + 1 to the last character in the input string:
            - Extract a substring from the input by starting at the starting index and ending at the ending index
            - Check if the substring is valid
            - If so, add to 'substrings'
    - Order the list by the length of the substrings in reverse order
    - Return 'substrings'

Subalgorithm: Check if a substring is valid
Input: String
Output: Boolean (True or False)
Algorithm:
    - Assign a constant variable VOWELS to the string 'aeiou'
    - If the first character of the substring is in the VOWELS string and the last character of the substring is 
      in the VOWELS string, return True
    - Else, return False

"""

VOWELS = 'aeiou'

def check_substring_validity(substr):
    return (substr[0] in VOWELS) and (substr[-1] in VOWELS)

def find_vowel_substrings(string):
    string = string.lower()
    substrings = []
    for idx_start in range(0, len(string)):
        for idx_end in range(idx_start + 1, len(string) + 1):
            substring = string[idx_start:idx_end]
            if check_substring_validity(substring):
                substrings.append(substring)
    substrings.sort(key=len, reverse=True)
    return substrings


# Test cases
print(find_vowel_substrings('banana'))
# Expected: ['anana', 'ana', 'ana', 'a', 'a', 'a']

print(find_vowel_substrings('aeiou'))
# Expected: ['aeiou', 'aeio', 'eiou', 'aei', 'eio', 'iou', 'ae', 'ei', 'io', 'ou', 'a', 'e', 'i', 'o', 'u']

print(find_vowel_substrings('Apple pie'))
# Expected: ['apple pie', 'apple pi', 'apple', 'ie', 'a', 'e', 'i', 'e']

print(find_vowel_substrings('rhythm'))
# Expected: []

print(find_vowel_substrings(''))
# Expected: []

print(find_vowel_substrings('programming'))
# Expected: ['ogrammi', 'ogra', 'o', 'a', 'i']