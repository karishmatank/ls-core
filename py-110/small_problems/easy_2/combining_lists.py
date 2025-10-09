"""
Write a function that takes two lists as arguments and returns a set 
that contains the union of the values from the two lists.
You may assume that both arguments will always be lists.

P:
Input: Two lists
Output: Set
Rules:
    - Explicit
        - Both arguments will always be lists
        - The output set should contain the union of the values from the two lists
    - Implicit
        - One test case given shows elements with integers, assume elements will be integers?
        - Assume that if we have two elements, one with value '3' and another with value 3, they should be considered
          separate
        - Assume input lists can be empty

Questions:
    - If a list has an element with value '3' as well as the integer 3, should those be considered separate elements?
    - Should we expect both input lists to have at least one element each?

D: Sets and lists

A:
    - Find the unique elements of the list passed in as first argument
    - Find the unique elements of the list passed in as second argument
    - Combine both lists to find the unique elements of the combination
    
"""

def union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.union(set2)

# Test cases
print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True