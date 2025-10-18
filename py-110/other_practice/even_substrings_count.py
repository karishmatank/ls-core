"""
Create a function that takes a string of digits as an argument and returns the number of even-numbered 
substrings that can be formed. For instance, in the string '1432', the even-numbered substrings are 
'14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

P:
Input: String of digits
Output: Integer
Rules:
    - Explicit
        - The output represents the number of even-numbered substrings that can be formed with the input string digits
        - Count duplicate substrings if they occur more than once
    - Implicit
        - Keep the order of the digits as per the input. For example, for '1432', we wouldn't count '1342' as a valid substring
        - Even-numbered substring refers to a substring where the last digit is an even number
        - Even-numbered substrings can be one or more digits
        - If the input string itself is even-numbered, it counts as a substring of itself (i.e. '1432' is a substring of '1432')
        - Assume our input will be made up of all digits and no other characters

Data structures:
    - We may be able to use a list to separate out the digits and form substrings that way
    - We may decide to form intermediary strings that are the substrings of our input
    - We may need a range to iterate over the indices of our input string

High-level ideas:
    - Iterate through the string to look for an even numbered digit. When we find one, create all substrings using the digits
      that come prior to the current even-numbered digit to form our substrings
    - Create a master list of all substrings that maintain the input digit order. Filter down to substrings that end with an
      even digit

A:
    - Create an empty list called 'even_substrings'
    - Iterate through each digit of the input string
    - If the current digit is an even number:
        - Record the index of this digit
        - Form substrings that end with the current digit by altering the start index 
          (for '1432', on '4', we would get '14' and '4' before we move on to the other digits in the string)
        - Add each substring to 'even_substrings'
    - Return the length of 'even_substrings'

Subproblem: Current digit is an even number
Input: String (character)
Output: Boolean
Algorithm:
    - Convert string to integer
    - If it is even, return True, else return False

"""

def is_even(char):
    return int(char) % 2 == 0

def even_substrings(input_str):
    even_substrings = []
    for idx, digit in enumerate(input_str):
        if is_even(digit):
            substrings = [input_str[idx_start:idx + 1] for idx_start in range(0, idx + 1)]
            even_substrings.extend(substrings)
    return len(even_substrings)



# Test cases
print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('2468') == 10)
print(even_substrings('246824') == 21)