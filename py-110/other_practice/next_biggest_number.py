"""
Write a function that takes a positive integer and returns the next bigger number that 
can be formed by rearranging its digits. If no bigger number can be formed, the function should return -1.

P:
Input: Positive integer
Output: Integer
Rules:
    - Explicit
        - The output represents the "next bigger number" that can be formed by rearranging digits
        - If not larger integer can be formed, return -1
    - Implicit
        - "Next bigger number" means an integer that is the next largest that can be formed from the digits when compared
            - For example, for the input 2017, the next largest is 2071, which is not the largest number that can be formed
          to the input, but not necessarily the largest number
        - If the number has one digit, return -1

E: Confirmed

D: We'll likely use intermediary strings to be able to work with the individual digits. We may need a range to iterate
   through these intermediary strings. We may also decide to use lists to work with the individual digits too

A:
    - Coerce the input into a string, assign to variable 'input_str'
    - Create a list that represents all of the possible integers we can form with the digits in 'input_str', assign to
      'all_possible_ints'
    - Sort 'all_possible_ints' from smallest to largest
    - Find the index of the input within 'all_possible_ints'
        - If the index of the last element in the list, return -1
        - Else, return the value at the index that is 1 larger than the index that the input number sits at

Subproblem: Create a list with all possible integers from digits
Input: String
Output: List of integers
Algorithm:
    - Assign an empty list to the variable 'numbers', add the input string as the first element to 'numbers'
    - Split the input string into a list of numerical characters, assign to 'digits'
    - For a 'digit_idx' ranging from 0 to the length of digits:
        - For a 'parse_idx' ranging from digit_idx + 1 to the length of digits + 1:
            - Take the element at 'digit_idx' and assign to variable 'current_digit'
            - Inserting 'digit_idx' into index 'parse_idx', creating a new intermediary list in the process
            - Join that list into one string and add to the end of 'numbers'
    - Get the unique elements of 'numbers', since we might get duplicates as we form 'numbers'
    - Convert each number in 'numbers' into an integer
    - Return 'numbers'

"""

def get_all_possible_integers(numeric_str):
    numbers = [numeric_str]
    digits = list(numeric_str)
    for digit_idx in range(0, len(digits)):
        for parse_idx in range(digit_idx + 1, len(digits)):
            current_digit = digits[digit_idx]
            reformed_digits = digits.copy()
            reformed_digits.pop(digit_idx)
            reformed_digits.insert(parse_idx, current_digit)
            numbers.append(''.join(reformed_digits))
    unique_numbers = set(numbers)
    return [int(num) for num in list(unique_numbers)]

def next_bigger(number):
    input_str = str(number)
    all_possible_ints = get_all_possible_integers(input_str)
    all_possible_ints.sort()
    idx = all_possible_ints.index(number)
    if idx == len(all_possible_ints) - 1:
        return -1
    return all_possible_ints[idx + 1]


# print(get_all_possible_integers('144'))

# Test cases
print(next_bigger(12) == 21)
print(next_bigger(513) == 531)
print(next_bigger(2017) == 2071)
print(next_bigger(414) == 441)
print(next_bigger(144) == 414)
print(next_bigger(9) == -1)
print(next_bigger(111) == -1)
print(next_bigger(531) == -1)