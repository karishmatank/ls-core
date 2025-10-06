# Selection
produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(d):
    new_dict = {}
    for fruit in d:
        if d[fruit] == 'Fruit':
            new_dict[fruit] = 'Fruit'
    return new_dict

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }


# Transformation with mutation
def double_numbers(numbers):
    for idx, current_num in enumerate(numbers):
        numbers[idx] = current_num * 2

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12] without mutation. I chose not to return a value given side effect
print(my_numbers)                 # [1, 4, 3, 7, 2, 6] without mutation, [2, 8, 6, 14, 4, 12] with mutation


# Transform numbers based on their position in the list (double numbers that have odd indices)
def double_odd_numbers(numbers):
    doubled_nums = []

    for idx in range(0, len(numbers)):
        if idx % 2 == 1:
            doubled_nums.append(numbers[idx] * 2)
        else:
            doubled_nums.append(numbers[idx])
    
    return doubled_nums

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_numbers(my_numbers)) # [1, 8, 3, 14, 2, 12]
print(my_numbers) # [1, 4, 3, 7, 2, 6]


# Multiply the elements of a list by an arbitrary number
def multiply(numbers, factor):
    return [num * factor for num in numbers]

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]
print(my_numbers) # [1, 4, 3, 7, 2, 6]