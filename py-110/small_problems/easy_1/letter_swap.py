"""
Problem (as provided):
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. 
You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or 
repeated spaces.

*** Step 1: Understand the problem ***
Input: String, includes space separating substrings
Output: A new string
Rules:
    - Explicit
        - Swaps the first and last letters of every word
        - Assume that every word contains at least one letter and that the string will always contain at least one word
        - Assume that each string contains nothing but words and spaces
        - Assume no leading, trailing, or repeated spaces
    - Implicit
        - From my second question, we would return "epplA" if we saw the word "Apple", not "Eppla"
        - If we get a string that is only one character, we would return the character back
        - We preserve the order of the words that appear in the string

Questions:
    - If punctuation exists, do we assume that's part of the word? Or does the problem statement mentioning nothing but words
      and spaces mean that we should not expect any punctuation or non alphabetical characters?
    - Does case matter?
        - If a word is "Apple", do we preserve case to return "Eppla"? Or do we return "epplA"?

*** Step 2: Examples and test cases ***
    - Confirmed my understanding that "Apple" returns "epplA", not "Eppla"
    - Noticed that a string with only one character just returns the character back

*** Step 3: Data structures ***
We'll have to work with strings, as that's both the input and output data type.
We will also have to work with lists to maintain the order of the words we are returning.

*** Step 4: Algorithm ***
    1. Take as input the string
    2. Parse the string for words
    3. Assign a variable "modified_words" to an empty list
    4. For each word
        a. Record the first and last letters
        b. Create a new word that starts with the last letter, the same middle letters, 
           and the first letter of the original word
        c. Add the newly created word to "modified_words"
    5. Combine the words within 'modified_words" back into one string, separated by spaces
    6. Return the resulting string from step 5

"""

def swap(text):
    words = text.split()
    
    modified_words = []
    for word in words:
        if len(word) == 1:
            modified_words.append(word)
            continue

        first, *middle, last = word
        new_word = last + ''.join(middle) + first
        modified_words.append(new_word)

    result = ' '.join(modified_words)
    return result


# Test cases
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True