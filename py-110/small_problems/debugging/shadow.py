"""
We defined a function intending to multiply the sum of numbers by a factor. 
However, the function raises an error. Why? How would you fix this code?

It raises an error because we are defining our own function 'sum', which overrides the built-in function 'sum'. Because
of this, we can't use the built-in function anymore within our own 'sum' function as we intend. The error comes from
the fact that inside our 'sum' function, we are trying to call the function recursively without the required second argument.

We should just rename our function.

"""

def sum_factor(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_factor(numbers, 2) == 20)