"""
Write a function that takes a list as an argument and reverses its elements, in place. 
That is, mutate the list passed into the function. The returned object should be the same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).

P:
Input: List
Output: Mutated list
Rules:
    - Explicit
        - The function will mutate the list passed in
        - The function will reverse the input list's arguments in place
        - The function should not use the reverse method or slicing.
    - Implicit
        - An empty input list means an empty output list
        - If the list passed in is of odd length, the middle element remains in its original spot
        - If the list passed in only has one element, we should return the list as is, as there is nothing to reverse

E: Confirmed

D: We'll use a range to iterate through half of the input list to swap elements from one half to the other

A:
    - Calculate the halfway index by taking the length of the input list and integer dividing by 2
    - For an variable 'idx' ranging from 0 to the halfway index (exclusive):
        - Assign a variable 'current_index_value' to the value at the index 'idx' within the input list
        - Get the value at the index equal to the length of the input list - 1 - 'idx' and reassign the element
          at index 'idx' to that value
        - Reassign the element at the index equal to the length of the input list - 1 - 'idx' to 'current_index_value'
    - Return the input list object
"""

def reverse_list(lst):
    halfway_index = len(lst) // 2
    for idx in range(halfway_index):
        current_index_value = lst[idx]
        lst[idx] = lst[len(lst) - 1 - idx]
        lst[len(lst) - 1 - idx] = current_index_value
    return lst
        

# Test cases
list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True