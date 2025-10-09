"""
Write a function that takes a list as an argument and returns a list that contains two elements, 
both of which are lists. Put the first half of the original list elements in the first element of the return value 
and put the second half in the second element. If the original list contains an odd number of elements, 
place the middle element in the first half list.

P:
Input: List
Output: New list with two nested lists
Rules:
    - Explicit
        - The first nested list in the output will contain the elements of the first half of the original list
        - The second nested list in the output will contain the elements of the second half of the original list
        - If the original list contains an odd number of elements, place the middle element in the first half list
    - Implicit
        - An input list with an even number of elements will see an output list with two nested lists of the same length
        - An input list with an odd number of elements will see an output list with the first nested list longer than
          the second nested list by 1 element
        - If our input list only has one element, we should place that element in the first nested list, leaving the second
          nested list empty
        - An empty input list means we should return an output list with empty nested lists
        - Assume there are no changes in behavior based on different element data types

Questions:
    - How would we treat an input list with only one element? Should that element go in the first nested list while the
      second nested list is empty?
    - How should we treat an empty input list?
    - Does the behavior of this program change based on element data type?

D:
Lists mainly

A:
    - Get the length of the input list
    - Calculate the index at which the second nested list will start
        - If the length is an odd number, our second nested list will start at an index of the length // 2 + 1
        - If the length is even, our second nested list will start at an index of length // 2
    - Separate the input list into two new lists based on the index we previously calculated
    - Combine both lists as separate elements inside a new list and return this result

"""

def halvsies(lst):
    length = len(lst)
    if length % 2 == 0:
        idx_split = length // 2
    else:
        idx_split = length // 2 + 1
    
    lst1 = lst[:idx_split]
    lst2 = lst[idx_split:]
    return [lst1, lst2]


# Test cases
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])