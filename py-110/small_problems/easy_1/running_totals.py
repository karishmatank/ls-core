"""
Problem (as provided):
Write a function that takes a list of numbers and returns a list with the same number of elements, 
but with each element's value being the running total from the original list.

*** Step 1: Understand the problem ***
Input: List of numbers (perhaps int or float)
Output: List of numbers
Rules:
    - Explicit
        - Output list has same number of elements as the input
        - Each element's value of the output list is a running total from the original list
    - Implicit
        - If we receive an empty list, we should return an empty list
        - An input list of one element returns the same list back
        - (Missed - record assumptions, such as accepting int and float, assume valid input)
        - (Missed - define the concept of running total here as we did in questions)
Questions:
    - Will the numbers be a combination of integers and floats?
    - Are the integers positive, or can they be negative as well?
    - Can you define the concept of running total?
        - i.e. is the output list element at index 1 the sum of the element values at indexes 0 and 1 of the input list?
    - (Missed- Should we return a new list, or mutate the original?)

*** Step 2: Examples and test cases ***
    - Confirmed from the test cases that our understanding of running total is correct
    - Learned that an empty list should just return an empty list back + a list with one element should return that list back

*** Step 3: Data structures ***
List is most appropriate here, as we have as input a list and need to maintain order as we go along.
We also need to output a list too.
(Missed - denote the variable to keep track of the rolling sum)

*** Step 4: Algorithm ***
    1. We receive a list as input
    2. Assign a variable 'rolling_sum' to 0, as well as a variable 'return_list' to an empty list
    3. For each element in the input list:
        a. Increment 'rolling_sum' by the value of that element
        b. Append the new value of 'rolling_sum' to 'return_list'
    4. Return 'return_list'
"""

def running_total(input_list):
    rolling_sum = 0
    return_list = []
    for val in input_list:
        rolling_sum += val
        return_list.append(rolling_sum)
    return return_list


# Test cases
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True