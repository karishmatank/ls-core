# Q1
# Create a generator expression that generates the reciprocals of the numbers from 1 to 10. 
# A reciprocal of a number n is 1 / n. Use a for loop to print each value.

print("Q1:")

reciprocals = (1 / n for n in range(1, 11))
print(reciprocals)

for num in reciprocals:
    print(num)

# Q2
# Create a generator function that generates the reciprocals of the numbers 
# from 1 to n, where n is an argument to the function. Use a for loop to print each value.

print("\nQ2:")

def calculate_reciprocals(n):
    for num in range(1, n + 1):
        reciprocal = 1 / num
        yield reciprocal

reciprocals = calculate_reciprocals(10)
for num in reciprocals:
    print(num)

# Q3
# Use a generator expression to capitalize every string in a list of strings. 
# Use a single print invocation to print all the capitalized strings as a tuple.

print("\nQ3:")


words = ['hello', 'world']
capitalized = (i.capitalize() for i in words)
print(tuple(capitalized))

# Q4
# Create a generator function that generates the capitalized version of every string in a list of strings. 
# Use a single print invocation to print all the capitalized strings as a tuple.

print("\nQ4:")

def capitalize_words(words):
    for word in words:
        yield word.capitalize()

print(tuple(capitalize_words(words)))

# Q5
# Use a generator expression to capitalize the strings in a list of strings whose length is at least 5. 
# Use a single print invocation to print all the capitalized strings as a set.

print("\nQ5:")

words = ['hello', 'world', 'hi', 'sounds', 'good']
capitalized = (word.capitalize() for word in words if len(word) >= 5)
print(set(capitalized))

# Q6
# Create a generator function that generates the capitalized version of every string in a list of strings 
# whose length is less than 5. Use a single print invocation to print all the capitalized strings as a set.

print("\nQ6:")

def capitalized_words(words):
    for word in words:
        if len(word) < 5:
            yield word.capitalize()

print(set(capitalized_words(words)))