"""
Write a function that combines two lists passed as arguments and returns a new list 
that contains all elements from both list arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.

P:
Input: Two lists
Output: A new list
Rules:
    - Explicit
        - The output list should take the first element from the first argument, followed by the first element
          from the second argument, and so on, interweaving elements
        - Both input lists will be non-empty
        - Both input lists will have the same number of elements
        - The output list should not mutate any one of the arguments
    - Implicit
        - Elements can be of mixed type, which shouldn't be an issue

E:
    - Confirmed understanding of problem

D:
Lists + ranges to iterate over each element in each list

A:
    - Find the length of the first argument, which will match the length of the second argument. Assign to variable 'length'
    - Assign an empty list to variable 'interleaved'
    - For an index starting from 0 and ending at 'length' - 1 (inclusive):
        - Add the element at the index in the first argument to the end of 'interleaved'
        - Add the element at the index in the second argument to the end of 'interleaved'
    - Return 'interleaved'

"""

def interleave(arg1, arg2):
    length = len(arg1)
    interleaved = []
    for idx in range(length):
        interleaved.append(arg1[idx])
        interleaved.append(arg2[idx])
    return interleaved


# Test cases
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True