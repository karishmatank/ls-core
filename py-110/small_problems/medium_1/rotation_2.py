"""

Write a function that rotates the last count digits of a number. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

P:
Input: Two integers
Output: Integer
Rules:
    - Explicit
        - The output integer rotates the last count digits of a number
        - Rotation means that we move the first of the digits that we want to rotate to the end, shift the remaining digits to the left
    - Implicit
        - The second argument specifies the index **from the right**, where we should get the digit X spots from the right, as specified by the second argument, and move that digit to the end of the integer, while shifting digits to the right "forward" (to the left)
        - Assume that we'll always have 2 arguments
        - Assume that the two arguments will always be integers
        - Assume that the second argument will refers to an index that is smaller than the number of digits in the first argument

E: Confirmed

D: Intermediary string to parse through each of the digits, intermediary list to change the order of the digits

A:
    - Coerce the first argument into a string, assign to variable 'input_str'
    - Turn 'input_str' into a list, assign to variable 'digits'
    - Assign a variable 'idx' to the negative value of the second argument
    - Find the element referenced by index 'idx' in 'digits'
    - With that element, remove the element from the list and add to the end of the list, mutating 'digits' in the process
    - Combine all of the strings in 'digits' into one string, coerce to an integer, return this integer

"""

def rotate_rightmost_digits(num, places):
    input_str = str(num)
    digits = list(input_str)

    idx = -places
    new_last_element = digits.pop(idx)
    digits.append(new_last_element)

    return int(''.join(digits))


# Examples

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
