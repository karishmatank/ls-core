def remainders_3(numbers):
    return [number % 3 for number in numbers]

def remainders_5(numbers):
    return [number % 5 for number in numbers]

## Q18: Which of the following lists contains at least one number that is *not* evenly divisible by 3?
numbers_1 = [0, 1, 2, 3, 4, 5, 6] # True
numbers_2 = [1, 2, 4, 5] # True
numbers_3 = [0, 3, 6] # False
numbers_4 = [] # False

# Use any because we only need to know if there is at least one non-zero value (at least one truthy value)
print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))

## Q19: Which of the following lists do not contain any numbers that are divisible by 5?
numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # False
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9] # True
numbers_3 = [0, 5, 10] # False
numbers_4 = [] # True

# Use all because we want to know if every element of the resulting list is non-zero (truthy)
print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))
