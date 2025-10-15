"""
Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs 
for the specified keys.

P:
Input: Dictionary, list of keys
Output: New dictionary
Rules:
    - Explicit
        - The output dictionary should only contain the key/value pairs for the specified keys
    - Implicit
        - If the dictionary doesn't have all of the keys specified in the second argument, the length of the
          dictionary can be different from the length of the input list

E: Confirmed

D: No intermediary data structures needed

A:
    - Create a new dictionary that only has the keys specified in the input list
    - Return that dictionary

"""

def keep_keys(dictionary, keys_list):
    return {key: value for key, value in dictionary.items() if key in keys_list}

# Test cases
input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True