"""
Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values 
and its values become keys.

P:
Input: Dictionary
Output: Dict
Rules:
    - Explicit
        - The output is an inverted form of the input dictionary, where the keys become values and values become keys
        - Keys and value of the input dictionary are unique
    - Implicit
        - Assume the input dictionary will always be populated
        - Assume the values of the dictionary are hashable
        - We should create a new dictionary object rather than mutate the original

E: Confirmed

D: We can use lists to store the keys and values in tuple pairs as we construct a new dictionary

A:
    - Get a list of the current key-value pairs, each pair in tuples
    - Create a new list, whose elements are new tuple objects that reverse the key and value order that we see in the
      dictionary today
    - Create a new dictionary off of the new list
    - Return the new dictionary

"""

def invert_dict(dictionary):
    key_value_pairs = list(dictionary.items())
    revised_pairs = [(pair[1], pair[0]) for pair in key_value_pairs]
    return dict(revised_pairs)

# Test cases
print(invert_dict({
    'apple': 'fruit',
    'broccoli': 'vegetable',
    'salmon': 'fish',
}) == {
    'fruit': 'apple',
    'vegetable': 'broccoli',
    'fish': 'salmon',
})  # True