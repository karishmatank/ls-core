"""
Write a function that takes two sorted lists as arguments and returns a new list that contains all the 
elements from both input lists in ascending sorted order. You may assume that the lists contain either 
all integer values or all string values.

You may not provide any solution that requires you to sort the result list. You must build the result list 
one element at a time in the proper order.

Your solution should not mutate the input lists.

P: Given two sorted lists, create a new list that combines the lists and places the combined elements in ascending order.

Rules:
    - Lists contain elements of the same data type, either all integer or all string
    - Do not use a built-in method or function to sort the list. Build the output list on element at a time
    - Do not mutate the input lists
    - If one of the input lists is empty, the result will be equal to the non-empty input list
    - Lists may contain repeating values
    - The input lists are already sorted themselves

E:
    [1, 5, 9] and [2, 6, 8]
    - Smallest value list1 is 1
    - 1 is smaller than all values in list2, so it becomes our first element
    - Smallest value now in list1 is 5
    - 2 in list2 is smaller than 5, so 2 is our next element in the output
    - 5 is the next smallest element in both lists
    - Then 6
    - Then 8
    - Then 9

    [1, 1, 3] and [2, 2]
    - Smallest value is 1
    - Second smallest value is also 1
    - Then 2
    - 2 again
    - 3

D:
    - Input: Two lists
    - Output: List with elements sorted one-by-one
    - Intermediary:
        - List: 
            - Record which elements of list1 or list2 we've already included in our output to help us account for repeating
                values
            - Create deep copies of the input lists and mutate those copies as we sort elements
        - Dictionary: Initialize a dictionary that includes elements as keys and their counts as values (1, 2, ...). When we
          include an element matching a key in our output, decrement the associated value

High-level ideas:
    - Create copies of the input lists. Find the smallest element in each and compare. Add the smaller element to the output 
      list. Repeat until we have gone through all elements of both lists.
    - Create a dictionary that includes the elements as keys and their counts as values. Create an output list that sorts
      the keys one by one, adding the element by the number of times specified by its value

A:
    - Create a new list 'lst1', which is a deep copy of the first list argument
    - Create a new list 'lst2', deep copy of second list argument
    - Create an empty list 'sorted_lst'
    - While both 'lst1' and 'lst2' have remaining elements:
        - Compare the first elements of each list
        - If 'lst1' has the smaller element (or equal):
            - move_smallest with lst1 as input
        - Else:
            - move_smallest with lst2 as input
    - If only lst1 has elements:
        - Add the rest of the lst1 elements to 'sorted_lst'
    - If only lst2 has elements:
        - Add the rest of the lst2 elements to 'sorted_lst'
    - Return 'sorted_lst'

    - Helper: move_smallest
        - Input: One of the two list copies (lst1 or lst2), output list 'sorted_lst'
        - Output: None
        - Algo:
            - Find the smallest element in the list copy
            - Add to the output list
            - Remove from the list copy

"""

def move_smallest(copied_list, output_list):
    output_list.append(copied_list[0])
    copied_list.remove(copied_list[0])

def merge(input1, input2):
    lst1 = input1.copy()
    lst2 = input2.copy()
    sorted_lst = []

    while lst1 and lst2:
        if lst1[0] <= lst2[0]:
            move_smallest(lst1, sorted_lst)
        else:
            move_smallest(lst2, sorted_lst)
    
    sorted_lst.extend(lst1)
    sorted_lst.extend(lst2)

    return sorted_lst
                


# Test cases
# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)