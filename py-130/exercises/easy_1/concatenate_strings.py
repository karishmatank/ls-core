# Use reduce to concatenate a list of strings into a single string.

from functools import reduce

strings = ['a', 'bee', 'cello', 'dog', 'ears']

combined = reduce(lambda x, y: x + y, strings)
print(combined)