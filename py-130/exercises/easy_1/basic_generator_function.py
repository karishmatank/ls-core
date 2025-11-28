# Create a generator function that yields numbers from 1 to 5.

def numbers(end_num):
    for num in range(1, end_num + 1):
        yield num

for number in numbers(5):
    print(number)