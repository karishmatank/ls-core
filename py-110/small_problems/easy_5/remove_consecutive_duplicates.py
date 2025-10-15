"""
Given a sequence of integers, filter out instances where the same value occurs successively, 
retaining only the initial occurrence. Return the refined sequence.

P:
Input: List of integers
Output: List of integers
Rules:
    - Explicit
        - The output list filters out instances where the same value occurs successively, retaining only the initial
          occurrence
    - Implicit
        - The output is not a mutation of the input list
        - An empty input list should return an empty output list
        - Successive match means that the element in a given index and the value in the index immediately prior match in value

E: Confirmed

D: We'll use a list to build the non-consecutive elements

A:
    - Assign an empty list to the variable 'unique_elements'
    - For each number in the input list:
        - If 'unique_elements' is empty or the value of the last element of 'unique_elements' is not equal to the number:
            - Add the number to the end of 'unique_elements'
    - Return 'unique_elements'

"""

def unique_sequence(numbers):
    unique_elements = []
    for num in numbers:
        if not unique_elements or unique_elements[-1] != num:
            unique_elements.append(num)
    return unique_elements


# Test cases
original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True