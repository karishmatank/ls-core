"""
Create a function that takes a list of numbers as an argument. For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.

P:
Given a list of numbers, return a list of the same size detailing # of numbers smaller than each element.

Rules:
    - Assume that our input list will have 1 or more integers
    - Only count unique values - don't count the same value multiple times if it is in the list multiple times
    - If list only has one element, return a list with element 0


[8, 1, 2, 2, 3]
- 8: 1, 2, 3 smaller than 8 -> 3
- 1: none smaller -> 0
- 2: 1 smaller -> 1
- 2: 1 smaller -> 1
- 3: 2 smaller -> 2

Data structures:
    - Input: List of integers
    - Output: List of integers (representing counts)
    - Intermediary:
        - Set: Get unique elements less than the element in question
        - Range: Iterate through the list
        - Boolean: Is another element less than the current element? Yes/no

High-level strategies:
    - Iterate through the input list. For each element, count the unique values less than the value of the element. Store in a list and return

A:
    - Create an empty list 'count_smaller'
    - For each element of the input list:
        - Get unique values less than the element's value -> *get_smaller*
        - Count the number of unique values
        - Add the count to the end of 'count_smaller'
    - Return 'count_smaller'

get_smaller: Get unique values less than a given value
Input: integer, list
Output: Set
Algo:
     - Get all elements in list smaller than the input int's value
     - Create a set out of those elements
     - Return the set

"""

def get_smaller(value, numbers):
    smaller_values = [num for num in numbers if num < value]
    return set(smaller_values)


def smaller_numbers_than_current(numbers):
    count_smaller = []
    for num in numbers:
        smaller = get_smaller(num, numbers)
        count_smaller.append(len(smaller))
    return count_smaller


# print(smaller_numbers_than_current([8, 1, 2, 2, 3]))

# Test cases
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

"""
Time: 16 min 50 s
"""