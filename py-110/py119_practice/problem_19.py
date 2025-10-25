"""
Create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times. There will always be exactly one such integer in the input list.

P:
Given a list of integers, return the integer that appears an odd number of times.

Rules:
    - There will only be one such integer in each list
    - There will always be at least one integer in the input

[7, 99, 7, 51, 99]
    - 7 appears 2x
    - 99: 2x
    - 51: 1x => return 51

[7, 99, 7, 51, 99, 7, 51]
    - 7 appears 3x => return 7
    - 99 appears 2x
    - 51 appears 2x

[25, 10, -6, 10, 25, 10, -6, 10, -6]
    - -6 appears 3x => return -6


Data structures:
    - Input: List of integers
    - Output: Integer
    - Intermediary:
        - Dictionary: Key = ele value, value = count of element
        - Set: Get all unique elements

High-level ideas:
    - Create a set of all unique elements. Iterate through set, once we find an element that occurs an odd number of times, return that element
    - Create a dictionary where key = element and value = its count. Iterate through each key value pair, and return the element with an odd value (count)

A:
    - *get_value_counts* -> Input: input list, output: 'counts'
    - For each key value pair in 'counts':
        - If value is odd, return the key


*get_value_counts*
    Input: List of integers
    Output: Dictionary
    Algo:
        - Create empty dictionary 'counts'
        - For each element in the input:
            - Check if in 'counts', add if not
            - Increment its value in 'counts' by 1
        - Return 'counts'

"""

def get_value_counts(numbers):
    counts = dict()
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return counts

def odd_fellow(numbers):
    counts = get_value_counts(numbers)
    for key, value in counts.items():
        if value % 2 == 1:
            return key


# Test cases
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

"""
Reflection: 
Time: 12 min 49 seconds. Probably too easy for the interview.
"""