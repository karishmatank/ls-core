"""
Create a function that takes a list of integers and returns the length of the longest consecutive elements sequence. 
The sequence doesn't need to be sorted.

P:
Input: List of integers
Output: Integer
Rules:
    - Explicit
        - The output integer represents the length of the longest consecutive elements sequence
    - Implicit
        - An empty input list means we return the integer 0
        - The input list doesn't necessarily come pre sorted, so if we have [4, 1, 3, 2], we shouldn't rely on the order
          passed in
        - Elements may be duplicated, which shouldn't factor into the end result. [1, 1, 2, 2, 3, 3] effectively turns into
          [1, 2, 3], which means a result of 3
        - Consecutive elements means that each element of the sequence is one more than another element in the sequence
        - Assume that if there is are only "disjointed" elements, where "disjointed" means that every element is not part of a 
          consecutive elements sequence, that we should return 1

E: Confirmed

D:
- We can use a set to handle unique elements from the input list
- We'll use a range to iterate through the indices of the numbers list

A:
    - If the length of the input list is 0:
        - Return 0
    - Create a set from the input list so that we can work with unique elements. Assign that to a variable 'unique_numbers'
    - Turn the set back into a list and sort from lowest to highest integer. Assign that to a variable 'sorted_list'
    - Assign the value 1 to a variable 'longest_count'
    - Assign the value 1 to a variable 'current_count'
    - For each element in 'sorted_list', starting from index 1:
        - If the current element is 1 larger than the prior element in the list:
            - Increment current_count by 1
        - Else
            - Set the value of longest_count to the max of the values of current_count and longest_count
            - Reassign current_count to 0
    - At the end of our loop, set the value of longest_count to the max of the values of current_count and longest_count
    - Return 'longest_count'
"""

def longest_consecutive(numbers):
    if not numbers:
        return 0

    unique_numbers = set(numbers)
    sorted_list = sorted(unique_numbers)
    
    longest_count = 1
    current_count = 1
    for idx in range(1, len(sorted_list)):
        if sorted_list[idx] == sorted_list[idx - 1] + 1:
            current_count += 1
        else:
            longest_count = max(current_count, longest_count)
            current_count = 0
    longest_count = max(current_count, longest_count)
    return longest_count
        

# Test cases
print(longest_consecutive([100, 4, 200, 1, 3, 2]) == 4) # The sequence is [1, 2, 3, 4]
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 9, 1]) == 10)
print(longest_consecutive([]) == 0)
print(longest_consecutive([1, 1, 2, 2, 3, 3]) == 3)