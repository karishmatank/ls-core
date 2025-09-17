def prompt(message, return_output=True):
    revised_message = f"==> {message}"
    if return_output:
        output = input(revised_message)
        return output
    print(revised_message)
    return ""

def get_valid_number(input_num):
    message = f"Enter the {"first" if input_num == 1 else "second"} number: "
    number_valid = False

    while not number_valid:
        number = prompt(message)
        try:
            number = float(number) if '.' in number else int(number)
            number_valid = True
        except ValueError:
            continue

    return number

def get_valid_operation():
    operation_valid = False
    while not operation_valid:
        op = prompt('What operation would you like to perform?\n'
            '1) Add 2) Subtract 3) Multiply 4) Divide: ')
        try:
            op = int(op)
        except ValueError:
            continue

        if 1 <= op <= 4:
            operation_valid = True

    return op

prompt('Welcome to Calculator!', return_output=False)

# Ask the user for the first number.
number1 = get_valid_number(1)

# Ask the user for the second number.
number2 = get_valid_number(2)

# Ask the user for an operation to perform.
operation = get_valid_operation()

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
prompt(f"The result is: {result}", return_output=False)