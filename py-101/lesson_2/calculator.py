import json

def message_translate(key, lang='en'):
    # Translate message to selected language
    if lang not in ['en', 'yoda']:
        lang = 'en'
    return CALCULATOR_MESSAGES[lang][key]

def prompt(message, return_output=True):
    # Return message with arrow formatting
    revised_message = f"==> {message}"
    if return_output:
        output = input(revised_message)
        return output
    print(revised_message)
    return ""

def get_valid_number(input_num):
    # Make sure user input is valid int or float
    if input_num == 1:
        message = message_translate('first_num', LANG)
    else:
        message = message_translate('second_num', LANG)

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
    # Make sure operation is 1, 2, 3, or 4
    operation_valid = False
    while not operation_valid:
        op = prompt(message_translate('operation', LANG))
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
    prompt(
        f"{message_translate('result', LANG)} {result}",
        return_output=False
    )


# Read the JSON file with our messages
with open('calculator_messages.json', 'r') as file:
    CALCULATOR_MESSAGES = json.load(file)

prompt(CALCULATOR_MESSAGES['welcome'], return_output=False)
LANG = prompt(CALCULATOR_MESSAGES['lang'])
KEEP_CALCULATING = True
while KEEP_CALCULATING:
    calculation()
    again = prompt(message_translate('new_calc', LANG))
    KEEP_CALCULATING = again.upper() == 'Y'