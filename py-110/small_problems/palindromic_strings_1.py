"""
Problem (as provided):
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. 
A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

**** Step 1: Understand the problem ****
Input: string
Output: Boolean (True or False)
Rules:
    - Explicit
        - Return true if the string passed as an argument is a palindrome, otherwise False
        - A palindrome means that the string has the same value when reversed
        - Case matters: 'aA' is not a palindrome
        - All characters matter
    - Implicit
        - All characters matter refers to punctuation and spaces as well, as per the last test case
            - Placement of the space matters, even if the phrase is a palindrome with spaces and punctuation stripped out,
              we need to check if it is with the punctuation or spaces included
        - We can have numbers, but the input will be a string, as per two of the test cases

Questions:
    - None

**** Step 2: Examples and test cases ****
See below for test cases. Thoughts and reflections added above

**** Step 3: Data structures ****
Strings will clearly be used here. No need for other sorts of data structures at this time.

**** Step 4: Algorithm ****
    1. Take as input a string
    2. Reverse the string
    3. Compare the reversed string value to the input string
        a. If the values match, return True
        b. Else, return False

Step 2 can be its own mini problem of sorts, although I have confidence in my ability to reverse a string,
so I won't expand upon it for now.

"""

def is_palindrome(input_str):
    reversed_str = input_str[::-1]
    return reversed_str == input_str


# Test cases: All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)