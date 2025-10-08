import random

# Q1: Compute and display the total age of the family's male members. 
# Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

print("Q1:")

# Using a loop:
total_age = 0
for details in munsters.values():
    if details['gender'] == 'male':
        total_age += details['age']
print(total_age)

# Using a comprehension
print(sum([person['age'] for person in munsters.values() if person['gender'] == 'male']))


# Q2: Given the following data structure, return a new list with the same structure, 
# but with the values in each sublist ordered in ascending order. 
# Use a comprehension if you can. (Try using a for loop first.)
# The string values should be sorted as strings, while the numeric values should be sorted as numbers.

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# Expected value: [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

print("\nQ2:")

# Using a loop
new_lst = []
for element in lst:
    new_element = sorted(element)
    new_lst.append(new_element)
print(new_lst)

# Using comprehension
print([sorted(sublist) for sublist in lst])


# Q3: Given the following data structure, return a new list with the same structure, 
# but with the values in each sublist ordered in ascending order as strings 
# (that is, the numbers should be treated as strings). 
# Use a comprehension if you can. (Try using a for loop first.)

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# Expected value: [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

print("\nQ3:")
print([sorted(sublist, key=str) for sublist in lst])


# Q4: Given the following data structure, write some code that uses comprehensions to define a dictionary 
# where the key is the first item in each sublist, and the value is the second.

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

print("\nQ4:")
print({sublist[0]: sublist[1] for sublist in lst})


# Q5: Given the following data structure, sort the list so that the sub-lists are ordered 
# based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

# Note that the first sublist has the odd numbers 1 and 7; 
# the second sublist has odd numbers 1, 5, and 3; 
# and the third sublist has 1 and 3. 
# Since (1 + 3) < (1 + 7) < (1 + 5 + 3), the sorted list should look like this:
# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

def sum_odd(x):
    return sum([i for i in x if i % 2 == 1])

print("\nQ5:")
print(sorted(lst, key=sum_odd))


# Q6: Given the following data structure, return a new list identical in structure to the original 
# but, with each number incremented by 1. Do not modify the original data structure. Use a comprehension.

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

print("\nQ6:")
print([{key: value + 1} for subdict in lst 
                        for key, value in subdict.items()])

# This is what the solution showed. My code above splits up each dictionary incorrectly
# So instead, we should have done the dictionary comprehension first followed by the list comprehension
print([{key: value + 1 for key, value in subdict.items()}
                       for subdict in lst])


# Q7: Given the following data structure return a new list identical in structure to the original, 
# but containing only the numbers that are multiples of 3.
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

print("\nQ7:")
print([[num for num in sublist if num % 3 == 0] for sublist in lst])


# Q8: Given the following data structure, write some code to return a list that contains the colors 
# of the fruits and the sizes of the vegetables. 
# The sizes should be uppercase, and the colors should be capitalized.

# The return value should look like: [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

print("\nQ8:")

return_list = []
for characteristics in dict1.values():
    if characteristics['type'] == 'fruit':
        return_list.append([color.capitalize() for color in characteristics['colors']])
    else:
        return_list.append(characteristics['size'].upper())
print(return_list)


# Q9: Given the following data structure, write some code to return a list 
# that contains only the dictionaries where all the numbers are even.

# Expected result: [{'e': [8], 'f': [6, 10]}]

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

print("\nQ9:")

new_lst = []
for subdict in lst:
    all_lists = list(subdict.values())

    all_even = all([num % 2 == 0 for lst in all_lists 
                                 for num in lst])
    if all_even:
        new_lst.append(subdict)

print(new_lst)

# The solution for Q9 has some better formatted answers, go back and look at those.


# Q10: Write a function that takes no arguments and returns a string that contains a UUID.
# See problem statement for a description of UUIDs

def create_uuid():
    # 8-4-4-4-12 pattern, mix of 0-9 and a-f
    int_options = [str(num) for num in range(0, 10)]
    str_options = ['a', 'b', 'c', 'd', 'e', 'f']
    options = [*int_options, *str_options]
    
    components = [''.join([random.choice(options) for _ in range(0, pattern + 1)])
                                                  for pattern in [8, 4, 4, 4, 12]]
    
    return '-'.join(components)

print("\nQ10:")
print(create_uuid())


# Q11: The following dictionary has list values that contains strings. 
# Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

print("\nQ11:")

# Your code goes here
list_of_vowels = [char for sublist in dict1.values() 
                       for word in sublist 
                       for char in word 
                       if char in 'aeiou']

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
