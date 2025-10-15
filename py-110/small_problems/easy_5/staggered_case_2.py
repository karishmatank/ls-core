"""
Modify the function from the previous exercise so it ignores non-alphabetic characters when determining 
whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included 
in the return value; they just don't count when toggling the desired case.

P:
Input: String
Output: String
Rules:
    - Explicit
        - The output returns the input with a staggered capitalization scheme
        - Staggered capitalization means that every other character, starting from the first, should be capitalized
          and followed by a lowercase or non-alphabetical character
        - Non-alphabetical characters should not be counted as characters for determining when to switch between 
          upper and lower case
        - Non-alphabetical characters should, however, still be included in the output
    - Implicit
        - An empty input string means an empty output string

E: Confirmed

D: We'll use an intermediary list to separate out the characters in the string.

A:
    - Create an empty string, assign to variable 'staggered'
    - Assign a variable 'last_alpha' to an empty string
    - For each character in the input list:
        - If the character is not alphabetical:
            - Append the character to the end of 'staggered'
            - Continue to the next iteration
        - If last_alpha is an empty string or 'last_alpha' is a lowercase character:
            - Convert the character into an upper case, assign to 'new_char'
        - Else (last_alpha' is an uppercase character):
            - Convert the character into lower case, assign to 'new_char'
            
        - Append 'new_char' to 'staggered'
        - Reassign 'last_alpha' to the value of 'new_char'
            
    - Return 'staggered'

"""

def staggered_case(text):
    staggered = ""
    last_alpha = ""
    for char in text:
        if not char.isalpha():
            staggered += char
            continue

        if not last_alpha or last_alpha.islower():    
            new_char = char.upper()
        else:
            new_char = char.lower()
        
        staggered += new_char
        last_alpha = new_char
    
    return staggered


# Test cases
string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True