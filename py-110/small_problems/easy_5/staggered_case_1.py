"""
Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. 
Every other character, starting from the first, should be capitalized and should be followed by a lowercase 
or non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters 
for determining when to switch between upper and lower case.

P:
Input: String
Output: String
Rules:
    - Explicit
        - The output returns the input with a staggered capitalization scheme
        - Staggered capitalization means that every other character, starting from the first, should be capitalized
          and followed by a lowercase or non-alphabetical character
        - Non-alphabetical characters should not be changed but should be counted as characters for determining when to
          switch between upper and lower case
    - Implicit
        - An empty input string means an empty output string

E: Confirmed

D: We'll use an intermediary list to separate out the characters in the string.

A:
    - Create a new list out of the input string, which will create individual elements for each of the characters
      in the input string. Assign this to variable 'characters'
    - For each index and character in 'characters':
        - If the index is divisible by 2:
            - Reassign the element at that index in 'characters' to the uppercase version of the current character
        - Else:
            - Reassign the element at that index in 'characters' to the lowercase version of the current character
    - Combine the characters in 'characters' back into one string and return this value

"""

def staggered_case(text):
    characters = list(text)
    for idx, char in enumerate(characters):
        if idx % 2 == 0:
            characters[idx] = char.upper()
        else:
            characters[idx] = char.lower()
    return ''.join(characters)

# Test cases
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True