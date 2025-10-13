"""
Transform two lists into frozen sets and find their common elements.

P:
Input: Two lists
Output: Frozen set
Rules:
    - Explicit
        - We are to transform two input lists into frozen sets
        - The output should be a frozenset that consists of the common elements between both inputs
    - Implicit
        - Assume that one empty input list means we should return an empty frozen set
        - Based on the test case, assume the input lists will contain integer elements

E: Confirmed

D: We'll use frozen sets when converting our input lists.

A:
    - Convert the first argument into a frozenset
    - Convert the second argument into a frozenset
    - Create a new frozenset based on the elements in common between the prior created frozensets, return this result

"""

def intersection(lst1, lst2):
    return frozenset(lst1).intersection(frozenset(lst2))

# Test cases
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True