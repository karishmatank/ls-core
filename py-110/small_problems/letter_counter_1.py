"""
Problem (as provided):
Write a function that takes a string consisting of zero or more space-separated words and 
returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

*** Step 1: Understand the problem ***
Input: String, may contain spaces
Output: Dictionary
Rules:
    - Explicit
        - Our input string may have zero words
        - Our input string may also have more than zero words, all separated by a space character
        - Our output dict gives a summary of the number of words of different sizes
    - Implicit
        - Word size is the length of the word
        - Punctuation counts as part of word length. The only delimiter is a space character
        - Our dictionary will have keys equal to the length of a string and values equal to the counts
          of the number of strings that meet that length
            - Keys and values are integers
        - An empty string input means we should return an empty dictionary
        - I don't see any delimiters of more than one space in the test cases, so we'll assume a delimiter
          is just one space and not worry for now about handling cases where there may be more than one space
          between words
Questions:
    - If we receive an empty string, should we return an empty dictionary?
    - How should we proceed if we don't get a string as input?
    - Will the delimiter always be spaces?
    - Can you clarify what "the number of words of different sizes" means?
        - What does "size" mean? Is it length of the word?
        - If we have 2 words in a string, each with length 4, does that mean the key is 2 and the value is 4?
    - (Missed- should have asked whether there can be more than one space in test cases, as we then could have
       altered our algorithm / code below)

*** Step 2: Examples and test cases ***
    - Confirmed that word size = length of word
    - Confirmed that punctuation is part of the word
    - Confirmed that empty string means returning an empty dict
    - Assume that we will always receive a string as input and not another data type

*** Step 3: Data structure ***
Definitely a dictionary, as that's what we will need to output.
We need to use strings as well, as our input is a string.
When we separate the string into individual words, we'll be able to store those in a list.

*** Step 4: Algorithm ***
    1. We take a string as input
    2. Assign a variable 'len_freq' to an empty dictionary
    3. If our string is empty, return 'len_freq', which is an empty dictionary
    4. Separate the string into individual words, using a single space character as delimiter.
    5. For each substring in the string
        a. Calculate its length
        b. If a key with the length of the word exists in the dictionary, increment the value associated
           with that key
        c. If a key with the length of the word doesn't exist, add it to the dictionary
    6. Return the dictionary
"""

def word_sizes(string):
    len_freq = {}

    if string:
        separated_words = string.split(" ")
        for word in separated_words:
            word_len = len(word)
            len_freq[word_len] = len_freq.get(word_len, 0) + 1

    return len_freq

# Test cases
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})