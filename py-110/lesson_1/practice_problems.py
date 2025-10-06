# Q1: How would you count the number of occurrences of "banana" in the tuple?
fruits = ("apple", "banana", "cherry", "date", "banana")

print("Q1:")
print(len([fruit for fruit in fruits if fruit == "banana"]))
print(fruits.count("banana"))

# Q2: What is the set's length? Answer without running the code
numbers = {1, 2, 3, 4, 5, 5, 4, 3}
# print(len(numbers))
# The set's length is 5, as numbers would print as {1, 2, 3, 4, 5}

# Q3: How would you obtain a set that contains all the unique values from both sets?
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Q3:")
print(a.union(b))
print(a | b)

# Q4: What is the output? Answer without running the code
names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
# print(name_positions)

# This would print a dictionary as follows:
# {"Fred": 0, "Barney": 1, "Wilma": 2, "Betty": 3, "Pebbles": 4, "Bambam": 5}

# Q5: Calculate the total age given the following dictionary
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

print("Q5:")
print(sum(list(ages.values())))

# Q6: Determine the minimum ages from the ages dict above
print("Q6:")
print(min(ages.values()))

# Q7: What would the following print? Don't run the code
words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

# print(selected_words)

# This would print ['bear'] as 'bear' is the only word with length > 3

# Q8: Given the following string, create a dictionary that represents the frequency with which each letter occurs. 
# The frequency count should be case-sensitive
statement = "The Flintstones Rock"

freq = {}
for char in statement:
    if char.isspace():
        continue
    elif char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Q8:")
print(freq)

# Q9: What is the return value of the list comprehension below? Try to answer without running the code
[num for num in [1, 2, 3] if num > 1]

# This will return [2, 3] because elements 2 and 3 are the only ones that are greater than 1

# Q10: What will this print and why?
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

# This will print ('b', 'bear'). The popitem method returns the last key-value pair as a tuple
# At this point, dictionary is mutated and would be {'a': 'ant'}

# Q11: What will the following return? Don't run the code
lst = [1, 2, 3, 4, 5]
lst[:2]

# This will return [1, 2]. We start at index 0 and go up to but not include index 1, 
# which means we include indexes 0 and 1 only.

# Q12: What is the output of the below? Don't run the code
frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)

# This will raise a TypeError, as we can't add elements to a frozenset.
# Correction: Not a TypeError, will raise an AttributeError as frozensets don't have the attribute .add()