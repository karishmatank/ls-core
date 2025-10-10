"""
Write a function that takes two list arguments, each containing a list of numbers, 
and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. 
You may assume that the arguments contain the same number of elements.

P:
Input: Two lists
Output: New list
Rules:
    - Explicit
        - The two list inputs each contain a list of numbers
        - The output list contains the product of each pair of number from the arguments with the same index
            - i.e. [1, 2] and [3, 4] as inputs should produce [3, 8]
        - The arguments will contain the same number of elements
        - The output list should not mutate either of the two input lists
    - Implicit
        - Assume that the lists won't be empty
        - Assume that the lists will only consist of elements that are integers or floats

Questions:
    - How should we handle empty input lists?
    - Will the elements always be integers or floats? Or can they be of other types?

E:
    - Confirmed my understanding

D:
Lists and ranges to iterate over the indices per list

A:
    - Assign a variable 'result' to an empty list
    - For an index that starts at 0 and ends at the length of each list - 1 (inclusive):
        - Multiply the elements at that index in the first input list and the second input list
        - Add that result to the end of of the 'result' list
    - Return 'result'

"""

def multiply_list(list1, list2):
    result = []
    for idx in range(0, len(list1)):
        result.append(list1[idx] * list2[idx])
    return result

# Test cases
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True