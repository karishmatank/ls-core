"""
Given an unordered list and the information that exactly one value in the list occurs twice 
(every other value occurs exactly once), determine which value occurs twice. 
Write a function that finds and returns the duplicate value.

You may assume that the input list will always have exactly one duplicate value.

P:
Input: List
Output: String
Rules:
    - Explicit
        - The input list is not in any particular order
        - Every element in the input list occurs once, except for one value which occurs twice
        - The output value is to be the value that is duplicated
        - The input list will always have exactly one duplicate
    - Implicit
        - It is possible the list can have multiple data types
        - Assume the input list will have integers, as per test cases
        - Assume there will always be more than 3 elements, as we need one of those element to be duplicated

Questions:
    - How should we handle empty input lists?
    - How should we handle lists with only one element?
    - Can there be duplicate values but differing data types? i.e. 3 vs 3.0?

D: In addition to the input *list*, two other ideas for intermediate data structures:
    - A set to capture all the unique elements, after which we can count the number of occurrences per element in the list 
    - A dictionary to keep track of counts, where key is the element and value is the count

A:
    - Capture a set of all unique values in the input list
    - For each unique value in the set:
        - Count how many times that value appears in the input list
        - If a value appears twice, return that value

"""

def find_dup(numbers):
    unique_numbers = set(numbers)
    for num in unique_numbers:
        if numbers.count(num) > 1:
            return num


# Test cases
print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True