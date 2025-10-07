"""
Problem (as provided):
Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. 
For instance, the word size of "it's" is 3, not 4.

*** Step 1: Understand the problem ***
Input: String, may contain spaces
Output: Dictionary
Rules:
    - Explicit
        - Similar explicit rules to part 1
    - Implicit
        - Differences here vs part 1 are that punctuation does not count as the word length
        - Punctuation at the end of a word should be excluded as well
        - One thing I just thought of- we don't need to sort the dictionary keys either
        - No info on how to treat numbers provided in strings. We'll assume numbers are fine.
            - *** MISSED: PROBLEM STATEMENT SAYS NON-LETTERS, DON'T INCLUDE NUMBERS!
        - MISSED: GUARD AGAINST EMPTY STRINGS AFTER STRIPPING OUT PUNCTUATION- DON'T WANT TO INCLUDE

Questions:
    - Should punctuation at the end of a word be excluded as well, in addition to characters mid word?
    - How do we treat numbers in strings?

*** Step 2: Examples and test cases ***
    - Confirmed answer to question above, added to implicit rules

*** Step 3: Data structures ***
We'll once again need to use a dictionary and strings given they represent the output and input, respectively.
We can use a list to store the individual words from the input string as well.

*** Step 4: Algorithm ***
    1. We'll take as input a string
    2. Assign a variable 'len_freq' to an empty dictionary
    3. Separate the words in the input string into individual words
    4. For each word in the input string
        a. Take out non alphabetical characters
        b. Count the length of the remaining characters in the word
        c. If there is a key matching the length already in 'len_freq', increment it by 1
        d. If there is not a key matching the length in 'len_freq', add it to the dictionary with value 1

Problem: Take out non alphabetical characters
Input: string
Output: New string
Algorithm:
    1. Assign a variable 'new_str' to an empty string
    2. For character in input string
        a. If character is alphanumeric, append to 'new_str'
    3. Return 'new_str'

MISSED: AN EASIER WAY TO TAKE OUT NON ALPHABETICAL CHARACTERS WOULD HAVE BEEN TO USE .JOIN()
"""

def clean_up_string(word):
    new_str = ''
    for char in word:
        # if char.isalnum():
        if char.isalpha():
            new_str += char
    
    return new_str

def word_sizes(text):
    len_freq = {}
    words = text.split()
    for word in words:
        word_len = len(clean_up_string(word))
        len_freq[word_len] = len_freq.get(word_len, 0) + 1
    return len_freq


# Test cases
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})