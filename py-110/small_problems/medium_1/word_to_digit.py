"""
Write a function that takes a string as an argument and returns that string with every occurrence of a 
"number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- 
converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.

P:
Input: String
Output: New string
Rules:
    - Explicit
        - The output should convert alphabetical representations of numbers into their corresponding digits
        - Assume that the string does not contain any punctuation
    - Implicit
        - The output should leave all other words as is
        - Assume that a word is defined as a contiguous sequence of characters, each separated by a single space
        - Assume that a "number word" won't be embedded within a larger sequence of characters
        - Ignore case. "Five" is the same as "five"
        - An empty input string means an empty output string

E: Confirmed

D: We can use a dictionary where the keys are the alphabetical representations and the values are the digits. We can also
   use an intermediary list to store each "word"

A:
    - Create a dictionary that matches number words to their digits, assign to a constant variable 'NUMBER_WORDS'
    - Split the string into individual words, as separated by space characters. Assign the resulting list to a variable 'words'
    - Assign an empty list to the variable 'modified_words'
    - For word in 'words':
        - If the lowercase representation of word matches a key within 'NUMBER_WORDS'
            - Append the value associated with the relevant key, where the key is the lowercase word, to the end 
              of 'modified_words'
            - Else, append the word to the end of 'modified_words'
    - Combine each of the strings in 'words' into one string, separated each by a space character
    - Return the resulting string from the prior step

"""

NUMBER_WORDS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def word_to_digit(text):
    words = text.split()
    modified_words = []
    for word in words:
        if word.lower() in NUMBER_WORDS:
            modified_words.append(NUMBER_WORDS[word.lower()])
        else:
            modified_words.append(word)
    return ' '.join(modified_words)

# Test cases
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True