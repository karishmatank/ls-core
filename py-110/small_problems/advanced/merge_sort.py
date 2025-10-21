"""
A merge sort is a recursive sorting algorithm that works by breaking down a list's elements into nested sub-lists, then combining 
those nested sub-lists back together in sorted order.

Write a function that takes a list argument and returns a new list that contains the values from the input list 
in sorted order. The function should sort the list using the merge sort algorithm as described above. 
You may assume that every element of the list will have the same data type: either all numbers or all strings.

Feel free to use the merge function you wrote in the previous exercise.

P:
Given a list, sort the list from smallest to largest value using merge sort.

Rules:
    - The list will once again only contain all integer or all string elements
    - The output list should be the same length as the input
    - Merge sort consists of creating a series of nested sub-lists and then combining those nested sub-lists in a sorted order
    - The input list will have 2 or more elements

E: [9, 5, 7, 1] => [[9, 5], [7, 1]] => [[[9], [5]], [[7], [1]]] => [[5, 9], [1, 7]] => [1, 5, 7, 9]
   [6, 2, 7, 1, 4] => [[6, 2], [7, 1, 4]] => [[[6], [2]], [[7], [1, 4]]] => [[[6], [2]], [[7], [[1], [4]]]]
                    => [[2, 6], [[7], [1, 4]]] => [[2, 6], [1, 4, 7]] => [1, 2, 4, 6, 7]

Data structures:
    - Input: List
    - Output: List (sorted version of original)
    - Intermediary:
        - List: Sublists nested
        - Integer: Keep track of indices within the input list for where to start and end sublists

High-level ideas:
    - Create all of the necessary nested lists until each nested list only has one element. Merge each of these lists back
      together, sorting them in the process, until we are left with one list object without nested lists.

A:
    - If the length of the input list is 1
        - Return the input list
    - Get the halfway index of the list => integer divide the length of the list by 2
    - Create two new lists - one with elements up until the halfway index, and another with all elements after
    - Recursively call the function on both of these lists
    - Call our merge function on both sides
    - Return the result of calling the merge function
        
"""

# From prior exercise
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

# New for this exercise

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    halfway = len(lst) // 2
    left = merge_sort(lst[:halfway])
    right = merge_sort(lst[halfway:])
    
    return merge(left, right)


# Test cases
# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)