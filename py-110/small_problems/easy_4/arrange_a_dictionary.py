"""
Given a dictionary, return its keys sorted by the values associated with each key.

P:
Input: Dictionary
Output: List
Rules:
    - Explicit
        - The output should be a list of dictionary keys, sorted by the values associated with each key
    - Implicit
        - Assume that an empty input dictionary yields an empty output list
        - The example shows string keys and integer values, so that's what we'll assume here
        - Assume we sort from lowest value to highest value

E: Confirmed

D: No intermediary structures needed

A:
    - Sort the dictionary based on the values of each key
    - Get the keys into a list, return the list

"""

def order_by_value(dictionary):
    return sorted(dictionary.keys(), key=lambda x: dictionary[x])

# Test cases
my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True