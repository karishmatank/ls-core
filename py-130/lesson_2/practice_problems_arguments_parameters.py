# Q1
# Write a function named combine that takes three positional arguments and returns a 
# tuple containing all three. Call this function with three different values.

print("Q1:")

def combine(arg1, arg2, arg3):
    return (arg1, arg2, arg3)

print(combine('a', 'b', 'c'))

# Q2
# Define a function named multiply that accepts two positional-only arguments and returns their product. 
# The function should not allow these parameters to be passed as keyword arguments.

print("\nQ2:")

def multiply(num1, num2, /):
    return num1 * num2

print(multiply(3, 5))
try:
    print(multiply(num1=3, num2=4))
except TypeError as e:
    print(f"Passed in keyword arguments: {e}")

# Q3
# Create a function named describe_pet that takes one positional argument animal_type 
# and one keyword argument name with a default value of an empty string. 
# The function should print a description of the pet. 
# The function should not accept more than 1 positional argument.

print("\nQ3:")

def describe_pet(animal_type, *, name=''):
    if name:
        desc = f"This is a {animal_type} whose name is {name}."
    else:
        desc = f"This is a {animal_type} who has no name."
    
    print(desc)

try:
    describe_pet("cat", "Kitty")
except TypeError as e:
    print(f"Error: {e}")

describe_pet("cat", name="Kitty")
describe_pet("cat")

# Q4
# Write a function named calculate_average that accepts any number of numeric arguments and returns their average. 
# Make sure it returns None if no arguments are provided.

print("\nQ4:")

def calculate_average(*args):
    if not args:
        return None
    return sum(args) / len(args)

print(calculate_average())
print(calculate_average(1, 2, 3, 4, 5, 6))

# Q5
# Create a function named find_person that accepts any number of keyword arguments in which each 
# key is someone's name and the value is their associated profession. 
# The function should check whether any of the key/value pairs has a key of "Antonina" and then, 
# if the key is found, print a message that shows Antonina's profession. 
# Otherwise, it should say "Antonina not found". 
# The function should not accept any positional arguments.

print("\nQ5:")

def find_person(**kwargs):
    print(kwargs.get('Antonina', 'Antonina not found'))

find_person(Bob='baker', Alice="accountant", Antonina="TA")
find_person(Bob='baker', Alice="accountant")

# Q6
# Define a function named concat_strings that takes any number of strings and returns the concatenation 
# of all the strings. Add a keyword-only argument sep with a default value of ' ' that specifies the 
# separator to use between the strings.

print("\nQ6:")

def concat_strings(*args, sep=' '):
    return sep.join(args)

print(concat_strings('hello', 'world', sep=', '))
print(concat_strings('hello', 'world'))

# Q7
# Create a function named register that takes exactly three arguments: 
# username as positional-only, password as keyword-only, and age as either a positional or keyword argument. 
# It should return a dictionary that includes username, password, and age keys with the values passed to the the function.

print("\nQ7:")

def register(username, /, age, *, password):
    return {
        'username': username,
        'password': password,
        'age': age
    }

print(register('abc', 18, password='123'))
print(register('abc', age=18, password='123'))
try:
    print(register(username='abc', age=18, password='123'))
except TypeError as e:
    print(f"Username can't be keyword: {e}")

try:
    print(register('abc', 18, '123'))
except TypeError as e:
    print(f"Password can't be positional: {e}")

# Q8
# Create a function named print_message that requires a keyword-only argument (message) 
# and an optional keyword-only argument (level) with a default value of "INFO". 
# The function should print out the message prefixed with the level. The function shouldn't accept any positional arguments.

print("\nQ8:")

def print_message(*, message, level="INFO"):
    print(f"{level} - {message}")

print_message(message="Hello world")
print_message(level='Urgent', message='Hello world')

try:
    print_message("Hello world")
except TypeError as e:
    print(f"No positional arguments allowed - {e}")