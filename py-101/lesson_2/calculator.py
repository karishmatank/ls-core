import json

def prompt(message, return_output=True):
    revised_message = f"==> {message}"
    if return_output:
        output = input(revised_message)
        return output
    print(revised_message)
    return ""

def get_valid_number(input_num):
    if input_num == 1:
        message = calculator_messages['first_num']
    else:
        message = calculator_messages['second_num']
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
        op = prompt(calculator_messages['operation'])
        try:
            op = int(op)
        except ValueError:
            continue

        if 1 <= op <= 4:
            operation_valid = True

    return op

def calculation():
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
    prompt(f"{calculator_messages['result']} {result}", return_output=False)


# Read the JSON file with our messages
with open('calculator_messages.json', 'r') as file:
    calculator_messages = json.load(file)

prompt(calculator_messages['welcome'], return_output=False)
KEEP_CALCULATING = True
while KEEP_CALCULATING:
    calculation()
    again = prompt(calculator_messages['new_calc'])
    KEEP_CALCULATING = again.upper() == 'Y'