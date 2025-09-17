print('Welcome to Calculator!')

# Ask the user for the first number.
number1_valid = False
number2_valid = False

while not number1_valid:
    number1 = input("Enter the first number: ")
    try:
        number1 = float(number1) if '.' in number1 else int(number1)
        number1_valid = True
    except ValueError:
        continue


# Ask the user for the second number.
while not number2_valid:
    number2 = input("Enter the second number: ")
    try:
        number2 = float(number2) if '.' in number2 else int(number2)
        number2_valid = True
    except ValueError:
        continue

# Ask the user for an operation to perform.
operation_valid = False
while not operation_valid:
    print('What operation would you like to perform?\n'
        '1) Add 2) Subtract 3) Multiply 4) Divide')
    operation = input()
    try:
        operation = int(operation)
    except ValueError:
        continue

    if operation >= 1 and operation <= 4:
        operation_valid = True

# Perform the operation on the two numbers.
match operation:
    case 1:
        # Addition
        result = number1 + number2
    case 2:
        # Subtraction
        result = number1 - number2
    case 3:
        # Multiplication
        result = number1 * number2
    case 4:
        # Division
        result = number1 / number2

# Print the result to the terminal.
print(f"The result is: {result}")