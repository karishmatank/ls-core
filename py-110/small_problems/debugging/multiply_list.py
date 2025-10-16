"""
You want to multiply all elements of a list by 2. However, the function is not returning the expected result. 
Explain the bug, and provide a solution.

We're multiplying each element by 2, but we aren't capturing that new value anywhere, whether by mutating the list or
appending the value to a new list. Therefore, in its current form, we're returning the same list as we're passing in to the
function.

Given how we're calling the function to compare the return value to the expected list, we should not mutate the list we are
passing in. Instead, we'll create a new list that multiplies each element by 2 and returns that new list.

"""

def multiply_list(lst):
    # for item in lst:
    #     item *= 2

    # return lst

    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])