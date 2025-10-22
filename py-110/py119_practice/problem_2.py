"""
Create a function that takes a list of integers as an argument. The function should return the minimum sum of 5 consecutive numbers in the list. If the list contains fewer than 5 elements, the function should return None.

P:
Given a list of integers, return the smallest sum of any 5 consecutive numbers. Return None if fewer than 5 numbers.

Rules:
    - The list can have both positive and negative integers
    - If the input list has fewer than 5 numbers, return None
    - Minimum sum is the smallest sum, including sign of integers
        - [2, 3, 4, 5, -5] => 9, *not* turned into [2, 3, 4, 5, 5] => 19
    - Consecutive means maintain order of the input list

E:
[1, 2, 3, 4, 5, -5]
- [1, 2, 3, 4, 5] => 15
- [2, 3, 4, 5, -5] -> 9 *

[1, 2, 3, 4, 5, 6]
- [1, 2, 3, 4, 5] => 15 *
- [2, 3, 4, 5, 6] => 20

[-1, -5, -3, 0, -1, 2, -4]
- [-1, -5, -3, 0, -1] => -10 *
- [-5, -3, 0, -1, 2] => -7
- [ -3, 0, -1, 2, -4] => -6

Data structures:
    - Input: List of integers
    - Output: Either int or None
    - Intermediary
        - Integer: Tracks the smallest sum
        - Range: Iterates through list
            - Start: Beginning
            - End: element 5th from the End

High-level strategies:
    - Iterate through a range starting from the beginning and ending at the 5th from the end. If the sum of the 5 elements starting at each index is less than current lowest sum, it becomes the new lowest. Return the lowest sum.

A:
    - Set variable 'NUM_COMPARE' to 5
    - If the length of input < 5:
        - Return None
    - Create variable 'lowest_sum', set to None
    - For an index starting at 0, ending at the length of input - NUM_COMPARE + 1
        - Get the NUM_COMPARE number of elements starting at the index
        - Calculate sum
        - If sum < current 'lowest_sum' or no 'lowest_sum':
            - Replace 'lowest_sum' with new sum
    - Return 'lowest_sum'

"""

NUM_COMPARE = 5

def minimum_sum(numbers):
    if len(numbers) < 5:
        return None

    lowest_sum = None
    for idx in range(len(numbers) - NUM_COMPARE + 1):
        elements = numbers[idx:idx + NUM_COMPARE]
        sum_elements = sum(elements)

        if not lowest_sum or sum_elements < lowest_sum:
            lowest_sum = sum_elements
        
    return lowest_sum

    

# Test cases
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)