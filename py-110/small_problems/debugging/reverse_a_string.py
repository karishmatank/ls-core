"""
You have a function that is supposed to reverse a string passed as an argument. However, it's not producing the expected output. 
Explain the bug, and provide a solution.

The bug is that we are reassigning 'string' as we are iterating through it. While this may not mess up the iteration in the way
that it would if we were mutating a list while iterating through it, it means that we are retaining the original string and
adding characters to the front of it, rather than creating a reversed version of the string.

Instead, I'm going to assign an empty string to a variable 'reversed_string', and as we iterate through each character of the
input, we'll add it to the front of the new string that we are now constructing in 'reversed_string'. We'll then return that
new string object.

"""

def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string

    return reversed_string

print(reverse_string("hello") == "olleh")
