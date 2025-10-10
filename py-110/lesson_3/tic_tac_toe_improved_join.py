# from tic_tac_toe_LS_walkthrough import *

"""
***** Improved "join" *****

Problem: Write a function named join_or that produces the following results:

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"

P:
Input: A list, a custom string delimiter (optional), a string to go before the last element (optional)
Output: String
Rules:
    - Explicit
        - The first argument is a list with elements that we will concatenate together
        - The second argument is what we insert between elements. Default is ", "
        - The third argument is what we insert before the last element. Default is "or"
    - Implicit
        - The list argument will have integers, if populated
        - An empty list argument means we return an empty string
        - If there is only one element in the list input, our string will not the values of the second or third arguments
        - If there are two elements in the list input, our string will not need the value of the second argument
        - The value of the second argument is present after each element except for the last element, if the list input has 3 or 
          more elements
        - The value of the third argument is present only before the last element, if the list input has 2 or more elements

E:
    - Confirmed understandings above

D: List and string inputs, use a string to build the output.

A:
    - Assign the variable 'string_output' to an empty string
    - Reassign the third argument to concatenate a space to the end
    - If the length of the input list is 1, return a string representation of the element in the list
    - If the length of the input list is 2:
        - Concatenate the first element of the list to 'string_output'
        - Concatenate a space character
        - Followed by the value of the third argument if provided. If not provided, concatenate "or"
        - Concatenate the last element
        - Return 'string_output'
    - For element in the input list:
        - Concatenate element to 'string_output'
        - If element is not the last element in the input list:
            - Concatenate the value of the second argument if provided. If not provided, concatenate ", "
        - If element is the second to last element in the input list:
            - Concatenate the value of the third argument if provided. If not provided, concatenate "or"
    - Return 'string_output'

"""

def join_or(lst, delimiter=", ", before_last_element="or"):
    string_output = ""
    before_last_element += " "

    if len(lst) == 1:
        return str(lst[0])
    elif len(lst) == 2:
        string_output = f"{lst[0]} {before_last_element}{lst[1]}"
    else:
        for idx, element in enumerate(lst):
            string_output += str(element)
            if idx != len(lst) - 1:
                string_output += delimiter
            if idx == len(lst) - 2:
                string_output += before_last_element
    
    return string_output


# Improved "join" test cases
print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"
