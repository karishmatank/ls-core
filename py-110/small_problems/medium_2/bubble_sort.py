"""
In this exercise, you will write a function that sorts a list using the bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list. On each pass, the two values of each pair of consecutive elements are compared. If the first value is greater than the second, the two elements are swapped. This process is repeated until a complete pass is made without performing any swaps. At that point, the list is completely sorted.

We can stop iterating the first time we make a pass through the list without making any swaps since that means the entire list is sorted.

Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm described above. The sorting should be done "in-place" -- that is, the function should mutate the list. You may assume that the list contains at least two elements.

P:
Given a list, sort this list using bubble sort. Mutate the input list in the process.

Rules:
    - Mutate the input list
    - On each pass, compare two consecutive elements and swap if the first value (left most) is greater than the second (right)
    - Repeat each pass until we make no swaps
    - If we receive a list of integers, sort from smallest to largest
    - If we receive a list of strings, sort lexicographically, a-z
    - Assume the lists we receive will have elements that we can compare to each other

E:
lst2 = [6, 2, 7, 1, 4]
lst2 = [2, 6, 7, 1, 4]
lst2 = [2, 6, 7, 1, 4]
lst2 = [2, 6, 1, 7, 4]
lst2 = [2, 6, 1, 4, 7]
...

Data structures:
    - Input: List of comparable elements
    - Output: Return none, mutate list in place
    - Intermediary
        - Integer: 
            - Keep track of the number of swaps we do in a pass
            - Integers to store values as we swap them
        - Range:
            - Iterate through pairs of consecutive elements
        - Boolean:
            - Is the value at the lower index > value at the higher index? Yes / no

High-level ideas:
    - Use a range to iterate through the list. Make swaps as necessary. Once we run through the list without making swaps, we are done.

A:
    - Iterate through each element, starting from the first and ending at the second to last index
    - Set a 'swaps' variable to the value 0
    - For each element and the one to the right of it:
        - If the value at the lower index > value at the higher index:
            - Set a 'smaller' variable to the value of the element at the higher index
            - Set a 'larger' variable to the value of the element at the lower index
            - Replace the value at the lower index with 'smaller'
            - Replace the value at the higher index with 'larger'
            - Increment 'swaps' by 1
    - If 'swaps' is 0, then we're done. Otherwise, repeat the process above
"""

def bubble_sort(lst):
    while True:
        swaps = 0
        for idx in range(len(lst) - 1):
            if lst[idx] > lst[idx + 1]:
                smaller = lst[idx + 1]
                larger = lst[idx]
                lst[idx] = smaller
                lst[idx + 1] = larger
                swaps += 1
        if swaps == 0:
            break

# Test cases
lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True

"""
Reflection: Just over 17 minutes. Did a good job testing and talking through everything.
"""