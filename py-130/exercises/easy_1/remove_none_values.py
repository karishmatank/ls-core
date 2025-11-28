# Remove all None values from a list using the filter method.

lst = [None, None, 'a', None, 'b', 'c']

cleaned = list(filter(lambda x: x is not None, lst))
print(cleaned)