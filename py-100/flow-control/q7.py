def number_range(num):
    match num:
        case num if num >= 0 and num <= 50:
            return f"{num} is between 0 and 50"
        case num if num >= 51 and num <= 100:
            return f"{num} is between 51 and 100"
        case num if num > 100:
            return f"{num} is greater than 100"
        case _:
            return f"{num} is less than 0"

print(number_range(0))
print(number_range(25))
print(number_range(50))
print(number_range(75))
print(number_range(100))
print(number_range(101))
print(number_range(-1))