"""
Write a function that takes a list of integers and returns the index where the sum of elements to the left 
equals the sum of elements to the right. If no such index exists, return -1. 
The balance index itself is not included in either sum.

P:
Return the index from the input list where the sum of elements to the left is equal to the sum of elements to the right.

Rules:
    - The value at the index itself should not be included in either side's sum
    - If we can't find an index where the left side sum = right side sum, return -1
    - Assume the list will be non-empty
    - If an index is the first in the list, the sum to the left would be 0. Likewise for the last index and right hand sum

Data structures:
    - Input: List of integers
    - Output: Integer (representing an index)
    - Intermediary:
        - Integers: Record the left and right hand sums as we go
        - Boolean: Check if the left and right sums are equal
        - Range: Iterate through each index of the list

High-level strategies:
    - Calculate the left and right sums for each index, starting from the first element of the list. When we encounter 
      equal sums, stop and return the index
    - Calculate the total sum of all elements in the list. Recalculate the left and right sums for each index based on the
      value of the current index and last value of the left sum. Stop when we find the index where both sums are equal
        - The difference between this one and the prior one is how often we recalculate the sums of the left + right hand side
          as in the first one, we continuously recalculate whereas here, we calculate a total sum once

A:
    - For each index of the input list:
        - Calculate the sum of the elements to the left of the current index
            - If the index is 0, sum of elements ot the left will be 0
        - Calculate the sum of the elements to the right of the current index
            - If the index is of the last element of the list, sum of elements to the right will be 0
        - If both sums are equal
            - Return the index
    - If we loop through and don't find equality, return -1    

"""

def find_balance_index(numbers):
    for idx in range(len(numbers)):
        left_sum = sum(numbers[:idx])
        right_sum = sum(numbers[idx + 1:])
        if left_sum == right_sum:
            return idx
    return -1

# Test cases
print(find_balance_index([1, 2, 3, 4, 6]) == 3) # left: 1+2+3=6, right: 6=6
print(find_balance_index([1, 5, 2, 3, 4, 5, 6]) == 4) # left: 1+5+2+3=11, right: 5+6=11
print(find_balance_index([20, 10, 30, 10, 10]) == -1) # no balance point
print(find_balance_index([1, 2, 10, 3, 4]) == -1) # no balance index
