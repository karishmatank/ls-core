## Q3
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

for i in my_list:
    print(i)

## Q4
index = 0
while index < len(my_list):
    num = my_list[index]
    if num % 2 == 0:
        print(num)
    index += 1

for num in my_list:
    if num % 2 == 1:
        print(num)

## Q5
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for i in my_list:
    for j in i:
        if j % 2 == 0:
            print(j)

## Q6
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
print(['odd' if i % 2 != 0 else 'even' for i in my_list])

## Q7
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(input):
    return [i for i in input if type(i) == int]

integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

## Q8
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

print({name: len(name) for name in my_set if len(name) % 2 != 0})

## Q9
def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product

print(factorial(5))

## Q10
import random

highest = 10

while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break

## Q11
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0
while outer_index < len(my_list):
    element = my_list[outer_index]

    inner_index = 0
    while inner_index < len(element):
        value = element[inner_index]
        if value % 2 == 0:
            print(value)
            
        inner_index += 1

    outer_index += 1