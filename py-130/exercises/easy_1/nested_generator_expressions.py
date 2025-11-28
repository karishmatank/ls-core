# Use nested generator expressions to create a flat list of numbers from a list of lists.

nested_lists = [[1], [2, 3], [4, 5, 6], [7, 8]]

nested_generators = (number for numbers in nested_lists for number in numbers)
print(list(nested_generators))