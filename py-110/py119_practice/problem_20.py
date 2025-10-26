"""
Create a function that takes a list of numbers, all of which are the same except one. Find and return the number in the list that differs from all the rest.

The list will always contain at least 3 numbers, and there will always be exactly one number that is different.

P:
Given a list of numbers, find the odd one out

Rules:
    - Input list can have integers or floats
    - All numbers in input list will be the same except one
    - The list will always have at least 3 nums
    - There will only be one number that is different

Data structures:
    - Input: List of numbers (ints, floats)
    - Output: Int / float
    - Intermediary:
        - Dictionary: Keys = ele values, Values = counts
        - Sets: Get unique elements

High-level strategies:
    - Create a dict with keys as element values and values as their counts. Return the key whose values is = 1
    - Create a set with the 2 unique elements of the input. Find the element whose count is 1 and return

A:
    - *get_counts* => Input: input list, Output: 'counts'
    - For each key in 'counts':
        - If value is 1:
            Return value from *convert_str_to_num*, input = value

*get_counts*
    Input: List
    Output: dict
    Algo:
        - Create an empty dict 'value_counts'
        - For each element in input:
            - Coerce element into string => 'num_str'
            - If 'num_str' not already a key in 'value_counts', add it
            - Increment value of key by 1

*convert_str_to_num*
Input: string
Output: Int / float
Algo:
    - If there is a decimal char in the key
        - Coerce key to float
        - Return the float
    - Else:
        - Coerce key to int
        - Return the int
"""


def get_counts(numbers):
    value_counts = dict()
    for num in numbers:
        num_str = str(num)
        value_counts[num_str] = value_counts.get(num_str, 0) + 1
    return value_counts

def convert_str_to_num(str_num):
    if '.' in str_num:
        return float(str_num)
    else:
        return int(str_num)

def what_is_different(numbers):
    counts = get_counts(numbers)
    for key, count in counts.items():
        if count == 1:
            return convert_str_to_num(key)



# # Test cases
print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)


"""
Reflection:
Time: 15 min 15 seconds. Almost didn't catch the floats can't be dict keys until I was writing my algorithm and realized it.
"""