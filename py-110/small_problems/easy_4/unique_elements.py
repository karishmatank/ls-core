"""
From two list arguments, determine the elements that are unique to the first list. 
The return value should be a set.

P:
Input: Two lists
Output: Set
Rules:
    - Explicit
        - Determine the elements that are unique to the first list, so elements in the first list not in the second list
        - The output should be those elements unique to the first list in a set
    - Implicit
        - Assume both inputs won't be empty lists
        - Assume duplicate elements in a list will only be represented once in the output, if the element is qualified to 
          be in the output

E: Confirmed

D:
We'll use intermediate set objects to represent the numbers in either list

A:
    - Turn both input lists into sets
    - Get the elements in the set created from the first argument that are not in the set created from the second argument
        - We'll check this by determining whether an element in the set created from the first argument is not in the set
          that would result if we took the intersection between both sets
    - Return the resulting set

"""

def unique_from_first(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)

    return {element for element in set1 if element not in set1.intersection(set2)}

# Test cases
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})