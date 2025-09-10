# Q1: Use concatenation to create your full name from your first and last names
first_name = 'Jane'
last_name = 'Smith'

name = first_name + " " + last_name
print(name)

# Q2: Extract each digit from 4936
number = 4936

ones = number % 10
print(f"Ones: {ones}")

tens = int(((number % 100) - (number % 10)) / 10)
print(f"Tens: {tens}")

hundreds = int(((number % 1000) - (number % 100)) / 100)
print(f"Hundreds: {hundreds}")

thousands = int((number - (number % 1000)) / 1000)
print(f"Thousands: {thousands}")

# Q4: Refactor print('5' + '10') to print 15 instead
print(int('5') + int('10'))