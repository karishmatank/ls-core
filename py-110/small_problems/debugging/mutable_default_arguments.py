"""
We want to create a function that appends a given value to a list. 
However, the function seems to be behaving unexpectedly:

So this is interesting, and I didn't get it upon first glance before I started inserting print statements into the function
below. So when we invoke the function the first time, we get an expected behavior, which is that lst is assigned an empty list
as we did not pass in a second argument, we mutate the list that 'lst' is referencing, and then we return the list, which
at this stage is [1].

However, when we invoke the function the second time, even though we did not pass in a second argument, we find that lst is
still pointing to the same list as it was during the prior function call. So we end up returning a list with value [1, 2] instead
of the [2] that we would have expected.

To fix this, it probably makes sense to reassign lst to a new list object if a valid second argument wasn't supplied, before
we attempt to append any values.

"""

# def append_to_list(value, lst=[]):
#     lst.append(value)
#     return lst

def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])