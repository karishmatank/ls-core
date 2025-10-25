"""
Create a function that takes a list of integers as an argument. Determine and return the index N for which all numbers with an index less than N sum to the same value as the numbers with an index greater than N. If there is no index that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the smallest value.

The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to the right of the last element is 0.

P:
Given a list of numbers, find the index such that all numbers to the "left" of the index sum to the same as all numbers to the "right" of the index. Return -1 if no index like this exists.

Rules:
    - Don't include index N when calculating any sums
    - If the list has multiple indices, return the smallest index
    - If no index that fulfills this exists, return -1
    - Sum of numbers to the left of index 0 is 0
    - Sum of numbers to the right of the last element is 0


[1, 2, 4, 4, 2, 3, 2]
- Index 3: Left is [1, 2, 4] = 7. Right is [2, 3, 2] = 7

[7, 99, 51, -48, 0, 4]
- Index 1: Left is [7] = 7. Right is [51, -48, 0, 4] = 7

Data structures:
    - Input: List of integers
    - Output: Integer
    - Intermediary
        - List: Elements on left vs elements on right
        - Integers: Left sum vs right sum
        - Range: Iterate through input list
        - Boolean: Are the sums equal? Yes/no

High-level ideas:
    - Iterate through input. For each index, calculate sum of elements to its left vs to its right. If sums match, return the index of the current element.
    - Calculate the total sum of the list. As we iterate through each element, recalculate the left and right sums. Return the index of the current element if they match

A:
    - For an 'idx' starting from 0, ending at last element:
        - Get a list of numbers with index less than 'idx' => 'left'
        - Get a list of numbers with index greater than 'idx' => 'right'
        - *is_matching_sum* => Input: 'left', 'right'
        - If sums match, return 'idx'
    - Return -1

*is_matching_sum*
    Input: 2 lists
    Output: Boolean
    Algo:
        - Calculate sum of each list
            - If a list is empty, sum is 0
        - If sums match, return True. Otherwise, False

"""

def is_matching_sum(left_list, right_list):
    left_sum = sum(left_list)
    right_sum = sum(right_list)

    return left_sum == right_sum

def equal_sum_index(numbers):
    for idx in range(len(numbers)):
        left = numbers[:idx]
        right = numbers[idx + 1:]
        if is_matching_sum(left, right):
            return idx
    return -1


# # Test cases
print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)


"""
Reflection:
Time: 20 min 15 seconds. Pretty straightforward. Took me longer than expected but process was very smooth.
"""