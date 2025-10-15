"""
Given two lists of integers of the same length, return a new list where each element is the product 
of the corresponding elements from the two lists.

P:
Input: Two lists of integers
Output: New list
Rules:
    - Explicit
        - The two input lists will be the same length
        - The output list is the product of the corresponding elements from the two lists
    - Implicit
        - "Corresponding elements" is defined as elements from both input lists with the same index
        - The output list will have the same length as both input lists
        - Empty input lists mean an empty output list

E: Confirmed

D: We'll build the results in a list that we'll return. We can also use a range to iterate through each index

A:
    - Assign an empty list to the variable 'products'
    - For an index ranging from 0 to the length of the input lists:
        - Add an element to the end of products whose value is the product between the element at the current index
          in the first input list and the element at the current index in the second input list
    - Return 'products'

"""

def multiply_items(lst1, lst2):
    products = []
    for idx in range(len(lst1)):
        products.append(lst1[idx] * lst2[idx])
    return products

# Test cases
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True