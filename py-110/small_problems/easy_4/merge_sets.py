"""
Given two lists, convert them to sets and return a new set which is the union of both sets.

P:
Input: Two lists
Output: A new set
Rules:
    - Explicit
        - Our output will be a set that represents the union of two sets
        - The sets that will be combined (into a union) represent set representations of the input lists
    - Implicit
        - An input list can be empty
        - Based on the test cases, we'll assume the input lists are made up of integer elements

E: Confirmed

D: We'll use intermediary sets, which will be created off of the input lists, before creating our output set

A:
    - Convert the first argument into a set
    - Convert the second argument into a set
    - Combine both sets into one
    - Return the result from the previous step
"""

def merge_sets(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return set1 | set2

# Test cases
list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True