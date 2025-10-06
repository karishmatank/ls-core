"""
Problem (as provided):
Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. 
This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. 
If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.

*** Step 1: Understand the problem ***
Input: string
Output: Boolean (True or False)
Rules:
    - Explicit
        - We will receive as input a string
        - We should reverse the string
        - A palindrome is when the reversed string has the same value as the input string
        - In this case, we want to be case-insensitive, which means we ignore differences in case
        - We should also ignore all non-alphanumeric characters
    - Implicit:
        - We should not ignore numbers, as the string representation of the number '356653' is a palindrome
        - We may want to strip out non-alphanumeric characters before doing any sort of analysis, as well as
          convert each alphabetical character to one case

Questions:
    - If we are given an empty string, should we return True?
    - How should we proceed if a string has no alphanumeric characters?

*** Step 2: Examples and test cases ***
Observations:
    - Confirmed my understanding that a string with all lowercase, all numbers, combo of letters and numbers
      behaves as expected
    - We see that when we have a combo of uppercase, lowercase, and other characters, as per the last test case,
      we should strip out non alphanumeric characters and ignore case before determining if it is a palindrome

*** Step 3: Data structures ***
Strings only. We'll return boolean as well from the function we write.

*** Step 4: Algorithm ***
    1. Take a string as input
    2. Clean up the string by taking out non-alphanumeric characters, as well as converting remaining characters
       to one case (lowercase)
    3. Compute the reversed version of the cleaned up string
    4. Compare this reversed version to the cleaned up string
        a. If both values match, return True
        b. Else, return False

I'm going to quickly break out step 2 to think through how to implement this:
Problem: Clean up non-alphanumeric characters from a string + convert to lowercase
Input: string
Output: new string
Algorithm:
    1. Assign a new variable 'new_str' to an empty string
    2. Loop through each character in the input string
    3. If character is alphanumeric, add on the lowercase version of the character onto the end of the string
    4. Otherwise, repeat until we get to the last character of the string

"""

def clean_up_string(string):
    new_str = ''
    for char in string:
        if char.isalnum():
            new_str += char.lower()
    
    return new_str

def is_real_palindrome(string):
    cleaned = clean_up_string(string)
    reversed = cleaned[::-1]
    return reversed == cleaned


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True