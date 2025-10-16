"""
Rotation (Part 1)
Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.

If the input is an empty list, return an empty list.
If the input is not a list, return None.
Review the test cases below, then implement the solution accordingly.

Copy Code
# All of these examples should print True

P:
Input: list
Output: list
Rules:
    - Explicit
        - The output should rotate the input list
        - Rotation means to move the first element of the list to the end
        - Return a new list, do not mutate the input
        - If input is empty list, return an empty list
        - If input is not a list, return None
    - Implicit
        - Type of the elements probably does not matter, as long as the input is a list Type
        - If the input only has one element, we should probably just return a list with the same value as the input
        - Assume there is an input argument, even if not a list

E: Confirmed

D: We are going to want to create a new list, which I'm guessing will just be the list we output at the end

A:
    - Check the data type of the input
        - If it is not a list, return None
    - If the input is an empty list, return an empty list
    - Take all of the elements of the input list besides the first element and add to a new list object as individual elements
    - Take the first element of the input list and append it to the end of the new list object
    - Return the list object

"""

def rotate_list(data):
    if not isinstance(data, list):
        return None
    if not data:
        return []
    return data[1:] + [data[0]]

    # if len(data) < 1:
    #     return []
    
    # first, *rest = data
    # return rest + [first]



print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

