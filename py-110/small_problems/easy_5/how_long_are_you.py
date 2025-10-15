"""
Write a function that takes a string as an argument and returns a list that contains every word from the string, 
with each word followed by a space and the word's length. If the argument is an empty string or if no argument 
is passed, the function should return an empty list.

You may assume that every pair of words in the string will be separated by a single space.

P:
Input: String
Output: List of strings
Rules:
    - Explicit
        - The output list contains every word from the string, with each word followed by a space and the word's length
        - If the input string is an empty string or no argument is passed, the output should be an empty list
        - Every pair of words in the string will be separated by a single space.
    - Implicit
        - [How is a "pair of words" defined? That implies 2 of something?]
        - Each word from the input is its own element in the output list, with the addition of an extra space and the word length
          all in one substring
        - We should count punctuation as part of the word count
        - The output substrings should maintain case

E: Confirmed

D: We'll use an intermediary list to store individual words from the input string. We'll also use intermediary strings
   to build new string objects that include the length of the string

A: 
    - Separate the input string into individual words. Words are separated by a space character
    - Assign an empty list to the variable 'words_with_len'
    - For each word:
        - Calculate the length of the word
        - Create a new string object that appends a space character and the string representation of the length to the
          current word
        - Add the new string object to the end of 'words_with_len'
    - Return 'words_with_len'

"""

def word_lengths(text=""):
    words = text.split()
    return [f"{word} {len(word)}" for word in words]



# Test cases
# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True