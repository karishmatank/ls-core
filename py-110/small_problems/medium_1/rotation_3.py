"""
Rotation (Part 3)
Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

ExamplesCopy Code

P:
Input: Integer
Output: Integer
Rules:
    - Explicit
        - Maximum rotation means to iterate through each "place" of the digit, and remove and add the element at that place to the very end. Start with the first digit and rotate, then rotate the second digit of the resulting integer, all the way to the second to last digit of the integer
    - Implicit
        - Assume that we'll have a valid integer argument
        - If input is one digit, return the input

E: Confirmed

D: Intermediary string to work with the integer , as well as an intermediary list to work with the individual digits. We may want to use a range to iterate through the indices of one of the intermediary objects we use

A:
    - Coerce the input into a string, assign to variable 'input_str'
    - For an index that ranges from length of the 'input_str' to 1 (exclusive), incrementing downward as we go
        - Use the rotate_rightmost_digits function, passing in the current value of the input argument as the first argument and the current index as the second argument
        - Reassign the input argument to the result of the prior step
    - Return the latest value of the input argument

"""

def rotate_rightmost_digits(num, places):
    input_str = str(num)
    digits = list(input_str)

    idx = -places
    new_last_element = digits.pop(idx)
    digits.append(new_last_element)

    return int(''.join(digits))

def max_rotation(number):
    input_str = str(number)
    for idx in range(len(input_str), 1, -1):
        return_value = rotate_rightmost_digits(number, idx)
        number = return_value
    return number


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True



"""
Rotation (Part 1): Start time 5:19 to 5:18
Rotation (Part 2): start time 5:36 to 5:45
Rotation (Part 3): start time 5:56 to 6:10

"""