"""
We have a list of lists and want to duplicate it. After making the copy, we modify the original list, 
but the copied list also seems to be affected

What's wrong here? How can you fix it?

We're making a shallow copy. Essentially, when we create 'copied', while we are creating a new outer list object in memory,
the elements of the list, which are nested lists, reference the same objects in memory as do the elements of 'original'. 
Therefore, when we try to mutate the first element of 'original', that mutation will be reflected in 'copied' as well.

You'd have to make a deep copy in this instance.

"""

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])