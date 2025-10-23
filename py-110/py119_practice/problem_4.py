"""
Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

P:
Given a list of numbers, return a tuple with the first pair of numbers that are closest in value.

Rules:
    - Closest in value mean absolute value of difference
    - First in list means we iterate keeping a constant start and iterating the end. First is the one with lowest start, then lowest end
    - Assume input list has more than 2 integers
    - Output tuple maintains order of integers as appears in input

[5, 25, 15, 11, 20]
- (5, 25) => absolute diff is 20
- (5, 15) => 10
- (5, 11) => 6
- (25, 20) => 5
- (15, 11) => 4 => output

[19, 25, 32, 4, 27, 16] 
- (19, 25) => 6
- (19, 16) => 3
- (25, 27) => 2 => output

[12, 22, 7, 17]
- (12, 22) => 10
- (12, 7) => 5 => output, first with lowest diff

Data structures:
    - Input: List of integers
    - Output: Tuple of integer pair
    - Intermediary
        - Ranges: Iterate through the input List
        - Integer: Keep track of lowest diff

High-level strategies:
    - Iterate through pairs of integers in the list. If a pair has a diff less than the current lowest diff, record that pair. Return the pair with the lowest difference.

A:
    - Set 'lowest_diff' to None
    - Set 'lowest_pair' to None
    - For a 'num_1' ranging from the start to the second to last element:
        - For a 'num_2' ranging from 'num_1' + 1 to the end:
            - Set 'new_diff' to abs difference between number at 'num_1' and number at 'num_2'
            - If difference < 'lowest_diff' or no 'lowest_diff':
                - Set 'lowest_diff' to the 'new_diff'
                - Set 'lowest_pair' to (number at 'num_1', number at 'num_2')
    - Return 'lowest_pair'

"""

def closest_numbers(numbers):
    lowest_diff = None
    lowest_pair = None

    for num_1 in range(len(numbers) - 1):
        for num_2 in range(num_1 + 1, len(numbers)):
            new_diff = abs(numbers[num_1] - numbers[num_2])
            if not lowest_diff or new_diff < lowest_diff:
                lowest_diff = new_diff
                lowest_pair = (numbers[num_1], numbers[num_2])
    
    return lowest_pair


# Test cases
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))


"""
Reflection:
Took 20 min 58 seconds. I messed up the algo by referring at first to just 'num_1' and 'num_2', taking their difference, and
including them directly in the end tuple. I actually caught that as I was testing my code that I needed to get the number at
those indices to do the difference, etc. Probably should have caught that sooner.
"""