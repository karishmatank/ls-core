"""
Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. The first list contains two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

P:
Given a list of numbers, count all occurrences of *complete pairs* of repeating numbers.

Rules:
    - Pairs means 2 elements with identical values
    - If the list is empty or < 2 elements, there are no pairs -> return 0
    - If a value occurs more than twice, only count the number of *complete pairs*
        - Ex: [3, 3, 3] only creates 1 pair of 3's, with one left over


[3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]
[1, 4, 2, 6, 5, 8, 7]
    - [3, 3]
    - [5, 5]
    - [9, 9] => 3

[2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]
[7, 2, 4]
    - [2, 2]
    - [8, 8]
    - [8, 8]
    - [1, 1]

Data structures:
    - Input: List of integers
    - Output: Integer (representing a count)
    - Intermediary:
        - List: Copy of the input so that we can mutate
        - Dictionary: Keys are the elements, values are their counts

High-level strategies:
    - Create a separate copy of the input. If a value is repeated, remove the first two occurrences of this element from the list and increment a count by 1. Continue until there are no more pairs. Return the count
    - Create a dictionary with keys as the element values and values as the counts. For each key-value pair, count a pair for every 2 occurrences there are. Return the count

A:
    - Set variable 'total_pairs' equal to 0
    - *create_count_dict* => variable 'counts'
    - For each key in 'counts':
        - If value associated w/ key >= 2:
            - Divide value by 2, keeping int portion only => 'pairs'
            - Increment 'total_pairs' by 'pairs'
    - Return 'total_pairs'

*create_count_dict*
Input: List of integers
Output: Dictionary
Algo:
    - Create empty dict 'counts'
    - For each number in the input list:
        - If the element value is not a key in 'counts', add it
        - Increment value associated w/ key by 1
    - Return 'counts'
"""

def create_count_dict(integer_lst):
    counts = dict()
    for num in integer_lst:
        counts[num] = counts.get(num, 0) + 1
    return counts


def pairs(numbers):
    total_pairs = 0
    counts = create_count_dict(numbers)
    for key in counts.keys():
        num_occurrences = counts[key]
        if num_occurrences >= 2:
            pairs = num_occurrences // 2
            total_pairs += pairs
    return total_pairs


# print(create_count_dict([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]))

# # Test cases
print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

"""
Reflection:
Time: 18 min 35 s
Felt pretty easy, liked that I came up with the dict idea since that felt easier in the end
"""