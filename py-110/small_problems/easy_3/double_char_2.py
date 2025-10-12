"""
Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. 
The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

P:
Input: String
Output: New string
Rules:
    - Explicit
        - The output string doubles every consonant in the input string
        - However, we won't double vowels (a, e, i, o, or u), digits, punctuation, or whitespace
        - Assume that only ASCII characters will be included in our input string
    - Implicit
        - An empty input string should result in an empty output string
        - We'll preserve case in the output
        - Doubles every consonant means 'd' turns into 'dd'
        - Not doubling vowels and the other types of characters means that 'a' remains in the string as 'a' instead of 'aa'

E:
    - Confirmed

D:
No intermediary data structures needed. We'll build the output string a character (or two) at a time

A:
    - Assign an empty string to a variable 'new_string'
    - For each character in the input string:
        - If the character is a consonant (i.e. the lowercase version of the character is not a, e, i, o, or u 
          and it is an alphabetical character):
            - Create a new substring that consists of the character doubled (i.e. substring = 'dd' if character = 'd')
            - Add that substring to the end of 'new_string'
        - Else
            - Add the character to the end of 'new_string'
    - Return 'new_string'

"""

def double_consonants(text):
    new_string = ''
    for char in text:
        if (char.lower() not in 'aeiou') and (char.isalpha()):
            new_string += char * 2
        else:
            new_string += char
    return new_string

# Test cases
# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")