# Create a list where each number from the original list is squared using the map method.

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(lambda x: x ** 2, numbers)
squared_numbers = list(squared_numbers)
print(squared_numbers)