# Q1
# What will the following code print?

def make_greeting():
    greeting = "Hello"

    def greet_func(name, greet=None):
        if not greet:
            return f"{greeting} {name}!"

        return f"{greet} {name}!"

    return greet_func

greet_person = make_greeting()
print(greet_person("John", "Goodbye"))
print(greet_person("Jane"))

# This will print "Goodbye John!" followed by "Hello Jane!" on a new line.
# On line 15, we're creating a closure that includes the `greet_func` function along with a cell consisting of 
# the object referenced by non-local variable `greeting`.

# Q2
# What will the following code print?

def make_counter():
    def counter_func():
        counter = 0
        counter += 1
        return counter

    return counter_func

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())

# This will print 1 \n 1 \n 1 \n 1. We reassign `counter` to 0 within each call to the function referenced by
# `increment_counter`

# Q3
# What will the following code print?

from functools import partial

def greet(name, greeting):
    return f"{greeting}, {name}!"

say_hello_to = partial(greet, greeting="Hello")
print(say_hello_to(name="Alice"))  # What will this print?

# This will print "Hello, Alice!" We're using keyword arguments here, so the order shouldn't matter. The use of `partial`
# creates a function referenced by `say_hello_to` where we've pre-filled the greeting parameter with the value 'Hello'.
# We then supply the name parameter afterwards.

# Q4
# Write a function named later that takes two arguments: a function, func, and an argument for that function, 
# argument. The return value should be a new function that calls func with argument as its argument. 
# Here's an example of how it might be used:
# 
# def printer(message):
#     print(message)

# print_warning = later(printer, "The system is shutting down!")
# print_warning()  # The system is shutting down!

def later(func, argument):
    def new_func():
        func(argument)
    return new_func

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()

# Q5
# Write a function named later2 that takes two arguments: a function, func, and an argument for that function, first_arg. 
# The return value should be a new function that takes an argument, second_arg. The new function should call the func 
# with the arguments provided by first_arg and second_arg. Here's an example of how it might be used:
# def notify(message, when):
#     print(f"{message} in {when} minutes!")

# shutdown_warning = later2(notify, "The system is shutting down")
# shutdown_warning(30) # The system is shutting down in 30 minutes!

def later2(func, first_arg):
    def new_func(second_arg):
        func(first_arg, second_arg)
    return new_func

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30)