# for_each function
# Print the squares of all the numbers in an iterable, but we don't want to collect them into a new collection.
print("*** for_each ***")

def for_each(callback, iterable):
    for item in iterable:
        callback(item)

for_each(lambda number: print(number ** 2), [1, 2, 3, 4, 5])

pets = ('cat', 'dog', 'fish', 'bearded dragon')
for_each(lambda string: print(string.title()), pets)

nested_lists = [[1, 2], [3, 4], [5, 6, 7]]
for_each(lambda sublist: sublist.pop(), nested_lists)
print(nested_lists)

# times function
# Call the callback function by the specified number of times

print("*** times ***")

def times(callback, number):
    for item in range(number):
        callback(item)

times(lambda number: print(number ** 2), 5)

pets = ('cat', 'dog', 'fish', 'bearded dragon')
new_pets = []
times(lambda index: new_pets.append(pets[index].title()), len(pets))
print(new_pets)