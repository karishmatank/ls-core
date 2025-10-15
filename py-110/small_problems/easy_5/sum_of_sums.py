"""
Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in 
that list. Examine the examples to see what we mean. You may assume that the list always contains at least one number.

P:
Input: List of numbers
Output: Integer / float?
Rules:
    - Explicit
        - The output is the sum of the sums of each leading subsequence in the list
        - Assume that the list always contains at least one number
    - Implicit
        - "Leading subsequence" implies a subsequence of each element of the list alongside the elements that come prior
        - "Sums of the sums of each leading subsequence" implies that we take the sum of the elements in each subsequence,
          and then take the sum of all the resulting sums
        - An empty input list means we should return 0
        - An input list with one element means we should return the value of the element
        - Assume the numbers in the input list are integers

E: Confirmed

D: We can use intermediary lists to keep track of each subsequence as its own list. We can also use a range to iterate
   through the input list

A:
    - Assign a variable 'total_sum' to 0
    - For each index ranging from 0 to the length of the input list:
        - Create a new list that contains the elements from the start of the list 
          up to and including the element we are looping over. Assign to a variable 'subsequence'
        - Calculate the sum of these elements in 'subsequence' and add to the current value of 'total_sum'
    - Return 'total_sum'

"""

def sum_of_sums(numbers):
    total_sum = 0
    for idx in range(len(numbers)):
        subsequence = numbers[:idx + 1]
        total_sum += sum(subsequence)
    return total_sum

# Test cases
print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True