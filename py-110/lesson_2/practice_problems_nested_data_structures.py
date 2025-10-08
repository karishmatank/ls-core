# Q1: For each object shown below, demonstrate how you would access the letter g.

lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
print(lst1[2][1][3])


lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]
print(lst2[1]['third'][0])

lst3 = [['abc'], ['def'], {'third': ['ghi']}]
print(lst3[2]['third'][0][0])


dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
print(dict1['b'][1])

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
print(list(dict2['3rd'].keys())[0])


# Q2: For each of these collection objects, demonstrate how you would change the value 3 to 4.

lst1 = [1, [2, 3], 4]
lst1[1][1] = 4

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
lst2[2] = 4

dict1 = {'first': [1, 2, [3]]}
dict1['first'][2][0] = 4

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
dict2['a']['a'][2] = 4

# Q3: Given the following code, what will the final values of a and b be? Try to answer without running the code.

a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

# First, a will have the value of 4, as we assign a to the value 2 to start and later add 2 when we reassign lst[0]
# Last, b will have the value [1, 8], as we first assign b to the value [5, 8], then later reassign the 0th element of b
# to take on the value of 5 - 4 = 1 via lst[1][0] -= a, which results in [1, 8]

# NOTE: This writeup above is incorrect. The code lst[0] += 2 modifies lst NOT a. So a remains at the value 2.
# We were correct that b will be mutated as b references a list, but because a remains 2, b[0] is modified to 5 - 2 = 3,
# therefore b has the value [3, 8].


# Q4: Print the name, age, and gender of each family member
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for person in munsters:
    print(f"{person} is a {munsters[person]['age']}-year-old {munsters[person]['gender']}.")