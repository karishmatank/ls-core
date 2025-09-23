## Q1: Do these return the same results?
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# I thought the answer was yes, but it is no, given for the second function, the dict comes after the return.

## Q2: What does the last line output?
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# It should output {'first': [1, 2]}. num_list is pointing to dictionary['first'] and then mutates it.

## Q3: What does each snippet print?

# Snippet 1:
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# I think this prints "one is: ['one']" \n "two is ['two']" \n "three is: ['three']"
# mess_with_vars assigns new local variables that don't impact the global variables (CORRECT)

# Snippet 2:
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# I think this prints "one is: ['one']" \n "two is ['two']" \n "three is: ['three']"
# mess_with_vars assigns new local variables that don't impact the global variables (CORRECT)

# Snippet 3:
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# This prints "one is ['two']" \n "two is ['three']" \n "three is ['one']" (CORRECT)

## Q4: Fix the function

# This function is correct as provided
def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")

    # Adding the if statement below to check how long the list is
    if len(dot_separated_words) != 4:
        return False

    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False # changed from just "break"

    return True

## Q5: What will happen in the code below?
# if False:
#     greeting = "hello world"

# print(greeting)
# This will print a NameError because the if statement will never run given if False is always False
